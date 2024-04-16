# [ ] Get the club names
# [ ] Display the club names
# [x] display the instructions
from base_screen import BaseScreen

class Main(BaseScreen):
    def __init__(self):
        print("Enter ")

    def get_command(self):
        while True:
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

    def run(self):
        self.get_command()

if __name__ == "__main__":
    main = Main()
    main.run()