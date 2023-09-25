class ChessFigure:

    color = 'white'
    first = 1
    second = 1

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

    def move(self, first, second):
        if self._check_spot(first, second) and self.check_move(first, second):
            print("Move is correct")
            self.set_spot(first, second)
            return True
        else:
            print("Move is incorrect")
            return False


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
        if figure.move(num1, num2) == True:
            figures_result.append(figure)
    return figures_result


pawn = Pawn()
pawn.change_color()
print(pawn.color)
pawn.set_spot(3, 2)
       
bishop = Bishop()
bishop.set_spot(3, 2)

knight = Knight()
knight.set_spot(3, 2)

king = King()
king.set_spot(3, 2)

rook = Rook()
rook.set_spot(3, 2)

queen = Queen()
queen.set_spot(3, 2)

print(f'Figures who can move to given place is: {figure_can_move([pawn, bishop, knight, king, rook, queen], 2, 2)}')