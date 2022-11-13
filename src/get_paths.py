import os
import threading
import time

from psutil import disk_partitions
from src.colors import Colors
disks = tuple(i.device for i in disk_partitions())[::-1]

genshin_path = False
c = Colors()


def searching_full_genshinpath(disk, filename="GenshinImpact.exe") -> None:
    """
    This func is searching for a file in system.
    """
    global genshin_path

    for root, _, files in os.walk(disk):
        print(root)
        if genshin_path:
            break
        if filename in files:
            print(f"{c.green}{filename} was found in {root}!{c.RESET}")
            genshin_path = os.path.abspath(f"{root}\\{filename}")
            break


def multithreading_search(func=searching_full_genshinpath) -> tuple | bool:
    print(f"Starting GenshinImpact.exe researcher func\nIt may take some time...")
    time.sleep(1)

    threads = []

    global genshin_path

    for disk in disks:
        t = threading.Thread(target=func, args=(disk,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    return genshin_path

