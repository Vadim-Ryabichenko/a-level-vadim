class ChessFigure:

    def __init__(self, color, first, second, name):
        self.color = color
        self.first = first
        self.second = second
        self.name = name

    def __str__(self):
        return f"figure name: {self.name}, start spot: {self.first}, {self.second}"

    def change_color(self):
        if self.color == 'white':
            self.color = 'black'
        else: self.color = 'white'

    def _check_spot(self, first, second):
        if 0 <= first <= 7 and 0 <= second <= 7:
            return True
        else: return False

    def set_spot(self, first, second):
        if self._check_spot(first, second) == True:
            self.first = first
            self.second = second
        
    def check_move(self, first, second):
        ...

class Pawn(ChessFigure):

    def check_move(self, first, second):
        if self.color == 'white' and (self.first - first == -1 and second == second):
            return True
        if self.color == 'black' and (self.first - first == 1 and second == second):
            return True
        else: return False

class Bishop(ChessFigure):

    def check_move(self, first, second):
        if abs(self.first - first) == abs(self.second - second):
            return True
        else: return False

class Knight(ChessFigure):

    def check_move(self, first, second):
        dfirst = abs(self.first - first)
        dsecond = abs(self.second - second)
        if (dfirst == 2 and dsecond == 1) or (dfirst == 1 and dsecond == 2):
            return True
        else: return False

class King(ChessFigure):
    
    def check_move(self, first, second):
        dfirst = abs(self.first - self.second)
        dsecond = abs(self.second - second)
        if dfirst <= 1 and dsecond <= 1:
            return True
        else: return False

class Rook(ChessFigure):

    def check_move(self, first, second):
        if self.first == first or self.second == second:
            return True
        else: return False

class Queen(ChessFigure):

    def check_move(self, first, second):
        dfirst = abs(self.first - first)
        dsecond = abs(self.second - second)
        if self.first == first or self.second == second or dfirst == dsecond:
            return True
        else: return False

figures_result = []

def figure_can_move(figures, num1, num2):
    for figure in figures:
        if figure.check_move(num1, num2) == True:
            figures_result.append(figure.__str__())
    return figures_result

pawn = Pawn('white', 3, 2, 'pawn')
pawn.change_color()
       
bishop = Bishop('black', 4, 4, 'bishop')
bishop.change_color()

knight = Knight('white', 2, 2, 'knight')
knight.change_color()

king = King('white', 5, 5, 'king')
king.change_color()

rook = Rook('black', 4, 4, 'rook')

queen = Queen('black', 3, 6, 'queen')
queen.change_color()


print(f'Figures who can move to given place is: {figure_can_move([pawn, bishop, knight, king, rook, queen], 2, 2)}')