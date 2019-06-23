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
    @abstractmethod
    def colide(self, vet_des):
        pass

    @abstractmethod
    def adiciona_sensor(self):
        pass


