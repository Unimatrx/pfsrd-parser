import json
from bs4 import BeautifulSoup


def open_monsters():
    with open('./data/monsters.json', 'r', encoding="utf-8") as f_:
        monsters_dict = json.load(f_)
    return monsters_dict

def clean_html(monsters_dict):
    return {key: BeautifulSoup(html, 'html5lib').prettify() for key, html in monsters_dict.items()}


def write_dict(monsters_dict):
    with open('./data/monsters_pretty.json', 'w', encoding='utf-8') as f:
        json.dump(monsters_dict, f, ensure_ascii=False, indent=2)
    

if __name__ == "__main__":
    write_dict(clean_html(open_monsters()))

