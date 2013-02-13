from setuptools import setup

setup(
    name='openexchangerates',
    py_modules=['openexchangerates'],
    version='0.0.1',
    description='openexchangerates.org python API client',
    author='Metglobal',
    author_email='kadir.pekel@metglobal.com',
    url='https://github.com/metglobal/openexchangerates',
    install_requires=[
        'requests',
    ],
    tests_require=[
        'httpretty',
        'mock'
    ],
)
