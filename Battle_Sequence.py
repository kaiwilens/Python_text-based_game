options = [
    "strike",
    "inventory",
    "retreat",
]


def do_battle(character, enemies):
    """
    Used to battle enemies.

    :param enemies: A list of enemies.
    The function does stuff.
    """
    # Battle each enemy
    in_battle = True
    while True:
        if not len(enemies):
            break
        for enemy in enemies:
            enemyHealth = enemy.get_health()
            if not enemyHealth:
                continue

            print(enemy.get_description())
            while True:
                try:
                    print(str(character.hub()) + "   " + str(enemy.hub()))
                    print("Your health:", character.get_health())
                    print("Enemy health:", enemyHealth)
                    for i in range(0, len(options)):
                        print("(%i) %s" % (i + 1, options[i]))
                    option_id = int(input("Pick an option: "))
                    # Check if good option
                    if option_id > 0 and option_id <= len(options):
                        break
                    print("Error: Input must be between 1-%i." % len(options))
                except ValueError:
                    print("Error: Input must be a number.")
            option = options[option_id - 1]
            # Do stuff based on option
            if option == "strike":
                enemy.set_health(enemyHealth - character.get_damage())
                print("<<<!!!>>>")
            elif option == "inventory":
                print("Inventory")
                # add code for inventory here
            elif option == "retreat":
                print("Retreating")
                return True
            # Check if enemy is still alive
            enemyHealth = enemy.get_health()
            if not enemyHealth:
                print("Enemy destroyed!")
                return True
               # continue
            # Enemy attack YOU
            character.reduce_health(enemy.get_damage())
            if not character.get_health():
                print("You died!")
                return False
    print("ALL ENEMIES DESTROYED!")
    return True
