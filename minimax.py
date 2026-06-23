import copy
import game


class MiniMax:
    def __init__(self):
        self.board = game.Board()
        

    def minimax(self, board, is_maximizing):
        if len(self.board.get_legal_moves()) == 0:
            return self.board.evaluate()

        if is_maximizing:
            max_val = -float("inf")
            for move in self.board.get_legal_moves():
                new_board = copy.deepcopy(board, False)
                new_board.make_move(move)

                score = new_board.minimax(new_board, False)
                max_val = max(max_val, score)
            
            return max_val

        if not is_maximizing:
            min_val = float("inf")
            for move in self.board.get_legal_moves():
                new_board = copy.deepcopy(board, True)
                new_board.make_move(move)

                score = new_board.max_state()
                min_val = min(min_val, score)    
            
            return min_val
        

    def best_move(self):
        best_score = float('inf')
        best_move = None
        for move in self.board.get_legal_moves():
            new_board = copy.deepcopy(self.board)
            new_board.make_move()

            score = self.minimax(new_board, False)
            if score > best_score:
                best_score = score
                best_move = move

            if score == 1:
                break
        
        return best_move
    
