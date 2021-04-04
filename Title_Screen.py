import os
import math


def title_screen():
    rows = int(os.popen("tput lines").read())
    cols = int(os.popen("tput cols").read())
    print("-" * cols)
    print(("|" + " " * (cols - 2) + "|") * int((rows - 3) / 2 - 3))
    print("|" + " " * math.floor((cols - 84) / 2) + "  ______                                      __   ____              ___ __       " + " " * math.ceil((cols - 84) / 2) + "|")
    print("|" + " " * math.floor((cols - 84) / 2) + " /_  __/__  ____ ___  ____  ____  _________ _/ /  / __ \__  ______ _/ (_) /___  __" + " " * math.ceil((cols - 84) / 2) + "|")
    print("|" + " " * math.floor((cols - 84) / 2) + "  / / / _ \/ __ `__ \/ __ \/ __ \/ ___/ __ `/ /  / / / / / / / __ `/ / / __/ / / /" + " " * math.ceil((cols - 84) / 2) + "|")
    print("|" + " " * math.floor((cols - 84) / 2) + " / / /  __/ / / / / / /_/ / /_/ / /  / /_/ / /  / /_/ / /_/ / /_/ / / / /_/ /_/ / " + " " * math.ceil((cols - 84) / 2) + "|")
    print("|" + " " * math.floor((cols - 84) / 2) + "/_/  \___/_/ /_/ /_/ .___/\____/_/   \__,_/_/  /_____/\__,_/\__,_/_/_/\__/\__, /  " + " " * math.ceil((cols - 84) / 2) + "|")
    print("|" + " " * math.floor((cols - 84) / 2) + "                  /_/                                                    /____/   " + " " * math.ceil((cols - 84) / 2) + "|")
    print(("|" + " " * (cols - 2) + "|") * int((rows - 3) / 2 - 3))
    print("-" * cols)
    input("Press Enter to continue")
