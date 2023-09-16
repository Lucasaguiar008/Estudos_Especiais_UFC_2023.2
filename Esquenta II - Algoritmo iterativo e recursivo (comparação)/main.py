# Autor: Antônio Lucas Sousa Aguiar

import os
import time
import psutil
import numpy as np

from maxVal1 import maxVal1
from maxVal2 import maxVal2
from readInstances import readInstances

os.system('cls') #Limpando a tela"

dim = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000]
for i in range(len(dim)):        
    vetor=readInstances(f'N_Ordenados/{dim[i]}.txt')
    # vetor = [int(valor) for valor in vetor]
    print(f'Experimento instância: {dim[i]}')
            
    experimentos = 10
    res_tempo = [0]*experimentos
    res_memoria = [0]*experimentos
    for j in range(experimentos):        
        memoria_antes = psutil.virtual_memory()
        tempo_inicio = time.time()

        maxVal1(vetor,dim[i]) # Função sendo executada
        # maxVal2(vetor,0,int(dim[i])-1) # Função sendo executada

        tempo_fim = time.time()
        memoria_depois = psutil.virtual_memory()

        tempo_execucao = tempo_fim - tempo_inicio
        uso_memoria = abs(memoria_depois.used - memoria_antes.used)
        
        res_tempo.append(tempo_execucao)
        res_memoria.append(uso_memoria)

    print(f"Tempo médio (milisegundos): {np.mean(res_tempo)*1000}")
    print(f'Tempo max (milisegundos): {np.max(res_tempo)*1000}')
    print(f'Tempo min (milisegundos): {np.min(res_tempo)*1000}')
    print(f'Tempo desvPad (milisegundos): {np.std(res_tempo)*1000}')
    
    print(f"Memória médio (bits): {np.mean(res_memoria)*8}")
    print(f'Memória max (bits): {np.max(res_memoria)*8}')
    print(f'Memória min (bits): {np.min(res_memoria)*8}')
    print(f'Memória desvPad (bits): {np.std(res_memoria)*8}')
    print('\n')