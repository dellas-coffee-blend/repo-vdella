# coding=utf-8
from structures.templates.DequeueTemplate import Dequeue


# Estrutura de dados First-in First-Out (FIFO)
class Stack(Dequeue):

    def push(self, new_node):
        return self.add_node(new_node)

    def pop(self):

        if self.is_empty():
            raise ValueError("Uma pilha vazia não pode remover elementos. ")

        pop = self._elements[self.last_index()]
        self.__size = self.__size - 1
        return pop, self
