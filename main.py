import os
import time

from src import downloading_akebi
from src import colors

c = colors.Colors()


def start_menu() -> None:
    os.system("cls")
    print(f"{c.yellow}\n\n"
          f"             + --------------------------------- +\n"
          f"             |     Welcome To Akebi loader!      |\n"
          f"             |   Installing will be start soon.  |\n"                                       
          f"             + --------------------------------- +\n{c.RESET}\n")
    print(f"{c.grey_bg} DEVELOPER #1: menleev#0001 {c.grey_bg}|{c.blue}| "
          f"DEVELOPER #2: phenacemide#2436 {c.RESET}")


def end_menu() -> None:
    os.system("cls")
    print(f"{c.green}Installing finished successfully.{c.RESET}\n")
    print(f"{c.yellow}\n"
          f"             + ------------------------------------- +\n"
          f"             |    Thank u for using Akebi loader!    |\n"
          f"             + ------------------------------------- +\n{c.RESET}")
    print(f"{c.grey_bg} DEVELOPER #1: menleev#0001 {c.grey_bg}|{c.blue}| "
          f"DEVELOPER #2: phenacemide#2436 {c.RESET}")
    print(f"{c.red}You can delete akebi-loader.exe and other unnecessaries files will be deleted{c.RESET}")


def _exit():
    for i in range(5, 0, -1):
        print(f"Closing in {i}...")
        time.sleep(1.3)


def installing_akebi():
    if res := downloading_akebi.installer():
        end_menu()
    else:
        print(f"{c.red}Something went wrong...\n Error: {res[0]}")


def main():
    start_menu()
    time.sleep(2)
    installing_akebi()
    _exit()


if __name__ == '__main__':
    main()
