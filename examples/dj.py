__author__ = 'yyyar'

import datetime
import os
from django.conf.urls.defaults import patterns
from pyappi import Pyappi
from pyappi.helpers import int_convert, date_current, date_convert
from pyappi.helpers.presets import limitable
from pyappi.adapters import django_adapter
from pyappi.formatters import simple_formatter

SECRET_KEY = '1'
DEBUG=True
filepath, extension = os.path.splitext(__file__)
ROOT_URLCONF = os.path.basename(filepath)


appi = Pyappi(adapter=django_adapter, formatter=simple_formatter)

@appi.wrap
@appi.presets(limitable(5))
@appi.params({
    'a': {
        'required': True,
        'description': "First Number",
        'converter': int_convert,
        'check': (lambda x: x != 0, 'should be != 0')
    },
    'b': {
        'required': True,
        'description': 'Second Number',
        'converter': int_convert
    },
    'date': {
        'required': False,
        'default': date_current('%d-%m-%Y'),
        'converter': date_convert('%d-%m-%Y'),
        'check': (lambda d: datetime.datetime.now() > d, 'should be < now')
    }
})
def my_sequence(request, a, b, date, limit):
    return {
        'numbers': [x for x in list(range(a, b))[:limit]],
        'date': date
    }

urlpatterns = patterns('', (r'', my_sequence))



