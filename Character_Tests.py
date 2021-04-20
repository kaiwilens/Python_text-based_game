import enum
import NPC
import Characters
import Enemies
import Battle_Sequence
from Playable_Characters import *
from Usable_Armor_Weapons import *


badGuy = Enemies.Enemy("Bad Guy", "Not good", 30, 20, 30, 2, False, 0, 50)

def do_increases(Character):
    print(Character.get_occupation().upper())
    print()
    print("LEVEL:", Character.get_level())
    print("STRENGTH: ", str(Character.get_strength()))
    print("HEALTH: ", str(Character.get_max_health()))
    print("DEFENSE: ", Character.get_defense())
    print("MAGIC: ", Character.get_magic())

    print("INCREASING LEVEL:")
    print()
    Character.increase_experience(150)

    print("LEVEL:", Character.get_level())
    print("STRENGTH: ", str(Character.get_strength()))
    print("HEALTH: ", str(Character.get_max_health()))
    print("DEFENSE: ", Character.get_defense())
    print("MAGIC: ", Character.get_magic())


#do_increases(blue_mage)
print()
#do_increases(white_mage)
print()
#do_increases(black_mage)
print()
#do_increases(red_mage)
print()
#do_increases(thief)
print()
#do_increases(berserker)
print()
#do_increases(warrior)
print()

print("FISTS")
warrior.hub()

print("KNIFE")
warrior.set_equipped_weapon(knife)

warrior.hub()

print("AXE")
warrior.set_equipped_weapon(axe)

warrior.hub()

print("WAND")
warrior.set_equipped_weapon(wand)

warrior.hub()

print("GATLING GUN")
warrior.set_equipped_weapon(gatling_gun)

warrior.set_equipped_weapon(sword)
warrior.hub()

warrior.equip_armor(leather_helm)
warrior.equip_armor(leather_chest)
warrior.equip_armor(leather_boots)
warrior.equip_armor(leather_chaps)

print("WITH ARMOR")
warrior.hub()

# thief.hub()
# badGuy.hub()


#basicBattleSequence
# Battle_Sequence.do_battle(warrior, [badGuy])
#=======

#testBeep = AudioSystem.SFX("", "300hz", ".mp3")  #Code is commented out because test file 300hz.mp3 was not uploaded to repository.
#testBeep.play()   