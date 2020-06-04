# Implement a class to hold room information. This should have name and
# description attributes.

# The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        output = f"{seld.name}, {self.description}"
        return output
