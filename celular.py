#!/usr/bin/env python
# -*- coding: utf-8 -*-

mapping = {'2': ['A', 'B', 'C'],
           '3': ['D', 'E', 'F'],
           '4': ['G', 'H', 'I'],
           '5': ['J', 'K', 'L'],
           '6': ['M', 'N', 'O'],
           '7': ['P', 'Q', 'R', 'S'],
           '8': ['T', 'U', 'V'],
           '9': ['W', 'X', 'Y', 'Z'],
           '0': [' '],
           '_': ['']
           }

class Escrever:

    def __init__(self, numeros):
        self.numeros = numeros

    def escrever_no_celular(self):
        lista_numeros = list(self.numeros)
        nova_lista1 = []
        nova_lista2 = []
        message2 = ''
        elemento_anterior = ''
        
        for elemento in lista_numeros:
            if elemento_anterior != elemento:
                nova_lista1.append(elemento)
                nova_lista2.append(1)
            else:
                quantidade = nova_lista2[-1]
                del nova_lista2[-1]
                nova_lista2.append(quantidade + 1)
            elemento_anterior = elemento

        zipped = zip(nova_lista1, nova_lista2)
        for x, y in zipped:
        	message2 = message2 + mapping[x][y-1]
        return message2
