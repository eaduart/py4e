#!/usr/bin/env python3
'''This is a part of the example for the Using Databases with Python in
   Python for Everybody certification.'''


class PartyAnimal:
    '''The party_animal class.'''
    attendees = 0

    def __init__(self):
        self.attendees = 0

    def howmany(self):
        '''How many party animals are attending.'''
        return self.attendees

    def party(self):
        '''Add another party animal to the class.'''
        self.attendees += 1
        print(f"So far {self.attendees}")


AN = PartyAnimal()

AN.party()
AN.party()
AN.party()
