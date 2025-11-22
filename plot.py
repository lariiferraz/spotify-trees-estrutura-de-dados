# Execute depois de ter carregado dataset (por exemplo em main.py ou em um script separado)
from trees import BST, AVL, RedBlack
from loader import load_spotify_dataset

dataset = load_spotify_dataset('dataset.csv')
tamanhos = [100, 500, 2000, 10000, 50000, 100000, len(dataset)]

print("Tamanho | Altura BST | Altura AVL | Altura RB | Comparações BST | Comparações AVL | Comparações RB")
for n in tamanhos:
    subset = dataset[:n]
    bst = BST(); avl = AVL(); rb = RedBlack()
    for linha in subset:
        chave = linha['popularity']
        dados = {'track_name': linha['track_name']}
        bst.inserir(chave, dados)
        avl.inserir(chave, dados)
        rb.inserir(chave, dados)
    print(f"{n:6} | {bst.altura():10} | {avl.altura():10} | {rb.altura():9} | {bst.contador_comparacoes():15} | {avl.contador_comparacoes():15} | {rb.contador_comparacoes():14}")
