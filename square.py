def array_to_cord(cord_array):
    if cord_array[0] > 7 or cord_array[0] < 0 or cord_array[1] > 7 or cord_array[1] < 0:
        return "invalid cords"

    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return files[cord_array[0]] + str(cord_array[1] + 1)


class Square:
    def __init__(self, file, row, color, piece):
        self.file = file
        self.row = row
        self.color = color
        self.piece = piece

    def __str__(self):
        return array_to_cord([self.file, self.row])

    def get_cord(self):
        return [self.file, self.row]


