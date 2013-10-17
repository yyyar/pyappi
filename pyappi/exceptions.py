__author__ = 'yyyar'

#-- Exceptions

class ApiError(Exception):
    '''
        api error
    '''
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class ParamValidationError(ApiError):
    '''
        validation api error
    '''
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)