import enum

import NPC

import Character_Helper_Functions


class Occupations(enum.Enum):
    na = 0
    Cop = 1
    Doctor = 2
    Zoo_Keeper = 3


class Enhancements(enum.Enum):
    """Set additional attributes according to occupation

    This will be used to set the specific enhancements/attributes for the
    various occupation types. The values I have right now are just place holders
    """
    na = 0
    DeadAim = 1
    StrongArm = 2


class Character(NPC.NPC):
    __occupation = Occupations.na
    __enhancement = Enhancements.na
    __is_alive = True  # is_alive can be used to exit battle functions once one of the characters health reaches 0
    __level = 1
    __experience = 0
    __experience_req = 100
    __has_magic = False
    __magic = 0

    def __init__(self, name, description, strength, damage, max_health, occupation, magic, magic_points):
        super().__init__(name, description, strength, damage, max_health)

        self.__occupation = Character_Helper_Functions.check_enum(Occupations, occupation)
        self.__has_magic = Character_Helper_Functions.check_boolean(magic)
        if self.__has_magic:
            self.__magic = Character_Helper_Functions.set_attributes(magic_points,"Magic Points")

    def set_occupation(self, occupation):
        self.__occupation = Character_Helper_Functions.check_enum(Occupations, occupation)

    def get_occupation(self):
        return self.__occupation.name

    def get_level(self):
        return self.__level

    def get_experience(self):
        return self.__experience

    def get_experience_req(self):
        return self.__experience_req

    def set_has_magic(self, magic):
        self.__has_magic = Character_Helper_Functions.check_boolean(magic)

    def get_has_magic(self):
        return self.__has_magic

    def set_magic(self, magic_points):
        if self.__has_magic:
            self.__magic = Character_Helper_Functions.set_attributes(magic_points,"Magic Points")

    def get_magic(self):
        return self.__magic

    def get_is_alive(self):
        return self.__is_alive

    #Character member functions for various actions

    def increase_damage(self, increase):
        """Used to increase the characters Damage

        :param increase: the amount the damage will increase by
        The function takes the increase amount and adds it to the characters current damage.
        """
        try:
            int(increase)
            total = self.get_damage() + increase
            self.set_damage(total)

        except ValueError:
            print("Damage must be increased by an integer. Damage remains at:", self.get_damage())

    def increase_strength(self, increase):
        """Used to increase the characters strength

        :param increase: the amount the strength will increase by
        The function takes the increase amount and adds it to the characters current strength.
        """
        try:
            int(increase)
            total = self.get_strength() + increase
            self.set_damage(total)

        except ValueError:
            print("Strength must be increased by an integer. Strength remains at:", self.get_strength())

    def increase_magic(self, increase):
        """Used to increase the characters Magic

        :param increase: the amount the magic will increase by
        The function check if the character is magical and if they are it takes
        the increase amount and adds it to the characters current magic.
        """

        if self.__has_magic:
            try:
                int(increase)
                total = self.get_magic() + increase
                self.set_magic(total)

            except ValueError:
                print("Magic must be increased by an integer. Magic remains at:", self.get_magic())

        else:
            None

    def heal_character(self, increase):
        """Used to increase the characters health

        :param increase: the amount the health will increase by
        The function takes the increase amount and adds it to the characters current health.
        If their health goes above max health it will be set equal to max health
        """
        try:
            int(increase)
            total_health = self.get_health() + increase

            if total_health > self.__max_health:
                self.set_health(self.__max_health)

            else:
                self.set_health(total_health)

        except ValueError:
            print("Health must be increased by an integer. Health remains at:", self.get_health())

    def reduce_health(self, reduction):
        """
        Used to decrease the characters health

        :param reduction: the amount the health will decreased by
        The function takes the reduction amount and subtracts it to the characters current health.
        This can be used in battle sequences.
        If the characters health goes below or is equal to 0 self.__is_alive will be set to false
        and can be used to end a battle sequence.
        """
        try:
            int(reduction)
            total_health = self.get_health() - reduction

            if total_health <= 0:
                self.__is_alive = False
                self.set_health(0)

            else:
                self.set_health(total_health)

        except ValueError:
            print("Health must be increased by an integer. Health remains at:", self.get_health())

    def increase_max_health(self, increase):
        """Used to increase the characters max health

        :param increase: the amount the health will increase by
        The function takes the increase amount and adds it to the characters max health.
        """
        try:
            int(increase)
            total = increase + self.get_max_health()
            self.set_max_health(total)

        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Value must be an integer. Max Health unchanged")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def increase_level(self):
        """"Used to increase character's level

        Character level will be increased by 1
        """
        self.__level = self.__level + 1
        total = self.get_experience_req() * 2

        self.__experience_req = total

    def increase_experience(self, increase):
        """Used to increase the characters Experience

        :param increase: the amount the character's experience will increase by
        The function takes the increase amount and adds it to the characters experience.
        If the characters total experience is more than experience_req they will be
        leveled up.
        """
        try:
            int(increase)
            total = increase + self.get_experience()

            if total >= self.get_experience_req():
                total = total - self.get_experience_req()
                self.__experience = total
                self.increase_level()

            else:
                self.__experience = total

        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Value must be an integer. Experience unchanged")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")