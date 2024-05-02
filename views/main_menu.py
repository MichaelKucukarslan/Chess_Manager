from .base_screen import BaseScreen
from views.clubs import ClubView
from views.clubs import ClubCreate

from commands import ClubCreateCmd
# from ..commands import 
# Create a tournament command


class MainMenu(BaseScreen):
    def __init__(self, clubs):
        print("--Main Menu--")
        self.clubs = clubs
        for index, club in enumerate (self.clubs, 1):
            print(index , club.name)
        pass

    def get_command(self):
        while True:
            print("")
            print("Type C to create a club or a club number to view/edit it.")
            print("Type T to enter Tournament Menu.")
            print("Type X to exit.")
            value = self.input_string()
            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.clubs) + 1):
                    club_view = ClubView(club=self.clubs[value - 1])
                    club_view.display()
                    club_view.get_command()
                    pass
            elif value.upper() == "C":
                create_club = ClubCreate()
                create_club.display()
                create_club.get_command()
                pass
            elif value.upper() == "T":
                club_view = ClubView(club=self.clubs[value - 1])
                club_view.display()
                club_view.get_command()
                pass
            elif value.upper() == "X":
                club_view = ClubView(club=self.clubs[value - 1])
                club_view.display()
                club_view.get_command()
                break

    def run(self):
        self.get_command()

if __name__ == "__main__":
    main = MainMenu()
    main.run()