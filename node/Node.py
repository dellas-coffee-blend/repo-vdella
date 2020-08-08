# coding=utf-8
class Node:

    """
    Classe que aproveita o duck typing da linguagem
    para permitir a criação de um nodo genérico.
    """

    def __init__(self, element):
        self.__element = element
        self.__next = None
        self.__previous = None

    def element(self):
        return self.__element

    def next_node(self):
        return self.__next

    def previous_node(self):
        return self.__previous
