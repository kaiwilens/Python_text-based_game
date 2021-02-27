import enum


def set_attributes(value, attribute):
    """Verifies integer input for attributes

    :param value: The integer input from the user
    :param attribute: The attribute to be set
    The code attempts to convert the input from the constructor and getters and setters
    and return the integer value for attributes such as strength, damage, health, and max health.
    If the return fails an error message is displayed and the attributes is set to 0.
    """
    try:
        int(value)
        return int(value)
    except ValueError:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Value must be an integer.", attribute.upper(), " set to 0")
        print("Use", attribute.upper(), "setter function to change attribute")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return 0


class Characters:
    # Character private variables
    __name = "na"
    __description = "na"
    __strength = 0
    __damage = 0
    __health = 0
    __max_health = 0  # MAX HEALTH IS USED SO THAT A CHARACTER CANNOT HAVE AN INFINITE AMOUNT OF HEALTH WHEN HEALING
    __is_alive = True  # is_alive can be used to exit battle functions once one of the characters health reaches 0

    # Character constructor
    def __init__(self, name, description, strength, damage, max_health):
        self.__name = name
        self.__description = description
        self.__strength = set_attributes(strength, "strength")
        self.__damage = set_attributes(damage, "Damage")
        self.__max_health = set_attributes(max_health, "Max health")
        self.__health = set_attributes(max_health, "health")

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
        self.__strength = set_attributes(strength, "strength")

    def get_strength(self):
        return self.__strength

    def set_damage(self, damage):
        self.__damage = set_attributes(damage, "Damage")

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
        self.__max_health = set_attributes(max_health, "Max Health")
        self.__health = set_attributes(max_health, "health")

    def get_max_health(self):
        return self.__max_health

    def get_is_alive(self):
        return self.__is_alive

    #Character member functions for various actions

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
            print("Health must be decreased by an integer. Health remains at:", self.get_health())

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


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




