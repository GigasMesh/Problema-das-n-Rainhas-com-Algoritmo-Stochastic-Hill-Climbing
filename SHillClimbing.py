from Board import Board
import numpy as np

def SHillClimbing(bd):

    if bd.h == 0:
        return bd.queens
    
    eachH = bd.eachH
    queens = bd.queens
    
    queen = queens[np.random.choice(np.arange(0,bd.n))][1]
    maxH = eachH[queen+1]
    row = bd.queens[queen][0]
    col = bd.queens[queen][1]
    
    #maxH = max(eachH.values())
    #queen = list(eachH.values()).index(maxH) # seleciona a rainha com maior custo
    #row = bd.queens[queen][0]
    #col = bd.queens[queen][1]
    
    candidates = {}
    
    for candidate in range(bd.n):

        if candidate == row: # pula a célula onde a rainha já está
            continue

        queens[queen] = tuple([candidate,queen]) # realiza a mudança de posição da rainha
        candidateH = Board(queens).eachH[queen+1] # novo custo com a mudança de posição

        if maxH > candidateH:
            candidates[tuple([candidate,queen])] = candidateH
            
    eachCandidateH = [h+1 for h in list(candidates.values())] # pega o H de cada candidato, é adicionado 1 para evitar a divisão por 0
    sumCandidatesH = sum(eachCandidateH) # soma todos os valores, que será usado no cálculo da probabilidade
    
    probability = [h/sumCandidatesH for h in eachCandidateH] # faz o cálculo da probabilidade
    
    if not candidates:
        return SHillClimbing(Board(queens))
    else:
        choiceCandidate = np.random.choice(np.arange(0,len(candidates)), 1, p=probability[::-1]) # escolhe um índice referente ao candidato
        choicedCandidate = list(candidates.keys())[choiceCandidate[0]] # retira-se o candidato do dicionário
        
        queens[queen] = choicedCandidate # atribui o candidato na lista de rainhas
        
        return SHillClimbing(Board(queens))