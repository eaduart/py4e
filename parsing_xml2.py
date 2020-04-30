#!/usr/bin/env python3
'''Second example on parsing xml.'''

import xml.etree.ElementTree as ET
INPUT = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>
'''

STUFF = ET.fromstring(INPUT)
LST = STUFF.findall('users/user')
print('User count', len(LST))
for item in LST:
    print('Name: ', item.find('name').text)
    print('Id: ', item.find('id').text)
    print('Attribute: ', item.get("x"))
