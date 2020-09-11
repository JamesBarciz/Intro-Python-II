# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, name, cur_room, items=[]):
        self.name = name
        self.cur_room = cur_room
        self.items = items

    def drop_item(self, item):
        self.items.remove(str(item))

    def pick_up_item(self):
        pass

    def __str__(self):
        return f'''
{self.name} is currently in {self.cur_room}.

Inventory: {self.items}

'''
    
    def __repr__(self):
        return f'{self.name}, {self.cur_room}'
