# trees.py
from node import Node

class BST:
    def __init__(self):
        self.raiz = None
        self.comparacoes = 0  # contador de comparações

    def inserir(self, chave, dados):
        """Insere um novo nó na BST"""
        self.raiz = self._inserir_rec(self.raiz, chave, dados)

    def _inserir_rec(self, no, chave, dados):
        if no is None:
            # Cria um nó novo com a lista de dados
            return Node(chave, [dados])

        self.comparacoes += 1

        if chave == no.chave:
            # Chave já existe, adiciona o novo dado à lista
            no.dados.append(dados)
        elif chave < no.chave:
            no.esquerdo = self._inserir_rec(no.esquerdo, chave, dados)
        else:
            no.direito = self._inserir_rec(no.direito, chave, dados)

        return no

    def buscar(self, chave):
        """Busca um nó pela chave e retorna todos os dados do nó"""
        return self._buscar_rec(self.raiz, chave)

    def _buscar_rec(self, no, chave):
        if no is None:
            return None
        self.comparacoes += 1
        if chave == no.chave:
            return no.dados
        elif chave < no.chave:
            return self._buscar_rec(no.esquerdo, chave)
        else:
            return self._buscar_rec(no.direito, chave)

    def buscar_todos(self, chave):
        """Retorna todos os dados de nós que possuem a chave informada"""
        resultados = []
        self._buscar_todos_rec(self.raiz, chave, resultados)
        return resultados

    def _buscar_todos_rec(self, no, chave, resultados):
        if no is None:
            return
        # Percorre esquerda
        self._buscar_todos_rec(no.esquerdo, chave, resultados)
        # Verifica se a chave é igual
        if no.chave == chave:
            resultados.extend(no.dados)
            self.comparacoes += 1
        # Percorre direita
        self._buscar_todos_rec(no.direito, chave, resultados)

    def altura(self):
        """Retorna a altura da árvore"""
        return self._altura_rec(self.raiz)

    def _altura_rec(self, no):
        if no is None:
            return 0
        return 1 + max(self._altura_rec(no.esquerdo), self._altura_rec(no.direito))

    def contador_comparacoes(self):
        return self.comparacoes
