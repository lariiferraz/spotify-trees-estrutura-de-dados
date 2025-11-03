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
            return Node(chave, [dados])

        self.comparacoes += 1

        if chave == no.chave:
            no.dados.append(dados)
        elif chave < no.chave:
            no.esquerdo = self._inserir_rec(no.esquerdo, chave, dados)
        else:
            no.direito = self._inserir_rec(no.direito, chave, dados)

        return no

    def buscar(self, chave):
        """Busca um nó pela chave"""
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

    # Adicione este método na classe BST

    def remover_n(self, chave, n):
        """Remove até n elementos com a chave informada"""
        for _ in range(n):
            if self.buscar(chave):
                self.raiz = self._remover_rec(self.raiz, chave)
            else:
                break

    def _remover_rec(self, no, chave):
        """Remoção recursiva de um nó pela chave"""
        if no is None:
            return None
        self.comparacoes += 1
        if chave < no.chave:
            no.esquerdo = self._remover_rec(no.esquerdo, chave)
        elif chave > no.chave:
            no.direito = self._remover_rec(no.direito, chave)
        else:
            # Caso haja múltiplos dados, remove apenas um do nó
            if len(no.dados) > 1:
                no.dados.pop(0)
                return no
            # Nó com zero ou um filho
            if no.esquerdo is None:
                return no.direito
            elif no.direito is None:
                return no.esquerdo
            # Nó com dois filhos: substitui pelo menor da subárvore direita
            temp = self._minimo(no.direito)
            no.chave = temp.chave
            no.dados = temp.dados
            no.direito = self._remover_rec(no.direito, temp.chave)
        return no

    def _minimo(self, no):
        """Retorna o nó com a menor chave da árvore/subárvore"""
        current = no
        while current.esquerdo is not None:
            current = current.esquerdo
        return current

    def altura(self):
        """Retorna a altura da árvore"""
        return self._altura_rec(self.raiz)

    def _altura_rec(self, no):
        if no is None:
            return 0
        return 1 + max(self._altura_rec(no.esquerdo), self._altura_rec(no.direito))

    def contador_comparacoes(self):
        return self.comparacoes
