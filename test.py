from dataclasses import dataclass
from pathlib import Path
import json

@dataclass
class Prepper:
    name: str
    game: str
    location: str
    role: str
    image: str
    folder: Path

    @classmethod
    def from_folder(clss, folder: Path) -> "Prepper":
        data = json.loads((folder / "data.json").read_text())
        return clss(**data, folder=folder)


# identify preppers who are missing a portrait (or is incorrectly named i guess)
def portrait_check():

    print("MISSING PORTRAITS:\n")

    prepper_folder = Path("preppers/")

    for prepper_path in prepper_folder.iterdir():
        portrait_path = Path(f"{prepper_path}/face_facility_portrait.jpg")

        if not portrait_path.is_file():
            print(f"{prepper_path}: Portrait Not Found")

portrait_check()

# identify preppers who are missing a data.json
def data_check():

    print("MISSING DATA:\n")

    prepper_folder = Path("preppers/")

    for prepper_path in prepper_folder.iterdir():
        data_path = Path(f"{prepper_path}/data.json")

        if not data_path.is_file():
            print(f"{prepper_path}: data.json Not Found")

data_check()


'''
prepper_folder = Path("preppers/")

for prepper_path in prepper_folder.iterdir():
    if not any(Path(prepper_path).iterdir()):
        continue
    else:
        prepper = Prepper.from_folder(prepper_path)
        print(f"{prepper.name}: {prepper.role}")
'''