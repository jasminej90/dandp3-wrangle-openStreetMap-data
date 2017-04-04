#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Parse OSM map file using ET iterative parsing 

"""
import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict

OSMFILE = 'riyadh_saudiArabia_map.osm'

def count_tags(filename):
        count = defaultdict(int)
        for event, node in ET.iterparse(filename):
            if event == 'end':
                count[node.tag] += 1
            node.clear()
        return count
    

if __name__ == "__main__":
    ct = count_tags(OSMFILE)
    pprint.pprint(ct)