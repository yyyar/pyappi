__author__ = 'yyyar'

def flask_adapter(f):
    """
        Flask adapter decorator.
    """
    from flask import request, Response

    def _inner(*p, **kw):
        request.params = request.args
        (response, content_type) = f(request, *p, **kw)
        return Response(response, content_type=content_type)
    return _inner


def django_adapter(f):
    """
        Django adapter decorator.
    """
    from django.http import HttpResponse

    def _inner(request, *p, **kw):
        request.params = request.REQUEST
        (response, content_type) = f(request, *p, **kw)
        return HttpResponse(response, content_type=content_type)
    return _inner
