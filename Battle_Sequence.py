def do_battle(self, enemies):
    """
    Used to battle enemies.

    :param enemies: A list of enemies.
    The function does stuff.
    """
    # Battle each enemy
    for enemy in enemies:
        while True:
            enemyHealth = enemy.get_health()
            if not enemyHealth:
                break
            while True:
                try:
                    print("Your health: ", self.get_health())
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
                self.heal_character(1)
            elif option == 2:
                if self.get_has_magic():
                    # How does magic work?
                    print("Magic!")
                else:
                    print("Error: No magic.")
            elif option == 3:
                enemy.set_health(enemyHealth - self.get_strength())
                print("<<<!!!>>>")
            # Enemy attack YOU
            self.reduce_health(enemy.get_strength())
            if not self.get_health():
                print("You died!")
                return
        print("DEAD!")
    print("ALL ENEMIES DESTROYED!")