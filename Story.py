from Battle_Sequence import do_battle
from Characters import Character, Occupations
from Enemy_Characters import *
from Playable_Characters import playable_characters
import Playable_Characters
from Usable_Armor_Weapons import *
import Characters

import random
from os import system, name

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


def character_creation():
    character_name = input('Enter Character Name:')
    # TODO Assign name to a character using the character class Luke made

    input_valid = False

    character_class = 0
    while not input_valid:
        character_class = input('Choose Character Class:\n'
                                '1. Warrior		    2. Berserker\n'
                                '3. Thief		    4. Dragoon\n'
                                '5. Black Mage		6. White Mage\n'
                                '7. Blue Mage 		8. Red Mage\n'
                                'Your Selection:')
        try:
            number = int(character_class)
            if number >= 1 and number <= 8:
                input_valid = True

        except ValueError:
            print("Selection must be between 0 and 8")

    character = Playable_Characters.warrior

    if character_class == 1:
        character = Playable_Characters.warrior

    elif character_class == 2:
        character = Playable_Characters.berserker

    elif character_class == 3:
        character = Playable_Characters.thief

    elif character_class == 4:
        character = Playable_Characters.dragoon

    elif character_class == 5:
        character = Playable_Characters.black_mage

    elif character_class == 6:
        character = Playable_Characters.white_mage

    elif character_class == 7:
        character = Playable_Characters.blue_mage

    elif character_class == 8:
        character = Playable_Characters.red_mage

    character.set_name(character_name)

    return character

def in_party(my_list, character = Character, player = Character):
    if character == player:
        return True
    else:
        for person in my_list:
            if character == person:
                return True
    return False

def create_party(player):
    my_list = []
    party_size = 0

    while party_size < 4:
        already_in_party = False
        myNum = random.randint(0, 7)
        new_char = playable_characters[myNum]

        if new_char.get_name() == player.get_name():
            already_in_party = True


        for character in my_list:
            if new_char.get_name() == character.get_name():

                already_in_party = True
                break

        if not already_in_party:
            my_list.append(new_char)
            party_size = party_size + 1


    return my_list

def play_game():
    def main_menu():
        main_menu_selection = input('1. Start Game \n'
                                    '2. Exit')

        if main_menu_selection == 2:
            exit()

        elif main_menu_selection != 1 or main_menu_selection != 2:
            print('Not a valid input')
            main_menu()

        elif main_menu_selection == 1:
            game_story()


def print_name(my_list, character):
    for person in my_list:
        if person.get_name() == character.get_name():
            print(character.get_name() + ":")
            print()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def press_any_key():

    input()


def equip_initial_armor(person = Character):
    person.equip_armor(leather_helm)
    person.equip_armor(leather_chest)
    person.equip_armor(leather_boots)
    person.equip_armor(leather_chaps)
    person.set_equipped_weapon(knife)

def game_story():

    player = character_creation()


    party = create_party(player)
    party.insert(0, player)

    warrior_present = in_party(party, Playable_Characters.warrior, player)
    berserker_present = in_party(party, Playable_Characters.berserker, player)
    thief_present = in_party(party, Playable_Characters.thief, player)
    dragoon_present = in_party(party, Playable_Characters.dragoon, player)
    black_mage_present = in_party(party, Playable_Characters.black_mage, player)
    white_mage_present = in_party(party, Playable_Characters.white_mage, player)
    blue_mage_present = in_party(party, Playable_Characters.blue_mage, player)
    red_mage_present = in_party(party, Playable_Characters.red_mage, player)

    warrior_and_dragoon = False
    berserker_and_thief = False
    blue_mage_and_black_mage = False
    red_mage_and_white_mage = False

    print('In the world of Aldurn, there was once magic and mystical creatures.\n'
          'They Inhabited every corner of the continent of Feorn and established great societies.\n'
          'However, over many centuries, the magic was forgotten and these mystical creatures\n'
          'became extinct. Aldurn now resembles a world not too different from ours.\n'
          'A world of humans and technology, of government and tedium. \n'
          'On what seemed like a normal day, a rift in time was created, sending four people, \n'
          'who depending on your choices, could save the world, or send it to oblivion.\n')

    press_any_key()
    print(player.get_name() + ":")
    print('??? - Ow, what happened?')
    press_any_key()

  #  character_creation(1)

    print()
    print(party[0].get_name() + ":")
    print('??? - I don’t know… WHOA, where are we?')
    press_any_key()

   # character_creation(2)

    print()
    print(party[1].get_name() + ":")
    print('??? - I’ve never seen this before… It’s so bizarre.')
    press_any_key()

  #  character_creation(3)

    print()
    print(player.get_name() + ":")
    print(' - Hey, are you alright? You gotta wake up!')
    press_any_key()

    print()
    print(party[2].get_name() + ":")
    print('??? - ZZZ… Five more minutes ... ZZZ')
    press_any_key()

    print()
    print(player.get_name() + ":")
    print(' - WAKE UP!')
    press_any_key()

    print()
    print(party[2].get_name() + ":")
    print('??? - AH! I’M AWAKE… Wait, Who are you guys?, and what the hell is going on?')

    press_any_key()

  #  character_creation(4)

    # IF PARTYMEMBERS 1-4 ARE WARRIOR AND DRAGOON

    if warrior_present and dragoon_present:
        warrior_and_dragoon = True

        print('You have both the Warrior and the Dragoon in your party.\n'
              'The Warrior and Dragoon have a special relationship,\n'
              'as they both knew each other in the present. The Warrior is\n'
              'a student of the Dragoon’s history class. They were both at\n'
              'a renaissance fair as the rift opened. The Dragoon was hoping\n'
              'that the Warrior would find some value in attending the fair,\n'
              'but the Warrior was mostly disinterested.')

        press_any_key()

        print_name(party, Playable_Characters.warrior)
        print(' - GODDAMN IT, THIS IS WHY I SHOULD NEVER HAVE LET YOU TALK ME INTO GOING \n'
              'TO THAT RENAISSANCE FAIR')

        press_any_key()

        print_name(party, Playable_Characters.dragoon)
        print(' - WHAT?! HOW IS ANY OF THIS MY FAULT? Besides, you were lacking in your\n'
              'essays and I thought it would help.')

        press_any_key()

        print_name(party, Playable_Characters.warrior)
        print(' - Well, a lot of good that did us, huh? Now I’m stuck in god knows where\n'
              'with you, who is wearing ridiculous armor and criticising my writing!')

        print_name(party, Playable_Characters.dragoon)
        print(" - Wha- MY ARMOR IS NOT RIDICULOUS! It's period accurate!")

        press_any_key()

        print_name(party, Playable_Characters.warrior)
        print(' - Whatever.')

        press_any_key()

    # IF PARTYMEMBERS 1-4 ARE BERSERKER AND THIEF

    if berserker_present and thief_present:
        berserker_and_thief = True

        print('You have both the Thief and the Berserker in your party.\n'
              'These two have a special relationship, as they both knew\n'
              'each other in the present. Both the Thief and the Berserker\n'
              'attended a support circle, the Thief for their Kleptomania, \n'
              'and the Berserker for their anger issues. They were both \n'
              'attending their support group when the rift opened.')

        press_any_key()

        print_name(party, Playable_Characters.thief)
        print(' - Hey buddy, are you alright?')
        press_any_key()

        print_name(party, Playable_Characters.berserker)
        print(' - AGHHH! WHO DID THAT? I SWEAR I’M GONNA STRANGLE THEM!!!')
        press_any_key()

        print_name(party, Playable_Characters.thief)
        print(' - WHOA, calm down pal, everything’s okay. I don’t think\n'
              'anybody did that, I think it was that big, bright circle.')
        press_any_key()

        print_name(party, Playable_Characters.berserker)
        print(' - Ah, I’m sorry little dude, I got out of control again.')
        press_any_key()

        print_name(party, Playable_Characters.thief)
        print(' - That’s alright, let’s just take a deep breath, and then\n'
              'we can think about what we need to do next, alright?')
        press_any_key()

        print_name(party, Playable_Characters.berserker)
        print(' - Okay...')

        press_any_key()

    # IF PARTYMEMBERS 1-4 ARE BLUE AND BLACK MAGES

    if blue_mage_present and black_mage_present:
        blue_mage_and_black_mage = True

        print('You have both the Blue and the Black Mages in your party.\n'
              'These two have a special relationship, as they both knew\n'
              'each other in the present. Both the Blue and Black Mages\n'
              'were at a scientific conference when the rift opened. The\n'
              'Black Mage was giving a presentation on the gastronomic\n'
              'benefits of eating meat, and the Blue Mage was in the\n'
              'crowd, heckling the Black Mage and advocating for veganism.')

        press_any_key()

        print_name(party, Playable_Characters.blue_mage)
        print(' - Hey, are you alright, that was a rough…  *gasps*  YOU!')
        press_any_key()

        print_name(party, Playable_Characters.black_mage)
        print(' - Oh great, you again…')
        press_any_key()

        print_name(party, Playable_Characters.blue_mage)
        print(' - Great, now I’m stuck here with this meat-eating monster!\n'
              'How could my day get any worse?')
        press_any_key()

        print_name(party, Playable_Characters.black_mage)
        print(' - Monster?! How dare you! I was trying to explain that there\n'
              'is a definitive health benefit to eating meat! There are specific\n'
              'enzymes that certain meats have that-')

        press_any_key()

        print_name(party, Playable_Characters.blue_mage)
        print(' - LALALALALALALA I CAN’T HEAR YOU LALALALA-')

        press_any_key()

        print_name(party, Playable_Characters.black_mage)
        print(' - Oh yeah, REAL MATURE! How could MY day get any worse?')

        press_any_key()

    # IF PARTYMEMBERS 1-4 ARE RED AND WHITE MAGES

    if red_mage_present and white_mage_present:
        red_mage_and_white_mage = True

        print('You have both the Red and White Mages in your party.\n'
              'These two have a special relationship, as they both knew\n'
              'each other in the present. Both the Red and White Mages\n'
              'were working at a hospital when the rift opened. The White\n'
              'Mage was observing an MRI scan of a patient being conducted\n'
              'by the Red Mage.')

        press_any_key()

        print_name(party, Playable_Characters.red_mage)
        print(' - What the hell? What happened to us?')
        press_any_key()

        print_name(party, Playable_Characters.white_mage)
        print(' - I’m not sure. All I remember was getting ready to send a \n'
              'patient to the MRI, and then waking up here.')
        press_any_key()

        print_name(party, Playable_Characters.red_mage)
        print(' - Huh, that’s all I remember too. Strange…')
        press_any_key()

        print_name(party, Playable_Characters.white_mage)
        print(' - We should look around to see if anyone is hurt.')
        press_any_key()

        print_name(party, Playable_Characters.red_mage)
        print(' - You can handle that, I’m gonna check out this portal-lookin thing.')
        press_any_key()

        print_name(party, Playable_Characters.white_mage)
        print(' - Alright.')

        press_any_key()

    # END OF RELATIONSHIP DIALOGUE

    print()
    print(player.get_name() + ":")
    print(' -  Are all of you alright?')
    press_any_key()

    print()
    print(party[0].get_name() + ":")
    print(' - Um… I think so')
    press_any_key()

    print()
    print(party[1].get_name() + ":")
    print(' - Yeah, for now')
    press_any_key()

    print()
    print(party[2].get_name() + ":")
    print(' - I’m just a little nauseous, but other than that, I’m fine.')
    press_any_key()

    print('From the distance, a small, winged creature was arriving.')
    press_any_key()

    press_any_key()

    print('??? -  GREETINGS, TRAVELLERS FROM THE FUTURE! I AM FISLYO,\n'
          'HERALD OF THE DARK LORD ROTHOS!')

    print()
    print(party[0].get_name() + ":")
    print(' - Whoa…')
    press_any_key()

    print()
    print(party[2].get_name() + ":")
    print(' - What is that thing?')
    press_any_key()

    print()
    print(party[1].get_name() + ":")
    print(' - Looks kinda gross…')
    press_any_key()

    print('Fislyo - HOW DARE Y-  AHEM… I HAVE BEEN SENT HERE BY MY \n'
          'MASTER TO REQUEST YOUR ASSISTANCE!')

    press_any_key()

    print()
    print(player.get_name() + ":")
    print(' - Assistance? With what?')
    press_any_key()

    print('Fislyo - IF YOU COULD NOT ALREADY TELL, YOU HAVE BEEN SENT\n'
          'BACK IN TIME. THIS TEMPORAL DISTURBANCE WAS CAUSED BY THE\n'
          'HELL’S CUBE. HOWEVER, AFTER THE CUBE WAS ACTIVATED, IT OPENED\n'
          'A PORTAL AND DISAPPEARED! MY MASTER WISHES TO HAVE IT BACK AT\n'
          'ONCE, AND HE WOULD LIKE YOU FOUR TO FIND IT!')
    press_any_key()


    print()
    print(party[2].get_name() + ":")
    print(' - What’s in it for us?')

    print('Fislyo - MY MASTER PROMISES THAT YOU WILL ALL RETURN TO YOUR\n'
          'TIME IF YOU ARE ABLE TO RETURN THE CUBE TO HIM!')

    press_any_key()

    good_evil_decision = input('What will you choose?:\n'
                               '1. Tell him to leave\n'
                               '2. Join him\n'
                               'Your Choice:')

    if good_evil_decision == str(1):
        good_story(party, player, warrior_and_dragoon, berserker_and_thief, blue_mage_and_black_mage, red_mage_and_white_mage)
    elif good_evil_decision == str(2):
        bad_story(party, player, warrior_and_dragoon, berserker_and_thief, blue_mage_and_black_mage, red_mage_and_white_mage)
    else:
        print('input not recognized - defaulting to good story')
        good_story(party, player, warrior_and_dragoon, berserker_and_thief, blue_mage_and_black_mage, red_mage_and_white_mage)


def good_story(party, player, warrior_and_dragoon, berserker_and_thief, blue_mage_and_black_mage, red_mage_and_white_mage):
    print()
    print(player.get_name() + ":")
    print(' - I don’t think so. Get outta here ya little slimeball!')
    press_any_key()

    print(' - FINE!, BUT KNOW THAT THERE WILL BE CONSEQUENCES FOR YOUR INSOLENCE!')
    press_any_key()

    print()
    print(party[2].get_name() + ":")
    print(' - Whatever dude.')
    press_any_key()

    print('Fislyo leaves in a huff')

    press_any_key()

    print()
    print(party[1].get_name() + ":")
    print(' - That was weird, we should look around and find someone to help us.')
    press_any_key()

    print()
    print(player.get_name() + ":")
    print(' - That’s a good idea.')
    press_any_key()

    print('The Party sets out for the Tavern.')
    press_any_key()

    press_any_key()

    print('CHAPTER 1 - The Map')

    print('The four heroes enter the tavern. It’s a sizable room with\n'
          'a spacy second floor loft. Behind the counter, the bartender\n'
          'notices the group’s arrival and gives them all a strange look.')

    press_any_key()

    # IF PARTYMEMBERS 1-4 ARE WARRIOR AND DRAGOON
    if warrior_and_dragoon:

        print_name(party, Playable_Characters.dragoon)
        print(' - Looks like we’re lucky I was wearing this armor. You must\n'
              'look strange to everyone wearing your street clothes.')
        press_any_key()

        print_name(party, Playable_Characters.warrior)
        print(' - I didn’t think I’d ever say this, but I actually agree with\n'
              'you. I didn’t like the look that the bartender was giving us.')
        press_any_key()

        print_name(party, Playable_Characters.dragoon)
        print(' - Yeah. Well I suppose this is as good a time as any: If you\n'
              'want information in the past, who do you talk to?')

        press_any_key()

        print_name(party, Playable_Characters.warrior)
        print(' - You’re quizzing me? Now? If you’re gonna do that, you’ll\n'
              'have to ask a harder question than that, old man. The answer\n'
              'is the bartender.')
        press_any_key()

        print_name(party, Playable_Characters.dragoon)
        print(' - I was just kidding. But where did you get that answer from?')
        press_any_key()

        print_name(party, Playable_Characters.warrior)
        print(' - You don’t know? It’s in, like, every RPG ever.')
        press_any_key()

        print_name(party, Playable_Characters.dragoon)
        print('Of course… Well, either way, we should still go talk to him,\n'
              'he might know something.')
        press_any_key()

    # IF PARTYMEMBERS 1-4 ARE BERSERKER AND THIEF

    if berserker_and_thief:
        press_any_key()


        print_name(party, Playable_Characters.thief)
        print(" - Look at all the people…! I’ll bet they're loaded!")
        press_any_key()

        print_name(party, Playable_Characters.berserker)
        print(' - Get a hold of yourself buddy. Remember the saying?')
        press_any_key()

        print_name(party, Playable_Characters.thief)
        print(' - *sighs. Let my hands roam and I’ll be fined out of house\n'
              'and home. Keep them close and I’ll make no foes. Do not let\n'
              'the urge guide. Let it go. Let it slide. I do not steal for\n'
              'that self is not real.\n'
              '...\n'
              'It feels Cheesy')
        press_any_key()

        print_name(party, Playable_Characters.berserker)
        print(' - We’ll bring it up in the next meeting then.')
        press_any_key()

        print_name(party, Playable_Characters.thief)
        print(' - If we can even get out of this mess. Anyway, let’s go talk\n'
              'to the bartender. You know as much as I do that the guy running\n'
              'this place will have information.')

        press_any_key()

    # IF PARTYMEMBERS 1-4 ARE BLUE AND BLACK MAGE

    if blue_mage_and_black_mage:
        press_any_key()

        print_name(party, Playable_Characters.black_mage)
        print(' - You know what’s always confused me?')
        press_any_key()

        print_name(party, Playable_Characters.blue_mage)
        print(' - How people can be perfectly healthy without eating meat?')
        press_any_key()

        print_name(party, Playable_Characters.black_mage)
        print(' - Now is not the time for that. It’s that no matter how much\n'
              'we may study science, bartenders just seem to have this strange\n'
              'power of knowing what you want to know and saying what you want to hear.')
        press_any_key()

        print_name(party, Playable_Characters.blue_mage)
        print(" - Actually it’s because they're in a place where all sorts of\n"
              "people gather. It’s not rocket science.")
        press_any_key()

        print_name(party, Playable_Characters.black_mage)
        print(' - Do you always have to take everything so seriously?')
        press_any_key()

        print_name(party, Playable_Characters.blue_mage)
        print(' - Considering our situation, we should be.')
        press_any_key()

    # IF PARTYMEMBERS 1-4 ARE RED AND WHITE MAGE

    if red_mage_and_white_mage:
        press_any_key()

        print_name(party, Playable_Characters.white_mage)
        print(' - I always feel bad for bartenders.')
        press_any_key()

        print_name(party, Playable_Characters.red_mage)
        print(' - Why’s that?')
        press_any_key()

        print_name(party, Playable_Characters.white_mage)
        print(' - Their work hours must be exhausting.')
        press_any_key()

        print_name(party, Playable_Characters.red_mage)
        print(' - Any more exhausting than ours?')
        press_any_key()

        print_name(party, Playable_Characters.white_mage)
        print(' - That’s a good point.')
        press_any_key()

        print_name(party, Playable_Characters.red_mage)
        print(' - He might know something that can help us. Let’s go ask him.')
        press_any_key()

        print_name(party, Playable_Characters.white_mage)
        print(' - Alright, lead the way.')
        press_any_key()

    # END OF RELATIONSHIP DIALOGUE

    print('The party approaches the bartender. He looks again at everyone suspiciously.')
    press_any_key()

    print('Bartender - You folks new around here? In that case I recommend the imported liquor.')
    press_any_key()

    print()
    print(party[0].get_name() + ":")
    print(' - Oh, we’re not here for drinks.')
    press_any_key()

    print()
    print(party[2].get_name() + ":")
    print(' - I’ll have some of your best ale please.')
    press_any_key()

    print()
    print(player.get_name() + ":")
    print(" - Ignore them. Even if we were here for drinks, we probably\n"
          "wouldn't even be able to pay for them.")
    press_any_key()

    print()
    print(party[1].get_name() + ":")
    print(' - Aw man… I wanted a drink!')
    press_any_key()

    print()
    print(party[2].get_name() + ":")
    print(' - It HAS been a rough day for all of us, but given our situation,\n'
          'it’s we should keep a clear head. Who knows what it would do to us.')
    press_any_key()

    print(' - So you aren’t here for drinks…  then what ARE you here for?')
    press_any_key()

    print('The bartender’s gaze sharpens.')
    press_any_key()

    print()
    print(player.get_name() + ":")
    print(' - Information.')
    press_any_key()

    print('The bartender raises an eyebrow.')
    press_any_key()

    print()
    print(party[2].get_name() + ":")
    print(' - This may sound crazy, but we’re from the future. We were brought\n'
          'back here to the past by some sort of rift. And then this creature\n'
          'named Fislyo asks us to help him find something called the Hell Cube.')

    print('The bartender blinks.')

    print()
    print(player.get_name() + ":")
    print(' - Do you know what this Hell Cube is?')
    press_any_key()

    print('The bartender is silent for a long moment. Then he nods silently and\n'
          'gestures toward the back room. The party follows him into the dimly lit room.')
    press_any_key()

    print('Bartender - You’re lucky, you know. If you had talked to anybody else,\n'
          "they wouldn't have believed you. But I do. There has been a prophecy known\n"
          'across the land for generations, but it has been mostly forgotten. Yet my\n'
          'family knew of this prophecy and waited for that time to come. Never did I\n'
          'think I’d see the prophecy come true, and yet, here you are.')

    press_any_key()

    print()
    print(player.get_name() + ":")
    print(' - How did your family know for certain that there was a prophecy?')
    press_any_key()

    print(' - Because of this.')
    press_any_key()

    print('The bartender opens a small chest that was hidden amongst some larger crates\n'
          'and takes out a rolled up sheet of parchment.')
    press_any_key()

    print('Bartender - The prophecy told of a map that would help guide those from the future. This…')
    press_any_key()

    print('The bartender unrolls that parchment.')
    press_any_key()

    print('Bartender - ...is that map. There are all these weird symbols on it that no one\n'
          'has been able to make out. And amidst those symbols is what appears to be some\n'
          'strange looking box. I’m willing to bet that that is the hell cube you speak of.\n'
          'Huh? What the…?')
    press_any_key()

    print('The map begins to emit a cyan colored glow and the symbols start moving on the parchment.')
    press_any_key()

    print('Bartender - That’s never happened before. This must be in response to your arrival.')


    press_any_key()

    print()
    print(party[1].get_name() + ":")
    print(' - Can we have the map then? Maybe it will help lead us back home.')
    press_any_key()

    print('Bartender - Yes, but there’s a catch… The prophecy warns of the duality of time\n'
          'and how things can be different throughout time’s flow. It says that those from\n'
          'the future should be tested first for they have the power to either right the wrongs\n'
          "of the world, create a new world, or even destroy it. Ideally we wouldn’t want\n"
          'something bad to happen. The prophecy mentions a magical stone in a cave not far\n'
          "from here. Only those who wish to not harm others can touch it. Those who don’t\n"
          'care about harming others will get hurt by the stone. If you bring me that stone\n'
          'and all of you pass it’s test, then I will give you the map.')

    press_any_key()

    print()
    print(party[0].get_name() + ":")
    print(' - A cave huh? Sounds easy enough.')
    press_any_key()

    print("Bartender - It isn’t actually. Otherwise I would’ve retrieved the stone myself long\n"
          "ago. There are monsters there and I’d rather not risk my life for it. But I’ll lend\n"
          'you all some gear and if you get the stone, then we can talk about the map.')

    press_any_key()

    print()
    print(party[2].get_name() + ":")
    print(' - Sounds good.')

    for person in party:
        equip_initial_armor(person)

    print("ALL PARTY MEMBERS HAVE BEEN EQUIPPED WITH LEATHER ARMOR AND A KNIFE")

    press_any_key()




    print('The Party finds themselves in the heart of a cave')
    press_any_key()

    print()
    print(party[1].get_name() + ":")
    print(' - Hey Look, A Chest!')
    press_any_key()

    print('At that moment, a monster leaped out and attacks')
    press_any_key()

    print()
    print(party[0].get_name() + ":")
    print(' - WHOA!')

    press_any_key()

    do_battle(player, enemy_list)
    do_battle(party[0], spider_list)

    # After beating the monster


    print()
    print(player.get_name() + ":")
    print(' - Grab The Stone! Quick!')
    press_any_key()

    print('The Party grabs the stone and escapes the cave as it collapses\n'
          'They then return to the bartender.')
    press_any_key()

    print()
    print(party[2].get_name() + ":")
    print(' - We got it!')

    print('Bartender - Great job heroes! I knew you could do it. Here.')
    press_any_key()

    print('The Bartender hands the map over to The Party.')
    press_any_key()

    print()
    print(player.get_name() + ":")
    print(' - Sweet!, Now what?')
    press_any_key()

    print('Bartender - I would recommend going to see the King! He should\n'
          'be able to help you get to where you need to be.')
    press_any_key()

    print()
    print(party[1].get_name() + ":")
    print(" - Alright, just point us in the right direction and we'll be on our way.")
    press_any_key()

    print('And with that, our Heroes journey began...')

    press_any_key()

    print('THANK YOU FOR PLAYING!')


def bad_story(party, player, warrior_and_dragoon, berserker_and_thief, blue_mage_and_black_mage, red_mage_and_white_mage):
    print()
    print(party[0].get_name() + ":")
    print(' - Sounds good to me.')

    print('Fislyo - GOOD… GOOD. NOW, YOUR FIRST TASK IS TO GO TO THE\n'
          'NEARBY TAVERN AND FIND AN ANCIENT MAP. YOU MUST GET IT BY\n'
          'ANY MEANS NECESSARY.')

    print()
    print(party[1].get_name() + ":")
    print(' - Wait, they aren’t just gonna give it to us?')

    print(' - NO, THE MEN HERE ARE STUBBORN AND VIOLENT!')

    print()
    print(player.get_name() + ":")
    print(' - Great, so we have to start a bar fight in order to get\n'
          'this map… that sounds like a good idea')

    print('Fislyo - JUST GET IT DONE')

    print('Fislyo leaves')

    print()
    print(party[2].get_name() + ":")
    print(' - Guess we better get going then.')

    print('The Party sets out for the Tavern.')

    print('CHAPTER 1 - The Map')

    print('Our four villains enter the tavern. It’s a sizable room with a\n'
          'spacy second floor loft. Behind the counter, the bartender notices\n'
          'the group’s arrival and gives them all a strange look.')

    # IF PARTYMEMBERS 1-4 ARE WARRIOR AND DRAGOON

    if warrior_and_dragoon:

        print_name(party, Playable_Characters.dragoon)
        print(' - Looks like we’re lucky I was wearing this armor. You must\n'
              'look strange to everyone wearing your street clothes.')

        print_name(party, Playable_Characters.warrior)
        print(' - I didn’t think I’d ever say this, but I actually agree with\n'
              'you. I didn’t like the look that the bartender was giving us.')

        print_name(party, Playable_Characters.dragoon)
        print(' - Yeah. Well I suppose this is as good a time as any: If you\n'
              'want information in the past, who do you talk to?')

        print_name(party, Playable_Characters.warrior)
        print(' - You’re quizzing me? Now? If you’re gonna do that, you’ll\n'
              'have to ask a harder question than that, old man. The answer\n'
              'is the bartender.')

        print_name(party, Playable_Characters.dragoon)
        print(' - I was just kidding. But where did you get that answer from?')

        print_name(party, Playable_Characters.warrior)
        print(' - You don’t know? It’s in, like, every RPG ever.')

        print_name(party, Playable_Characters.dragoon)
        print('Of course… Well, either way, we should still go talk to him,\n'
              'he might know something.')

    # IF PARTYMEMBERS 1-4 ARE BERSERKER AND THIEF

    if berserker_and_thief:

        print_name(party, Playable_Characters.thief)
        print(" - Look at all the people…! I’ll bet they're loaded!")

        print_name(party, Playable_Characters.berserker)
        print(' - Get a hold of yourself buddy. Remember the saying?')

        print_name(party, Playable_Characters.dragoon)
        print(' - *sighs. Let my hands roam and I’ll be fined out of house\n'
              'and home. Keep them close and I’ll make no foes. Do not let\n'
              'the urge guide. Let it go. Let it slide. I do not steal for\n'
              'that self is not real.\n'
              '...\n'
              'It feels Cheesy')

        print_name(party, Playable_Characters.berserker)
        print(' - We’ll bring it up in the next meeting then.')

        print_name(party, Playable_Characters.dragoon)
        print(' - If we can even get out of this mess. Anyway, let’s go talk\n'
              'to the bartender. You know as much as I do that the guy running\n'
              'this place will have information.')

    # IF PARTYMEMBERS 1-4 ARE BLUE AND BLACK MAGE

    if blue_mage_and_black_mage:

        print_name(party, Playable_Characters.black_mage)
        print(' - You know what’s always confused me?')

        print_name(party, Playable_Characters.blue_mage)
        print(' - How people can be perfectly healthy without eating meat?')

        print_name(party, Playable_Characters.black_mage)
        print(' - Now is not the time for that. It’s that no matter how much\n'
              'we may study science, bartenders just seem to have this strange\n'
              'power of knowing what you want to know and saying what you want to hear.')

        print_name(party, Playable_Characters.blue_mage)
        print(" - Actually it’s because they're in a place where all sorts of\n"
              "people gather. It’s not rocket science.")

        print_name(party, Playable_Characters.black_mage)
        print(' - Do you always have to take everything so seriously?')

        print_name(party, Playable_Characters.black_mage)
        print(' - Considering our situation, we should be.')

    # IF PARTYMEMBERS 1-4 ARE RED AND WHITE MAGE

    if red_mage_and_white_mage:

        print_name(party, Playable_Characters.white_mage)
        print(' - I always feel bad for bartenders.')

        print_name(party, Playable_Characters.red_mage)
        print(' - Why’s that?')

        print_name(party, Playable_Characters.white_mage)
        print(' - Their work hours must be exhausting.')

        print_name(party, Playable_Characters.red_mage)
        print(' - Any more exhausting than ours?')

        print_name(party, Playable_Characters.white_mage)
        print(' - That’s a good point.')

        print_name(party, Playable_Characters.red_mage)
        print(' - He might know something that can help us. Let’s go ask him.')

        print_name(party, Playable_Characters.white_mage)
        print(' - Alright, lead the way.')

    # END OF RELATIONSHIP DIALOGUE

    print('The party approaches the bartender. He looks again at everyone\n'
          'suspiciously and with great concern.')

    print('Bartender - You folks new around here? I’d recommend the imported\n'
          'liquor; it’s our best drink.')

    print(party[1].get_name() + ":")
    print(' - Oh, we’re not here for drinks.')

    print(player.get_name() + ":")
    print(' - We need information. And we need it fast-- we don’t have neither\n'
          'the time nor the energy to waste on useless conversations.')

    print(party[1].get_name() + ":")
    print(' - Aw, but I wanted a drink!')

    print(party[2].get_name() + ":")
    print(' - Me too… but, we have to stay focused. The more time we waste, the\n'
          'longer we’re stuck here.')

    print('Bartender - So, what, you just barge in here and demand information,\n'
          'when I don’t even know what you people or what you want? Talk about\n'
          'rudeness! What are you here for, anyways?')

    print('The bartender’s gaze sharpens, as he warily moves his hand to one of\n'
          'the knives under the counter.')

    print(player[2].get_name() + ":")
    print(' - Let this be your first warning; I don’t like repeating myself. We’re\n'
          'here for information. You seem like the only person around here who might\n'
          'have some idea what’s going on.')

    print('The bartender moves his hand away from the knife, without the party seeing.')

    print(party[2].get_name() + ":")
    print(' - There’s no simple way to say this, so listen carefully; We’re from the\n'
          'future. We were brought back to the past by some sort of rift. Some sort of\n'
          'creature, apparently named Fislyo, asked us to help him find something called\n'
          'the Hell Cube.')

    print('The bartender emits a long sigh.')

    print(player[2].get_name() + ":")
    print(' - Do you know anything about the Hell Cube?')

    print('The bartender is silent for a moment. Then, he nods silently and gestures\n'
          'towards the back room. The party follows him into the dimly lit room. The\n'
          'room is dusty, and full of cobwebs and crates. One wall is adorned with weapons\n'
          'of a bygone era, waiting to be used. Another, with 8 distinct sets of armor.\n'
          'It seems almost perfect. There is another moment of silence.')

    print('Bartender - You’re lucky, you know. If you had talked to anybody else,\n'
          "they wouldn't have believed you. But I do. There has been a prophecy known\n"
          'across the land for generations, but it has been mostly forgotten. Yet my\n'
          'family knew of this prophecy and waited for that time to come. Never did I\n'
          'think I’d see the prophecy come true, and yet, here you are.')

    print(player[2].get_name() + ":")
    print(' - How did your family know for certain that there was a prophecy?')

    print(' - Because of this.')

    print('The bartender opens a small chest that was hidden amongst some larger crates\n'
          'and takes out a rolled up sheet of parchment.')

    print('Bartender - The prophecy told of a map that would help guide those from the future. This…')

    print('The bartender unrolls that parchment.')

    print('Bartender - ...is that map. There are all these weird symbols on it that no one\n'
          'has been able to make out. And amidst those symbols is what appears to be some\n'
          'strange looking box. I’m willing to bet that that is the hell cube you speak of.\n'
          'Huh? What the…?')

    print('The map begins to glow a dark blood colored glow, and the symbols start moving\n'
          'on the parchment.')

    print('Bartender - That’s never happened before. This must be in response to your arrival.')

    print(party[1].get_name() + ":")
    print(' - Wonderful. We’ll be taking that, then.')

    print('Bartender - I can’t just give this away, there’s a catch! The prophecy warns\n'
          'of the duality of time and how things can be different throughout time’s flow…\n'
          'It says that those from the future need to be tested first lest they ruin the\n'
          'world. For obvious reasons, we don’t want that… right?')

    print(party[2].get_name() + ":")
    print(' - … Right, sure.')

    print('Bartender - So; the prophecy mentions a magical stone in a cave not far from\n'
          'here. Only those who wish to not harm others can touch it. Those who don’t care\n'
          'about harming others will get hurt by the stone. If you bring me that stone and\n'
          'all of you pass it’s test, then I will give you the map.')

    print(player.get_name() + ":")
    print(' - Yeah, I think we’ll be skipping that stone. We told you to be fast, and here\n'
          'you are trying to send us on a side quest. The way I see it; why should we get you\n'
          'your stone when the map is right here? It’d be just as easy…')

    print('The bartender draws his knife')

    print('Bartender - Don’t you dare. I’ve been protecting this map and this prophecy for\n'
          '57 years, and I’m not going to have it ruined by some ruffians like you!')

    print(party[2].get_name() + ":")
    print(' - Well, that’s a real shame then, isn’t it?')

    print('The rest of the party draws the weapons and armor from nearby stands in the back room')

    equip_initial_armor(player)

    for person in party:
        equip_initial_armor(person)

    print("ALL PARTY MEMBERS HAVE BEEN EQUIPPED WITH LEATHER ARMOR AND A KNIFE")

    print(party[0].get_name() + ":")
    print(' - Because we’re not standing down.')

    print(party[1].get_name() + ":")
    print(' - Because we have a goal.')

    print(player.get_name() + ":")
    print(' - And you’re in our way.')

    print('The bartender looks panicked, clearly outnumbered and surrounded by the party.')

    print('Bartender - HELP!!!')

    print('The bar’s 3 bouncers rush into the back room and see the commotion unfolding.\n'
          'They draw their weapons.')

    do_battle(player, enemy_list)

    # AFTER THEY WIN THE FIGHT

    print(party[1].get_name() + ":")
    print('Grab the map! Quick!')

    print('The Party leaves the bar through a window with the map in hand. They see a castle\n'
          'in the distance.')

    print(player.get_name() + ":")
    print("Let's see if we can go and swindle whoever lives in that castle into giving us some\n"
          "better stuff, maybe even figure out where we need to go next.")

    print('And with that, our villains became determined to get home, no matter the cost.\n')

    print('THANK YOU FOR PLAYING!')