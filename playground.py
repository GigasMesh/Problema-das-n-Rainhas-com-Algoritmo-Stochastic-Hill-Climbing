from chess_board import ChessBoard
from stochastic_hill_c import stochastic_hill_climbing as shc

b = ChessBoard() # criação do tabuleiro
print("ORIGINAL: ", b.fitness)
print(b)
b.queens = shc(b) # aplicação do hill climbing
b.update_board()
print("ALTERADO: ", b.fitness)
print(b)