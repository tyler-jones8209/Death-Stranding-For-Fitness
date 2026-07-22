from dataclasses import dataclass
from pathlib import Path
import json
from locations import business_list
from locations import misc_list
import random
import orders


@dataclass
class Character:
    name: str
    game: str
    location: str
    affiliation: str
    role: str
    image: str
    folder: Path

    @classmethod
    def from_folder(clss, folder: Path) -> "Character":
        data = json.loads((folder / "data.json").read_text())
        return clss(**data, folder=folder)


# identify characters who are missing a portrait (or is incorrectly named i guess)
def portrait_check():

    print("MISSING PORTRAITS:\n")

    character_folder = Path("characters/")

    for character_path in character_folder.iterdir():
        portrait_path = Path(f"{character_path}/face_facility_portrait.jpg")

        if not portrait_path.is_file():
            print(f"{character_path}: Portrait Not Found")

# identify characters who are missing a data.json
def data_check():

    print("MISSING DATA:\n")

    character_folder = Path("characters/")

    for character_path in character_folder.iterdir():
        data_path = Path(f"{character_path}/data.json")

        if not data_path.is_file():
            print(f"{character_path}: data.json Not Found")


# meant to check if the affiliation var was present but this also works if it's present but empty too lmao
def affiliation_check():

    print("MISSING AFFILIATION:\n")

    character_folder = Path("characters/")

    for character_path in character_folder.iterdir():
        character = Character.from_folder(character_path)

        if not character.affiliation:
            print(f"{character_path}: Missing Affiliation")

def get_avail_characters():

    avail_char_paths = []

    character_folder = Path("characters/")

    for character_path in character_folder.iterdir():

        data_path = Path(f"{character_path}/data.json")
        portrait_path = Path(f"{character_path}/face_facility_portrait.jpg")

        if not data_path.is_file() or not portrait_path.is_file():
            continue

        else:
            avail_char_paths.append(character_path)

    return avail_char_paths

avail_char_paths = get_avail_characters()

random_location1 = business_list[random.randint(0, len(business_list) - 1)]
random_location2 = business_list[random.randint(0, len(business_list) - 1)]

while True:
    if random_location2 == random_location1:
        random_location2 = business_list[random.randint(0, len(business_list) - 1)]
    break

random_misc1 = misc_list[random.randint(0, len(misc_list) - 1)]

random_character_path1 = avail_char_paths[random.randint(0, len(avail_char_paths) - 1)]
random_character_path2 = avail_char_paths[random.randint(0, len(avail_char_paths) - 1)]

random_character1 = Character.from_folder(random_character_path1)
random_character2 = Character.from_folder(random_character_path2)

while True:
    if random_character_path2 == random_character_path1:
        random_character_path2 = avail_char_paths[random.randint(0, len(avail_char_paths) - 1)]
        random_character2 = Character.from_folder(random_character_path2)
    break

random_order = orders.retrieve_order(character1=random_character1.name, character2=random_character2.name, location1=random_location1, location2=random_location2, misc_location1=random_misc1)

#print(random_order)
#portrait_check()
#data_check()
#affiliation_check()