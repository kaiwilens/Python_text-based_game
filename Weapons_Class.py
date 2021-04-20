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
