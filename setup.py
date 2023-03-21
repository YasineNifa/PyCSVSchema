#!/usr/bin/python
# -*-coding: utf-8 -*-

from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pycsvschema",
    version="0.1.0",
    description="PyCSVSchema is an implementation of CSV Schema in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Guangyang Li",
    author_email="mail@guangyangli.com",
    license="MIT",
    packages=["pycsvschema", "pycsvschema.validators"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="csv schema json jsonschema validation validator",
    url="https://github.com/csv-schema/PyCSVSchema",
    install_requires=["jsonschema", "rfc3986", "pycountry"],
    package_data={"pycsvschema": ["schema.json"]},
    include_package_data=True,
)
