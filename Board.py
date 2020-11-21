import numpy as np

class Board(object):
    
    def __init__(self, queens=None, n=4):
      
        self.n = n
        self.pos = np.zeros((n,n))
        self.queens = queens
        self.h = 0

        if not self.queens: self.createQueens()
        self.setQueens()

        # cria um dicionário para armazenar o custo individual por rainha
        self.eachH = {queen+1:0 for queen in range(n)}
        self.setH()
    
    def resetBoard(self):
        self.resetPos()
        self.setQueens()
        self.setH()
        
    # realiza a criação aleatória das rainhas pelo tabuleiro
    def createQueens(self):
        n= self.n
        self.queens = list(zip(np.random.randint(0,n,n), range(n)))
    
    '''
    TO-DO
      settar e remover apenas uma rainha e não todo o tabuleiro
    '''
    # insere as rainhas no tabuleiro
    def setQueens(self):
        for queen,col in self.queens:
            self.pos[queen][col] = col+1

    # reinicia o tabuleiro
    def resetPos(self):
        n = self.n
        self.pos = np.zeros((n, n))
    
    # realiza o cálculo da função de custo H
    def setH(self):
        self.h = 0
        for queen in self.queens:
            row,col = queen
                    
            # verificar a linha inteira
            for j in range(col, -1, -1):
                if self.pos[row][j]  and j != col:
                    self.h += 1 # soma no custo total

                    # soma nos custos individuais
                    self.eachH[col+1] += 1 
                    self.eachH[j+1] += 1
            '''
            # verificar a coluna inteira
            for i in range(row, self.n, 1):
                if self.pos[i][col] ==1 and i != row:
                    self.h += 1
            '''
            # verificar a diagonal superior esquerda
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                #print("Diag acima ",queen," - ", i,j)
                if self.pos[i][j] and row != i and col != j: 
                    self.h +=1 # soma no custo total

                    # soma nos custos individuais
                    self.eachH[col+1] += 1
                    self.eachH[j+1] += 1
            
            # verificar a diagonal inferior esquerda
            for i, j in zip(range(row, self.n, 1), range(col, -1, -1)): 
                if self.pos[i][j] and row != i and col != j: 
                    self.h +=1 # soma no custo total

                    # soma nos custos individuais
                    self.eachH[col+1] += 1
                    self.eachH[j+1] += 1

    def __repr__(self):
        return str(np.matrix(self.pos))
