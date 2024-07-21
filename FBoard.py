class FBoard:
    """
    A game of FBoard includes an 8x8 playing board and its current win state.
    """

    def __init__(self):
        """
        Instantiates a new game of FBoard. Player X has one piece starting at row 0 column 3.
        Player O has four pieces, all on row 7: columns 0, 2, 4, and 6. Creates a variable to hold
        the coordinate for the X player. Creates the game_state with the value "UNFINISHED".
        """
        self.__game_state = "UNFINISHED"  # Possible states are "UNFINISHED", "X_WON", and "O_WON".
        self.__board = [
            ["", "", "", "x", "", "", "", ""], 
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""], 
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""], 
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""], 
            ["o", "", "o", "", "o", "", "o", ""]
        ]
        self.__x_coor = (0, 3)

    def get_game_state(self):
        """
        Returns game_state
        """
        return self.__game_state

    def move_x(self, row, column):
        """
        If the game is UNFINISHED and the given coordinates are valid for player X to move to,
        moves X to the given row, column with player X, updates game_state, then returns True.
        If the attempted move is not valid, returns False.
        """
        if self.__game_state == "UNFINISHED":
            if (row, column) in self.__get_valid_x_moves():
                self.__board[row][column] = "x"  # Sets the new space to "x"
                self.__board[self.__x_coor[0]][self.__x_coor[1]] = ""  # Then clears the previous space
                self.__x_coor = (row, column)  # Updates x_coor to current player X coordinate.

                # If player X has reached row 7, player X wins.
                if self.__x_coor[0] == 7:
                    self.__game_state = "X_WON"
                return True
        return False

    def move_o(self, from_row, from_column, to_row, to_column):
        """
        If the game is UNFINISHED, the given from_row, from column contain an O piece, and the given to_row, to_column
        # are valid for the O piece to move to, moves it to to_row, to_column, updates game_state, then returns True.
        If the attempted move is not valid, returns False.
        """
        if self.__game_state == "UNFINISHED":
            if self.__board[from_row][from_column] == "o":
                if (to_row, to_column) in self.__get_valid_o_moves(from_row, from_column):
                    self.__board[to_row][to_column] = "o"  # Sets the new space to "o"
                    self.__board[from_row][from_column] = ""  # Then clears the previous space

                    # If player O blocked player X from new valid moves, player O wins.
                    if not self.__get_valid_x_moves():
                        self.__game_state = "O_WON"
                    return True
        return False

    def __get_valid_x_moves(self):
        """
        Helper method for move_x(). Returns a list of valid potential locations from the current player X location.
        """
        # Creates a dictionary containing the potential diagonal spaces around x_coor.
        potential_moves = {
            "row_plus_one_column_plus_one": (self.__x_coor[0] + 1, self.__x_coor[1] + 1),
            "row_plus_one_column_minus_one": (self.__x_coor[0] + 1, self.__x_coor[1] - 1),
            "row_minus_one_column_plus_one": (self.__x_coor[0] - 1, self.__x_coor[1] + 1),
            "row_minus_one_column_minus_one": (self.__x_coor[0] - 1, self.__x_coor[1] - 1)
        }

        return self.__check_potential_moves(potential_moves)

    def __get_valid_o_moves(self, row, column):
        """
        Helper method for move_o(). Returns a list of valid potential locations for the given O piece.
        """
        # Creates a dictionary containing the potential diagonal spaces around the given O piece.
        # An O piece cannot increase row, only decrease row.
        potential_moves = {
            "row_minus_one_column_plus_one": (row - 1, column + 1),
            "row_minus_one_column_minus_one": (row - 1, column - 1)
        }

        return self.__check_potential_moves(potential_moves)

    def __check_potential_moves(self, potential_moves):
        """
        Helper method that returns a list of valid moves from a given list of potential moves
        """
        valid_moves = list()

        for move in potential_moves:
            # Adds a value from potential_moves to valid_moves if it is within the bounds of the 8x8 game board
            if 0 <= potential_moves[move][0] <= 7 and 0 <= potential_moves[move][1] <= 7:
                # And if that space on the game board is not already occupied by another piece.
                if self.__board[potential_moves[move][0]][potential_moves[move][1]] == "":
                    valid_moves.append(potential_moves[move])

        # print(valid_moves)
        return valid_moves


# TESTING THE CODE
fb = FBoard()
fb.move_x(1, 4)
fb.move_x(2, 5)
fb.move_o(7, 0, 6, 1)
print(fb.get_game_state())
