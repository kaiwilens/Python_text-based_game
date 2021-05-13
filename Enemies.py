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
            self.__magic = Character_Helper_Functions.set_attributes(magic_points, "Magic Points")

    def hub(self):
        info_panel = str(self.get_name()) + "   LEVEL: " + str(self.get_level()) + \
                     "   HP: " + str(self.get_health()) + "   DMG: " + str(self.get_damage())

        border = "-" * len(info_panel)

        print(border)
        print(info_panel)
        print(border)

    def set_level(self, level):
        self.__level = Character_Helper_Functions.set_attributes(level, "Level")

    def set_experience(self, experience):
        self.__experience = Character_Helper_Functions.set_attributes(experience, "Experience")

    def get_level(self):
        return self.__level

    def get_experience(self):
        return self.__experience

    def set_is_alive(self, value):

        try:
            bool(value)
            self.__is_alive = value

        except:
            print("Invalid Value. Is Alive status unchanged")



    def get_is_alive(self):
        return self.__is_alive

    def reduce_health(self, damage):
        """
        Used to decrease the characters health

        :param damage: the amount the health will decreased by
        The function takes the damage amount and reduces it according the to character's defense attribute.
        It takes product of damage * defense percentage and subtracts it from the damage they would have received
        and stores the total damage in health_ reduction. It then and subtracts this from the characters current health.
        This can be used in battle sequences.
        If the characters health goes below or is equal to 0 self.__is_alive will be set to false
        and can be used to end a battle sequence.
        """
        try:
            int(damage)

            total_health = self.get_health() - damage

            if total_health <= 0:
                self.__is_alive = False
                self.set_health(self.get_max_health())

            else:
                self.set_health(total_health)

        except ValueError:
            print("Health must be decreased by an integer. Health remains at:", self.get_health())
