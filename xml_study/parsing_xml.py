#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
# -*- coding: utf-8 -*-
"""
Created on 01/Jul/2017 with PyCharm Community Edition
@title:  IMIR - parsing_xml
@author: rafaenune - Rafael Nunes - rnunes@cos.ufrj.br

"""
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
print('--- x ---')
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
print('--- x ---')
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

