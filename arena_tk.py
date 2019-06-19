# -*- coding: utf-8 -*-
"""
ECT/UFRN - POO - Projeto Final
Módulo que contém uma arena
na forma de um Canvas TK.
"""

import tkinter as tk
from robo_tipo_2tk import *
from itens_tk import *

class ErroArena(Exception):
    """
    Erro base para a classe Arena.
    """
    pass

class ArenaTK(tk.Canvas):
    def __init__(self,root,arq,w,h,p):
        tk.Canvas.__init__(self,root,width=w, height=h,bg='#888888')
        self.robos = {}
        
        self.largura = int(w)
        self.altura = int(h)
        self.tam_celula = int(p)

        robo = RoboTipo2TK('R2-D2')
        robo.arena = self
        robo._inicializa_forma()
        self.adiciona_robo(robo)
        print('posição do robô: {}'.format(self.robos[1].pos()))

        
    def adiciona_robo(self,robo):
        self.robos[robo.item_canvas] = robo







