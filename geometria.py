# -*- coding: utf-8 -*-
"""
ECT/UFRN - POO - Projeto Final
Módulo que contém classes utilitárias
para geometria.
"""

import math

class ErroGeometria(Exception):
    """
    Erro base para o módulo geometria.
    """
    pass

class Ponto2D:
    """
    Representa um ponto bidimensional.
    Oferece acesso às coordenadas x e y de um ponto,
    sobrecarga de operadores +, +=, -, -= e
    método de classe para operações entre pontos.
    """
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def __repr__(self):
        return '({:.2f}, {:.2f})'.format(self._x, self._y)

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, nx):
        self._x = nx

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, ny):
        self._y = ny

    def __add__(self, t):
        r = Ponto2D()
        r.x = self.x + t.x
        r.y = self.y + t.y
        return r

    def __iadd__(self, t):
        self.x += t.x
        self.y += t.y
        return self

    def __sub__(self, t):
        r = Ponto2D()
        r.x = self.x - t.x
        r.y = self.y - t.y
        return r

    def __isub__(self, t):
        self.x -= t.x
        self.y -= t.y
        return self

    @staticmethod
    def gera_ponto2D(p):
        """
        Retorna Ponto2D a partir de uma tupla ou
        o proprio ponto se ele já for Ponto2D.
        Caso não seja nenhum dos dois, levanta erro.
        """
        if type(p) == tuple:
            p = Ponto2D(p[0], p[1])
        elif type(p) != Ponto2D:
            raise ErroGeometria('Coordenadas devem ser fornecidas como tupla ou Ponto2D.')
        return p

    @staticmethod
    def rotaciona(p, ang, o):
        """
        Retorna a rotação do ponto p em torno do ponto o por um angulo
        dado por ang (fornecido em graus).
        A rotação se dá no sentido anti-horário com ângulo positivo.
        """
        p = Ponto2D.gera_ponto2D(p)
        o = Ponto2D.gera_ponto2D(o)
        pr = Ponto2D()

        # converte angulo para radianos
        rad = math.pi/180*ang

        # 1. translada para a origem
        pl = p - o

        # 2. aplica rotação
        pr.x =  math.cos(rad)*pl.x - math.sin(rad)*pl.y
        pr.y =  math.sin(rad)*pl.x + math.cos(rad)*pl.y

        # 3. translada de volta à posição original
        pr = pr + o

        return pr

    @staticmethod
    def distancia(p1, p2):
        p1 = Ponto2D.gera_ponto2D(p1)
        p2 = Ponto2D.gera_ponto2D(p2)
        return math.sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y))

class Poligono:
    """
    Representa um polígono,
    que possui posição e uma lista de Ponto2D
    contendo os seus vértices.
    """
    def __init__(self, vertices, pos_ini=None, ang_ini=None):
        """
        Inicia polígono a partir de tupla ou lista
        contendo os vértices do polígono (cada vértice é uma tupla),
        posição inicial do polígno (tupla ou Ponto2D) e
        ângulo de orientação do polígono.
        """
        self.vertices = []
        self.pos = Ponto2D(0, 0)
        self.ang = 0.0


        if type(vertices) != tuple and type(vertices) != list:
            raise ErroGeometria('Vertices do poligono devem ser informados por tupla ou lista')
        
        for v in vertices:
            if type(v) != tuple:
                raise ErroGeometria('Cada vertice deve ser informado por uma tupla do tipo (x,y)')
            self.vertices.append(Ponto2D(v[0], v[1]))

        if pos_ini:
            if type(pos_ini) != tuple and type(pos_ini) != Ponto2D:
                raise ErroGeometria('Posicao inicial deve ser especificada por tupla ou Ponto2D')
            print()
            self.move(pos_ini)

        if ang_ini:
            self.rotaciona(ang_ini)

    def move(self, desl):
        """
        Move o polígono aplicando uma translação
        em cada vértice de acordo com o deslocamento
        (tupla ou Ponto2D) informado.
        """
        desl = Ponto2D.gera_ponto2D(desl)

        self.pos += desl
        for i in range(len(self.vertices)):
            self.vertices[i] += desl

    def rotaciona(self, ang):
        """
        Rotaciona o polígono aplicando uma rotação
        em cada vértice em torno do seu próprio eixo
        de acordo com o ângulo informado.
        """
        self.ang += ang
        if self.ang == 360:
            self.ang = 0
        if self.ang < 0:
            self.ang = 360 + self.ang
        for i in range(len(self.vertices)):
            self.vertices[i] = Ponto2D.rotaciona(self.vertices[i], ang, self.pos)

    def __repr__(self):
        s = ''
        for v in self.vertices:
            s += v.__repr__() + ', '
        s = s.rstrip(', ')
        return s

    def __getitem__(self, idx):
        if type(idx) != int:
            raise ErroGeometria('Indice fornecido para o vertice deve ser do tipo int')
        else:
            if idx >= len(self.vertices) or idx < 0:
                raise ErroGeometria('Indice fornecido para o vertice fora do intervalo')
            else:
                return (self.vertices[idx].x, self.vertices[idx].y)

if __name__ == "__main__":
    p1 = Ponto2D(30, 0)
    r1 = p1 + Ponto2D(50, -50)
    print('Translacao: {}'.format(r1))

    r2 = Ponto2D.rotaciona(p1, 90, Ponto2D(0, 0))
    print('Rotacao 1: {}'.format(r2))

    p2 = Ponto2D(30, 30)
    r3 = Ponto2D.rotaciona(p1, 90, p2)
    print('Rotacao 2: {}'.format(r3))

    vertices = ((-15, 0), (15, 0), (0,15))
    posicao_ini = (15, 0)
    angulo = 0.0
    pol1 = Poligono(vertices, posicao_ini, angulo)
    print('Poligono antes da rotacao: {}'.format(pol1))
    pol1.rotaciona(90)
    print('Poligono depois da rotacao: {}'.format(pol1))