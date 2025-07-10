import json


lista = ["sapato", 39 , 10.38, True]

Produto_01: dict = {
    "nome": "sapato",
    "tamanho": 39,
    "preco": 10.38,
    "disponibilidade": True
}

produto_02: dict = {
    "nome": "Televisao",
    "tamanho": 40,
    "preco": 20.50,
    "disponibilidade": False
}

carrinho = []

carrinho.append(Produto_01)
carrinho.append(produto_02) 

carrinho_json = json.dumps(carrinho)
print(carrinho_json)


