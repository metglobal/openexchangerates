import unittest
from decimal import Decimal

from httpretty import HTTPretty, httprettified

import openexchangerates

from datetime import date as Date

class TestOpenExchangeRates(unittest.TestCase):

    _FIXTURE_CURRENCIES = """{
    "AED": "United Arab Emirates Dirham",
    "AFN": "Afghan Afghani",
    "ALL": "Albanian Lek",
    "USD": "United States Dollar"
}
"""

    _FIXTURE_LATEST = """{
    "disclaimer": "<Disclaimer data>",
    "license": "<License data>",
    "timestamp": 1358150409,
    "base": "USD",
    "rates": {
        "AED": 3.666311,
        "AFN": 51.2281,
        "ALL": 104.748751,
        "USD": 1
    }
}
"""

    _FIXTURE_HISTORICAL = """{
    "disclaimer": "<Disclaimer data>",
    "license": "<License data>",
    "timestamp": 1358150409,
    "base": "USD",
    "rates": {
        "AED": 3.666311,
        "AFN": 51.2281,
        "ALL": 104.748751,
        "USD": 1
    }
}
"""

    @httprettified
    def test_historical(self):
        """Tests openexchangerates.OpenExchangeRateClient.historical``"""
        client = openexchangerates.OpenExchangeRatesClient('DUMMY_API_KEY')
        date = Date.fromtimestamp(1358150409)
        HTTPretty.register_uri(HTTPretty.GET, client.ENDPOINT_HISTORICAL %
                               date.strftime("%Y-%m-%d"),
                               body=self._FIXTURE_LATEST)
        historical = client.historical(date)
        self.assertIn('rates', historical)
        rates = historical['rates']
        self.assertEqual(len(rates), 4)
        self.assertIn('AED', rates)
        self.assertEqual(rates['AED'], Decimal('3.666311'))
        self.assertIn('AFN', rates)
        self.assertEqual(rates['AFN'], Decimal('51.2281'))
        self.assertIn('ALL', rates)
        self.assertEqual(rates['ALL'], Decimal('104.748751'))
        self.assertIn('USD', rates)
        self.assertEqual(rates['USD'], Decimal('1'))

    @httprettified
    def test_currencies(self):
        """Tests ``openexchangerates.OpenExchangeRateClient\.currencies``"""
        client = openexchangerates.OpenExchangeRatesClient('DUMMY_API_KEY')
        HTTPretty.register_uri(HTTPretty.GET, client.ENDPOINT_CURRENCIES,
                               body=self._FIXTURE_CURRENCIES)
        currencies = client.currencies()
        self.assertEqual(len(currencies), 4)
        self.assertIn('AED', currencies)
        self.assertIn('AFN', currencies)
        self.assertIn('ALL', currencies)
        self.assertIn('USD', currencies)

    @httprettified
    def test_latest(self):
        """Tests openexchangerates.OpenExchangeRateClient.latest``"""
        client = openexchangerates.OpenExchangeRatesClient('DUMMY_API_KEY')
        HTTPretty.register_uri(HTTPretty.GET, client.ENDPOINT_LATEST,
                               body=self._FIXTURE_LATEST)
        latest = client.latest()
        self.assertIn('rates', latest)
        rates = latest['rates']
        self.assertEqual(len(rates), 4)
        self.assertIn('AED', rates)
        self.assertEqual(rates['AED'], Decimal('3.666311'))
        self.assertIn('AFN', rates)
        self.assertEqual(rates['AFN'], Decimal('51.2281'))
        self.assertIn('ALL', rates)
        self.assertEqual(rates['ALL'], Decimal('104.748751'))
        self.assertIn('USD', rates)
        self.assertEqual(rates['USD'], Decimal('1'))


    @httprettified
    def test_latest_with_local_base_conversion(self):
        client = openexchangerates.OpenExchangeRatesClient('DUMMY_API_KEY')
        HTTPretty.register_uri(HTTPretty.GET, client.ENDPOINT_LATEST,
                               body=self._FIXTURE_LATEST)
        rates = client.latest(local_base='AED')['rates']
        self.assertEqual(rates['AED'], Decimal('1'))
        self.assertEqual(rates['AFN'], Decimal('13.97265535'))
        self.assertEqual(rates['ALL'], Decimal('28.57061253'))
        self.assertEqual(rates['USD'], Decimal('0.27275373'))


    @httprettified
    def test_historical_with_local_base_conversion(self):
        client = openexchangerates.OpenExchangeRatesClient('DUMMY_API_KEY')
        date = Date.fromtimestamp(1358150409)
        HTTPretty.register_uri(HTTPretty.GET, client.ENDPOINT_HISTORICAL %
                               date.strftime("%Y-%m-%d"),
                               body=self._FIXTURE_HISTORICAL)
        rates = client.historical(date, local_base='AED')['rates']
        self.assertEqual(rates['AED'], Decimal('1'))
        self.assertEqual(rates['AFN'], Decimal('13.97265535'))
        self.assertEqual(rates['ALL'], Decimal('28.57061253'))
        self.assertEqual(rates['USD'], Decimal('0.27275373'))


    @httprettified
    def test_exception(self):
        """Tests ``openexchangerates.OpenExchangeRateClientException``"""
        client = openexchangerates.OpenExchangeRatesClient('DUMMY_API_KEY')
        HTTPretty.register_uri(HTTPretty.GET, client.ENDPOINT_LATEST,
                               status=404)
        with(self.assertRaises(
                openexchangerates.OpenExchangeRatesClientException)) as e:
            client.latest()
