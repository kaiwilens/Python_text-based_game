import Enemies

slime_description = "This slime is equipped with a hover board. This makes it difficult to hit," \
                    "but one blow will kill it."

troll_description = "This troll is equipped with a rifle. " \
                    "It can attack from a distance, but its lack of experience with the weapon makes it inaccurate."

bouncer_description = "A bulky warrior who does not like you at all"

laser_spider_description = "This spider is equipped with high tech lasers. " \
                           "This gives it the ability to attack from a distance " \
                           "as well as bite at close range."

army_jeep_orcs_description = "A group of orcs armed with a jeep with a " \
                             "mounted gatling gun. YOU ARE FUCKED!"

# name, description, strength, damage, max_health, level, magic, magic_points, experience):
class Bouncer(Enemies.Enemy):
    def __init__(self):
        super().__init__("Bouncer", bouncer_description, 40, 5, 25, 2, False, 0, 30)
        
class BadGuy(Enemies.Enemy):
    def __init__(self):
        super(BadGuy, self).__init__("Bad Guy", "Not good", 30, 20, 30, 2, False, 0, 50)

class HBSlime(Enemies.Enemy):
    def __init__(self):
        super(HBSlime, self).__init__("Slime", slime_description, 5, 5, 10, 1, False, 0, 10)

class RifleTroll(Enemies.Enemy):
    def __init__(self):
        super(RifleTroll, self).__init__("Rifle Troll", troll_description, 40, 10, 50, 2, False, 0, 30)

class LSpider(Enemies.Enemy):
    def __init__(self):
        super(LSpider, self).__init__("Laser Spider", laser_spider_description, 40, 25, 50, 3, False, 0, 100)

class ArmyJeepOrcs(Enemies.Enemy): #The hell were you smoking luke ?
    def __init__(self):
        super(ArmyJeepOrcs, self).__init__("Army Jeep Orcs", army_jeep_orcs_description, 100, 100, 500, 10, False, 0, 1000)

badGuy = Enemies.Enemy("Bad Guy", "Not good", 30, 20, 30, 2, False, 0, 50)
hover_board_slime = Enemies.Enemy("Slime", slime_description, 5, 5, 10, 1, False, 0, 10)
troll_with_gun = Enemies.Enemy("Rifle Troll", troll_description, 40, 10, 50, 2, False, 0, 30)
bouncer = Enemies.Enemy("Rifle Troll", bouncer_description, 40, 5, 25, 2, False, 0, 30)
laser_spider = Enemies.Enemy("Laser Spider", laser_spider_description, 40, 25, 50, 3, False, 0, 100)
army_jeep_orcs = Enemies.Enemy("Army Jeep Orcs", army_jeep_orcs_description, 100, 100, 500, 10, False, 0, 1000)

enemy_list = [HBSlime, RifleTroll, LSpider]
bouncer_list = [Bouncer]
spider_list = [LSpider]