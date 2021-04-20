import Armor_Weapons_Class


# Name, Damage, Strength, Magic

fists = Armor_Weapons_Class.Weapons()

pistol = Armor_Weapons_Class.Weapons("Pistol", 5, 20, 0)

magnum_revolver = Armor_Weapons_Class.Weapons("Magnum", 10, 30, 0)

shotgun = Armor_Weapons_Class.Weapons("Shot Gun", 20, 45, 0)

gatling_gun = Armor_Weapons_Class.Weapons("Gatling Gun", 50, 75, 0)

knife = Armor_Weapons_Class.Weapons("Knife", 5, 20, 0)

sword = Armor_Weapons_Class.Weapons("Sword", 10, 30, 0)

axe = Armor_Weapons_Class.Weapons("Axe", 20, 45, 0)

enchanted_ring = Armor_Weapons_Class.Weapons("Ring", 5, 0, 100)

wand = Armor_Weapons_Class.Weapons("Wand", 10, 0, 150)

staff = Armor_Weapons_Class.Weapons("Staff", 25, 25, 175)

# ARMOR

# (self, name="None", body_part="None", strength_req=0, magic_req=0, strength=0, magic=0, defense=0):

naked = Armor_Weapons_Class.Armor("Naked", "None", 0, 0, 0, 0, 0)

leather_helm = Armor_Weapons_Class.Armor("Leather Helm", "Head", 0, 0, 0, 0, 1)
leather_chaps = Armor_Weapons_Class.Armor("Leather Chaps", "Legs", 0, 0, 0, 0, 2)
leather_chest = Armor_Weapons_Class.Armor("Leather Chest", "Chest", 0, 0, 0, 0, 3)
leather_boots = Armor_Weapons_Class.Armor("Leather Boots", "Feet", 0, 0, 0, 0, 1)

