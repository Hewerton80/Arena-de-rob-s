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

if __name__ == '__main__':

    root = tk.Tk()
    root.title('Arena de Robos')
    root.geometry('400x400+0+0')

    # toda arena é um canvas: um canvas pode ser utilizado para exibir
    # vários ItemTK
    c = tk.Canvas(root, width=400, height=400, bg='gray', highlightthickness=0, borderwidth=0)
    c.pack(expand=tk.TRUE, fill=tk.BOTH)
    c.focus_set()

    # cria sensor de proximidade
    sensor = SensorProximidadeTK(c, 50)

    # cria robô tipo3 com sensor de proximidade
    r1 = RoboTipo3TK('r1', (50, 50), 0, 'red', c, sensor)

    # controla robô r1
    c.bind('<Key>', r1.processa_teclado)

    root.mainloop()
