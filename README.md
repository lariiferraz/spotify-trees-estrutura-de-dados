# Spotify Trees - Estrutura de Dados

## 📚 Descrição do Projeto
Este projeto implementa **três tipos de árvores** (Árvore Binária de Busca, AVL e Red-Black) para organizar e analisar dados do **Spotify Tracks Dataset**.  
O objetivo é estudar a **eficiência das árvores** em operações de inserção, busca e remoção, além de analisar métricas como altura, número de comparações e balanceamento.

---

## 🎯 Dataset
**Nome:** Spotify Tracks Dataset  
**Fonte:** [Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)  
**Descrição:** Conjunto de dados com informações de músicas do Spotify, incluindo:
- `track_name` (nome da música)  
- `artist_name` (nome do artista)  
- `popularity` (popularidade da música, de 0 a 100)  
- Outros atributos opcionais: `album`, `genre`, `duration_ms`, etc.  

**Quantidade de registros:** ~115.000  

**Chave utilizada nas árvores:** `popularity`  
**Dados associados:** `track_name` e `artist_name`  

---

## ⚙️ Funcionalidades Implementadas
1. **Árvore Binária de Busca (BST)**  
2. **Árvore AVL (balanceada)**  
3. **Árvore Red-Black (balanceada)**  

**Métodos implementados:**
- `inserir(chave, dados)`  
- `buscar(chave) → dados`  
- `remover(chave)`  
- `altura() → inteiro`  
- `contador_comparacoes() → inteiro` (para métricas)  

---

## 📊 Métricas e Análise
- **Tempo de execução** para cada operação  
- **Número de comparações realizadas**  
- **Altura e balanceamento das árvores**  
- **Visualização comparativa** entre as três árvores  

---

## 💡 Objetivo do Trabalho
Demonstrar como diferentes tipos de árvores afetam o desempenho de operações básicas sobre dados reais, e como o **balanceamento** influencia a eficiência de busca, inserção e remoção.

---

## 🛠️ Estrutura do Repositório
- `dataset/` → arquivo CSV do Spotify  
- `trees/` → implementação das árvores (BST, AVL, Red-Black)  
- `tests/` → scripts de teste e métricas  
- `README.md` → descrição do projeto  

---

## ⚡ Observações
- Todas as operações são realizadas com **a popularidade das músicas como chave**.  
- Cada nó armazena os dados adicionais da música (`track_name` e `artist_name`).  
- Gráficos de desempenho e balanceamento serão gerados para análise comparativa.
