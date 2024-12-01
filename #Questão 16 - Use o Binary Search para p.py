#Questão 16 - Use o Binary Search para procurar um livro específico por ISBN em uma lista ordenada de registros de biblioteca.

# --- Algoritmo de Busca Binária para Livro por ISBN ---

def binary_search_by_isbn(library, target_isbn):
    low, high = 0, len(library) - 1
    while low <= high:
        mid = (low + high) // 2
        if library[mid]['ISBN'] == target_isbn:
            return mid  # Retorna o índice do livro encontrado
        elif library[mid]['ISBN'] < target_isbn:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Retorna -1 se o livro não for encontrado

# --- Função Principal para Testar a Busca Binária ---

def test():
    # Lista de livros ordenada por ISBN
    library = [
        {'title': 'O Senhor dos Anéis', 'author': 'J.R.R. Tolkien', 'ISBN': '978-0-261-10221-1'},
        {'title': '1984', 'author': 'George Orwell', 'ISBN': '978-0-452-28423-4'},
        {'title': 'Dom Casmurro', 'author': 'Machado de Assis', 'ISBN': '978-85-359-0277-2'},
        {'title': 'Harry Potter e a Pedra Filosofal', 'author': 'J.K. Rowling', 'ISBN': '978-0-545-01022-1'},
        {'title': 'O Pequeno Príncipe', 'author': 'Antoine de Saint-Exupéry', 'ISBN': '978-85-325-3133-3'}
    ]
    
    # ISBN a ser procurado
    target_isbn = '978-0-452-28423-4'
    
    # Realiza a busca binária
    index = binary_search_by_isbn(library, target_isbn)
    
    # Exibe o resultado
    if index != -1:
        book = library[index]
        print(f'Livro encontrado: {book["title"]} por {book["author"]} (ISBN: {book["ISBN"]})')
    else:
        print(f'O livro com ISBN {target_isbn} não foi encontrado.')

if __name__ == "__main__":
    test()
