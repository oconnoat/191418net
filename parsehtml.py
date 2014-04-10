#!/usr/bin/python

# -*- coding: utf-8 -*-

import os
import sys

from bs4 import BeautifulSoup

__author__ = "Alexander O'Connor <oconnoat@gmail.com>"
__copyright__ = "Copyright 2012, Alexander O'Connor <oconnoat@gmail.com>"
__credits__ = ["Alexander O'Connor <oconnoat@gmail.com>"]
__license__ = "Copyright"
__version__ = "0.1"
__email__ = "Alexander O'Connor <oconnoat@gmail.com>"
__status__ = "Prototype"

def parse_battle(paths):
    """take a list of file paths and output the xml version"""
    for filename in paths:
        soup = BeautifulSoup(open(filename))
        inside_div = soup.find("div", class_="inside")
        print 'title %s' % inside_div.find('h1').text
        print inside_div

if __name__=="__main__":
    parse_battle(['data/bat30.htm'])



