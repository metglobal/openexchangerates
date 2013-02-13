=================
openexchangerates
=================

This is a simple python client implementation og openexhangerates.org services.

Usage
-----

First of all, you have to obtain an API key by visiting
https://openexchangerates.org

Then it is a matter of cake to start using the service::

    >>> from openexchangerate import OpenExchageRatesClient
    >>> client = OpenExchangeRatesClient('<YOUR_API_KEY>')
    >>> client.currencies()
    {'AED': 'United Arab Emirates Dirham',
    'AFN': u'Afghan Afghani',
    'ALL': u'Albanian Lek',
    'AMD': u'Armenian Dram',
    'ANG': u'Netherlands Antillean Guilder',
    'AOA': u'Angolan Kwanza',
    'ARS': u'Argentine Peso',
    'AUD': u'Australian Dollar',
    ...

    >>> client.latest()
    {'base': u'USD',
    'disclaimer': u'<disclaimer>',
    'license': u'<license>',
    'rates': {u'AED': 3.672701,
        'AFN': 51.621833,
        'ALL': 104.032,
        'AMD': 406.489997,
        'ANG': 1.7888,
        'AOA': 95.936967,
        'ARS': 4.995484,
        'AUD': 0.966637,
        ...

You are also free to select base currency (Supported by non-free licenses)::

    >>> client.latest(base='GBP')
    {'base': u'GBP',
    'disclaimer': u'<disclaimer>',
    'license': u'<license>',
    'rates': {u'AED': 3.672701,
        'AFN': 51.621833,
        'ALL': 104.032,
        'AMD': 406.489997,
        'ANG': 1.7888,
        'AOA': 95.936967,
        'ARS': 4.995484,
        'AUD': 0.966637,
        ...

License
-------
Copyright (c) 2013 Metglobal LLC.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the 'Software'), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.