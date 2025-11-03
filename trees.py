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
    
class AVL:
    def __init__(self):
        self.raiz = None
        self.comparacoes = 0

    def altura_no(self, no):
        if no is None:
            return 0
        return no.altura

    def atualizar_altura(self, no):
        no.altura = 1 + max(self.altura_no(no.esquerdo), self.altura_no(no.direito))

    def fator_balanceamento(self, no):
        return self.altura_no(no.esquerdo) - self.altura_no(no.direito)

    def rotacionar_direita(self, y):
        x = y.esquerdo
        T2 = x.direito
        x.direito = y
        y.esquerdo = T2
        self.atualizar_altura(y)
        self.atualizar_altura(x)
        return x

    def rotacionar_esquerda(self, x):
        y = x.direito
        T2 = y.esquerdo
        y.esquerdo = x
        x.direito = T2
        self.atualizar_altura(x)
        self.atualizar_altura(y)
        return y

    def inserir(self, chave, dados):
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

        self.atualizar_altura(no)
        balance = self.fator_balanceamento(no)

        # Rotação esquerda-direita
        if balance > 1 and chave > no.esquerdo.chave:
            no.esquerdo = self.rotacionar_esquerda(no.esquerdo)
            return self.rotacionar_direita(no)
        # Rotação direita-esquerda
        if balance < -1 and chave < no.direito.chave:
            no.direito = self.rotacionar_direita(no.direito)
            return self.rotacionar_esquerda(no)
        # Rotação direita-direita
        if balance < -1 and chave > no.direito.chave:
            return self.rotacionar_esquerda(no)
        # Rotação esquerda-esquerda
        if balance > 1 and chave < no.esquerdo.chave:
            return self.rotacionar_direita(no)

        return no

    def buscar(self, chave):
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

    def remover_n(self, chave, n):
        """Remove até n elementos com a chave informada"""
        for _ in range(n):
            if self.buscar(chave):
                self.raiz = self._remover_rec(self.raiz, chave)
            else:
                break

    def _remover_rec(self, no, chave):
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

        # Atualiza altura e balanceia
        self.atualizar_altura(no)
        balance = self.fator_balanceamento(no)

        # Rotação esquerda-esquerda
        if balance > 1 and self.fator_balanceamento(no.esquerdo) >= 0:
            return self.rotacionar_direita(no)
        # Rotação esquerda-direita
        if balance > 1 and self.fator_balanceamento(no.esquerdo) < 0:
            no.esquerdo = self.rotacionar_esquerda(no.esquerdo)
            return self.rotacionar_direita(no)
        # Rotação direita-direita
        if balance < -1 and self.fator_balanceamento(no.direito) <= 0:
            return self.rotacionar_esquerda(no)
        # Rotação direita-esquerda
        if balance < -1 and self.fator_balanceamento(no.direito) > 0:
            no.direito = self.rotacionar_direita(no.direito)
            return self.rotacionar_esquerda(no)

        return no

    def _minimo(self, no):
        current = no
        while current.esquerdo is not None:
            current = current.esquerdo
        return current

    def altura(self):
        return self.altura_no(self.raiz)

    def contador_comparacoes(self):
        return self.comparacoes
