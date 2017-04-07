import decimal
import six

import requests

__version__ = '0.1.0'
__author__ = 'Metglobal'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 Metglobal'


class OpenExchangeRatesClientException(requests.exceptions.RequestException):
    """Base client exception wraps all kinds of ``requests`` lib exceptions"""
    pass


class OpenExchangeRatesClient(object):
    """This class is a client implementation for openexchangerate.org service

    """
    BASE_URL = 'http://openexchangerates.org/api'
    ENDPOINT_LATEST = BASE_URL + '/latest.json'
    ENDPOINT_CURRENCIES = BASE_URL + '/currencies.json'
    ENDPOINT_HISTORICAL = BASE_URL + '/historical/%s.json'

    def __init__(self, api_key):
        """Convenient constructor"""
        self.client = requests.Session()
        self.client.params.update({'app_id': api_key})

    def _parsed_response(self, response, local_base=None):
        data = response.json(parse_int=decimal.Decimal,
                             parse_float=decimal.Decimal)

        if local_base:
            return self._local_conversion(data, local_base)
        else:
            return data

    def _local_conversion(self, data, base):
        """Change base using local conversion, only useful for the free plan
        """
        data['base'] = base
        new_rates = {}
        for curr, value in six.iteritems(data['rates']):
            new_rates[curr] = round(value / data['rates'][base], 8)

        data['rates'] = new_rates
        return data

    def latest(self, base='USD', local_base=None):
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
            resp = self.client.get(self.ENDPOINT_LATEST, params={'base': base})
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise OpenExchangeRatesClientException(e)
        return self._parsed_response(resp, local_base)

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

    def historical(self, date, base='USD', local_base=None):
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
            resp = self.client.get(self.ENDPOINT_HISTORICAL %
                                   date.strftime("%Y-%m-%d"),
                                   params={'base': base})
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise OpenExchangeRatesClientException(e)
        return self._parsed_response(resp, local_base)

