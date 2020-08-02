#Aug 2, Wirt Salthouse


class Player:

    def __init__(self, name, color_bool):
        self.is_white = color_bool
        if name == "":
            self.name = "White Player" if self.is_white else "Black_Player"
        else:
            self.name = name
