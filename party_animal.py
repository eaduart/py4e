#!/usr/bin/env python3
'''This is a part of the example for the Using Databases with Python in
   Python for Everybody certification.'''

from random import choice

class PartyAnimal:
    '''The party_animal class.'''
    attendees = 0
    name = ""

    def __init__(self, name):
        self.attendees = 0
        self.name = name
        print(f'{self.name} says \'I am alive\' {id(self)}')

    def __del__(self):
        print(f'{id(self)} {self.name} says \'I\'m melting away\'')

    def howmany(self):
        '''How many party animals are attending.'''
        return self.attendees

    def party(self):
        '''Add another party animal to the class.'''
        self.attendees += 1
        print(f"So far {self.attendees}")


names = ['Fred', 'Wilma', 'Barney', 'Betty', 'Bambam', 'Pebbles', 'Dino' ]

AN = PartyAnimal('Dummy')

AN.party()
AN.party()
AN.party()

print(f"Type: {type(AN)}")
print(f"DIR: {dir(AN)}")

AN = 42
print(f'AN contians {AN}')

ANlst = []
[ ANlst.append(PartyAnimal(choice(names))) for x in range(10) ]

[ print(ANlst[i].name) for i in range(len(ANlst)) ]
