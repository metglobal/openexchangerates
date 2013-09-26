from setuptools import setup

import openexchangerates

setup(
    name='openexchangerates',
    version=openexchangerates.__version__,
    description='openexchangerates.org python API client',
    long_description=open('README.rst').read(),
    url='https://github.com/metglobal/openexchangerates',
    license=openexchangerates.__license__,
    author=openexchangerates.__author__,
    author_email='kadir.pekel@metglobal.com',
    packages=['openexchangerates'],
    install_requires=[
        'requests',
    ],
    tests_require=[
        'httpretty',
        'mock'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
