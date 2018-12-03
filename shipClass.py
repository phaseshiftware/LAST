# Ship Class
# Common: Engine, Navigation
# Rooms: MedBay, Engine, Dorm, Navigation, Cargo, Holding Cell, Show
# Transport, Station, Scout, Fighter
ENGINE = 100

station = {}
transport = {'cargo1':'', 'cargo2':'', 'engine': ENGINE}

class Ship():
    def __init__(self, shipType):
        self.fuel = fuel
        self.health = health


    def leave(self):
        # none -> dict
        # Displays list of all rooms on the ship
        #!!!
        return {}

    def inspect(self):
        # none -> dict
        # Inspect the current room
        # Used to detect problems, and repairs
        #!!!
        return {}

    def talk(self):
        # none -> string
        # Engage in dialogue with crew members
        #!!!

        #if nobody else in the room..
        # display names of others in same room
        return {}

    def suit(self):
        # none -> dict
        # Configure space suit
        #!!!
        return {}
