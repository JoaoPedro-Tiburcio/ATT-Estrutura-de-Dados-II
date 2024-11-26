#Questão 1 - Implemente o algoritmo Binary Search em uma lista ordenada e encontre o índice de um elemento dado.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # Verifica se x está presente no meio
        if arr[mid] == x:
            return mid
        # Se x for maior, ignore a metade esquerda
        elif arr[mid] < x:
            low = mid + 1
        # Se x for menor, ignore a metade direita
        else:
            high = mid - 1
    # Se chegarmos até aqui, o elemento não está presente
    return -1

# Lista ordenada de exemplo
arr = [3, 14, 25, 36, 47, 58, 69, 70, 81, 92]
x = 47

# Chamando a função de busca binária
result = binary_search(arr, x)

if result != -1:
    print(f"Elemento encontrado no índice: {result}")
else:
    print("Elemento não encontrado na lista.")


