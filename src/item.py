# Item class
# Should have:
#   1. name (one word)
#   2. description

class Item:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<{self.name} - {self.description}>'
    
    def __str__(self):
        return f'''
        Item name: {self.name}
        Item description: {self.description}
        '''