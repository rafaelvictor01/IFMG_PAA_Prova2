import time


def insertion_sort(vetor):
    comparacoes = 0
    movimentacoes = 0
    inicio = time.time()

    ''' Complexidade: n '''
    for index in range(1, len(vetor)):

        ''' Complexidade: n-1 '''
        valor = vetor[index]

        ''' Complexidade: n '''
        i = index - 1

        ''' Complexidade: desprezível (utilizado apenas para esta atividade) '''
        comparacoes += 1
        movimentacoes += 1

        ''' Complexidade: somatório de 1 a n '''
        while i >= 0 and vetor[i] > valor:

            ''' Complexidade: desprezível (utilizado apenas para esta atividade) '''
            movimentacoes += 1

            ''' Complexidade: somatório de 1 a n-1 '''
            vetor[i+1] = vetor[i]

            ''' Complexidade: somatório de 1 a n-1 '''
            i = i - 1

        ''' Complexidade: n-1 '''
        vetor[i+1] = valor

        ''' Complexidade: desprezível (utilizado apenas para esta atividade) '''
        movimentacoes += 1

    tempo_segundos = time.time() - inicio
    return comparacoes, movimentacoes, tempo_segundos


def selection_sort(vetor):
    comparacoes = 0
    movimentacoes = 0
    inicio = time.time()

    ''' Complexidade: n '''
    for i in range(0, len(vetor)-1):

        ''' Complexidade: n '''
        menor_index = i

        ''' Complexidade: n^2 '''
        for j in range(i, len(vetor)-1):

            ''' Complexidade: desprezível (utilizado apenas para esta atividade) '''
            comparacoes += 1

            ''' Complexidade: n^2 '''
            if vetor[menor_index] > vetor[j]:

                ''' Complexidade: n^2 '''
                menor_index = j

        ''' Complexidade: n '''
        aux = vetor[i]
        vetor[i] = vetor[menor_index]
        vetor[menor_index] = aux
        movimentacoes += 3

    tempo_segundos = time.time() - inicio
    return comparacoes, movimentacoes, tempo_segundos


def merge_sort(vetor):
    comparacoes = 0
    movimentacoes = 0
    tempo_segundos = 0
    inicio = time.time()

    ''' Complexidade: 1 '''
    if len(vetor) > 1:

        ''' Complexidade: 1 '''
        meio = len(vetor)//2

        ''' Complexidade: 1 '''
        metade_esquerda = vetor[:meio]

        ''' Complexidade: 1 '''
        metade_direita = vetor[meio:]

        ''' Complexidade para a chamada recursiva do merge_sort: T([n/2])'''
        c, m, t = merge_sort(metade_esquerda)

        ''' Complexidade: desprezível (utilizado apenas para esta atividade) '''
        comparacoes += c
        movimentacoes += m
        tempo_segundos += t

        ''' Complexidade para a chamada recursiva do merge_sort: T([n/2])'''
        c, m, t = merge_sort(metade_direita)

        ''' Complexidade: desprezível (utilizado apenas para esta atividade) '''
        comparacoes += c
        movimentacoes += m
        tempo_segundos += t

        ''' Complexidade atribuição das variaveis: 1 '''
        i = 0
        j = 0
        k = 0

        ''' Complexidade do trecho abaixo (referente a intercalação): 6n+5 '''
        while i < len(metade_esquerda) and j < len(metade_direita):
            comparacoes += 1
            if metade_esquerda[i] < metade_direita[j]:
                vetor[k] = metade_esquerda[i]
                i = i+1
            else:
                vetor[k] = metade_direita[j]
                j = j+1
            k = k+1

        while i < len(metade_esquerda):
            comparacoes += 1
            vetor[k] = metade_esquerda[i]
            i = i+1
            k = k+1

        while j < len(metade_direita):
            comparacoes += 1
            vetor[k] = metade_direita[j]
            j = j+1
            k = k+1

    tempo_segundos = time.time() - inicio
    return comparacoes, movimentacoes, tempo_segundos
