import time
import matplotlib.pyplot as plt
from trees import BST, AVL, RedBlack
from loader import load_spotify_dataset
import pandas as pd


def submenu_arvore(arvore, nome):
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
    tamanhos = [100, 500, 2000, 10000, 50000, 100000, len(dataset)]
    resultados_gerais = []

    for n in tamanhos:
        print(f"\n--- Teste com {n} músicas ---")
        dataset_teste = dataset[:n]
        arvores = [("BST", BST()), ("AVL", AVL()), ("Red-Black", RedBlack())]
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

            altura = arvore.altura()
            comparacoes = arvore.contador_comparacoes()

            resultados.append({
                "Árvore": nome,
                "Tamanho": n,
                "Altura": altura,
                "Comparações": comparacoes,
                "Tempo inserção": end_insercao - start_insercao,
            })

        resultados_gerais.extend(resultados)

        for r in resultados:
            print(f"{r['Árvore']}: Altura = {r['Altura']}, "
                  f"Comparações = {r['Comparações']}, "
                  f"Tempo Inserção = {r['Tempo inserção']:.4f}s")

    gerar_grafico_insercao(resultados_gerais)


def gerar_grafico_insercao(resultados):
    df = pd.DataFrame(resultados)
    plt.figure(figsize=(8,5))
    for arvore in df["Árvore"].unique():
        subset = df[df["Árvore"] == arvore]
        plt.plot(subset["Tamanho"], subset["Tempo inserção"], marker='o', label=arvore)
    plt.title("Tempo de Inserção vs Número de Músicas")
    plt.xlabel("Número de Músicas")
    plt.ylabel("Tempo (s)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def grafico_altura_vs_nos(dataset):
    tamanhos = [100, 500, 2000, 10000, 50000, 100000, len(dataset)]
    alturas_bst, alturas_avl, alturas_rb = [], [], []

    for n in tamanhos:
        dataset_teste = dataset[:n]
        bst = BST()
        avl = AVL()
        rb = RedBlack()

        for linha in dataset_teste:
            chave = linha['popularity']
            dados = {
                'track_name': linha['track_name'],
                'artist_name': linha['artist_name'],
                'genre': linha['genre']
            }
            bst.inserir(chave, dados)
            avl.inserir(chave, dados)
            rb.inserir(chave, dados)

        alturas_bst.append(bst.altura())
        alturas_avl.append(avl.altura())
        alturas_rb.append(rb.altura())

    plt.figure(figsize=(8,5))
    plt.plot(tamanhos, alturas_bst, marker='o', label="BST")
    plt.plot(tamanhos, alturas_avl, marker='o', label="AVL")
    plt.plot(tamanhos, alturas_rb, marker='o', label="Red-Black")
    plt.title("Altura da Árvore vs Número de Nós")
    plt.xlabel("Número de Nós")
    plt.ylabel("Altura da Árvore")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def tabela_altura_comparacoes(dataset):
    tamanhos = [100, 500, 2000, 10000, 50000, 100000, len(dataset)]
    print("\nTamanho | Altura BST | Altura AVL | Altura RB | Comparações BST | Comparações AVL | Comparações RB")
    print("-"*90)
    for n in tamanhos:
        subset = dataset[:n]
        bst = BST(); avl = AVL(); rb = RedBlack()
        for linha in subset:
            chave = linha['popularity']
            dados = {'track_name': linha['track_name']}
            bst.inserir(chave, dados)
            avl.inserir(chave, dados)
            rb.inserir(chave, dados)
        print(f"{n:6} | {bst.altura():10} | {avl.altura():10} | {rb.altura():9} | "
              f"{bst.contador_comparacoes():15} | {avl.contador_comparacoes():15} | {rb.contador_comparacoes():14}")


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
        print("3 - Usar árvore Red-Black")
        print("4 - Comparação de desempenho entre árvores (gera gráfico)")
        print("5 - Gerar gráfico: Altura da Árvore vs Número de Nós")
        print("6 - Gerar tabela: Altura e Comparações entre Árvores")
        print("7 - Sair")
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

        elif opcao == '3':
            arvore = RedBlack()
            print("Árvore Red-Black criada!")
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
            print(f"Tempo de inserção na Red-Black: {end_time - start_time:.4f} segundos")
            submenu_arvore(arvore, "Red-Black")

        elif opcao == '4':
            comparar_arvores(dataset)

        elif opcao == '5':
            grafico_altura_vs_nos(dataset)

        elif opcao == '6':
            tabela_altura_comparacoes(dataset)

        elif opcao == '7':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
