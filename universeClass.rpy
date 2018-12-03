# A new instance of world is created when a new game begins.

init python:

    class Universe(object):
        '''Contains all celestial objects in the game.'''

        # Should be node like in structure
        # start with predifned hotspots, move onto random universe

        # Constructor
        def __init__(self, name="The Universe"):
            self.name = self

        def createGlobalAffection(self, lst, func):
            '''List -> Dictonary
             Runs createAffection() on every object in List.'''

            for g in lst:
                func
