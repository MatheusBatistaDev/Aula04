# para armazenar infomações de um livro,
#incluindo título, autor, ano de publicação.imprima cada informação.

from typing import Dict, Any

livro: dict[str, any] = {
    "título": "Game of Thrones",
    "autor": "George R. R. Martin",
    "ano_publicacao": 1996,

}


livro_02: dict[str, any] = {
    "título": "Harry Potter e a Pedra Filosofal",
    "autor": "J.K. Rowling",
    "ano_publicacao": 1997,
}

lista_de_livros = []

lista_de_livros.append(livro)
lista_de_livros.append(livro_02)

# print("Lista_de_livros:")

lista_de_livros_usando_dict:dict = {
        "livro": {"título": "Game of Thrones",
    "autor": "George R. R. Martin",
    "ano_publicacao": 1996},

    "livro_02": {"título": "Harry Potter e a Pedra Filosofal",
    "autor": "J.K. Rowling",
    "ano_publicacao": 1997},

}

print(lista_de_livros_usando_dict["livro_02"]["título"])

