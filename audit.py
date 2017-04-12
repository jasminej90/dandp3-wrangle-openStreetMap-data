#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""

Audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
street names.

"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE_PATH = open("riyadh_saudiArabia_map.osm", "r")

OSMFILE = "riyadh_saudiArabia_map.osm"

problemchars = re.compile(r'\,|\.\b')
street_type_re = re.compile(r'\b[a-zA-Z]+\.?$', re.IGNORECASE)
street_start_re = re.compile(r'^[a-zA-Z]+', re.IGNORECASE)
street_type_ar_re = re.compile(r'([\u0621-\u06FF]+)')


expected = ["Road", "Street", "Prince"]

discard = ["terminal 1", "no name", "P.O. Box", "infront of riyadh galleria", "K.K.I.A"]

mapping = { "St": "Street",
            "St.": "Street",
            "street": "Street",
            "Rd" : "Road",
            "road" : "Road",
            "Ath Thumamah Rd, Ar Rabi, Riyadh 13315" : "Ath Thumamah Road",
            "Salim Ibn Maqil, An Nakhil" : "Salim Ibn Maqil Street",
            "Uthman Ibn Affan Branch Rd, At Taawun, Riyadh 12478" : "Uthman Ibn Affan Branch Road",
            "No. 6" : "6th Street",
            "Abdulaziz" : "Abdul Aziz",
            "Pr." : "Prince",
            "Exit 5, King Abdulaziz Road - North Ring Road (west)" : "Exit 5, King Abdul Aziz Road",
            "Prince Faisal Ibn Turki Ibn Abdulaziz, Al Murabba, Riyadh 12612, Saudi Arabia" : "Prince Faisal Ibn Turki Ibn Abdulaziz"
            }

def audit_street_type(prob_streets, street_types, street_name):

	if problemchars.search(street_name):
		prob_streets[problemchars.search(street_name).group()].add(street_name)

	else:
		m = street_type_re.search(street_name)
		if m:
			street_type = m.group()
			if street_type not in expected:
				street_types[street_type].add(street_name)

def audit_street_start(street_starts, street_name):
	m = street_start_re.search(street_name)
	if m:
		street_start = m.group()
		if street_start not in expected:
			street_starts[street_start].add(street_name)

def is_street_name(elem):
	return (elem.attrib['k'] == "addr:street")

def merge_two_dicts(x, y):
	z = x.copy()
	z.update(y)
	return z


def audit(osmfile):
    street_types = defaultdict(set)
    prob_streets = defaultdict(set)
    street_starts = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(prob_streets, street_types, tag.attrib['v'])
                    audit_street_start(street_starts, tag.attrib['v'])
    osm_file.close()

    d = merge_two_dicts(merge_two_dicts(prob_streets, street_types), street_starts)
    return d

def string_case(s):
    if s.isupper():
        return s
    else:
        return s.title()

def update_name(name, mapping):

	if name in mapping:
		name = mapping[name]

	else:
	    name = name.split(' ')

	    for i in range(len(name)):
	        if name[i] in mapping:
	        	name[i] = mapping[name[i]]
	        	name[i] = string_case(name[i])
	        else:
	            name[i] = string_case(name[i])

	    # is last word is street?
	    if (name[len(name) - 1] not in expected) & ('Road' not in ' '.join(name)):
	    	name = ' '.join(name) + " Street"
	    else:
	    	name = ' '.join(name)

	return name


if __name__ == '__main__':
	aud = audit(OSMFILE)
	# pprint.pprint(aud)

	for st_type, ways in aud.items():
		for name in ways:
			if name not in discard:
				better_name = update_name(name, mapping)
				print (name, "=>", better_name)

