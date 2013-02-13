=================
openexchangerates
=================

This is a simple python client implementation of http://openexhangerates.org
web services.

Install
-------

openexchangerates is avaiable on pypi repositories. Just simply install
by using ``easy_install`` or ``pip``::

    $ pip install openexchangerates

Usage
-----

First of all, you have to sign up the service for an API key by visiting
https://openexchangerates.org

Then it is a matter of cake to start using the service::

    >>> from openexchangerate import OpenExchageRatesClient
    >>> client = OpenExchangeRatesClient('<YOUR_API_KEY>')
    >>> client.currencies()
    {'AED': 'United Arab Emirates Dirham',
    'AFN': 'Afghan Afghani',
    'ALL': 'Albanian Lek',
    'AMD': 'Armenian Dram',
    'ANG': 'Netherlands Antillean Guilder',
    'AOA': 'Angolan Kwanza',
    'ARS': 'Argentine Peso',
    'AUD': 'Australian Dollar',
    ...

    >>> client.latest()
    {'base': 'USD',
    'disclaimer': '<disclaimer>',
    'license': '<license>',
    'rates': {'AED': 3.672701,
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
    {'base': 'GBP',
    'disclaimer': '<disclaimer>',
    'license': '<license>',
    'rates': {'AED': 3.672701,
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