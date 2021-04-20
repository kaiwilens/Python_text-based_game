class Weapons:
    __name = "Fist"
    __damage = 0
    __strength_req = 0
    __magic_req = 0

    def __init__(self, name="Fist", damage=0, strength_req=0, magic_req=0):
        self.__name = name
        self.__damage = damage
        self.__strength_req = strength_req
        self.__magic_req = magic_req

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def get_strength_req(self):
        return self.__strength_req

    def get_magic_req(self):
        return self.__magic_req

class Armor:
    __name = "None"
    __body_part = "None"
    __strength_req = 0
    __magic_req = 0
    __strength = 0
    __magic = 0
    __defense = 0

    def __init__(self, name="None", body_part="None", strength_req=0, magic_req=0, strength=0, magic=0, defense=0):
        self.__name = name
        self.__body_part = body_part
        self.__strength_req = strength_req
        self.__magic_req = magic_req
        self.__strength = strength
        self.__magic = magic
        self.__defense = defense

    def get_name(self):
        return self.__name

    def get_body_part(self):
        return self.__body_part

    def get_strength_req(self):
        return self.__strength_req

    def get_magic_req(self):
        return self.__magic_req

    def get_strength_increase(self):
        return self.__strength

    def get_magic_increase(self):
        return self.__magic

    def get_defense_increase(self):
        return self.__defense