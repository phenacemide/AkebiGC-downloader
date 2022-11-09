import os
import threading

from psutil import disk_partitions
from pyperclip import copy
from .GetTime_func import total_time

disks = tuple(i.device for i in disk_partitions())

genshin_path = None


def copy_to_clipboard(data) -> copy:
    print(fr'Full path "{data}" is copied to the clipboard')
    return copy(data)


def searching_full_genshinpath(disk, filename="GenshinImpact.exe") -> str:

    global genshin_path

    for root, _, files in os.walk(disk):
        if filename in files:
            genshin_path = f"{root}\\{filename}"
            return genshin_path


@total_time
def multithreading_search(func=searching_full_genshinpath) -> str | None:
    threads = []
    for disk in disks:
        t = threading.Thread(target=func, args=(disk,), daemon=True)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return genshin_path


def main():
    func = searching_full_genshinpath
    path = multithreading_search(func)
    copy_to_clipboard(path)


if __name__ == '__main__':
    main()
