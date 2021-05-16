import Characters
import Armor_Weapons_Class

potions = []
weapons = []
armor = []
valuables = []

def main_inventory(party):
    exit = False

    while not exit:

        print("0: Exit")
        print("1: Weapons")
        print("2: Armor")
        print("3: Potions")
        print("4: Valuables")


        alpha_selection = input()

        try:
            selection = int(alpha_selection)
            if selection < 0 or selection > 4:
                print("Invalid selection")

            else:
                if selection == 0:
                    exit = True

                elif selection == 1:
                    weapons_inventory(party)

                elif selection == 2:
                    armor_inventory(party)

                elif selection == 3:
                    print("STUFF")

                else:
                    print("STUFF")

        except ValueError:
            print("BAD")

def weapons_inventory(party):
    exit = False

    while not exit:
        index = 1
        print("NAME  DAMAGE  STRENGTH  MAGIC")
        print("0: Exit")

        for weapon in weapons:
            print(index,":",weapon.get_hub())
            index += 1

        alpha_selection = input()

        try:
            selection = int(alpha_selection)

            if selection < 0 or selection > len(weapons):
                print("Invalid Input")

            else:
                if selection == 0:
                    exit = True

                else:

                    choice = selection - 1
                    if not weapons[choice].get_equipped():
                        valid_choice = False

                        while not valid_choice:
                            print("Who will equip this weapon?")
                            party_index = 1
                            for person in party:
                                print(party_index,":")
                                print(person.hub())
                                party_index += 1

                            alpha_person = input()

                            try:
                                int_person = int(alpha_person)

                                if int_person < 1 or int_person > len(party):
                                    print("Invalid Input")

                                else:
                                    party_choice = int_person - 1
                                    party[party_choice].set_equipped_weapon(weapons[choice])
                                    owner_name = party[party_choice].get_name()
                                    for weapon in weapons:
                                        if weapon.get_owner() == owner_name:
                                            weapon.set_equipped(False)
                                            break

                                    weapons[choice].set_equipped(True)
                                    weapons[choice].set_owner(owner_name)


                                    valid_choice = True

                            except ValueError:
                                print("Alpha exception")
                                print("Invalid Input")

                    else:
                        print("Weapons is already equipped")

        except ValueError:
            print("Invalid Input")

def armor_inventory(party):
    exit = False

    while not exit:
        index = 1
        print("NAME  BODY PART  STRENGTH REQ  MAGIC REQ  STRENGTH  MAGIC  DEFENSE")
        print("0: Exit")

        for protection in armor:
            print(index,":", protection.get_hub())
            index += 1

        alpha_selection = input()

        try:
            selection = int(alpha_selection)

            if selection < 0 or selection > len(armor):
                print("Invalid Input")

            else:
                if selection == 0:
                    exit = True

                else:
                    choice = selection - 1

                    if not armor[choice].get_equipped():
                        valid_choice = False

                        while not valid_choice:
                            print("Who will equip this weapon?")
                            party_index = 1
                            for person in party:
                                print(party_index,":")
                                print(person.hub())
                                party_index += 1

                            alpha_person = input()

                            try:
                                int_person = int(alpha_person)

                                if int_person < 1 or int_person > len(party):
                                    print("Invalid Input")

                                else:

                                    party_choice = int_person - 1
                                    party[party_choice].equip_armor(armor[choice])

                                    owner_name = party[party_choice].get_name()
                                    body_part = armor[choice].get_body_part()
                                    for protection in armor:
                                        if protection.get_owner() == owner_name and\
                                           protection.get_body_part() == body_part:
                                            protection.set_equipped(False)
                                            break

                                    armor[choice].set_equipped(True)
                                    armor[choice].set_owner(owner_name)

                                    valid_choice = True

                            except ValueError:
                                print("Alpha exception")
                                print("Invalid Input")

                    else:
                        print("Armor is already equipped")

        except ValueError:
            print("Invalid Input")