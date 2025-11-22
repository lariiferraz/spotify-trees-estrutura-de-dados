import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# test_rbt_manual.py
from trees import RedBlack

# Criar a árvore Red-Black
arvore = RedBlack()

print("\nTESTE ÁRVORE REDBLACK")

# Inserir alguns nós manualmente (chave = popularidade)
arvore.inserir(50, {'track_name': 'Song A', 'artist_name': 'Artist 1', 'genre': 'Pop'})
arvore.inserir(70, {'track_name': 'Song B', 'artist_name': 'Artist 2', 'genre': 'Rock'})
arvore.inserir(30, {'track_name': 'Song C', 'artist_name': 'Artist 3', 'genre': 'Jazz'})
arvore.inserir(60, {'track_name': 'Song D', 'artist_name': 'Artist 4', 'genre': 'Pop'})
arvore.inserir(80, {'track_name': 'Song E', 'artist_name': 'Artist 5', 'genre': 'Hip-Hop'})

# Buscar um nó
resultado = arvore.buscar(70)
print("\nBusca por popularidade 70:", resultado)

# Altura da árvore
print("Altura da árvore:", arvore.altura())

# Comparações realizadas
print("Comparações realizadas:", arvore.contador_comparacoes(), "\n")
