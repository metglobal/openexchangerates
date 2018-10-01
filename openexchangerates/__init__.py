import decimal

import requests

__version__ = "0.1.0"
__author__ = "Metglobal"
__license__ = "MIT"
__copyright__ = "Copyright 2013 Metglobal"


class OpenExchangeRatesClientException(requests.exceptions.RequestException):
    """Base client exception wraps all kinds of ``requests`` lib exceptions"""

    pass


class OpenExchangeRatesClient(object):
    """This class is a client implementation for openexchangerate.org service

    """

    BASE_URL = "http://openexchangerates.org/api"
    ENDPOINT_LATEST = BASE_URL + "/latest.json"
    ENDPOINT_CURRENCIES = BASE_URL + "/currencies.json"
    ENDPOINT_HISTORICAL = BASE_URL + "/historical/%s.json"
    ENDPOINT_TIME_SERIES = BASE_URL + "/time-series.json"

    def __init__(self, api_key):
        """Convenient constructor"""
        self.client = requests.Session()
        self.client.params.update({"app_id": api_key})

    def latest(self, base="USD"):
        """Fetches latest exchange rate data from service

        :Example Data:
            {
                disclaimer: "<Disclaimer data>",
                license: "<License data>",
                timestamp: 1358150409,
                base: "USD",
                rates: {
                    AED: 3.666311,
                    AFN: 51.2281,
                    ALL: 104.748751,
                    AMD: 406.919999,
                    ANG: 1.7831,
                    ...
                }
            }
        """
        try:
            resp = self.client.get(self.ENDPOINT_LATEST, params={"base": base})
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise OpenExchangeRatesClientException(e)
        return resp.json(parse_int=decimal.Decimal, parse_float=decimal.Decimal)

    def currencies(self):
        """Fetches current currency data of the service

        :Example Data:

        {
            AED: "United Arab Emirates Dirham",
            AFN: "Afghan Afghani",
            ALL: "Albanian Lek",
            AMD: "Armenian Dram",
            ANG: "Netherlands Antillean Guilder",
            AOA: "Angolan Kwanza",
            ARS: "Argentine Peso",
            AUD: "Australian Dollar",
            AWG: "Aruban Florin",
            AZN: "Azerbaijani Manat"
            ...
        }
        """
        try:
            resp = self.client.get(self.ENDPOINT_CURRENCIES)
        except requests.exceptions.RequestException as e:
            raise OpenExchangeRatesClientException(e)

        return resp.json()

    def historical(self, date, base="USD"):
        """Fetches historical exchange rate data from service

        :Example Data:
            {
                disclaimer: "<Disclaimer data>",
                license: "<License data>",
                timestamp: 1358150409,
                base: "USD",
                rates: {
                    AED: 3.666311,
                    AFN: 51.2281,
                    ALL: 104.748751,
                    AMD: 406.919999,
                    ANG: 1.7831,
                    ...
                }
            }
        """
        try:
            resp = self.client.get(
                self.ENDPOINT_HISTORICAL % "{0:%Y-%m-%d}".format(date),
                params={"base": base},
            )
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise OpenExchangeRatesClientException(e)
        return resp.json(parse_int=decimal.Decimal, parse_float=decimal.Decimal)

    def time_series(self, start, end, base="EUR"):
        """Fetches historical exchange rate data from service

        :Example Data:
            {
                disclaimer: "<Disclaimer data>",
                license: "<License data>",
                "start_date": "2018-09-01",
                "end_date": "2018-09-04",
                "base": "USD",
                "rates": {
                    "2018-09-01": {
                        "BRL": 4.055308,
                        "EUR": 0.8612,
                        "GBP": 0.771545
                    },
                    "2018-09-02": {
                        "BRL": 4.055175,
                        "EUR": 0.862199,
                        "GBP": 0.773893
                    },
                    "2018-09-03": {
                        "BRL": 4.156288,
                        "EUR": 0.860993,
                        "GBP": 0.777115
                    },
                    "2018-09-04": {
                        "BRL": 4.1565,
                        "EUR": 0.863017,
                        "GBP": 0.777736
                    }
                }
            }
        """
        try:
            resp = self.client.get(
                self.ENDPOINT_TIME_SERIES,
                params={
                    "start": "{0:%Y-%m-%d}".format(start),
                    "end": "{0:%Y-%m-%d}".format(end),
                    "base": base,
                },
            )
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise OpenExchangeRatesClientException(e)
        return resp.json(parse_int=decimal.Decimal, parse_float=decimal.Decimal)
