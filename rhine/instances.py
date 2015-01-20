'''
Rhine Python Library 
(c) Speare Inc. 2015
'''

try:
  import ujson as json
except ImportError:
  import json

import requests

from .exceptions import *

class RhineInstance:
  def __init__(self, apikey, ssl = False):
    self.apikey = apikey
    self.url = 'https://api.rhine.io' if ssl else 'http://api.rhine.io/'

  def __str__(self):
    return 'RhineInstance<apikey:{0}>'.format(self.apikey)

  def _run(self, req):
    result = requests.post(self.url, data = json.dumps({'request': {'method': req, 'key': self.apikey}})).json()
    if 'success' in result:
      return result['success']
    else:
      if result['failure'] == 'invalidjson': raise InvalidRequest()
      if result['failure'] == 'invalidauthentication': raise InvalidAuthentication()
      if result['failure'] == 'internalerror': raise InternalError()

  def run(self, req):
    name = list(req.keys())[0]
    return self._run(req)[name]

  def pipeline(self, reqs):
    return [x[0][x[1]] for x in zip(self._run({'pipelined': reqs})['multiple'], [list(r.keys())[0] for r in reqs])]    

def instantiate(key, ssl = False):
  return RhineInstance(key, ssl)
