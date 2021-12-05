#!/usr/bin/env python
########################################
#       tool name : port scaner        #
#  ----------------------------------  #
#                                      #
#   create by : #a409                  #
#   my chanell: t.me/ashrarhack_apps   #
#                                      #
#                       version : 1.09 #
########################################

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='port_scaner',
    packages=[
        'port_scaner',
        'port_scaner.static'
    ],
    package_data = {
        'port_scaner.static': ['*.txt']
    },
    version='1.09',
    description='An port scaner.',
########################################
#       tool name : port scaner        #
#  ----------------------------------  #
#                                      #
#   create by : #a409                  #
#   my chanell: t.me/ashrarhack_apps   #
#                                      #
#                       version : 1.09 #
########################################

    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Unlicense',
#https://github.com/ashrarhacka409/port_scaner/tree/main
    url='https://github.com/ashrarhacka409/port_scaner',
    author='a409',
    author_chanell='t.me/ashrarhack_apps',
    entry_points={
        'console_scripts': [
            'scanless = port_scaner.cli:main',
        ]
    },
########################################
#       tool name : port scaner        #
#  ----------------------------------  #
#                                      #
#   create by : #a409                  #
#   my chanell: t.me/ashrarhack_apps   #
#                                      #
#                       version : 1.09 #
########################################

    install_requires=[
        'beautifulsoup4',
        'crayons',
        'requests'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: Public Domain',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Security'
    ]
)
########################################
#       tool name : port scaner        #
#  ----------------------------------  #
#                                      #
#   create by : #a409                  #
#   my chanell: t.me/ashrarhack_apps   #
#                                      #
#                       version : 1.09 #
########################################
