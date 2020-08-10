# coding=utf-8


def extensive_search(wanted, a_list):
    """
    Passa por cada elemento da lista até achar a posição que
    contém aquele que é procurado; caso não o número requerido
    acabe por não ser achado, retorna-se None.

    O(n) é o seu pior caso, pois teremos que correr por cada
    elemento, até o último, na posição "n".
    """
    assert isinstance(a_list, list)

    wanted_position = 0
    for value in range(len(a_list)):
        if value == wanted:
            return wanted_position
        wanted_position = wanted_position + 1

    return None


def binary_search(wanted, a_list):
    """
    Realiza uma busca binária por uma lista: sempre olha pro meio,
    vê se o número requerido é maior ou menor do o que está no meio
    da lista. Se for maior, vai pra primeira metade da lista e,
    se for menor, vai pra segunda metade. Olha-se o meio da metade
    em que se está e o algoritmo se repete.

    O(log n) é o seu pior caso. O logaritmo está sempre na base 2
    quando fala-se de Notação Big O: O(...). Será "log n"
    porque estaremos sempre cortando a lista pela metade.
    """
    assert isinstance(a_list, list)

    # A lista precisa, necessariamente, estar ordenada.
    a_list.sort()

    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (high + low) / 2
        guess = a_list[mid]

        if wanted == guess:
            return mid
        if guess > wanted:
            high = mid - 1
        else:
            low = mid + 1

    return None
