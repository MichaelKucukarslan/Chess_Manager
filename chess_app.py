from views import MainMenu
from commands import GetClubsCommand

class ChessApp:
    def __init__(self) -> None:
        pass

    def run(self):
        # Start main menu
        self.clubs = GetClubsCommand().execute()
        main = MainMenu(self.clubs)
        main.run()
        # continue the program
        
if __name__ == "__main__":
    app = ChessApp()
    app.run()