from commands import ClubCreateCmd
from models.club_manager import ClubManager
from ..base_screen import BaseScreen


class ClubCreate(BaseScreen):
    """Screen displayed when creating a club"""

    def display(self):
        print("## Create club")

    def get_command(self):
        print("Type in the name of the club")
        name = self.input_string()
        cm = ClubManager()
        cm.create(name)
        # return ClubCreateCmd(name)