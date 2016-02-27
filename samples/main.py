#!/usr/bin/env python
# -*- coding: utf-8 -*-

from barchart import getHistory, getQuote, QUOTE_TIMESTAMP_COLS, QUOTE_DATE_COLS

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
print("=========================\n")

# Set Up Common Parameters
one_symbol = "IBM"
many_symbols = ["BAC", "IBM", "GOOG", "HBAN"]
startDate = datetime.date(year=2016, month=2, day=10)
quote_fields = [
    "previousTimestamp",
    "preMarketTimestamp",
    "afterHoursTimestamp",
    "fiftyTwoWkHighDate",
    "fiftyTwoWkLowDate",
    "exDividendDate",
    "twelveMnthPctDate",
    "tradeSize",
    "tick",
    "previousLastPrice",
    "bid",
    "bidSize",
    "ask",
    "askSize",
    "previousClose",
    "settlement",
    "previousSettlement",
    "openInterest",
    "fiftyTwoWkHigh",
    "fiftyTwoWkLow",
    "avgVolume",
    "sharesOutstanding",
    "dividendRateAnnual",
    "dividendYieldAnnual",
    "impliedVolatility",
    "twentyDayAvgVol",
    "twelveMnthPct",
    "preMarketPrice",
    "preMarketNetChange",
    "preMarketPercentChange",
    "afterHoursPrice",
    "afterHoursNetChange",
    "afterHoursPercentChange",
    "averageWeeklyVolume",
    "averageQuarterlyVolume",
    "exchangeMargin"
]

# getQuote with ONE symbol
print("{0} Quote".format(one_symbol))
print("=========")
quote = getQuote(one_symbol, fields=quote_fields, session=session)
for timestamp in QUOTE_TIMESTAMP_COLS:
    if timestamp in quote and quote[timestamp]:
        quote[timestamp] = quote[timestamp].isoformat()
for datefield in QUOTE_DATE_COLS:
    if datefield in quote and quote[datefield]:
        quote[datefield] = quote[datefield].isoformat()
print(pp.pprint(quote))

# getQuote with SEVERAL symbols
# =============================
print("\n{0} Quotes".format(many_symbols))
print("=====================================")
quotes = getQuote(many_symbols, fields=quote_fields, session=session)
for quote in quotes:
    for timestamp in QUOTE_TIMESTAMP_COLS:
        if timestamp in quote and quote[timestamp]:
            quote[timestamp] = quote[timestamp].isoformat()
    for datefield in QUOTE_DATE_COLS:
        if datefield in quote and quote[datefield]:
            quote[datefield] = quote[datefield].isoformat()
print(pp.pprint(quotes))

# getHistory with ONE symbol
# ==========================
print("\nHistory of {0} since {1}".format(one_symbol, startDate))
print("===============================")
history = getHistory(one_symbol, typ="daily", startDate=startDate, maxRecords=5, session=session)
for key, val in history.items():
    print("Symbol: {0}".format(key))
    for v in val:
        print("==========================")
        v["timestamp"] = v["timestamp"].isoformat()
        v["tradingDay"] = v["tradingDay"].isoformat()
        print(pp.pprint(v))

# getHistory with SEVERAL symbols
# ===============================
print("\nHistories of {0} since {1}".format(many_symbols, startDate))
histories = getHistory(many_symbols, typ="daily", startDate=startDate, maxRecords=5, order="desc", session=session)
for key, history in histories.items():
    print("============================================================")
    print("Symbol: {0}".format(key))
    for item in history:
        print("==========================")
        item["timestamp"] = item["timestamp"].isoformat()
        item["tradingDay"] = item["tradingDay"].isoformat()
        print(pp.pprint(item))
