import pathlib
import json

def generate_dict():
    filelist = []
    monster_dict = {}
    location = pathlib.Path("data/monsterpages_url")
    for entry in location.iterdir():
        if entry.is_file():
            filelist.append(entry)
    print(len(filelist))

    for file_ in filelist:
        with open(file_, 'r', encoding='utf-8') as f_:
            key_ = str(file_).split("_monster-listings_")[-1].removesuffix('_.html')
            value_ = f_.read()
            monster_dict.update({key_: value_})

    with open('monsters.json', 'w', encoding='utf-8') as f_:
        json.dump(monster_dict, f_, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_dict()