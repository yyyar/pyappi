__author__ = 'yyyar'

# package
from functools import wraps
from pyappi.exceptions import ParamValidationError, ApiError

def no_formatter(f):
    '''
        No format at all
    '''
    return f

def simple_formatter(f):
    '''
        Simple formatter with exception handling
    '''
    @wraps(f)
    def inner(request, *args, **kwargs):
        try:
            obj = f(request, *args, **kwargs)
            return obj
        except ApiError as e:
            return { 'error' : e.message.replace('"', "'") }

    return inner


def withstatus_formatter(f):
    '''
        Pretty status/response format
    '''

    api_ok = lambda obj: {
        'status' : {
            'code' : 0,
            'msg' : 'ok'
        },
        'response': obj
    }

    api_err = lambda e : {
        'status' : {
            'code' : e.code,
            'msg' :  e.msg
        },
        'response': None
    }

    @wraps(f)
    def inner(request, *args, **kwargs):
        try:
            obj = f(request, *args, **kwargs)
            return api_ok(obj)
        except ApiError as e:
            return api_err(e)
        except ParamValidationError as e:
            return api_err(ApiError(-1, e.message))

    return inner
