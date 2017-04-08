#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re

"""

Count certain regular expression patterns in the OSM file tags.

"""


lower = re.compile(r'^([0-9a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([0-9a-z]|_|-)*$')
upper = re.compile(r'^([A-Z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


OSMFILE = 'riyadh_saudiArabia_map.osm'


def key_type(element, keys):
    if element.tag == "tag":
        if lower.search(element.attrib['k']):
            keys['lower'] += 1
            # print('lower: ' + element.attrib['k'])
        elif lower_colon.search(element.attrib['k']):
            keys['lower_colon'] += 1
            # print('lower_col: ' + element.attrib['k'])
        elif upper.search(element.attrib['k']):
            keys['upper'] += 1
            # print('upper: ' + element.attrib['k'])
        elif problemchars.search(element.attrib['k']):
            keys['problemchars'] += 1
            # print('prob: ' + element.attrib['k'])
        else:
            # print('other--  ' + element.attrib['k'])
            keys['other'] += 1
    return keys



def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "upper":0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys


if __name__ == "__main__":
    pm = process_map(OSMFILE)
    pprint.pprint(pm)
