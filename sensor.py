# -*- coding: utf-8 -*-
"""
ECT/UFRN - POO - Projeto Final
Módulo que contém a hierarquia de sensores.
Cada classe provê comportamento único relativo
a como os sensores detectam obstáculos presentes
na arena.
"""

from abc import ABC, abstractmethod

class ErroSensor(Exception):
    """
    Erro base para a classe Sensor.
    """
    pass

class Sensor(ABC):
    """
    Classe base abstrata para representar um sensor.
    """
    tipos = ('PROXIMIDADE1', 'PROXIMIDADE2', 'ONISCIENTE')
    def __init__(self):
        self.robo = None
        self.robos_detec = []
        self.celulas_detec = []

    @abstractmethod
    def inicializa_sensor(self, robo):
        """
        Associa o sensor a um robô
        (deve ser chamado uma vez
         antes do sensor começar a
         obter medições)
        """
        self.robo = robo
        print('Sensor inicializado no robo {}'.format(self.robo.nome))

    @abstractmethod
    def obtem_medicao(self):
        """
        Obtem uma medição sensorial a partir
        da posição do robô ao qual o sensor
        está associado:
        o sensor é "disparado" e os robôs e
        objetos detectados são atualizados,
        de acordo com a lógica
        de funcionamento de cada sensor.
        """
        if not self.robo:
            raise ErroSensor('O sensor deve estar associado a um robo para obter medicao.')
        self.robos_detec.clear()
        self.celulas_detec.clear()