import copy


class ABPruning:
    def __init__(self):
        self.nodes_visited = 0


    def ab_prune(self, board, depth, alpha, beta):
        self.nodes_visited += 1
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

                score = self.ab_prune(new_board, depth + 1, alpha, beta)
                max_val = max(max_val, score)
                alpha = max(alpha, max_val)
                if alpha >= beta:
                    break
            
            return max_val

        else:
            min_val = float("inf")
            for move in board.get_legal_moves():
                new_board = copy.deepcopy(board)
                new_board.make_move(move)

                score = self.ab_prune(new_board, depth + 1, alpha, beta)
                min_val = min(min_val, score)    
                beta = min(beta, min_val)
                if alpha >= beta:
                    break
            
            return min_val
        

    def best_move(self, board):
        best_score = -float('inf')
        best_move = None
        alpha, beta = float("-inf"), float("inf")
        for move in board.get_legal_moves():
            new_board = copy.deepcopy(board)
            new_board.make_move(move)

            score = self.ab_prune(new_board, 0, alpha, beta)
            print(f"move = {move}, score = {score}")
            if score > best_score:
                best_score = score
                best_move = move
                
            alpha = max(alpha, score)
        
        return best_move
    
