#!/usr/bin/env python
# -*- coding: utf-8 -*-

from barchart import getHistory, getQuote

# API key setup
# =============
# barchart.API_KEY = "YOURAPIKEY"
# You can also set an environment variable using Bash
# export BARCHART_API_KEY="YOURAPIKEY"


# requests_cache is optional
# use it to have a cache mechanism
# a session parameter can be pass to functions
# =============================================
import datetime
import pprint
import requests_cache
#session = requests_cache.CachedSession(cache_name="cache",
#                                       backend="sqlite", expire_after=datetime.timedelta(days=1))
session = None  # pass a None session to avoid caching queries

pp = pprint.PrettyPrinter(indent=4)

print("\nTest BarchartOnDemand API")
print("===========================\n")

# Set Up Common Parameters
one_symbol = "IBM"
many_symbols = ["BAC", "IBM", "GOOG", "HBAN"]
startDate = datetime.date(year=2016, month=2, day=10)

# getQuote with ONE symbol
print("{0} Quote".format(one_symbol))
print("=========")
quote = getQuote(one_symbol, session=session)
quote["tradeTimestamp"] = quote["tradeTimestamp"].isoformat()
quote["serverTimestamp"] = quote["serverTimestamp"].isoformat()
print(pp.pprint(quote))

# getQuote with SEVERAL symbols
# =============================
print("\n{0} Quotes".format(many_symbols))
print("=====================================")
quotes = getQuote(many_symbols, session=session)
for quote in quotes:
    quote["tradeTimestamp"] = quote["tradeTimestamp"].isoformat()
    quote["serverTimestamp"] = quote["serverTimestamp"].isoformat()
print(pp.pprint(quotes))

# getHistory with ONE symbol
# ==========================
print("\nHistory of {0} since {1}".format(one_symbol, startDate))
print("===============================")
history = getHistory(one_symbol, typ="daily", startDate=startDate, session=session)
print(pp.pprint(history))

# getHistory with SEVERAL symbols
# ===============================
print("Histories of {0} since {1}".format(many_symbols, startDate))
histories = getHistory(many_symbols, typ="daily", startDate=startDate, session=session)
for key, history in histories.items():
    print("============================================================")
    print("Key: {0}".format(key))
    for item in history:
        print(pp.pprint(item))
