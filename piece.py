class Piece:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        
    def __str__(self):
        string = ""
        if self.color == "w":
            string += "white "
        elif self.color == "b":
            string += "black "
        else:
            string += "colorless "

        if self.id == "p":
            string += "pawn"

        if self.id == "b":
            string += "bishop"

        if self.id == "k":
            string += "king"

        if self.id == "n":
            string += "knight"

        if self.id == "r":
            string += "rook"

        if self.id == "q":
            string += "queen"
        return string
