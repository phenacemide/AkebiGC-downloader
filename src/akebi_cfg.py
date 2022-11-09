import os


def create_akebi(path: str, version: str) -> None:
    os.system('mkdir akebi_cheat')
    os.system('cd akebi_cheat')
    print('Checking cfg.ini\n')
    with open("cfg.ini", 'w', encoding='UTF-8') as file:
        file.write(f"[Inject]\nGenshinPath = {path}")

    # with open("version.txt", 'w', encoding='UTF-8') as file:
    #     file.write(f"{version}")
