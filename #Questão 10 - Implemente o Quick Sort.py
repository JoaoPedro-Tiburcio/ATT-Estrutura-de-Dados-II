#Questão 10 - Implemente o Quick Sort

import time
import random

def quick_sort(arr, pivot_strategy='first'):
    """Quick Sort com diferentes estratégias de pivô."""
    if len(arr) <= 1:
        return arr

    if pivot_strategy == 'first':
        pivot = arr[0]
    elif pivot_strategy == 'last':
        pivot = arr[-1]
    elif pivot_strategy == 'middle':
        pivot = arr[len(arr) // 2]
    else:
        raise ValueError("Estratégia de pivô inválida. Escolha 'first', 'last' ou 'middle'.")

    # Separação dos elementos com base no pivô
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    return quick_sort(less, pivot_strategy) + equal + quick_sort(greater, pivot_strategy)

def analyze_performance():
    """Analisa o desempenho do Quick Sort em diferentes condições."""
    list_sizes = [100, 200, 300]  # Tamanhos ajustados
    
    for size in list_sizes:
        print(f"\nTamanho da lista: {size}")
        
        # Lista completamente desordenada
        unordered_list = random.sample(range(size * 10), size)
        # Lista quase ordenada
        nearly_sorted_list = sorted(unordered_list)[:size - 1] + [unordered_list[-1]]
        
        for strategy in ['first', 'last', 'middle']:
            print(f"\nEstratégia de pivô: {strategy.upper()}")

            # Lista desordenada
            start = time.time()
            quick_sort(unordered_list[:], strategy)
            duration = time.time() - start
            print(f"Lista desordenada: {duration:.5f} segundos")

            # Lista quase ordenada
            start = time.time()
            quick_sort(nearly_sorted_list[:], strategy)
            duration = time.time() - start
            print(f"Lista quase ordenada: {duration:.5f} segundos")

if __name__ == "__main__":
    # Teste simples
    test_list = [3, 6, 8, 10, 1, 2, 1]
    print("Lista Original:", test_list)
    
    # Teste com diferentes pivôs
    print("\nOrdenação com pivô 'first':", quick_sort(test_list, 'first'))
    print("Ordenação com pivô 'last':", quick_sort(test_list, 'last'))
    print("Ordenação com pivô 'middle':", quick_sort(test_list, 'middle'))

    # Análise de desempenho
    print("\n### Análise de Desempenho ###")
    analyze_performance()
