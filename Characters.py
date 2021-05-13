import enum

import NPC

import Character_Helper_Functions
from Character_Helper_Functions import my_banner
import Usable_Armor_Weapons
import Armor_Weapons_Class


class Occupations(enum.Enum):
    na = 0
    Cop = 1
    Doctor = 2
    Zoo_Keeper = 3
    Fire_Fighter = 4
    Thief = 5
    Blue_Collar = 6
    Chemist = 7


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
    __defense = 0
    __has_magic = False
    __magic = 0
    __equipped_weapon = Usable_Armor_Weapons.fists
    __head = Usable_Armor_Weapons.naked
    __chest = Usable_Armor_Weapons.naked
    __legs = Usable_Armor_Weapons.naked
    __feet = Usable_Armor_Weapons.naked


    def __init__(self, name, description, strength, damage, max_health, defense, occupation, magic, magic_points):
        super().__init__(name, description, strength, damage, max_health)


        self.__defense = Character_Helper_Functions.set_attributes(defense, "Defense")
        self.__occupation = Character_Helper_Functions.check_enum(Occupations, occupation)
        self.__has_magic = Character_Helper_Functions.check_boolean(magic)
        if self.__has_magic:
            self.__magic = Character_Helper_Functions.set_attributes(magic_points, "Magic Points")

    def hub(self):
        info_panel = "NAME: " + str(self.get_name()) + "   LEVEL: " + str(self.get_level()) + "   HP: " + str(self.get_health()) + "/" + str(self.get_max_health()) + \
                     "   WEAPON: " + str(self.get_equipped_weapon()) + \
                     "   DMG: " + str(self.get_damage()) + "   DEF: " + str(self.get_defense()) + \
                     "   XP: " + str(self.get_experience()) + "/" + str(self.get_experience_req())
        border = "-" * len(info_panel)

        print(border)
        print(info_panel)
        print(border)
        print()

    def get_damage(self):
        return NPC.NPC.get_damage(self) + self.__equipped_weapon.get_damage()

    def get_strength(self):
        total_strength = 0

        total_strength += self.__feet.get_strength_increase()
        total_strength += self.__legs.get_strength_increase()
        total_strength += self.__chest.get_strength_increase()
        total_strength += self.__head.get_strength_increase()

        return NPC.NPC.get_strength(self) + total_strength



    def set_defense(self, defense):
        self.__defense = Character_Helper_Functions.set_attributes(defense, "Defense")

    def get_defense(self):
        total = 0

        total += self.__feet.get_defense_increase()
        total += self.__legs.get_defense_increase()
        total += self.__chest.get_defense_increase()
        total += self.__head.get_defense_increase()
        return self.__defense + total

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
            self.__magic = Character_Helper_Functions.set_attributes(magic_points, "Magic Points")

    def get_magic(self):
        total = 0

        total += self.__feet.get_magic_increase()
        total += self.__legs.get_magic_increase()
        total += self.__chest.get_magic_increase()
        total += self.__head.get_magic_increase()

        return self.__magic + total

    def get_is_alive(self):
        return self.__is_alive

    def set_equipped_weapon(self, weapon=Armor_Weapons_Class.Weapons()):

        strength_met = False
        magic_met = False

        if weapon.get_strength_req() <= self.get_strength():
            strength_met = True
        else:
            print("You are not strong enough to wield this weapon")

        if weapon.get_magic_req() <= self.get_magic():
            magic_met = True
        else:
            print("You do not have enough magic to wield this weapon")

        if strength_met and magic_met:
            self.__equipped_weapon = weapon

    def equip_armor(self, armor=Armor_Weapons_Class.Armor()):
        strength_met = False
        magic_met = False

        if armor.get_strength_req() <= self.get_strength():
            strength_met = True
        else:
            print("You are not strong enough to wear the " + armor.get_name())

        if armor.get_magic_req() <= self.get_magic():
            magic_met = True
        else:
            print("You do not have enough magic to wear the " + armor.get_name())

        if strength_met and magic_met:
            body_part = armor.get_body_part().upper()

            if body_part == "FEET":
                self.__feet = armor

            if body_part == "LEGS":
                self.__legs = armor

            if body_part == "CHEST":
                self.__chest = armor

            if body_part == "HEAD":
                self.__head = armor


    def get_equipped_weapon(self):
        return self.__equipped_weapon.get_name()

    def get_head_armor(self):
        return self.__head.get_name()

    def get_chest_armor(self):
        return self.__chest.get_name()

    def get_leg_armor(self):
        return self.__legs.get_name()

    def get_feet_armor(self):
        return self.__feet.get_name()

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
            self.set_strength(total)

        except ValueError:
            print("Strength must be increased by an integer. Strength remains at:", self.get_strength())

    def increase_defense(self, increase):
        """Used to increase the characters Defense

        :param increase: the amount the defense will increase by
        The function takes the increase amount and adds it to the characters current defense.
        Defense is used to reduce the damage taken by enemies
        """
        try:
            int(increase)
            total = self.get_defense() + increase
            self.set_defense(total)

        except ValueError:
            print("Damage must be increased by an integer. Defense remains at:", self.get_defense())

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

            if total_health > self.get_max_health():
                self.set_health(self.get_max_health())

            else:
                self.set_health(total_health)

        except ValueError:
            print("Health must be increased by an integer. Health remains at:", self.get_health())

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
            defense_percentage = self.get_defense() / 1000
            damage_reduction = damage * defense_percentage
            health_reduction = damage - damage_reduction

            total_health = self.get_health() - health_reduction

            if total_health < 1:
                self.__is_alive = False
                self.set_health(0)

            else:
                self.set_health(total_health)

        except ValueError:
            print("Health must be decreased by an integer. Health remains at:", self.get_health())

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
            my_banner("Value must be an integer. Max Health unchanged")

    def increase_level(self):
        """"Used to increase character's level

        Character level will be increased by 1 and their attributes will be increased
        according to what the character occupation is. Health get set to max_health
        """
        self.__level = self.__level + 1
        total = self.get_experience_req() * 2
        self.__experience_req = total

        if self.get_occupation() == "Zoo_Keeper":
            self.increase_strength(2)
            self.increase_defense(2)
            self.increase_max_health(10)
            self.increase_magic(15)

        if self.get_occupation() == "Doctor":
            self.increase_strength(2)
            self.increase_defense(2)
            self.increase_max_health(8)
            self.increase_magic(10)

        if self.get_occupation() == "Chemist":
            self.increase_strength(3)
            self.increase_defense(2)
            self.increase_max_health(8)
            self.increase_magic(12)

        if self.get_occupation() == "Fire_Fighter":
            self.increase_strength(2)
            self.increase_defense(3)
            self.increase_max_health(8)
            self.increase_magic(8)

        if self.get_occupation() == "Thief":
            self.increase_strength(2)
            self.increase_defense(2)
            self.increase_max_health(12)

        if self.get_occupation() == "Cop":
            self.increase_strength(2)
            self.increase_defense(3)
            self.increase_max_health(15)

        if self.get_occupation() == "Blue_Collar":
            self.increase_strength(3)
            self.increase_defense(2)
            self.increase_max_health(10)

        self.set_health(self.get_max_health())

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
                # ADDING WHILE LOOP TO KEEP INCREASING LEVEL
                while total >= self.get_experience_req():
                    total = total - self.get_experience_req()
                    self.__experience = total
                    self.increase_level()

            else:
                self.__experience = total

        except ValueError:
            my_banner("Value must be an integer. Experience unchanged")
