__author__ = 'yyyar'


import datetime

#-- Defaulters

def date_current(f, days_interval=0):
    return lambda: (datetime.datetime.now() + datetime.timedelta(days=days_interval)).strftime(f)
