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

thomas_southerland = Prepper.from_folder(Path("preppers/thomas_southerland"))

print(thomas_southerland.role)