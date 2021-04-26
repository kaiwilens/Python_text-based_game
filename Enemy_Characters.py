import Enemies

# name, description, strength, damage, max_health, level, magic, magic_points, experience):

badGuy = Enemies.Enemy("Bad Guy", "Not good", 30, 20, 30, 2, False, 0, 50)

slime_description = "This slime is equipped with a hover board. This makes it difficult to hit," \
                    "but one blow will kill it."

hover_board_slime = Enemies.Enemy("Slime", slime_description, 5, 5, 10, 1, False, 0, 10)

troll_description = "This troll is equipped with a rifle. " \
                    "It can attack from a distance, but its lack of experience with the weapon makes it inaccurate."

troll_with_gun = Enemies.Enemy("Rifle Troll", troll_description, 40, 10, 50, 2, False, 0, 30)

bouncer_description = "A bulky warrior who does not like you at all"
bouncer = Enemies.Enemy("Rifle Troll", bouncer_description, 40, 5, 25, 2, False, 0, 30)

laser_spider_description = "This spider is equipped with high tech lasers. " \
                           "This gives it the ability to attack from a distance " \
                           "as well as bite at close range."

laser_spider = Enemies.Enemy("Laser Spider", laser_spider_description, 40, 25, 50, 3, False, 0, 100)

army_jeep_orcs_description = "A group of orcs armed with a jeep with a " \
                             "mounted gatling gun. YOU ARE FUCKED!"

army_jeep_orcs = Enemies.Enemy("Army Jeep Orcs", army_jeep_orcs_description, 100, 100, 500, 10, False, 0, 1000)

enemy_list = [hover_board_slime, troll_with_gun, laser_spider]
bouncer_list = [bouncer]
spider_list = [laser_spider]