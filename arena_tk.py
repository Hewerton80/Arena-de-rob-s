# -*- coding: utf-8 -*-
"""
ECT/UFRN - POO - Projeto Final
Módulo que contém uma arena
na forma de um Canvas TK.
"""

import tkinter as tk
from robo_tipo_2tk import *
from robo_tipo_3tk import *
from itens_tk import *
from celula_tk import *

class ErroArena(Exception):
    """
    Erro base para a classe Arena.
    """
    pass

class ArenaTK(tk.Canvas):
    def __init__(self,root,arq,w,h,p):
        tk.Canvas.__init__(self,root,width=w, height=h,bg='#888888',borderwidth=0, highlightthickness=0,)
        self.id_robo_lidado = None
        self.largura = int(w/p)
        self.altura = int(h/p)
        self.tam_celula = int(p)
        self.info = tk.StringVar()

        self.cria_arquivo()
        self.carrega_de_arquivo('arena.txt')

        self.robos = {}
        
    def cria_robo(self,nome,x,y,ori):
        #print(nome,x,y,ori)
        robo = RoboTipo3TK(nome,x,y,ori)
        robo.arena = self
        robo._inicializa_forma()
        self.adiciona_robo(robo)
        self.focus_set()
        

    def adiciona_robo(self,robo):
        self.robos[robo.item_canvas] = robo
        self.robos[robo.item_canvas].nome = robo.nome if robo.nome else 'robô ' + str(robo.item_canvas)
       

    def ativa_controle_robo(self,evento):
        arenatk = evento.widget
        item = arenatk.find_overlapping(evento.x+1, evento.y+1,evento.x-1, evento.y-1)
        item = item[len(item)-1]
        print(arenatk.type(item))
        if arenatk.type(item)=='polygon':
            self.id_robo_lidado = item

            if not self.robos[item].sensor:
                self.robos[item].adiciona_sensor()
            
            self.itemconfig(self.robos[item].sensor_id,state='normal')
            self.robos[item].sensor.obtem_medicao()#ocultar todos blocos
            print(self.id_robo_lidado)

        self.mostra_info()

    def processa_teclado(self,evento):
        if self.id_robo_lidado:
            self.robos[self.id_robo_lidado].processa_teclado(evento)
        self.mostra_info()

    def mostra_info(self):
        robo = self.robos[self.id_robo_lidado]
        pos = robo.pos()
        blocos = len(self.find_withtag('bloco'))
        blocos_explorados = len(robo.sensor.celulas_detec)
        robos_detectados = len(robo.sensor.robos_detec)-1
        info = 'Nome: {}             '.format(robo.nome)
        info += 'X: {:.2f}, Y: {:.2f}                '.format(pos.x,pos.y)
        info += 'Área explorada: {:.2f}%             '.format((blocos_explorados/blocos)*100)
        info+='Robôs detectados: {:02d}'.format(robos_detectados)
        self.info.set(info)

    def cria_arquivo(self):
        arq = open('arena.txt','w')
        arq.write('arena {} {} {}\n'.format(str(self.largura),str(self.altura),str(self.tam_celula)))
        for i in range(0,self.largura):
            for  j in range(0,self.altura):
                prob = random() * 100
                if prob > 5 and prob <= 100:
                    arq.write('0')
                else:
                    arq.write('1')
            arq.write('\n')

    def carrega_de_arquivo(self,arquivo):
        arq = open(arquivo,'r')
        linha1 = arq.readline()
        linha1=linha1.rstrip('\n')
        linha1=linha1.split(' ')
        p = int(linha1[3])
        i=0
        for linha in arq.readlines():
            linha=linha.rstrip('\n')
            j=0
            for c in linha:
                cel = CelulaTK((i,j), p, False, not int(c))
                cel.arena = self
                cel._inicializa_forma()
                j+=1
            i+=1
                
                

        

        








