from game import Board
from minimax import MiniMax


if __name__ == "__main__":
    board = Board()
    ai = MiniMax()

    while not board.is_game_over():
        if board.player == 'X':
            legal_moves = board.get_legal_moves()
            move = None
            while move not in legal_moves:
                move = int(input(f"Enter move: {legal_moves}"))
            board.make_move(move)
        else:
            best_move = ai.best_move(board)
            print(f"best move= {best_move}")
            board.make_move(best_move)
        print(board)
    
    print("done!", board.winner)
