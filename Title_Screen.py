import os
import math

banner = [
    "  ______                                      __   ____              ___ __       ",
    " /_  __/__  ____ ___  ____  ____  _________ _/ /  / __ \__  ______ _/ (_) /___  __",
    "  / / / _ \/ __ `__ \/ __ \/ __ \/ ___/ __ `/ /  / / / / / / / __ `/ / / __/ / / /",
    " / / /  __/ / / / / / /_/ / /_/ / /  / /_/ / /  / /_/ / /_/ / /_/ / / / /_/ /_/ / ",
    "/_/  \___/_/ /_/ /_/ .___/\____/_/   \__,_/_/  /_____/\__,_/\__,_/_/_/\__/\__, /  ",
    "                  /_/                                                    /____/   ",
]

def title_screen():
    badResponse = False
    while True:
        os.system("clear")
        rows = int(os.popen("tput lines").read())
        cols = int(os.popen("tput cols").read())
        print("-" * cols)
        print(("|" + " " * (cols - 2) + "|") * math.ceil((rows - math.ceil(len(banner) / 2)) / 2 - 3))
        for line in banner:
            print("|" + " " * math.floor((cols - len(line) - 2) / 2) + line + " " * math.ceil((cols - len(line) - 2) / 2) + "|")
        print(("|" + " " * (cols - 2) + "|") * math.floor((rows - math.floor(len(banner) / 2)) / 2 - 3 - 2))
        print("|1. Start Game" + " " * (cols - 15) + "|")
        print("|2. Exit      " + " " * (cols - 15) + "|")
        print("-" * cols)
        try:
            response = int(input("Invalid response! " if badResponse else ""))
            if response == 1:
                return
            elif response == 2:
                exit()
        except ValueError:
            pass
        badResponse = True
