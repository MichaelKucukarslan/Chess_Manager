# [x] Get the club names
# [x] Display the club names
# [x] display the instructions
# [ ] Clean up class OOP
from base_screen import BaseScreen
import json
from pathlib import Path
from club import ChessClub

class Main(BaseScreen):
    def __init__(self):
        pass

    def get_command(self):
        while True:
            print("--Main Menu--")
            self.get_clubs()
            print("")
            print("Type C to create a club or a club number to view/edit it.")
            print("Type T to enter Tournament Menu.")
            print("Type X to exit.")
            value = self.input_string()
            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.clubs) + 1):
                    pass
            elif value.upper() == "C":
                pass
            elif value.upper() == "T":
                pass
            elif value.upper() == "X":
                break

    def get_clubs(self):
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

        for index, club in enumerate (self.clubs, 1):
            print(index , club.name)

    def run(self):
        self.get_command()

if __name__ == "__main__":
    main = Main()
    main.run()