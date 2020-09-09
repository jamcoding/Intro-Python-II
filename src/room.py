# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def moveRooms(self, user_input):
        if user_input == "n":
            return self.n_to
        if user_input == "e":
            return self.e_to
        if user_input == "s":
            return self.s_to
        elif user_input == "w":
            return self.w_to
        else:
            pass