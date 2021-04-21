def do_battle(character, enemies):
    """
    Used to battle enemies.

    :param enemies: A list of enemies.
    The function does stuff.
    """
    # Battle each enemy
    while True:
        if not len(enemies): break
        for enemy in enemies:
            enemyHealth = enemy.get_health()
            if not enemyHealth:
                continue
            while True:
                try:
                    print("Your health: ", character.get_health())
                    print("Enemy health: ", enemyHealth)
                    print(
                        "(1) heal\n"
                        "(2) magic\n"
                        "(3) strike"
                    )
                    option = int(input("Pick an option: "))
                    # Check if good option
                    if option > 0 and option < 4:
                        break
                    print("Error: Input must be between 1-3.")
                except ValueError:
                    print("Error: Input must be a number.")
            # Do stuff based on option
            if option == 1:
                character.heal_character(1)
            elif option == 2:
                if character.get_has_magic():
                    # How does magic work?
                    print("Magic!")
                else:
                    print("Error: No magic.")
            elif option == 3:
                enemy.set_health(enemyHealth - character.get_damage())
                print("<<<!!!>>>")
            # Check if enemy is still alive
            enemyHealth = enemy.get_health()
            if not enemyHealth:
                continue
            # Enemy attack YOU
            character.reduce_health(enemy.get_damage())
            if not character.get_health():
                print("You died!")
                return
        #print("DEAD!")
    print("ALL ENEMIES DESTROYED!")