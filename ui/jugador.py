__author__ = 'user'
## @package Jugador
#  Este archivo la clase Jugador
#


""" _Clase Jugador
Clase Jugador con el nivel que escogio, nombre, tiempo y el valor.
"""
class Jugador:

    def __init__(self, nivel, nombre, tiempo, valor):
        self.nivel = nivel
        self.nombre = nombre
        self.tiempo = tiempo
        self.valor = valor