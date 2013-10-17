__author__ = 'yyyar'

from .converters import *
from .checks import *

#-- Parameters presets

'''
    No-Cache parameter
'''
noncacheable = {'_' : {}}

scopeable = {'scope' : {'omit' : True} }
authenticable = {'auth_token' : {'omit' : True}}

def offsetable(value=0):
    '''
        Provides offset parameter
    '''
    return {
        'offset' : {
            'description': 'Offset of returned records',
            'default': value,
            'check': int_check,
            'message': 'Should be integer',
            'converter': int_convert
        }
    }

def limitable(value=20):
    '''
        Provides limit parameter
    '''
    return {
            'limit': {
                'description' : 'Limit returned records to this value',
                'default': value,
                'check':  int_check,
                'message': 'Should be integer',
                'converter': int_convert
            }
    }
