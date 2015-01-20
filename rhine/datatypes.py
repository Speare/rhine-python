'''
Rhine Python Library
(c) Speare Inc. 2015
'''

class article:
  fromurl = staticmethod(lambda url: {'article': {'fromurl': url}})

class image:
  fromurl = staticmethod(lambda url: {'image': {'fromurl': url}})

text = lambda t: {'text': t}

entity = lambda e: {'entity': e}

grouped = lambda *os: {'grouped': os}
