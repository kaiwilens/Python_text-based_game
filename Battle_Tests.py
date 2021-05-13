from Enemy_Characters import *
from Playable_Characters import *
import Battle_Sequence

# Battle_Sequence.single_battle(warrior, hover_board_slime)
# Battle_Sequence.single_battle(warrior, hover_board_slime)

test_list = [warrior, blue_mage]
test_list_two = [hover_board_slime, laser_spider, troll_with_gun, bouncer]

# for person in test_list:
    # print(person.get_name(), ", ")

# Battle_Sequence.multiple_enemies_battle(test_list, laser_spider, 3)

# for person in test_list:
    # print(person.get_name(), ", ")

# print("DONE")

Battle_Sequence.random_enemies_battle(test_list, test_list_two, 2)
