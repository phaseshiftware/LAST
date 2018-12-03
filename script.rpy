


label start:

    menu:
        'Story mode or Custom characters?'
        'Story':
            'Okay let\'s start a new story.'
            jump story
        'Custom':
            'Okay. Let\'s do a custom story.'
            jump randomStory

label story:
    # Characters are in storyData.rpy
    k.character 'Ouch my head hurts..'
    l.character 'Hold still. I am trying to treat your wounds.'

    return

label randomStory:
    # User wants to pick thier own characters
    # Need name, race, and job picked from lists
    $ renpy.say(None, 'Okay let\'s make some characters!.')

    # get desired name, prompt to confirm
    # name code

    # display races
    # confirm

    # display jobs
    # confirm

    # show user their build, confirm character else change piece
    # add character to crew list

    return
