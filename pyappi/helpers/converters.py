__author__ = 'yyyar'

import datetime

#-- Converters

def date_convert(f):
    '''
        Converts date string into datetime
    '''
    def _f(s):
        return datetime.datetime.strptime(s, f) if s else None
    return _f

def int_convert(s):
    '''
        Converts int string into int
    '''
    return int(s)

def bool_convert(s):
    '''
        Converts bool string into bool
    '''
    return s == 'true'

def float_convert(s):
    '''
        Converts float string to float
    '''
    return float(s)

def tokenize_convert(separator):
    '''
        Converts string to list of tokenized strings
    '''
    def _f(s):
        return s.split(separator) if s else None
    return _f

def no_convert(x):
    '''
        No conversion
    '''
    return x