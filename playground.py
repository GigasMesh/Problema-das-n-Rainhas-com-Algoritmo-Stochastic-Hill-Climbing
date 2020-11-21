from Board import Board
from SHillClimbing import SHillClimbing as shc

b = Board() # criação do tabuleiro
print("ORIGINAL: ", b.h)
print(b)
b.queens = shc(b) # aplicação do hill climbing
b.resetBoard()
print("ALTERADO: ", b.h)
print(b)