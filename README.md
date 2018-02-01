## Python client for Barchart OnDemand


Get a free API key at:

 - http://freemarketdataapi.barchartondemand.com/

### Currently supports

* getHistory
* getQuote
* getFinancialHighlights (requires paid license key)

### Example Code

[See how to use the client in your project here](https://github.com/lanshark/barchart-ondemand-client-python/blob/master/samples/main.py).

To set the API_KEY for these applications, set an environment variable as follows:

    export BARCHART_API_KEY="xxxxxxxxxxxxxxxxxxxx"

To set the URL_BASE (ondemand or marketdata) for these applications, set an environment variable as follows:

    export BARCHART_URL_BASE="marketdata.websol.barchartondemand.com"

To enable the Financial Highlights (paid key required):

    export BARCHART_USE_HIGHLIGHTS=True

### Additional remarks

This project is not a [Barchart](http://www.barchartondemand.com/) project.  This project was forked from [femtotrader's](http://github.com/femtotrader) project and extended/modified.

Use it at your own risk.

Some Barchart projects are available at https://github.com/barchart/
