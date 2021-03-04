import enum

import Character_Helper_Functions


class NPC:
    # Character private variables
    __name = "na"
    __description = "na"
    __strength = 0
    __damage = 0
    __health = 0
    __max_health = 0  # MAX HEALTH IS USED SO THAT A CHARACTER CANNOT HAVE AN INFINITE AMOUNT OF HEALTH WHEN HEALING

    # Character constructor
    def __init__(self, name, description, strength, damage, max_health):
        self.__name = name
        self.__description = description
        self.__strength = Character_Helper_Functions.set_attributes(strength, "strength")
        self.__damage = Character_Helper_Functions.set_attributes(damage, "Damage")
        self.__max_health = Character_Helper_Functions.set_attributes(max_health, "Max health")
        self.__health = Character_Helper_Functions.set_attributes(max_health, "health")

    # Setters and Getters

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def set_strength(self, strength):
        self.__strength = Character_Helper_Functions.set_attributes(strength, "strength")

    def get_strength(self):
        return self.__strength

    def set_damage(self, damage):
        self.__damage = Character_Helper_Functions.set_attributes(damage, "Damage")

    def get_damage(self):
        return self.__damage

    def set_health(self, health):
        try:
            int(health)
            if health > self.get_max_health():
                print("Health cannot be greater than max health. Health set to max health")
                self.__health = self.__max_health
            elif health < 0:
                print("Health must be greater than 0. Health set to max health")
                self.__health = self.__max_health
            else:
                self.__health = health

        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Value must be an integer. HEALTH set to 0.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.__health = 0

    def get_health(self):
        return self.__health

    def set_max_health(self, max_health):
        self.__max_health = Character_Helper_Functions.set_attributes(max_health, "Max Health")
        self.__health = Character_Helper_Functions.set_attributes(max_health, "health")

    def get_max_health(self):
        return self.__max_health



