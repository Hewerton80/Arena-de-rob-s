# -*- coding: utf-8 -*-
"""
ECT/UFRN - POO - Projeto Final
Módulo que contém a hierarquia de robôs.
Cada classe provê comportamento único quanto
ao seu tipo de movimento e sensores utilizados.
"""

from abc import ABC, abstractmethod
import geometria as geom

class Robo():
    """
    Classe base abstrata para representar um robô.
    """
    DELTA = 5 # incremento do movimento (5 pixels)
    ALPHA = 5 # incremento da rotação (5 graus)
    def __init__(self, nome):
        self.nome = nome
        #self.pos = None

    def __repr__(self):
        """
        Robo no formato nome: (x, y).
        """
        return '{}: {}'.format(self.nome, self.pos)

    @property
    @abstractmethod
    def pos(self):
        """
        Retorna posição do robô em forma de tupla
        (armazenada na sua forma).
        """
        pass

    @property
    @abstractmethod
    def ang(self):
        """
        Retorna ângulo de orientação do robô
        (armazenado na sua forma).
        """
        pass

    @abstractmethod
    def move(self, delta):
        """
        Move o robô na arena de acordo com
        vetor deslocamento dado pela tupla
        em delta
        (delta é dado no sist. de coord.
        global).
        """
        pass

class RoboTipoX(Robo):
    """
    Implemente aqui a lógica de movimentação
    para o tipo de robô escolhido.
    """
    pass

if __name__ == '__main__':

    r3 = RoboTipo3('r_tipo3', (50, 50), 90)
    print(r3.forma)
