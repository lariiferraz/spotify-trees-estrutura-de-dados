# main.py
import time
from trees import BST, AVL
from loader import load_spotify_dataset

def submenu_arvore(arvore, nome):
    """
    Submenu padrão para interagir com uma árvore (BST ou AVL)
    """
    while True:
        print(f"\n--- Submenu {nome} ---")
        print("1 - Buscar música por popularidade")
        print("2 - Remover música por popularidade")
        print("3 - Mostrar altura e comparações")
        print("4 - Voltar ao menu principal")
        opcao = input("\nEscolha uma opção: \n")
        
        if opcao == '1':
            pop = int(input("Digite a popularidade da música: "))
            start_time = time.time()
            resultados = arvore.buscar(pop)
            end_time = time.time()
            print(f"\nTempo de busca: {end_time - start_time:.6f} segundos")
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
            resultados = arvore.buscar(pop)
            if resultados:
                print(f"{len(resultados)} música(s) encontrada(s) com popularidade {pop}.")
                qtd = int(input(f"Quantas você quer remover? (máx {len(resultados)}): "))
                qtd = min(qtd, len(resultados))
                start_time = time.time()
                arvore.remover_n(pop, qtd)
                end_time = time.time()
                print(f"{qtd} música(s) com popularidade {pop} removida(s).")
                print(f"\nTempo de remoção: {end_time - start_time:.6f} segundos")
            else:
                print("Nenhuma música encontrada para remover.")

        elif opcao == '3':
            print(f"\nAltura da {nome}: {arvore.altura()}")
            print(f"Comparações realizadas: {arvore.contador_comparacoes()}")
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def comparar_arvores(dataset):
    """
    Executa um teste de comparação entre BST e AVL para tamanhos progressivos.
    """
    tamanhos = [100, 500, 2000, 10000, 50000, 100000, len(dataset)]
    
    for n in tamanhos:
        print(f"\n--- Teste com {n} músicas ---")
        dataset_teste = dataset[:n]
        arvores = [("BST", BST()), ("AVL", AVL())]
        resultados = []

        for nome, arvore in arvores:
            start_insercao = time.time()
            for linha in dataset_teste:
                chave = linha['popularity']
                dados = {
                    'track_name': linha['track_name'],
                    'artist_name': linha['artist_name'],
                    'genre': linha['genre']
                }
                arvore.inserir(chave, dados)
            end_insercao = time.time()

            start_busca = time.time()
            for linha in dataset_teste[:10]:  # busca 10 elementos aleatórios
                arvore.buscar(linha['popularity'])
            end_busca = time.time()

            start_remocao = time.time()
            for linha in dataset_teste[:10]:  # remove 10 elementos aleatórios
                arvore.remover_n(linha['popularity'], 1)
            end_remocao = time.time()

            resultados.append({
                "Árvore": nome,
                "Altura": arvore.altura(),
                "Comparações": arvore.contador_comparacoes(),
                "Tempo inserção": end_insercao - start_insercao,
                "Tempo busca": end_busca - start_busca,
                "Tempo remoção": end_remocao - start_remocao
            })

        for r in resultados:
            print(f"{r['Árvore']}: Altura = {r['Altura']}, Comparações = {r['Comparações']}, "
                  f"Tempo Inserção = {r['Tempo inserção']:.4f}s, Tempo Busca = {r['Tempo busca']:.6f}s, "
                  f"Tempo Remoção = {r['Tempo remoção']:.6f}s")

def main():
    dataset = load_spotify_dataset('dataset.csv')
    print(f"Total de músicas carregadas: {len(dataset)}")
    print("Exemplo das 5 primeiras músicas:")
    for linha in dataset[:5]:
        print(linha)

    while True:
        print("\n--- Menu Principal ---")
        print("1 - Usar árvore AVL")
        print("2 - Usar árvore BST")
        # print("3 - Usar árvore Red-Black")  # ainda não implementada
        print("4 - Comparação de desempenho entre árvores")
        print("5 - Sair")
        opcao = input("\nEscolha uma opção: \n")

        if opcao == '1':
            arvore = AVL()
            print("Árvore AVL criada!")
            start_time = time.time()
            for linha in dataset:
                chave = linha['popularity']
                dados = {
                    'track_name': linha['track_name'],
                    'artist_name': linha['artist_name'],
                    'genre': linha['genre']
                }
                arvore.inserir(chave, dados)
            end_time = time.time()
            print(f"Tempo de inserção na AVL: {end_time - start_time:.4f} segundos")
            submenu_arvore(arvore, "AVL")

        elif opcao == '2':
            arvore = BST()
            print("Árvore BST criada!")
            start_time = time.time()
            for linha in dataset:
                chave = linha['popularity']
                dados = {
                    'track_name': linha['track_name'],
                    'artist_name': linha['artist_name'],
                    'genre': linha['genre']
                }
                arvore.inserir(chave, dados)
            end_time = time.time()
            print(f"Tempo de inserção na BST: {end_time - start_time:.4f} segundos")
            submenu_arvore(arvore, "BST")

        elif opcao == '4':
            comparar_arvores(dataset)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
