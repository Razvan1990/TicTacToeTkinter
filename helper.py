class Helper:

    @staticmethod
    def check_number(number, dict_squares):
        if dict_squares[number] == "":
            return False
        else:
            return True

    @staticmethod
    def get_player_turn(dictionary_squares):
        counter_values = 0
        for square_index in dictionary_squares:
            if dictionary_squares[square_index] != "":
                counter_values += 1
        if counter_values % 2 == 1:
            return True
        else:
            return False

    def check_if_grid_full(self, dictionary_squares):
        for square in dictionary_squares:
            if dictionary_squares[square] == "":
                return True
        return False

    def define_winner(self, dictionary_squares):
        list_winner_squares = []
        '''define player1 winner'''
        # horizontal grids
        if (dictionary_squares[1] == "X" and dictionary_squares[2] == "X" and dictionary_squares[
            3] == "X"):
            list_winner_squares.append(1)
            list_winner_squares.append(2)
            list_winner_squares.append(3)
            return 1, list_winner_squares
        elif (dictionary_squares[4] == "X" and dictionary_squares[5] == "X" and dictionary_squares[
            6] == "X"):
            list_winner_squares.append(4)
            list_winner_squares.append(5)
            list_winner_squares.append(6)
            return 1, list_winner_squares
        elif (dictionary_squares[7] == "X" and dictionary_squares[8] == "X" and dictionary_squares[
            9] == "X"):
            list_winner_squares.append(7)
            list_winner_squares.append(8)
            list_winner_squares.append(9)
            return 1, list_winner_squares
        # vertical grids
        elif (dictionary_squares[1] == "X" and dictionary_squares[4] == "X" and dictionary_squares[
            7] == "X"):
            list_winner_squares.append(1)
            list_winner_squares.append(4)
            list_winner_squares.append(7)
            return 1, list_winner_squares
        elif (dictionary_squares[2] == "X" and dictionary_squares[5] == "X" and dictionary_squares[
            8] == "X"):
            list_winner_squares.append(2)
            list_winner_squares.append(5)
            list_winner_squares.append(8)
            return 1, list_winner_squares
        elif (dictionary_squares[3] == "X" and dictionary_squares[6] == "X" and dictionary_squares[
            9] == "X"):
            list_winner_squares.append(3)
            list_winner_squares.append(6)
            list_winner_squares.append(9)
            return 1, list_winner_squares
        # diagonal grids
        elif (dictionary_squares[1] == "X" and dictionary_squares[5] == "X" and dictionary_squares[
            9] == "X"):
            list_winner_squares.append(1)
            list_winner_squares.append(5)
            list_winner_squares.append(9)
            return 1, list_winner_squares
        elif (dictionary_squares[3] == "X" and dictionary_squares[5] == "X" and dictionary_squares[
            7] == "X"):
            list_winner_squares.append(3)
            list_winner_squares.append(5)
            list_winner_squares.append(7)
            return 1, list_winner_squares

        '''define player2 winner'''

        # horizontal grids
        if (dictionary_squares[1] == "0" and dictionary_squares[2] == "0" and dictionary_squares[
            3] == "0"):
            list_winner_squares.append(1)
            list_winner_squares.append(2)
            list_winner_squares.append(3)
            return 2, list_winner_squares
        elif (dictionary_squares[4] == "0" and dictionary_squares[5] == "0" and dictionary_squares[
            6] == "0"):
            list_winner_squares.append(4)
            list_winner_squares.append(5)
            list_winner_squares.append(6)
            return 2, list_winner_squares
        elif (dictionary_squares[7] == "0" and dictionary_squares[8] == "0" and dictionary_squares[
            9] == "0"):
            list_winner_squares.append(7)
            list_winner_squares.append(8)
            list_winner_squares.append(9)
            return 2, list_winner_squares
        # vertical grids
        elif (dictionary_squares[1] == "0" and dictionary_squares[4] == "0" and dictionary_squares[
            7] == "0"):
            list_winner_squares.append(1)
            list_winner_squares.append(4)
            list_winner_squares.append(7)
            return 2, list_winner_squares
        elif (dictionary_squares[2] == "0" and dictionary_squares[5] == "0" and dictionary_squares[
            8] == "0"):
            list_winner_squares.append(2)
            list_winner_squares.append(5)
            list_winner_squares.append(8)
            return 2, list_winner_squares
        elif (dictionary_squares[3] == "0" and dictionary_squares[6] == "0" and dictionary_squares[
            9] == "0"):
            list_winner_squares.append(3)
            list_winner_squares.append(6)
            list_winner_squares.append(9)
            return 2, list_winner_squares
        # diagonal grids
        elif (dictionary_squares[1] == "0" and dictionary_squares[5] == "0" and dictionary_squares[
            9] == "0"):
            list_winner_squares.append(1)
            list_winner_squares.append(5)
            list_winner_squares.append(9)
            return 2, list_winner_squares
        elif (dictionary_squares[3] == "0" and dictionary_squares[5] == "0" and dictionary_squares[
            7] == "0"):
            list_winner_squares.append(3)
            list_winner_squares.append(5)
            list_winner_squares.append(7)
            return 2, list_winner_squares

        '''define equality'''
        #if all conditions have not been met, then it is equality -> check if the board is full
        if not self.check_if_grid_full(dictionary_squares): #it's implemented inverse
            return 3, list_winner_squares
        #nothing happenned
        return 0, list_winner_squares
