class Board:
    def __init__(self):
        self.winning_combinations = [[0, 1, 2],
                                [3, 4, 5],
                                [6, 7, 8],
                                [0, 3, 6],
                                [1, 4, 7],
                                [2, 5, 8],
                                [0, 4, 8],
                                [2, 4, 6]]

        self.board = [[" "] * 3 for _ in range(3)]
        self.winner = None
        self.player = 'X'
    

    def __str__(self):
        rows = []
        for row in self.board:
            rows.append(" | ".join(row))
        
        return "\n---------\n".join(rows)


    def get_legal_moves(self):
        viable_moves = []
        for idx in range(9):
            if self.board[idx // 3][idx % 3] == " ":
                viable_moves.append(idx)
        return viable_moves
    
    
    def is_game_over(self):
        return self.check_win() is not None or len(self.get_legal_moves()) == 0


    def make_move(self, move):
        legal_moves = self.get_legal_moves()
        if move not in legal_moves:
            print("Invalid move!")
            return
        self.board[move // 3][move % 3] = self.player
        self.player = 'O' if self.player == 'X' else 'X'


    def check_win(self):
        for c in self.winning_combinations:
            values = [
                self.board[idx // 3][idx % 3] for idx in c
            ]
            if values[0] != " " and all(v == values[0] for v in values):
                return values[0]

        return None
    

    def evaluate(self):
        winner = self.check_win()

        if winner == "O":
            self.winner = "O"
            return 100
        elif winner == "X":
            self.winner = "X"
            return -100
        else:
            self.winner = "TIE"
            return 0
