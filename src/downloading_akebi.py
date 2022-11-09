import os
import time
import requests

from .colors import c
from json import loads
from zipfile import ZipFile
from .GetTime_func import total_time
from .get_paths import multithreading_search


def get_downloading_link() -> str:

    latest_version = loads(requests.get('https://api.github.com/repos/Taiga74164/Akebi-GC/releases/latest').text)

    for item in latest_version['assets']:
        link = item['browser_download_url']
        if 'global' in link.lower().strip():
            return link


def downlaod_akebi() -> str:
    """
    Downloading an "Akebi-global.zip" archie and returning path to this file for next functions
    """
    start = time.time()

    link = get_downloading_link()
    filename = link.split('/')[-1]
    if os.path.exists(filename):
        return os.path.abspath(filename)

    print(f"{c.green}Starting download: {filename}{c.RESET}")

    req = requests.get(link)
    with open(filename, 'wb') as file:
        file.write(req.content)

    print(f"{c.green}{filename} has been download. {filename} was downloaded for {time.time() - start}{c.RESET}")

    return os.path.abspath(filename)


def creating_cheat_folder() -> str | None:
    path = multithreading_search()
    os.system('mkdir akebi_cheat')
    akebi_cheat_folder = os.path.abspath("akebi_cheat")
    with open(f"{akebi_cheat_folder}\\cfg.ini", 'w', encoding='UTF-8') as file:
        file.write(f"[Inject]\nGenshinPath = {path}")
    print(f'{c.green}{akebi_cheat_folder}\\cfg.ini was created succesfully{c.RESET}')
    return akebi_cheat_folder


@total_time
def excrat_akebi_zip(zip_path: str, cheat_folder: str):
    akebi_zip_path = zip_path
    akebi_cheat_folder = cheat_folder
    with ZipFile(akebi_zip_path, 'r') as z:
        z.extractall(akebi_cheat_folder)


def installer():
    try:
        creating_cheat_folder()
        print(f'{c.green}Extracting files{c.RESET}')
        akebi_zip_path = downlaod_akebi()
        akebi_cheat_folder = creating_cheat_folder()
        excrat_akebi_zip(akebi_zip_path, akebi_cheat_folder)
        return True
    except Exception as ex:
        return ex, False


def main():
    installer()


if __name__ == '__main__':
    main()
