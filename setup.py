#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

package_name = "servy"
filename = package_name + ".py"


setup(
    name=package_name,
    version="1.0.2",
    author="@axbg && @StefanLazea",
    author_email="bisagalexstefan@gmail.com",
    description="your ultimate cli action tracking app",
    url="https://github.com",
    long_description="servy is a CLI app written in python & bash that helps a team to keep a clean history of its actions without leaving the terminal",
    packages=["py"],
    entry_points={
        "console_scripts": [
            "servy = py.servy:main"
        ]
    },
    license="MIT License",
)
