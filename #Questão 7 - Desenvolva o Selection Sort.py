#Questão 7 - Desenvolva o Selection Sort

import time

def selection_sort_verbose(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Troca
        print(f"Iteração {i+1}: {arr}")  # Exibe a lista após cada troca

def analyze_performance():
    import random
    
    sizes = [10, 100, 1000]  # Tamanhos de listas
    for size in sizes:
        test_list = random.sample(range(1, 10000), size)  # Gera listas aleatórias
        print(f"\nOrdenando lista de tamanho {size}...")
        start_time = time.time()
        selection_sort_verbose(test_list[:])  # Ordena e acompanha
        end_time = time.time()
        print(f"Tempo para ordenar lista de {size} elementos: {end_time - start_time:.4f} segundos\n")

if __name__ == "__main__":
    # Lista de exemplo
    example_list = [64, 25, 12, 22, 11]
    print("Lista inicial:", example_list)
    print("\n### Processamento passo a passo ###")
    selection_sort_verbose(example_list)
    
    print("\n### Análise de Desempenho ###")
    analyze_performance()
