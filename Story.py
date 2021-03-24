from Characters import Occupations


classes = [
    {
        "name": "Warrior",
        "desc": "This character is a college student in the"
        " present. They are headstrong and will become proficient"
        " in sword fighting and other offensive tactics. They"
        " are well rounded and are a natural leader."
    },
    {
        "name": "Berserker",
        "desc": "This character is a pro wrestler in the present."
        " They are brutish, tough, and have a tendency to showboat."
        " They are also prone to violent episodes. This character"
        " can endure heavy attacks and often inflicts massive"
        " amounts of damage."
    },
    {
        "name": "Thief",
        "desc": "This character is a delinquent street punk"
        " in the present. They have kleptomaniac tendencies"
        " and have incredible speed. They are known to dodge"
        " attacks well, but inflict little damage."
    },
    {
        "name": "Dragoon",
        "desc": "This character is a college professor of"
        " history in the present. They are very interested"
        " in the past that they are now in, as this was a"
        " period of history never recorded. This character"
        " was pulled into the past during a renaissance"
        " fair where they were preparing for a joust. This"
        " character is proficient in spears, lances and"
        " other polearms. They are on the more defensive"
        " side, but deal a moderate amount of damage as well."
    },
    {
        "name": "Black Mage",
        "desc": "This character is a chemist in the present."
        " They are skillful and use offensive magic proficiently"
        " on the battlefield."
    },
    {
        "name": "White Mage",
        "desc": "[Add description for White Mage here]"
    },
    {
        "name": "Blue Mage",
        "desc": "[Add description for Blue Mage here]"
    },
    {
        "name": "Red Mage",
        "desc": "[Add description for Red Mage here]"
    },
]
def play_game():
    # This paragraph is supposed to help the player understand
    # the world that they are about to be thrown into. As of
    # right now, I haven’t decided on a continent name or a world
    # name, but they will be added to this when they are solidified.
    print(
        "In the world of [WORLD NAME], there was once\n"
        "magic and mystical creatures. They inhabited\n"
        "every corner of the continent of [CONTINENT\n"
        "NAME] and established great societies. However,\n"
        "over many centuries, the magic was forgotten and\n"
        "these mystical creatures became extinct.\n"
        "[WORLD NAME] now resembles a world not too\n"
        "different from ours. A world of humans and\n"
        "technology, of government and tedium. On what\n"
        "seemed like a normal day, a rift in time was\n"
        "created, sending many things to the past,\n"
        "including four people, who depending on your\n"
        "choices, could save the world, or send it to\n"
        "oblivion."
    )
    print()
    print("??? - Ow, what happened?")
    name = input("Enter Character Name: ")
    while True:
        try:
            classID = int(input("Choose Character Class: "))
            if classID >= 1 and classID <= 8:
                break
            print("Error: input must be within 1-8.")
        except ValueError:
            print("Error: input must be a number.")
    occupation = Occupations(classID)
    print(name)
    print(occupation)
    # End of script