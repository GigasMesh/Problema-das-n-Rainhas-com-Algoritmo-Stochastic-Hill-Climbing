from Board import Board

def SHillClimbing(bd):

    if bd.h == 0:
        return bd.queens
    
    eachH = bd.eachH
    queens = bd.queens
    
    maxH = max(eachH.values())
    
    queen = list(eachH.values()).index(maxH) # rainha com maior custo
    
    row = bd.queens[queen][0]
    col = bd.queens[queen][1]
    
    for candidate in range(bd.n):

        if candidate == row: # pula o lugar onde a rainha já está
            continue

        queens[queen] = tuple([candidate,queen]) # realiza a mudança de posição da rainha
        candidateH = Board(queens).eachH[queen+1] # novo custo com a mudança de posição

        '''
        Possíveis mudanças na implementação:
          Ao encontrar a primeira célula com custo menor já faz a troca,
          mas é possível analisar todas as posisões e escolher a menor
        '''
        if maxH > candidateH:
            return queens