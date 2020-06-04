# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def __str__(self):
        return f'\n{self.__class__.__name__} {self.name} <{", ".join(item.name for item in self.items)}>\
            location: {self.location}'