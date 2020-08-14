# coding=utf-8
from structures.node.Node import Node


class Dequeue:  # Double Ended Queue.

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__size = 0
        self._elements = []

    def capacity(self):
        return self.__capacity

    def size(self):
        return self.__size

    def elements(self):
        return self._elements

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity()

    def last_index(self):
        return self.size() - 1

    def add_node(self, new_node):
        """
                Adiciona um elemento à estrutura.

                :param  new_node: Um novo nodo a ser adicionado à estrutura.
                :return O método retorna a própria lista, como forma
                        de permitir o encadeamento de adições

                        ex:
                            UmaEstruturaQualquer.add_element(...).add_element(...) [...]
                """

        assert isinstance(new_node, Node)  # Deve-se checar se o nodo passado é realmente um nodo.

        if self.is_full():
            raise ValueError("A estrutura já está cheia. ")
        else:
            # Como self.__size começa em 0, precisamos diminuir 1 para alcançar a posição
            # do último nodo adicionado e, então, aumentamos o tamnho de nossa estrutura em 1.
            self._elements[self.size() - 1] = new_node
            self.__size = self.__size + 1
            return self
