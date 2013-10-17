__author__ = 'yyyar'

import types
from functools import wraps
from .exceptions import ParamValidationError

def parameters_presets(*params):
    """
        Combines parameters from a several presets
    """
    d = {}
    for e in params:
        d.update(e)
    return parameters(d, allow_undeclared=True)

def parameters(d = {}, allow_undeclared=False):
    '''
        Checks and converts GET parameters of HTTP request
    '''

    # Convert tuples of params to a separate params
    # So {('p1', 'p2') : {} } will become:
    # {'p1' : {}, 'p2' : {} }
    for (k,v) in d.items():
        if type(k) == tuple:
            for a in k:
                d[a] = v
            del d[k]

    # parameters defaults
    DEFAULTS = {
        'required': False,  # bool - if parameter required to be presented in request
        'default': None,  # object - default value of parameter is it is not in requests
        'check': lambda x: True, # tuple(func, message) - parameter validator
        'converter': lambda x: x, # func - converter from string to any type
        'description': '',  # string - description of parameter
        'omit': False,  # bool - if parameter is not required and not exists, do not use default value
        'collection': False  # bool - parameter is a collection of parameters (when it repeats several times in request)
    }

    def get(opts, param):
        return opts.get(param, DEFAULTS[param])

    def outer(f):

        @wraps(f)
        def inner(request, *args, **kwargs):

            if 'doc' in request.params:
                pass  # TODO: render doc page

            for param, opts in d.items():

                # - parameter value
                if get(opts, 'collection'):
                    value = request.params.getall(param)
                else:
                    value = request.params.get(param, None)

                    # Do not process if parameter allowed to be omitted and IS is omitted
                    if value is None and get(opts, 'omit'):
                        continue

                if value == "":
                    value = None

                # - required
                required = get(opts, 'required')
                if required and value == None:
                    raise ParamValidationError('"%s" parameter required' % param)

                # - converter
                converter = get(opts, 'converter')
                if value:
                    value = converter(value)


                # - default
                if value is None:
                    default = get(opts, 'default')
                    value = default() if type(default) == types.LambdaType else default
                else:
                    # - check
                    check = get(opts, 'check')
                    if type(check) == tuple:
                        (check, msg) = check
                    else:
                        msg = ''
                    if not check(value):
                        raise ParamValidationError(param + ": " + msg)

                kwargs[param] = value

            # - exibit parameters
            if not allow_undeclared:
                unknown = set(request.params.keys()) - set(kwargs.keys())
                if len(unknown) > 0:
                    raise ParamValidationError("Unknown parameters: " + ", ".join(unknown))

            return f(request, *args, **kwargs)

        return inner

    return outer
