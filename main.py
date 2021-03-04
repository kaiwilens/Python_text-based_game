# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import enum

import NPC
import Characters

bob = NPC.NPC("Bob", "DUDE", 5, 4, 50)

warrior = Characters.Character("Warrior", "A Warrior", 30, 50, 50, Characters.Occupations.Cop, False, 0)

wizard = Characters.Character("Wizard", "A Wizard", 10, 20, 50, Characters.Occupations.Cop, True, 50)

badWarrior = Characters.Character("Warrior", "A Warrior", 30, 50, 50, Characters.Occupations.Cop, False, 50)

badWizard = Characters.Character("Wizard", "A Wizard", 10, 20, 50, Characters.Occupations.Cop, "True", 50)

print("Warrior:", warrior.get_has_magic(), "POINTS: ", warrior.get_magic())
print("Wizard:", wizard.get_has_magic(), "POINTS: ", wizard.get_magic())
print("badWarrior:", badWarrior.get_has_magic(), "POINTS: ", badWarrior.get_magic())
print("badWizard:", badWizard.get_has_magic(), "POINTS: ", badWizard.get_magic())

print("Warrior Level: ", warrior.get_level())
warrior.increase_experience(25)
print("Warrior XP: ", warrior.get_experience())
print("Warrior XP_REQ", warrior.get_experience_req())
print("INCREASING LEVEL")
warrior.increase_experience(150)
print("Warrior Level: ", warrior.get_level())
print("Warrior XP: ", warrior.get_experience())
print("Warrior XP_REQ", warrior.get_experience_req())


