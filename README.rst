=================
openexchangerates
=================

This is a simple python client implementation of https://openexchangerates.org
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

    >>> from openexchangerates import OpenExchangeRatesClient
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
