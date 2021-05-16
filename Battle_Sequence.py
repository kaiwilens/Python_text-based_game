import Characters
import Enemies
import Inventory
import enum
import random

class return_options(enum.Enum):
    victory = 0
    defeat = 1
    retreat = 2

def same_enemy_battle(characters, enemy, num_enemies, retreat_option = True):
    """Fight numerous enemies

    This code is used for the characters to fight numerous enemies.
    The function cycles through the characters list making them fight
    until all enemies or all characters are dead. If a character
    dies they will be removed from the party list.

    :param characters: List that contains the players party
    :param enemy: The enemy the character will fight
    :param num_enemies: The number of enemies the characters will need to fight.
    :return: breaks out of battle if all characters are dead
    """
    print(enemy.get_description())

    while True:
        for character in characters:
            while character.get_is_alive() and enemy.get_is_alive():
                character.hub()
                enemy.hub()

                valid_input = False

                while not valid_input:

                    print("1: Attack")
                    print("2: Inventory")

                    if retreat_option:
                        print("3: Retreat")

                    selection = input()

                    try:
                        int_selection = int(selection)

                        if int_selection == 1:
                            enemy.reduce_health(character.get_damage())
                            character.reduce_health(enemy.get_damage())
                            valid_input = True

                        elif int_selection == 2:
                            Inventory.main_inventory(characters)

                        elif int_selection == 3:
                            if retreat_option:
                                return return_options.retreat

                            else:
                                print("Invalid Selection")

                        else:
                            print("Invalid Selection")


                    except:
                        print("Invalid Selection")
                        print()

            if not enemy.get_is_alive():
                print(enemy.get_name(), "has been defeated")
                enemy.set_is_alive(True)
                num_enemies = num_enemies - 1
                if num_enemies == 0:
                    return return_options.victory


            else:
                characters.remove(character)
                print(character.get_name(), "is dead")
                if not len(characters):
                    return return_options.defeat

def random_enemies_battle(characters, enemies, num_enemies, retreat_option = True):
    """Fight numerous random enemies

    This code is used for the characters to fight numerous random enemies.
    The function cycles through the characters list making them fight random enemies
    until all enemies or all characters are dead. If a character
    dies they will be removed from the party list.

    :param characters: List that contains the players party
    :param enemis: List that contains the possible enemies the characters will fight
    :param num_enemies: The number of enemies the characters will need to fight.
    :return: breaks out of battle if all characters are dead
    """
    max_int = len(enemies) - 1
    while True:

        index = random.randint(0, max_int)

        enemy = enemies[index]
        print(enemy.get_description())
        for character in characters:
            while character.get_is_alive() and enemy.get_is_alive():
                character.hub()
                enemy.hub()

                valid_input = False

                num_options = 2
                if retreat_option:
                    num_options += 1

                while not valid_input:

                    print("1: Attack")
                    print("2: Inventory")

                    if retreat_option:
                        print("3: Retreat")

                    selection = input()

                    try:
                        int_selection = int(selection)

                        if int_selection == 1:
                            enemy.reduce_health(character.get_damage())
                            character.reduce_health(enemy.get_damage())
                            valid_input = True

                        elif int_selection == 2:
                            Inventory.main_inventory(characters)

                        elif int_selection == 3:
                            if retreat_option:
                                return return_options.retreat

                            else:
                                print("Invalid Selection")

                        else:
                            print("Invalid Selection")


                    except ValueError:
                        print("Invalid Selection")
                        print()

            if not enemy.get_is_alive():
                print(enemy.get_name(), "has been defeated")
                enemy.set_is_alive(True)
                num_enemies -= 1
                if num_enemies == 0:
                    return return_options.victory
                break


            else:
                characters.remove(character)
                print(character.get_name(), "is dead")
                if not len(characters):
                    return return_options.defeat


