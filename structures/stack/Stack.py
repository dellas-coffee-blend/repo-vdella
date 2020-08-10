# coding=utf-8
from structures.node import Node


# Estrutura de dados First-in First-Out (FIFO)
class Stack:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__size = 0
        self.__elements = []

    def capacity(self):
        return self.__capacity

    def size(self):
        return self.__size

    def elements(self):
        return self.__elements

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity()

    def push(self, new_node):
        """
        Adiciona um elemento à pilha.

        :param  new_node: Um novo nodo a ser adicionado à pilha.
        :return O método retorna a própria lista, como forma
                de permitir o encadeamento de adições

                ex:
                    UmaPilhaQualquer.push(...).push(...) [...]
        """
        assert isinstance(new_node, Node)  # Deve-se checar se o nodo passado é realmente um nodo.

        if self.is_full():
            raise ValueError("A pilha já está cheia. ")
        else:
            # Como self.__size começa em 0, precisamos diminuir 1 para alcançar a posição
            # do último nodo adicionado e, então, aumentamos o tamnho de nossa pilha em 1.
            self.__elements[self.size() - 1] = new_node
            self.__size = self.__size + 1
            return self

    def pop(self):
        """
        Retira um elemento da pilha.

        :return: o elemento retirado e a própria pilha, para permitir o encadeamento de retiradas

                ex:
                        var1, var2 = UmaPilhaQualquer.pop(...).pop(...) [...]
        """
        if self.is_empty():
            raise ValueError("Uma pilha vazia não pode remover elementos. ")
        else:
            # Acessamos o último nodo fazendo self.__size - 1
            # E depois diminuímos o tamanho de nossa pilha.
            pop = self.__elements[self.size() - 1]
            self.__size = self.__size - 1
            return pop, self
