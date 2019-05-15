# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __repr__(self):

        output = ""
        output += "Name: " + self.name + "\n"
        output += "Room: " + self.room
        return output
