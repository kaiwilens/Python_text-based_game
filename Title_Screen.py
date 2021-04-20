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


def print_banner(rows, cols):
    """Print the banner above, but with lines around it."""

    print("-" * cols)  # first row
    print(("|" + " " * (cols - 2) + "|\n") *
          math.ceil((rows - math.ceil(len(banner) / 2)) / 2 - 3),
          end='')
    for line in banner:
        print("|" + " " * math.floor((cols - len(line) - 2) / 2) + line +
              " " * math.ceil((cols - len(line) - 2) / 2) + "|")
    print(("|" + " " * (cols - 2) + "|\n") *
          math.floor((rows - math.floor(len(banner) / 2)) / 2 - 3 - 2),
          end='')
    print("|1. Start Game" + " " * (cols - 15) + "|")
    print("|2. Exit      " + " " * (cols - 15) + "|")

    print("-" * cols)  # last row


def title_screen():
    """Print out the initial title screen, and ask to start the game or exit."""

    badResponse = False
    while True:
        # Windows (nt) version
        if os.name == 'nt':
            lines = os.popen("mode con").read().split("\n")
            rows = 35  # int(lines[3].split(" ")[-1]) - 1
            cols = int(lines[4].split(" ")[-1]) - 1
            os.system("cls")
        else:
            # Linux Version
            os.system("clear")
            rows = int(os.popen("tput lines").read())
            cols = int(os.popen("tput cols").read())

        print_banner(rows, cols)

        try:
            response = int(input("Invalid response! " if badResponse else ""))
            if response == 1:
                return
            elif response == 2:
                exit()
        except ValueError:
            pass
        badResponse = True
