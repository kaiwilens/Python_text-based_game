from Enemy_Characters import *
from Playable_Characters import *
import Inventory
from Usable_Armor_Weapons import *
import Battle_Sequence

Inventory.weapons.append(fists)
Inventory.weapons.append(knife)
Inventory.weapons.append(sword)

Inventory.armor.append(leather_helm)
Inventory.armor.append(leather_chest)
Inventory.armor.append(leather_chaps)
Inventory.armor.append(iron_helm)

test_list = [warrior, blue_mage]
test_list.insert(0, thief)

# Inventory.main_inventory(test_list)



# Battle_Sequence.single_battle(warrior, hover_board_slime)
# Battle_Sequence.single_battle(warrior, hover_board_slime)


test_list_two = [hover_board_slime, laser_spider, troll_with_gun, bouncer]

# for person in test_list:
    # print(person.get_name(), ", ")

# Battle_Sequence.same_enemy_battle(test_list, hover_board_slime, 2, True)

# Battle_Sequence.same_enemy_battle(test_list, hover_board_slime, 2, True)

Battle_Sequence.same_enemy_battle(test_list, hover_board_slime, 1, True)

# Battle_Sequence.same_enemy_battle(test_list, hover_board_slime, 2, False)

for person in test_list:
    print(person.get_name(), ", ")

# print("DONE")

# Battle_Sequence.random_enemies_battle(test_list, test_list_two, 2, True)
# Battle_Sequence.random_enemies_battle(test_list, test_list_two, 2, False)
