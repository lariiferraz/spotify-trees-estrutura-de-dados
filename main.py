# main.py
from trees import BST
from loader import load_spotify_dataset

def main():
    # Criar árvore BST
    bst = BST()
    
    # Carregar dataset do Spotify (popularidade como chave)
    print("Carregando dataset e inserindo dados na BST...")
    dataset = load_spotify_dataset('dataset.csv')

    print(f"Total de músicas carregadas: {len(dataset)}")
    print("Exemplo das 5 primeiras músicas:")
    for linha in dataset[:5]:
        print(linha)

    # Inserir todos os dados na BST
    for linha in dataset:
        chave = linha['popularity']
        dados = {
            'track_name': linha['track_name'],
            'artist_name': linha['artist_name'],
            'genre': linha['genre']
        }
        bst.inserir(chave, dados)

    print("Inserção completa!")
    print(f"Altura da BST: {bst.altura()}")
    print(f"Comparações realizadas: {bst.contador_comparacoes()}")

    # Menu interativo
    while True:
        print("\nMenu:")
        print("1 - Buscar música por popularidade")
        print("2 - Remover música por popularidade")
        print("3 - Mostrar altura e comparações")
        print("4 - Sair")
        opcao = input("Escolha uma opção: \n")
        
        if opcao == '1':
            pop = int(input("Digite a popularidade da música: "))
            resultados = bst.buscar_todos(pop)  # precisa implementar buscar_todos na BST
            if resultados:
                print(f"{len(resultados)} música(s) encontrada(s) com popularidade {pop}.")
                qtd = int(input(f"Quantas você quer mostrar? (máx {len(resultados)}): "))
                qtd = min(qtd, len(resultados))
                for r in resultados[:qtd]:
                    print(r)
            else:
                print("Música não encontrada.")
        elif opcao == '2':
            pop = int(input("Digite a popularidade da música a remover: "))
            bst.remover(pop)  # ainda precisa implementar o método remover
            print(f"Música com popularidade {pop} removida (se existia).")
        elif opcao == '3':
            print(f"Altura da BST: {bst.altura()}")
            print(f"Comparações realizadas: {bst.contador_comparacoes()}")
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
