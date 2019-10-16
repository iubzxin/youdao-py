# -*- coding:utf-8 -*-

import setuptools
from distutils.core import setup

setup(
    name='youdao-py',
    version='0.0.1',
    author='iubzxin',
    author_email='641015302@qq.com',
    url='https://github.com/iubzxin/youdao-py',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    zip_safe=True,
)