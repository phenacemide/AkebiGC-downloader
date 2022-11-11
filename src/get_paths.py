import os
import threading

from psutil import disk_partitions
from .GetTime_func import total_time

disks = tuple(i.device for i in disk_partitions())

genshin_path = False


def searching_full_genshinpath(disk, filename="GenshinImpact.exe") -> None:
    """
    This func is searching for a file in system.
    """
    global genshin_path

    for root, _, files in os.walk(disk):
        if filename in files:
            genshin_path = os.path.abspath(f"{root}\\{filename}")


@total_time
def multithreading_search(func=searching_full_genshinpath) -> tuple | bool:
    threads = []

    for disk in disks:
        t = threading.Thread(target=func, args=(disk,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    return genshin_path

