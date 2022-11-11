import os
import time
from json import loads
from zipfile import ZipFile

import requests
from tqdm import tqdm

from .GetTime_func import total_time
from .colors import Colors
from .get_paths import multithreading_search

c = Colors()

desktop = os.path.abspath(os.environ['USERPROFILE'] + '\\Desktop')


def get_downloading_link() -> tuple:
    latest_version = loads(requests.get('https://api.github.com/repos/Taiga74164/Akebi-GC/releases/latest').text)

    for item in latest_version['assets']:
        link = item['browser_download_url']
        if 'global' in link.lower().strip():
            size = item['size']
            name = item['name']
            return link, size, name


def downlaod_akebi() -> str:
    """
    Downloading an "Akebi-global.zip" archie and returning path to this file for next functions
    """
    start = time.time()

    link, total_size, filename = get_downloading_link()

    if os.path.exists(filename):
        if not total_size > 40000000:
            return os.path.abspath(filename)
        os.remove(filename)

    print(f"{c.green}Starting download: {filename}{c.RESET}")

    chunk_size = 1024

    req = requests.get(link, stream=True)
    with open(filename, 'wb') as file:
        for data in tqdm(iterable=req.iter_content(chunk_size=chunk_size), total=int(total_size / chunk_size),
                         unit='KB'):
            file.write(data)

    print(f"{c.green}{filename} has been download. {filename} was downloaded for {time.time() - start}{c.RESET}")

    return os.path.abspath(filename)


def creating_cheat_folder() -> str | None:
    path = multithreading_search()
    akebi_cheat_folder = os.path.abspath(f'{desktop}\\akebi_cheat')
    os.system(f'mkdir {akebi_cheat_folder}')
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
    os.remove(akebi_zip_path)


def installer() -> tuple | bool:
    try:
        akebi_cheat_folder = creating_cheat_folder()
        akebi_zip_path = downlaod_akebi()
        print(f'{c.green}Extracting files{c.RESET}')
        excrat_akebi_zip(akebi_zip_path, akebi_cheat_folder)
        print(f"{c.green}Installation completed! Have fun ;){c.RESET}")
        return True
    except Exception as ex:
        return ex, False


def main():
    installer()


if __name__ == '__main__':
    main()
