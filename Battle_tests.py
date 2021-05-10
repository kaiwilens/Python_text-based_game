
from Story import Character, Occupations, do_battle
from Enemy_Characters import Bouncer, enemy_list
god = Character('God', 'Literally god himself', 999, 999, 9999, 999, Occupations.Chemist, False, 0)

def do_battle_single(player, enemy, count):
    enemies=[]
    for i in range(1,count):
        enemies.append(enemy())
    do_battle(player, enemies)

def do_battle_list(player, raw_enemies):
    enemies=[]
    for e in raw_enemies:
        enemies.append(e())
    do_battle(player, enemies)
do_battle_list(god, enemy_list)
#do_battle_single(god, Bouncer, 8)