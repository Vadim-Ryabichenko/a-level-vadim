class ChessFigure:

    color = 'white'
    spot_digit_ver = 1
    spot_letter_gor = 1

    def change_color(self):
        if self.color == 'white':
            self.color = 'black'
        else: self.color = 'white'
    
    def _set_spot(self, first, second):
        if first >= 0 and first <= 7 and second >= 0 and second <= 7:
            self.spot_digit_ver = first
            self.spot_letter_gor = second

class Pawn(ChessFigure):

    def go(self, first, second):
        if self.color == 'white':
            self.first = first + 1
            self.second = second
        else: 
            self.first = first - 1
            self.second = second
        

     
            
class Officer(ChessFigure):
    pass

class Horse(ChessFigure):
    pass

    
class King(ChessFigure):
    pass

    

class Tour(ChessFigure):
    pass

    

class Queen(ChessFigure):
    pass
    
   

def check_spot(figures, num_1, num_2):
   
    figure_success = []

    for figure in figures:
        if  figure.first == num_1 and figure.second == num_2:
            figure_success.append(figure)

    return figure_success

officer = Officer()
officer.o_set_spot(2, 2)

print(check_spot([officer], 4, 4))
