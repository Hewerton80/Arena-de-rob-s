# -*- coding: utf-8 -*-
"""
ECT/UFRN - POO - Projeto Final
Módulo que contém hierarquia de todos
os itens desenháveis no canvas TK.
Serve como uma casca ("wrapper")
por cima das classes que pertencem
ao domínio do problema.
"""

from abc import ABC, abstractmethod
import tkinter as tk
from robo import *
from sensor import *

class ItemTK(ABC):
    """
    Representa um objeto referente
    a um item desenhável em um canvas TK.
    """
    def __init__(self, arena):
        # arena (canvas) na qual o item está desenhado
        self.arena = arena
        # nr. de id. correspondente ao item no canvas
        self.item_canvas = None

    @abstractmethod
    def _inicializa_forma(self):
        """
        Inicializa a forma geométrica
        e a associa ao canvas:
        chama a função create_* do
        canvas TK.
        """
        pass

    @abstractmethod
    def _move_forma(self, delta):
        """
        Move a forma geométrica
        no canvas TK.
        """
        pass

    def oculta(self):
        """
        Oculta o item
        no canvas TK.
        """
        self.arena.itemconfig(self.item_canvas, state='hidden')

    def exibe(self, contorno='black'):
        """
        Exibe o item
        no canvas TK.
        """
        self.arena.itemconfig(self.item_canvas, state='normal', outline=contorno)
