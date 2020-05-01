#!/usr/bin/env python3
'''This is a json tutorial script.'''
import json

DATA = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "int1",
    "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
  }
}
'''

INFO = json.loads(DATA)
print('INFO:', INFO)
print('Type INFO:', type(INFO))
print('Name:', INFO["name"])
print('Hide:', INFO["email"]["hide"])
print('Phone Number:', INFO["phone"]["number"])
print('Phone Type:', INFO["phone"]["type"])
print('Phone:', INFO["phone"])

print("json dump of INFO:")
print(json.dumps(INFO, indent=4))
