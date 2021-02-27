# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import enum

import baseCharacterClass
import Players

bob = baseCharacterClass.Characters("Bob", "DUDE", 5, 4, 50)
notBob = Players.Player("Not BOB", "NOT DUDE", "five", 4, 50, Players.Occupations.Cop)

print("Reducing health")

notBob.reduce_health(20)
print("Bob's health:", notBob.get_health())

print("Healing bob")
notBob.heal_character(15)
print("Bob's health:", notBob.get_health())
notBob.heal_character(15)
print("Bob's health:", notBob.get_health())
notBob.heal_character(15)
print("Bob's health:", notBob.get_health())
notBob.heal_character(15)
print("Bob's health:", notBob.get_health())

print("Increasing max health by 50")
notBob.increase_max_health(50)
print(notBob.get_max_health())

print("Reducing health by 40")

notBob.reduce_health(40)
print("Bob's health:", notBob.get_health())

print("Increasing bob health")

notBob.heal_character(15)
print("Bob's health:", notBob.get_health())
notBob.heal_character(15)
print("Bob's health:", notBob.get_health())
notBob.heal_character(15)
print("Bob's health:", notBob.get_health())
notBob.heal_character(15)
print("Bob's health:", notBob.get_health())

print("Killing bob")
notBob.reduce_health(400)
print("Bob's health:", notBob.get_health())

Pob = Players.Player("Not BOB", "NOT DUDE", 5, 4, 50, "Cop")


"""
NEED TO FIX ENUM ERROR AND TEST ENUM'S FROM PLAYER CLASS
MAY NEED TO CHANGE THE check_enum function
"""