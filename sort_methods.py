from generate_array import *
from sort_algorithms import *
from auxiliary_methods import *

n = 10000

print(f'\n========= N = {n} ========\n')

print('\n\nVETOR ORDENADO - SELECTION:')
comparacoes, movimentacoes, tempo_segundos = selection_sort(vetor_ordenado(n))
print_results(comparacoes, movimentacoes, tempo_segundos)

print('\nVETOR DESORDENADO - SELECTION: ')
comparacoes, movimentacoes, tempo_segundos = selection_sort(vetor_desordenado(n))
print_results(comparacoes, movimentacoes, tempo_segundos)

print('\nVETOR ALEATORIO - SELECTION: ')
comparacoes, movimentacoes, tempo_segundos = selection_sort(vetor_aleatorio(n))
print_results(comparacoes, movimentacoes, tempo_segundos)

print('\n\nVETOR ORDENADO - INSERTION: ')
comparacoes, movimentacoes, tempo_segundos = insertion_sort(vetor_ordenado(n))
print_results(comparacoes, movimentacoes, tempo_segundos)

print('\nVETOR DESORDENADO - INSERTION: ')
comparacoes, movimentacoes, tempo_segundos = insertion_sort(vetor_desordenado(n))
print_results(comparacoes, movimentacoes, tempo_segundos)

print('\nVETOR ALEATORIO - INSERTION: ')
comparacoes, movimentacoes, tempo_segundos = insertion_sort(vetor_aleatorio(n))
print_results(comparacoes, movimentacoes, tempo_segundos)

print('\n\n VETOR ORDENADO - MERGE: ')
comparacoes, movimentacoes, tempo_segundos = merge_sort(vetor_ordenado(n))
print_results(comparacoes, movimentacoes, tempo_segundos)

print('\nVETOR DESORDENADO - MERGE: ')
comparacoes, movimentacoes, tempo_segundos = merge_sort(vetor_desordenado(n))
print_results(comparacoes, movimentacoes, tempo_segundos)

print('\nVETOR ALEATORIO - MERGE: ')
comparacoes, movimentacoes, tempo_segundos = merge_sort(vetor_aleatorio(n))
print_results(comparacoes, movimentacoes, tempo_segundos)
