from Battle_Sequence import do_battle
from Characters import Character, Occupations
from Enemy_Characters import enemy_list
from Playable_Characters import playable_characters

classes = [
    {
        "name": "Blue Mage",
        "desc": "[Add description for Blue Mage here]"
    },
    {
        "name": "White Mage",
        "desc": "[Add description for White Mage here]"
    },
    {
        "name":
        "Black Mage",
        "desc":
        "This character is a chemist in the present."
        " They are skillful and use offensive magic proficiently"
        " on the battlefield."
    },
    {
        "name": "Red Mage",
        "desc": "[Add description for Red Mage here]"
    },
    {
        "name":
        "Thief",
        "desc":
        "This character is a delinquent street punk"
        " in the present. They have kleptomaniac tendencies"
        " and have incredible speed. They are known to dodge"
        " attacks well, but inflict little damage."
    },
    {
        "name":
        "Berserker",
        "desc":
        "This character is a pro wrestler in the present."
        " They are brutish, tough, and have a tendency to showboat."
        " They are also prone to violent episodes. This character"
        " can endure heavy attacks and often inflicts massive"
        " amounts of damage."
    },
    {
        "name":
        "Warrior",
        "desc":
        "This character is a college student in the"
        " present. They are headstrong and will become proficient"
        " in sword fighting and other offensive tactics. They"
        " are well rounded and are a natural leader."
    },
    #{
    #    "name":
    #    "Dragoon",
    #    "desc":
    #    "This character is a college professor of"
    #    " history in the present. They are very interested"
    #    " in the past that they are now in, as this was a"
    #    " period of history never recorded. This character"
    #    " was pulled into the past during a renaissance"
    #    " fair where they were preparing for a joust. This"
    #    " character is proficient in spears, lances and"
    #    " other polearms. They are on the more defensive"
    #    " side, but deal a moderate amount of damage as well."
    #},
]


def play_game():
    # This paragraph is supposed to help the player understand
    # the world that they are about to be thrown into. As of
    # right now, I haven’t decided on a continent name or a world
    # name, but they will be added to this when they are solidified.
    print("In the world of [WORLD NAME], there was once\n"
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
          "oblivion.")
    print()
    print("??? - Ow, what happened?")
    name = input("Enter Character Name: ")
    while True:
        try:
            classID = int(input("Choose Character Class: "))
            if classID >= 1 and classID <= len(playable_characters):
                break
            print("Error: input must be within 1-%i." %
                  len(playable_characters))
        except ValueError:
            print("Error: input must be a number.")
    print(name)
    character = playable_characters[classID - 1]
    do_battle(character, enemy_list)
    # End of script