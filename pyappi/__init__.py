__author__ = 'yyyar'

from .validation import parameters, parameters_presets
from .serializers import json

ident = lambda _:_


class Pyappi:
    """
        Pyappi base class
    """

    def __init__(self, adapter=ident, serializer=json, formatter=ident, **kw):
        """
            Creates new instance of Pyappi
        """

        self.validation = parameters
        self.adapter = adapter
        self.serializer = serializer
        self.formatter = formatter


    def wrap(self, f):
        """
            Wraps view with adapter, serializer and formatter
        """

        return \
            self.adapter(
                self.serializer(
                    self.formatter(f)))


    @property
    def presets(self):
        """
            Parameters presets processing
        """

        def _outer(*p, **kw):
            def _inner(f):
                 return parameters_presets(*p, **kw)(f)
            return _inner
        return _outer


    @property
    def params(self):
        """
            Parameters processing
        """

        def _outer(*p, **kw):
            def _inner(f):
                return self.validation(*p, **kw)(f)
            return _inner
        return _outer

