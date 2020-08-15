# coding=utf-8

# Exercício 1:
# Miguelzinho se diverte horrores adicionando números de celular para contatinhos
# O objetivo de Miguel é adicionar um nome de forma que, quando procurar o nome colocado,
# lhe seja dado o número de celular associado ao nome procurado.
def contact_dict(contact_name):
    """
    TODO
     Objetivos:
     1. Juntar ambas as listas, de forma que, se eu procurar um nome, recebo o número de telefone deste, caso exista.
     2. Se eu não achar o nome que estou procurando, posso assumir seguramente que não há também
        um número a ele associado -> Retorno "0" (String 0 ou outro valor arbitrário).
    """
    contacts = ["João", "Mariazinha", "Fabiana"]
    tel_numbers = ["997998765", "998790098", "98765773"]
