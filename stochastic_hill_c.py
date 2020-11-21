from chess_board import ChessBoard
import numpy as np
from numpy import random as npr

def stochastic_hill_climbing(bd):

    if bd.h == 0:
        return bd.queens
    
    indv_fitness = bd.indv_fitness
    queens = bd.queens
    
    queen = queens[npr.choice(range(0, bd.n))][1] # pega a coluna da rainha(uma tupla, com a localização) escolhida aleatoriamente
    max_fitness = indv_fitness[queen+1] # +1 pois o dict inicia em n=1
    q_row = bd.queens[queen][0]
    q_col = bd.queens[queen][1]
    
    # max_fitness = max(indv_fitness.values())
    # queen = list(indv_fitness.values()).index(max_fitness) # seleciona a rainha com maior custo
    # q_row = bd.queens[queen][0]
    # q_col = bd.queens[queen][1]
    
    candidates = {} # {(candidate, queen): fitness}
    
    for candidate in range(bd.n):

        if candidate == q_row: # pula a posição onde a rainha já está
            continue

        queens[queen] = (candidate, queen) # realiza a mudança de posição da rainha
        candidate_fitness = ChessBoard(queens).indv_fitness[queen+1] # novo custo com a mudança de posição

        if max_fitness > candidate_fitness:
            candidates[(candidate, queen)] = candidate_fitness
            
    indv_candidate_fitness = [fitness+1 for fitness in candidates.values()] # pega o fitness de cada candidato, é adicionado 1 para evitar a divisão por 0

    sorted_candidates = {k: v for k, v in sorted(candidates.items(), key=lambda item: item[1])} # ordena o dict pelos valores, nesse caso o fitness

    sum_candidates_fitness = sum(indv_candidate_fitness) # soma todos os valores, que será usado no cálculo da probabilidade
    
    probability_weights = [fitness/sum_candidates_fitness for fitness in indv_candidate_fitness] # faz o cálculo da probabilidade
    sorted_probability_weights = sorted(probability_weights, reverse=True) # ordenado e na ordem reversa, já que o pior fitness (maior número) deve receber a menor probabilidade

    if not sorted_candidates: # nenhum candidato tem um fitness melhor
        return stochastic_hill_climbing(ChessBoard(queens))
    else:
        choice_i_candidate = npr.choice(len(sorted_candidates), p=sorted_probability_weights) # escolhe um índice referente ao candidato
        chosen_candidate = list(sorted_candidates.keys())[choice_i_candidate] # retira-se o candidato do dicionário
        
        queens[queen] = chosen_candidate # atribui o candidato na lista de rainhas
        
        return stochastic_hill_climbing(ChessBoard(queens)) # recursão
