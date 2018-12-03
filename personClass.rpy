# Person Class
# Generator for characters in the universe

init python:

    races = ('Human', 'Mech Doll', 'Hybrid')
    jobs = ('Pilot', 'Mechanic', 'Engineer', 'Medic', 'Soldier', 'Scientist')
    names = ('Katie', 'Susann', 'Sara', 'Beth', 'Carly', 'Nikki', 'Amber',
    'Amy', 'Elizabeth', 'Michelle', 'Laura', 'Amanda', 'Joline', 'Kate',
    'Danielle', 'Erin', 'Olivia', 'Nancy', 'Annie', 'Kira', 'Star', 'Ashley',
    'Alex', 'Candi', 'Rose', 'Tamara', 'Miranda', 'Hitomi', 'Sharon', 'Doris',
    'Rey', 'Marcy', 'Tanya', 'Carla', 'Jenni', 'Fox', 'Hannah', 'Wendy',
    'Emma', 'Lucy', 'Brandy', 'Krystal', 'Kristen', 'Kelly', 'Rebecca',
    'Karen', 'Artemis', 'Monica', 'Sasha', 'Mily')

    class Person(object):
        def __init__(self, name="Name", race="Race", job="Job"):
            '''Crew descrition'''
            self.name = name
            self.race = race
            self.job = job
            self.character = Character(self.name)

        def getStatus(self):
            '''none -> string
            Displays status info to the user'''
            renpy.say(self.character, 'Name ' + self.name + ' Job ' + self.job
             + ' Race ' + self.race)

        def basicCrew(self, num):
            '''number -> list
            Generates crew with one of each job type'''
            crew = []

            for x in range(num):
                name = renpy.random.chocie(names)
                job = jobs[x]
                race = renpy.random.choice(races)

                obj = Person(name, race, job)
                crew.append(obj)

            return crew

        def randomCrew(self, num):
            '''number -> list
            Generates crew with random stats'''
            crew = []

            for x in range(num):
                name = renpy.random.choice(names)
                job = renpy.random.choice(jobs)
                race = renpy.random.choice(races)

                obj = Person(name, race, job)
                crew.append(obj)

            return crew

        def customCrew(self, num):
            '''number -> list
            User defined crew'''
            #!!! to-do
            crew = []

            for x in range(num):
                # prompt user for this info, capitalize job/race
                # !!! prompt in renpy...
                #name = choice(names)
                #job = choice(jobs)
                #race = choice(races)

                obj = Person(name, race, job)
                crew.append(obj)

            return crew

    # screen character_generator():
    #
    #     textbutton "Create Character!":
    #         xalign .5
    #         action Function(randomCrew(6))
    #
    #     vbox:
    #         xalign .5
    #         yalign .5
    #         for c in crew_list:
    #             c.getStatus()
