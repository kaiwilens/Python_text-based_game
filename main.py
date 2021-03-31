# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import enum
import NPC
import Characters
import Enemies
import Battle_Sequence
import AudioSystem
import Story

warrior = Characters.Character("Warrior", "A Warrior", 30, 50, 50, Characters.Occupations.Cop, False, 0)

wizard = Characters.Character("Wizard", "A Wizard", 10, 20, 50, Characters.Occupations.Cop, True, 50)

badWarrior = Characters.Character("Warrior", "A Warrior", 30, 50, 50, Characters.Occupations.Cop, False, 50)

badWizard = Characters.Character("Wizard", "A Wizard", 10, 20, 50, Characters.Occupations.Cop, "True", 50)

badGuy = Enemies.Enemy("Bad Guy", "Not good", 30, 20, 30, 2, False, 0, 50)

print("Warrior:", warrior.get_has_magic(), "POINTS: ", warrior.get_magic())
print("Wizard:", wizard.get_has_magic(), "POINTS: ", wizard.get_magic())
print("badWarrior:", badWarrior.get_has_magic(), "POINTS: ", badWarrior.get_magic())
print("badWizard:", badWizard.get_has_magic(), "POINTS: ", badWizard.get_magic())
print()

print("Warrior Level: ", warrior.get_level())
warrior.increase_experience(25)

print("Warrior XP: ", warrior.get_experience())
print("Warrior XP_REQ", warrior.get_experience_req())
print()
print("INCREASING LEVEL")
print()
warrior.increase_experience(85)

print("Warrior Level: ", warrior.get_level())
print("Warrior XP: ", warrior.get_experience())
print("Warrior XP_REQ", warrior.get_experience_req())
print()

print("Increasing with Enemy XP")
print()
warrior.increase_experience(badGuy.get_experience())

print("Warrior Level: ", warrior.get_level())
print("Warrior XP: ", warrior.get_experience())
print("Warrior XP_REQ", warrior.get_experience_req())

#basicBattleSequence
#warrior.do_battle([badGuy])
#=======

#testBeep = AudioSystem.SFX("", "300hz", ".mp3")  #Code is commented out because test file 300hz.mp3 was not uploaded to repository.
#testBeep.play()                                  #Code is mostly included just to show use case for the SFX wrapper.

#main
Story.play_game()
