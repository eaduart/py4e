#!/usr/bin/env python3
'''This is an example of codethat parses xml.'''

import xml.etree.ElementTREE as ET
DATA = '''<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>'''

TREE = ET.fromstring(DATA)
print('Name:', TREE.find('name').text)
print('Attr:', TREE.find('email').get('hide'))
