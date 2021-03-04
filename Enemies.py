import NPC
import Character_Helper_Functions

class Enemy(NPC.NPC):
    __is_alive = True  # is_alive can be used to exit battle functions once one of the characters health reaches 0
    __level = 0
    __experience = 0
    __has_magic = False
    __magic = 0

    def __init__(self, name, description, strength, damage, max_health, level, magic, magic_points, experience):
        super().__init__(name, description, strength, damage, max_health)
        self.__level = Character_Helper_Functions.set_attributes(level, "Level")
        self.__experience = Character_Helper_Functions.set_attributes(experience, "Experience")
        self.__has_magic = Character_Helper_Functions.check_boolean(magic)
        if self.__has_magic:
            self.__magic = Character_Helper_Functions.set_attributes(magic_points,"Magic Points")

    def set_level(self, level):
        self.__level = Character_Helper_Functions.set_attributes(level, "Level")

    def set_experience(self, experience):
        self.__experience = Character_Helper_Functions.set_attributes(experience, "Experience")

    def get_level(self):
        return self.__level

    def get_experience(self):
        return self.__experience

