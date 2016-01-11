#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Python library for Barchart API
http://freemarketdataapi.barchartondemand.com/.

Fix up Documentation HERE
"""

import os
import datetime
import requests
import six
from collections import OrderedDict

URL_BASE = 'http://marketdata.websol.barchart.com'
TIMESTAMP_FMT = '%Y-%m-%dT%H:%M:%S%z'
DATE_FMT = '%Y-%m-%d'
TIMESTAMP_NOSEP_FMT = '%Y%m%d%H%M%S'

try:
    API_KEY = os.environ['BARCHART_API_KEY']
except:
    API_KEY = ''


def _create_from(session):
    """
    Returns a requests.Session (if session is None)
    or session (requests_cache.CachedSession)
    """
    if session is None:
        return requests.Session()
    else:
        return session


def _parse_json_response(response):
    """
    Parse JSON response
    """
    status_code = response.status_code
    status_code_expected = 200
    if status_code == status_code_expected:
        response = response.json()
        try:
            if response['status']['code'] == status_code_expected:
                return response
            else:
                raise NotImplementedError("Error code: %d - %s" %
                                          (response['status']['code'], response['status']['message']))
        except Exception as e:
            raise e
    else:
        raise NotImplementedError("HTTP status code is %d instead of %d" %
                                  (status_code, status_code_expected))


def _parse_timestamp(results, cols, timestamp_fmt=TIMESTAMP_FMT):
    """
    Returns a result where string timestamps have been parsed
    """
    for col in cols:
        if isinstance(results, list):
            for result in results:
                s = result[col]
                result[col] = datetime.datetime.strptime(s[0:19] + s[19:].replace(':', ''), timestamp_fmt)
        else:
            s = results[col]
            results[col] = datetime.datetime.strptime(s[0:19] + s[19:].replace(':', ''), timestamp_fmt)
    return results


def _parse_date(results, cols, date_fmt=DATE_FMT):
    """
    Returns a result where string dates have been parsed
    """
    for col in cols:
        if isinstance(results, list):
            for result in results:
                s = result[col]
                result[col] = datetime.datetime.strptime(s, date_fmt).date()
        else:
            s = results[col]
            results[col] = datetime.datetime.strptime(s, date_fmt).date()
    return results


def getQuote(symbols, session=None):
    """
    Returns quote for one (or several) symbol(s)
    getQuote sample query:
        http://marketdata.websol.barchart.com/getQuote.json?key=YOURAPIKEY&symbols=BAC,IBM,GOOG,HBAN
    """
    endpoint = '/getQuote.json'
    url = URL_BASE + endpoint
    params = {
        'key': API_KEY,
        'symbols': ",".join(symbols) if isinstance(symbols, list) else symbols
    }
    session = _create_from(session)
    response = session.get(url, params=params)
    response = _parse_json_response(response)
    timestamp_cols = ['serverTimestamp', 'tradeTimestamp']
    results = response['results']
    if isinstance(symbols, six.string_types):
        d = results[0]
        d = _parse_timestamp(d, timestamp_cols)
        return d  # returns a dict
    else:
        for i, d in enumerate(results):
            d = _parse_timestamp(d, timestamp_cols)
        return results  # returns a list


def _getHistory_one_symbol(symbol, startDate, typ='daily', session=None):
    """
    getHistory sample query:
        http://marketdata.websol.barchart.com/getHistory.json?key=YOURAPIKEY&symbol=IBM&type=daily&startDate=20140928000000
    """

    endpoint = '/getHistory.json'
    url = URL_BASE + endpoint
    params = {
        'key': API_KEY,
        'symbol': symbol,
        'type': typ,
        'startDate': startDate
    }
    session = _create_from(session)
    response = session.get(url, params=params)
    response = _parse_json_response(response)
    d = response['results']
    timestamp_cols = ['timestamp']
    date_cols = ['tradingDay']
    d = _parse_timestamp(d, timestamp_cols)
    d = _parse_date(d, date_cols)
    return d


def getHistory(symbols, startDate, typ='daily', session=None):
    """
    Returns history for ONE (or SEVERAL) symbol(s)
    """
    try:
        startDate = startDate.strftime(TIMESTAMP_NOSEP_FMT)
    except Exception:
        # this should be logged and not catching everything
        pass

    d = OrderedDict()
    if isinstance(symbols, list):
        for symbol in symbols:
            d[symbol] = _getHistory_one_symbol(symbol, startDate, typ, session)
    else:
        d[symbols] = _getHistory_one_symbol(symbols, startDate, typ, session)

    return d  # returns an OrderedDict
