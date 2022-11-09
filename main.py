import os
import time

from src.get_paths import copy_to_clipboard, multithreading_search
from src.downloading_akebi import installer
from src.colors import c


def print_menu() -> None:
    os.system("cls")
    print(f"{c.red}\n\n"
          f"                 + --------------------------------- +\n"
          f"                 |      A K E B I  - L O A D E R     |\n"
          f"                 + --------------------------------- +\n")
    print(c.RESET)
    print('[- ======================================================================= -]')
    print(c.yellow)
    print(f"[1]   Default Installer (genshin path, install akebi, create akebi folder)")
    print(f"[2]   Get full path to 'GenshinImpact.exe' and copy it to clipboard")
    print(f"[3]   About devs")
    # print(f"[4]   Check latest akebi version and install it (if akebi has new release)")
    print(f"[Q]   Exit")
    print(c.RESET)
    print('[- ======================================================================= -]\n')
    print(f"{c.green}[MENU] Please select operation number:{c.RESET}", end=' ')


def case_1():
    if res := installer():
        input(f"{c.green}Installing finished successfully. Press enter to exit.{c.RESET}")
    print(f"{c.red}Something went wrong...\n Error: {res[0]}")


def case_2():
    return copy_to_clipboard(multithreading_search())


def case_3():
    print(
        f"{c.grey_bg} DEVELOPER #1: menleev#0001 {c.RESET}\n{c.grey_bg}{c.blue} "
        f"DEVELOPER #2: phenacemide#2436 {c.RESET}")


def main() -> str | bool:
    print_menu()
    action = input().lower().strip()
    match action:
        case '1':
            case_1()
        case '2':
            case_2()
        case '3':
            case_3()
        case 'q' | 'e':
            return True
        case other:
            input('\bUnavailable command! Try again (press enter) ')
            time.sleep(1)
            os.system("cls")
            main()


if __name__ == '__main__':
    main()
