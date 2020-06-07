# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f'\n{self.__class__.__name__} {self.name}, {self.current_room}'

    def print_inventory(self):
        print(f'{"".join(str(item) for item in self.items)}' if len(self.items) > 0 else "You aren't carrying anything.")
        return

    def get(self, item):
        self.items.append(item)
        return
    
    def drop(self,item):
        self.items.remove(item)
        return