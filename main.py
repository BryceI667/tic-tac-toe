from game import Board
from minimax import MiniMax
from ab_pruning import ABPruning


if __name__ == "__main__":
    board_minimax, board_ab = Board(), Board()
    ai_minimax = MiniMax()
    ai_ab = ABPruning()

    while not board_minimax.is_game_over():
        if board_minimax.player == 'X':
            legal_moves = board_minimax.get_legal_moves()
            move = None
            while move not in legal_moves:
                move = int(input(f"Enter move: {legal_moves}"))
            board_minimax.make_move(move)
            board_ab.make_move(move)
        else:
            print("minimax scores:")
            best_move_minimax = ai_minimax.best_move(board_minimax)
            print("ab score:")
            best_move_ab = ai_ab.best_move(board_ab)
            print(f"minimax best move= {best_move_minimax}, nodes visited = {ai_minimax.nodes_visited}")
            print(f"ab best move= {best_move_ab}, nodes visited = {ai_ab.nodes_visited}")
            ai_minimax.nodes_visited = 0
            ai_ab.nodes_visited = 0
            board_minimax.make_move(best_move_minimax)
            board_ab.make_move(best_move_ab)
        print(board_minimax)
    
    board_minimax.evaluate()
    board_ab.evaluate()
    print("done!", board_minimax.winner, board_ab.winner)
    