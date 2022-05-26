#ABC, acrônimo para Abstract Base Classes
from collections.abc import MutableSequence # Importamos o pacote collections.abc, que contém diversas classes que podem ser utilizadas, inclusive o MutableSequence, uma sequência mutável cujos valores podem ser alterados.

class MinhaListinhaMutavel(MutableSequence):
    pass

objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)