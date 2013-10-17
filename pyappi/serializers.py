__author__ = 'yyyar'

import json as j

def json(f):
    '''
        JSON serializer
    '''

    def _inner(*p, **kw):
        return j.dumps(f(*p, **kw), indent=4), 'application/json; charset=utf-8'
    return _inner