#Questão 15 - Adapte os algoritmos de ordenação (Merge Sort e Quick Sort) para ordenar palavras em ordem alfabética.

import time

# --- Algoritmos de Ordenação para Palavras ---

# Merge Sort adaptado para palavras
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i].lower() < right[j].lower():  # Comparação lexicográfica
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Quick Sort adaptado para palavras
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high].lower()  # Pivô é a palavra no final
    i = low - 1
    for j in range(low, high):
        if arr[j].lower() < pivot:  # Comparação lexicográfica
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# --- Algoritmo de Busca Binária para Palavras ---

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].lower() == target.lower():  # Comparação lexicográfica
            return mid
        elif arr[mid].lower() < target.lower():
            low = mid + 1
        else:
            high = mid - 1
    return -1

# --- Função Principal para Testes ---

def test():
    words = ["banana", "apple", "grape", "cherry", "kiwi", "lemon", "orange"]
    
    # Ordenando com Merge Sort
    merge_sort(words)
    print("Palavras ordenadas com Merge Sort:", words)
    
    # Ordenando com Quick Sort
    quick_sort(words, 0, len(words) - 1)
    print("Palavras ordenadas com Quick Sort:", words)
    
    # Testando Busca Binária
    word_to_search = "cherry"
    index = binary_search(words, word_to_search)
    if index != -1:
        print(f"A palavra '{word_to_search}' foi encontrada na posição {index}.")
    else:
        print(f"A palavra '{word_to_search}' não foi encontrada.")

if __name__ == "__main__":
    test()
