# coding=utf-8

"""
Exercício 1:
A Cifra de Vernam, conhecida também como "One-time Pad" é magnífica por ser extremamente simples e,
ao mesmo tempo, poderosa. De fácil implementação, consiste em criptografar uma
dada mensagem com uma chave usando uma operação XOR.

No seguinte exemplo, sendo "a" a mensagem, "b" a chave e "c" o resultado, encriptado, temos:

                                        a xor b = c

E, ao obtermos "c", podemos enviar essa mensagem e outra pessoa será capaz de ler o texto original se tiver
a chave "b" em mãos , mas...

TODO Por quê? Reveja as propriedades da operação XOR.
 Essa cifra foi usada como mecanismo de garantia de confidencialidade
 em ligações Moscou-Washington e vice-versa. Logo, assume-se que era
 vista como um método bom para garantir a privicidade de informações.
 Na verdade, a cifra é tão segura que é dita "inquebrável". No entanto,
 algumas condições precisam ser cumpridas.
 Quais são elas?
"""


def vernam_cipher(message, text):
    # TODO implementar a Cifra de Vernam
    return message, text
