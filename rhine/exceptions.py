'''
Rhine Python Library
(c) Speare Inc. 2015
'''

class RhineException(Exception):
  pass

class InvalidAuthentication(RhineException):
  pass

class InvalidRequest(RhineException):
  pass

class InternalError(RhineException):
  pass
