#Questão 20 - - Crie um programa que permita ao usuário escolher um algoritmo de busca e ordenação para ordenar uma lista ou procurar um elemento, oferecendo comparações automáticas entre os métodos.2

import time
import random
import math

# --- Algoritmos de Ordenação ---

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# --- Algoritmos de Busca ---

# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Interpolation Search
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# --- Função para medir o tempo de execução de cada algoritmo ---

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

# --- Função para exibir o menu e realizar a operação escolhida ---

def user_menu():
    print("\n### Menu de Algoritmos de Busca e Ordenação ###")
    print("1. Ordenar Lista")
    print("2. Procurar Elemento")
    choice = input("Escolha uma opção (1 ou 2): ")

    # Gerar lista de números aleatórios
    arr = random.sample(range(1, 100), 10)
    print(f"\nLista original: {arr}")

    if choice == '1':  # Ordenação
        print("\nEscolha um algoritmo de ordenação:")
        print("1. Merge Sort")
        print("2. Quick Sort")
        print("3. Bubble Sort")
        algo_choice = input("Escolha um algoritmo de ordenação (1, 2, 3): ")

        if algo_choice == '1':
            sorted_list, time_taken = measure_time(merge_sort, arr.copy())
            print(f"Lista ordenada com Merge Sort: {sorted_list}")
        elif algo_choice == '2':
            sorted_list, time_taken = measure_time(quick_sort, arr.copy())
            print(f"Lista ordenada com Quick Sort: {sorted_list}")
        elif algo_choice == '3':
            sorted_list, time_taken = measure_time(bubble_sort, arr.copy())
            print(f"Lista ordenada com Bubble Sort: {sorted_list}")
        print(f"Tempo de execução: {time_taken:.6f} segundos")

    elif choice == '2':  # Busca
        print("\nEscolha um algoritmo de busca:")
        print("1. Binary Search")
        print("2. Interpolation Search")
        algo_choice = input("Escolha um algoritmo de busca (1, 2): ")

        target = int(input("\nDigite o elemento que deseja procurar: "))

        if algo_choice == '1':
            sorted_arr = sorted(arr)
            print(f"Lista ordenada para busca binária: {sorted_arr}")
            result, time_taken = measure_time(binary_search, sorted_arr, target)
        elif algo_choice == '2':
            sorted_arr = sorted(arr)
            print(f"Lista ordenada para busca por interpolação: {sorted_arr}")
            result, time_taken = measure_time(interpolation_search, sorted_arr, target)

        if result != -1:
            print(f"Elemento {target} encontrado na posição {result}")
        else:
            print(f"Elemento {target} não encontrado")
        print(f"Tempo de execução: {time_taken:.6f} segundos")

# --- Executando o programa ---

if __name__ == "__main__":
    user_menu()
