import numpy as np

class ChessBoard(object):
    
    def __init__(self, queens=None, n=8):
        self.queens = queens
        self.n = n
        self.positions = np.zeros((n, n))
        self.fitness = 0

        if not self.queens:
            self.create_queens()

        self.set_queens()

        # cria um dicionário para armazenar o custo individual por rainha
        self.indv_fitness = {queen: 0 for queen in range(1, n+1)}
        self.set_fitness()
    
    def update_board(self):
        self.reset_positions()
        self.set_queens()
        self.set_fitness()
        
    # realiza a criação aleatória das rainhas pelo tabuleiro
    def create_queens(self):
        n= self.n
        self.queens = list(zip(np.random.randint(0,n,n), range(n)))
    
    '''
    TO-DO
      settar e remover apenas uma rainha e não todo o tabuleiro
    '''
    
    # insere as rainhas no tabuleiro
    def set_queens(self):
        for queen,col in self.queens:
            self.positions[queen][col] = col+1

    # reinicia o tabuleiro
    def reset_positions(self):
        n = self.n
        self.positions = np.zeros((n, n))
    
    # realiza o cálculo da função de custo, o fitness
    def set_fitness(self):

        self.fitness = 0

        for queen in self.queens:
            row, col = queen
                    
            # verificar a linha inteira, só pelo lado esquerdo
            for j in range(col, -1, -1):
                if self.positions[row][j]  and j != col:
                    self.fitness += 1 # soma no custo total

                    # soma nos custos individuais
                    self.indv_fitness[col+1] += 1 # col+1 pois no dict inv_fitness as rainhas começam em n=1
                    self.indv_fitness[j+1] += 1
            
            # não precisa verificar a coluna pois como premissa tem-se que cada rainha ocupa uma coluna diferente

            # verificar a diagonal superior esquerda
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                #print("Diag acima ",queen," - ", i,j)
                if self.positions[i][j] and row != i and col != j: 
                    self.fitness += 1 # soma no custo total

                    # soma nos custos individuais
                    self.indv_fitness[col+1] += 1
                    self.indv_fitness[j+1] += 1
            
            # verificar a diagonal inferior esquerda
            for i, j in zip(range(row, self.n, 1), range(col, -1, -1)): 
                if self.positions[i][j] and row != i and col != j: 
                    self.fitness +=1 # soma no custo total

                    # soma nos custos individuais
                    self.indv_fitness[col+1] += 1
                    self.indv_fitness[j+1] += 1

    def __repr__(self):
        return str(np.matrix(self.positions))
