"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""
papapapapapaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaatatataaaaaaaaaaaaaaaaaaaaaaaaaa
class Coche:

"""
Clase coche con numero de serie, cilindrada,abricante y color
"""
    num_serie = 1;
    cilindrada = 1000;
    fabricante = 'seat';
    color = 'rojo';
""""super clase de coche """""""""2""""
    def __init__(self):
        pass;

    def __init__(self, num_serie, cilindrada, fabricante, color):
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;
"""
Definición numero de serie, cilindrada,fabricante y color
"""
    @property
    def num_serie(self):
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        self.__num_serie = value

"""
:param num serie
"""

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value: int):
        self.__color = value
"""
:param color
"""
    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        self.__cilindrada = value

"""
:param cilindrada
"""

    @property
    def fabricante(self):
        return self.__fabricante
"""
:param fabricante
"""
    @fabricante.setter
    def fabricante(self, value):
        self.__fabricante = value
