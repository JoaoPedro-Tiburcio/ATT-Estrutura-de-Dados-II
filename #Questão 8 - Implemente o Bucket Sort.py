#Questão 8 - Implemente o Bucket Sort

def insertion_sort(arr):
    """Ordena a lista usando Insertion Sort (usado nos baldes)."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort_floats(arr):
    """Bucket Sort para números em ponto flutuante no intervalo [0, 1)."""
    n = len(arr)
    buckets = [[] for _ in range(n)]  # Cria n baldes
    
    # Distribuição dos elementos nos baldes
    for num in arr:
        bucket_index = int(num * n)  # Calcula índice do balde
        buckets[bucket_index].append(num)

    # Ordena cada balde individualmente
    for bucket in buckets:
        insertion_sort(bucket)
    
    # Combina os baldes em uma única lista
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array

def bucket_sort_integers(arr):
    """Bucket Sort para números inteiros positivos."""
    if not arr:
        return arr
    
    max_value = max(arr)
    num_buckets = len(arr)  # Define o número de baldes proporcional ao tamanho da lista
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribuição dos elementos nos baldes
    for num in arr:
        bucket_index = num * num_buckets // (max_value + 1)  # Calcula índice do balde
        buckets[bucket_index].append(num)
    
    # Ordena cada balde individualmente
    for bucket in buckets:
        insertion_sort(bucket)
    
    # Combina os baldes em uma única lista
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array

# Testes
if __name__ == "__main__":
    # Teste com números em ponto flutuante [0, 1)
    float_list = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Lista original (floats):", float_list)
    print("Lista ordenada (floats):", bucket_sort_floats(float_list))
    
    # Teste com números inteiros positivos
    int_list = [78, 17, 39, 26, 72, 94, 21, 12, 23, 68]
    print("\nLista original (inteiros):", int_list)
    print("Lista ordenada (inteiros):", bucket_sort_integers(int_list))
