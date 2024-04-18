from pathlib import Path
import json
from models.club import ChessClub
from .base import BaseCommand

class GetClubsCommand(BaseCommand):
    def execute(self):
        data_folder="data/clubs"
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.clubs = []
        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    self.clubs.append(ChessClub(filepath))
                except json.JSONDecodeError:
                    print(filepath, "is invalid JSON file.")

        return self.clubs