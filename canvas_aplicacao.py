# -*- coding: utf-8 -*-

import tkinter as tk

class App:
    def __init__(self):
        self._item_desenho = None
        self._item_poligono = None
        self._poligono_ativo = False
        self._inicializa_gui()
        self._configura_eventos()

    def _inicializa_gui(self):
        # janela principal
        self.root = tk.Tk()
        self.root.title('Aplicacao com Canvas')
        self.root.geometry('400x400+100+100')

        # canvas
        self.canvas = tk.Canvas(self.root, width=200, height=200)
        self.canvas['bg'] = 'yellow'
        self.canvas['bd'] = 0
        self.canvas['highlightthickness'] = 0
        self.canvas.pack(expand=tk.YES)

        # label com informacoes
        self.info_var = tk.StringVar(self.root)
        self.info_var.set('Pos: 0, 0. Mouse sobre poligono: Nao')
        self.lbl_info = tk.Label(self.root, textvar=self.info_var)
        self.lbl_info.pack()

        id_item = self.canvas.create_oval(100-1, 100-1, 100, 100, fill = 'black')

        id_item = self.canvas.create_line(100, 100 - 50, 100, 100 + 50, fill='orange')
        id_item = self.canvas.create_line(100-50, 100, 100 + 50, 100, fill='orange')

        self._item_poligono = self.canvas.create_polygon((150, 150), (175, 175), (125, 175), fill='blue')

    def _configura_eventos(self):
        self.canvas.bind('<Motion>', self._movimento_mouse)
        self.canvas.tag_bind(self._item_poligono, '<Motion>', self._poligono_mouse)

    def _desenha(self, x, y):
        if self._item_desenho:
            self.canvas.delete(self._item_desenho)

        self._item_desenho = self.canvas.create_rectangle(x-20, y-10, x+20, y+10, outline='red')

    def _movimento_mouse(self, ev):
        msg = ''
        if self._poligono_ativo:
            msg += 'Mouse sobre poligono: Sim'
        else:
            msg += 'Mouse sobre poligono: Nao'
        self.info_var.set('Pos: {}, {}. '.format(ev.x, ev.y) + msg)
        self._desenha(ev.x, ev.y)
        self._poligono_ativo = False

    def _poligono_mouse(self, ev):
        self._poligono_ativo = True

    def executa(self):
        self.root.mainloop()

if __name__ == "__main__":
    a = App()
    a.executa()