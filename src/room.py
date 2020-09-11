# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    
    def __init__(self, room_name, description, items=[]):
        self.room_name = room_name
        self.description = description
        self.items = items

    def display_items(self):
        pass

    def __str__(self):
        # Change to fit certain rooms
        #if room == treasure
        if len(self.items) == 0:
            return f'''
{self.room_name} - {self.description}

There are no items in this room.
'''
        else:
            return f'''
{self.room_name} - {self.description}

In this room you see {', '.join(self.items)}.
'''

    def __repr__(self):
        # Change to fit certain rooms
        #if room == treasure
        return f'<{self.room_name} - {self.description} - {self.items}>'
