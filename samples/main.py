#!/usr/bin/env python
# -*- coding: utf-8 -*-

from barchart import getHistory, getQuote

# API key setup
# =============
# barchart.API_KEY = 'YOURAPIKEY'
# You can also set an environment variable using Bash
# export BARCHART_API_KEY="YOURAPIKEY"


# requests_cache is optional
# use it to have a cache mechanism
# a session parameter can be pass to functions
# =============================================
import datetime
import pprint
import requests_cache
session = requests_cache.CachedSession(cache_name='cache',
                                       backend='sqlite', expire_after=datetime.timedelta(days=1))
# session = None # pass a None session to avoid caching queries

pp = pprint.PrettyPrinter(indent=4)

print('\nTest BarchartOnDemand API')
print('===========================\n')

# Set Up Common Parameters
one_symbol = "IBM"
many_symbols = ["BAC", "IBM", "GOOG", "HBAN"]
startDate = datetime.date(year=2015, month=12, day=15)

# getQuote with ONE symbol
print('%s Quote' % (one_symbol,))
print('=========')
quote = getQuote(one_symbol, session=session)
quote['tradeTimestamp'] = quote['tradeTimestamp'].isoformat()
quote['serverTimestamp'] = quote['serverTimestamp'].isoformat()
print(pp.pprint(quote))

# getQuote with SEVERAL symbols
# =============================
print('\n%s Quotes' % (many_symbols,))
print('=====================================')
quotes = getQuote(many_symbols, session=session)
for quote in quotes:
    quote['tradeTimestamp'] = quote['tradeTimestamp'].isoformat()
    quote['serverTimestamp'] = quote['serverTimestamp'].isoformat()
print(pp.pprint(quotes))

# getHistory with ONE symbol
# ==========================
print('\nHistory of %s since %s' % (one_symbol, startDate,))
print('===============================')
history = getHistory(one_symbol, typ='daily', startDate=startDate, session=session)
print(type(history))
for symbol in history:
    for day in symbol:
        print(day)
        # day['tradeTimestamp'] = day['tradeTimestamp'].isoformat()
print(pp.pprint(history))

# getHistory with SEVERAL symbols
# ===============================
print('Histories of %s since %s' % (many_symbols, startDate,))
print('============================================================')
histories = getHistory(many_symbols, typ='daily', startDate=startDate, session=session)
print(type(histories))
for symbol in histories:
    for day in symbol:
        print(day)
        # day['tradeTimestamp'] = day['tradeTimestamp'].isoformat()
print(pp.pprint(histories))
