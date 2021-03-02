import enum

import baseCharacterClass


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


def check_enum(enumerator, value):
    """Verifies value input for enumerators

     :param enumerator: The enumerator that will be checked
     :param value: The value that will be checked against enumerator values
     The code checks the value entered by the user and compares it to the enumerator values.
     If it matches one of the enumerator values then the member variable will be set.
     If it does not then the member variable will be set to NA
     """
    is_valid = False
    for data in enumerator:
        if data == value:
            is_valid = True
            break

    if is_valid:
        return value
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Value must be from enum ", enumerator, " Value has been set to N/A")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return "na"


class Player(baseCharacterClass.Characters):
    __occupation = Occupations.na
    __enhancement = Enhancements.na

    def __init__(self, name, description, strength, damage, max_health, occupation):
        super().__init__(name, description, strength, damage, max_health)
        self.__occupation = check_enum(Occupations, occupation)

    def set_occupation(self, occupation):
        self.__occupation = check_enum(Occupations, occupation)

    def get_occupation(self):
        return self.__occupation.name
