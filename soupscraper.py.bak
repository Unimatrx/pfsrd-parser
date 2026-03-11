import requests
import csv
from bs4 import BeautifulSoup
from pathlib import Path
import re

types = ["aberrations", "animals", "constructs", "dragons", "fey", "humanoids", "magical-beasts", "monstrous-humanoids", "oozes", "outsiders", "plants", "undead", "vermin"]

def scrape_creatures():
    with open("data/all_links.csv", "r") as link_file_read:
        csv_reader = csv.reader(link_file_read)
        all_links = list(csv_reader)[0]
    
    pages = []
    for i, link in enumerate(all_links):
        contents = requests.get(link).content
        assert type(contents) is bytes
        soup = BeautifulSoup(contents, "html.parser")
        chunk = soup.find(class_="article-content")
        filename = chunk.find("h1").text
        filename = filename.replace("/", " ")
        file_path = Path(f"data/monsterpages/{filename}.html")
        print(f"{i} {type(chunk)} {link}")
        if file_path.exists():
            filename = filename + "-2"
            file_path = Path(f"data/monsterpages/{filename}.html")
            with open(file_path, "w", encoding="utf-8") as writepage:
                    writepage.write(str(chunk))
        else:
            with open(file_path, "w", encoding="utf-8") as writepage:
                    writepage.write(str(chunk))

def scrape_creatures_url():
    with open("data/all_links.csv", "r") as link_file_read:
        csv_reader = csv.reader(link_file_read)
        all_links = list(csv_reader)[0]
    
    pages = []
    for i, link in enumerate(all_links):
        contents = requests.get(link).content
        assert type(contents) is bytes
        soup = BeautifulSoup(contents, "html.parser")
        chunk = soup.find(class_="article-content")
        filename = link
        safe_name = re.sub(r'[^\w\-_.]', '_', filename)
        file_path = f"data/monsterpages_url/{safe_name}.html"
        print(f"{i} {type(chunk)} {link}")
        with open(file_path, "w", encoding="utf-8") as writepage:
            writepage.write(str(chunk))


# def make_test_links(all_links):
#     test_links = []
#     for i, link in enumerate(all_links):
#         if i < 5500:
#             if link in all_links[i+1]:
#                 print(link)
#                 test_links.append(link)
#     with open("data/test_links.csv", "w") as link_file_write:
#         write = csv.writer(link_file_write)
#         write.writerow(test_links)

def make_all_links():
    all_links = []
    for ctype in types:
        some_links = link_scraper(ctype)
        for link in some_links:
            all_links.append(link)
    print(len(all_links))
    with open("data/all_links.csv", "w") as link_file_write:
        write = csv.writer(link_file_write)
        write.writerow(all_links)

def link_scraper(creaturetype):
    some_links = []
    link = f"https://www.d20pfsrd.com/bestiary/monster-listings/{creaturetype}"
    contents = requests.get(link).text
    soup = BeautifulSoup(contents, "html.parser")
    piece = soup.find(class_="ogn-childpages")
    monsterlist = piece.find_all(class_="page new parent")
    for monster in monsterlist:
        monsterhref = monster.find("a").get("href")
        # print(monsterhref)
        some_links.append(monsterhref)
    return some_links


if __name__ == "__main__":
    make_all_links()
    # scrape_creatures()
    scrape_creatures_url()

