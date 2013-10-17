__author__ = 'yyyar'

import datetime

from flask import Flask

from pyappi import Pyappi
from pyappi.serializers import json
from pyappi.formatters import simple_formatter
from pyappi.helpers import int_convert, date_current, date_convert
from pyappi.helpers.presets import limitable
from pyappi.adapters import flask_adapter


app = Flask(__name__)

appi = Pyappi(formatter=simple_formatter,
              adapter=flask_adapter,
              serializer=json)

@app.route("/")
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

@app.errorhandler(500)
def internal_error(error):
    return str(error)

if __name__ == "__main__":
    app.run(debug=True)
