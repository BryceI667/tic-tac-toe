import copy


class MiniMax:
    def minimax(self, board, depth):
        if board.is_game_over():
            score = board.evaluate()

            if score > 0: # ai wins, prioritize quicker win
                return score - depth
            elif score < 0: # player wins, prioritize slower loss
                return score + depth
            else:
                return 0

        if board.player == 'O':
            max_val = -float("inf")
            for move in board.get_legal_moves():
                new_board = copy.deepcopy(board)
                new_board.make_move(move)

                score = self.minimax(new_board, depth + 1)
                max_val = max(max_val, score)
            
            return max_val

        else:
            min_val = float("inf")
            for move in board.get_legal_moves():
                new_board = copy.deepcopy(board)
                new_board.make_move(move)

                score = self.minimax(new_board, depth + 1)
                min_val = min(min_val, score)    
            
            return min_val
        

    def best_move(self, board):
        best_score = -float('inf')
        best_move = None
        for move in board.get_legal_moves():
            new_board = copy.deepcopy(board)
            new_board.make_move(move)

            score = self.minimax(new_board, 0)
            print(f"move = {move}, score = {score}")
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
