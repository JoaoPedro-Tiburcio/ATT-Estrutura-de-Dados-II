#Questão 9 - Impemente o Radix Sort

def counting_sort(arr, exp, base=10):
    """Ordena a lista com base no dígito atual (exp) usando Counting Sort."""
    n = len(arr)
    output = [0] * n
    count = [0] * base
    
    # Contagem de ocorrências para o dígito atual
    for i in range(n):
        index = (arr[i] // exp) % base
        count[index] += 1
    
    # Acumulação das contagens
    for i in range(1, base):
        count[i] += count[i - 1]
    
    # Construção do array de saída
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copia o resultado para o array original
    for i in range(n):
        arr[i] = output[i]

def radix_sort_base10(arr):
    """Radix Sort usando base 10."""
    max_value = max(arr)
    exp = 1  # Dígito menos significativo
    while max_value // exp > 0:
        counting_sort(arr, exp, base=10)
        exp *= 10

def radix_sort_base2(arr):
    """Radix Sort usando base 2."""
    max_value = max(arr)
    exp = 1  # Começa no bit menos significativo
    while max_value // exp > 0:
        counting_sort(arr, exp, base=2)
        exp *= 2

# Testes
if __name__ == "__main__":
    # Lista de exemplo para base 10
    list_base10 = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original (Base 10):", list_base10)
    radix_sort_base10(list_base10)
    print("Lista ordenada (Base 10):", list_base10)
    
    # Lista de exemplo para base 2
    list_base2 = [170, 45, 75, 90, 802, 24, 2, 66]
    print("\nLista original (Base 2):", list_base2)
    radix_sort_base2(list_base2)
    print("Lista ordenada (Base 2):", list_base2)
    
    # Teste com números de diferentes tamanhos
    large_numbers = [12345, 6789, 2, 989898, 5678, 1234567890, 987, 65432]
    print("\nLista original (Grandes Números):", large_numbers)
    radix_sort_base10(large_numbers)
    print("Lista ordenada (Grandes Números):", large_numbers)
