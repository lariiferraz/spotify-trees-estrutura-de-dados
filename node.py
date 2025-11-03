# node.py

class Node:
    """
    Classe que representa um nó da árvore.
    Cada nó possui:
    - chave: valor para ordenar (popularity)
    - dados: dicionário com track_name, artist_name, genre
    - esquerdo: referência para filho esquerdo
    - direito: referência para filho direito
    - cor: opcional, usado em árvores Red-Black ('red' ou 'black')
    """
    def __init__(self, chave, dados, cor='black'):
        self.chave = chave          # Popularidade
        self.dados = dados          # Ex: {'track_name': ..., 'artist_name': ..., 'genre': ...}
        self.esquerdo = None        # Filho esquerdo
        self.direito = None         # Filho direito
        self.cor = cor              # Para Red-Black
