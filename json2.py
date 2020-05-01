'''This is a json problem. Notice the nice pprint usage to lay out the
   data structureof what is retrieved.'''

import json
from pprint import pprint
import sys

DATA = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

try:
    INFO = json.loads(DATA)
except json.decoder.JSONDecodeError:
    print('ERROR: json.decoder.JSONDecodeError')
    sys.exit(1)

print('User count:', len(INFO))

pprint(INFO)

for item in INFO:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
