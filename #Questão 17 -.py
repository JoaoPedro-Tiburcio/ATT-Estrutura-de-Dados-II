#Questão 17 -  - Implemente Bucket Sort para ordenar as notas de uma turma de alunos, classificadas entre 0 e 100. Em seguida, utilize o Interpolation Search para encontrar um aluno com uma nota específica.

import random

# --- Algoritmo de Bucket Sort ---

def bucket_sort(arr):
    # Cria os baldes (buckets)
    n = len(arr)
    if n <= 1:
        return arr
    
    # Cria n baldes vazios
    buckets = [[] for _ in range(n)]
    
    # Coloca os elementos nos baldes
    for num in arr:
        index = int(num * n / 101)  # Mapeia a nota para um balde
        buckets[index].append(num)
    
    # Ordena cada balde usando insertion sort
    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])
    
    # Junta todos os baldes em uma lista ordenada
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# --- Algoritmo de Insertion Sort (para ordenar dentro dos baldes) ---

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --- Algoritmo de Interpolation Search ---

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        # Calcula a posição do valor usando interpolação
        if arr[high] == arr[low]:  # Evita divisão por zero
            if arr[low] == target:
                return low
            return -1
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# --- Função Principal para Testar ---

def test():
    # Lista de alunos com notas aleatórias entre 0 e 100
    students = [
        {'name': 'Aluno A', 'grade': random.randint(0, 100)},
        {'name': 'Aluno B', 'grade': random.randint(0, 100)},
        {'name': 'Aluno C', 'grade': random.randint(0, 100)},
        {'name': 'Aluno D', 'grade': random.randint(0, 100)},
        {'name': 'Aluno E', 'grade': random.randint(0, 100)},
        {'name': 'Aluno F', 'grade': random.randint(0, 100)},
        {'name': 'Aluno G', 'grade': random.randint(0, 100)},
        {'name': 'Aluno H', 'grade': random.randint(0, 100)},
        {'name': 'Aluno I', 'grade': random.randint(0, 100)},
        {'name': 'Aluno J', 'grade': random.randint(0, 100)},
    ]
    
    # Exibe as notas antes da ordenação
    print("Notas antes da ordenação:")
    for student in students:
        print(f"{student['name']}: {student['grade']}")
    
    # Ordenando as notas dos alunos usando Bucket Sort
    grades = [student['grade'] for student in students]
    sorted_grades = bucket_sort(grades)
    
    # Exibe as notas após a ordenação
    print("\nNotas após a ordenação (Bucket Sort):")
    for grade in sorted_grades:
        print(grade, end=' ')
    
    # Solicita uma nota para procurar usando Interpolation Search
    target_grade = int(input("\nDigite a nota a ser procurada (entre 0 e 100): "))
    
    # Busca pelo índice da nota utilizando Interpolation Search
    index = interpolation_search(sorted_grades, target_grade)
    
    if index != -1:
        # Encontramos a nota, agora procuramos o aluno correspondente
        for student in students:
            if student['grade'] == target_grade:
                print(f"\nO aluno com a nota {target_grade} é: {student['name']}")
                break
    else:
        print(f"\nA nota {target_grade} não foi encontrada.")

if __name__ == "__main__":
    test()
