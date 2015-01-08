from setuptools import setup

setup(
    name='openexchangerates',
    version='0.1.1',
    description='openexchangerates.org python API client',
    long_description=open('README.rst').read(),
    url='https://github.com/metglobal/openexchangerates',
    license='MIT',
    author='Metglobal',
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
