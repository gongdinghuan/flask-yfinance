#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name='flask-yfinance',
    version='1.0.0',
    description='Flask application for yfinance data visualization',
    long_description='A Flask web application that provides visualization for financial market data using yfinance library',
    author='Your Name',
    author_email='contact@example.com',
    url='https://github.com/yourusername/flask-yfinance',
    license='Apache',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==3.1.2',
        'Flask-CORS==6.0.2',
        'yfinance==1.0',
        'pandas>=1.3.0',
        'numpy>=1.16.5',
        'requests>=2.31',
        'multitasking>=0.0.7',
        'platformdirs>=2.0.0',
        'pytz>=2022.5',
        'frozendict>=2.3.4',
        'beautifulsoup4>=4.11.1',
        'peewee>=3.16.2',
        'curl_cffi>=0.7,<0.14',
        'protobuf>=3.19.0',
        'websockets>=13.0',
    ],
    entry_points={
        'console_scripts': [
            'flask-yfinance=run:app',
        ],
    },
    zip_safe=False,
)
