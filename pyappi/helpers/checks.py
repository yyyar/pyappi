
import datetime

#-- Checkers

def date_check(f):
    '''
        Check of date string is fine for format
    '''
    def _f(s):
        try:
            datetime.datetime.strptime(s, f)
            return True
        except:
            return False
    return _f

def bool_check(s):
    '''
        Check boolean
    '''
    return s in ['true', 'false']

def int_check(s):
    '''
        Check integer
    '''
    try:
        int(s)
        return True
    except:
        return False

def float_check(s):
    '''
        Check float
    '''
    try:
        float(s)
        return True
    except:
        return False


def variants_check(elems):
    '''
        Check if params exists in elems
    '''
    return lambda e: e in set(elems)