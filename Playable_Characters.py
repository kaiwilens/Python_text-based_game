import Characters

from Character_Descriptions import *

# (self, name, description, strength, damage, max_health, defense, occupation, magic, magic_points):

blue_mage = Characters.Character("Ezekiel", blue_mage_description, 25, 10, 150, 15,
                                 Characters.Occupations.Zoo_Keeper, True, 100)

white_mage = Characters.Character("Christine", white_mage_description, 15, 10, 100,
                                  10, Characters.Occupations.Doctor, True, 150)

black_mage = Characters.Character("Walter", black_mage_description, 20, 10, 125,
                                  15, Characters.Occupations.Chemist, True,
                                  150)

red_mage = Characters.Character("Steve", red_mage_description, 15, 10, 150, 15,
                                Characters.Occupations.Fire_Fighter, True, 175)

thief = Characters.Character("Carmen", thief_description, 20, 10, 100, 10,
                             Characters.Occupations.Thief, False, 0)

berserker = Characters.Character("Karry", berserker_description, 20, 10, 200, 32,
                                 Characters.Occupations.Cop, False, 0)

warrior = Characters.Character("Brian", warrior_description, 20, 10, 150, 20,
                               Characters.Occupations.Blue_Collar, False, 0)

dragoon = Characters.Character("Michael", black_mage_description, 20, 10, 125,
                                  15, Characters.Occupations.Chemist, True,
                                  150)

playable_characters = [
    blue_mage,
    white_mage,
    black_mage,
    red_mage,
    thief,
    berserker,
    warrior,
    dragoon,
]