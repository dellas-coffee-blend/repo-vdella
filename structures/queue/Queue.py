# coding=utf-8
from structures.templates.DequeueTemplate import Dequeue


# Representação da estrutura de dados Fila -> First In, First Out (FIFO)
class Queue(Dequeue):

    def forward_positions(self):
        i = 0
        forwarding = self.elements()
        for _ in range(self.size() - 1):
            self._elements[i] = forwarding[i + 1]
            i = i + 1

    def enqueue(self, new_node):
        return self.add_node(new_node)

    def dequeue(self):

        if self.is_empty():
            raise ValueError("Não se pode tirar elementos de uma fila vazia. ")

        head = self.elements()[0]
        self.forward_positions()
        return head, self
