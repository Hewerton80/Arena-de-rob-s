from robo_tipo_2 import *
from itens_tk import *
from geometria import *
class RoboTipo2TK(ItemTK,RoboTipo2):
	def __init__(self,nome):
		RoboTipo2.__init__(self,nome)
		self.l=None
		

	def _inicializa_forma(self):
		self.l = 25 #base do triângulo (que é igual a sua altura)
		pos0=Ponto2D(50,50)# posição inicial
		p1=(self.l/2 +pos0.x, 0 + pos0.y)
		p2=(-self.l/2 +pos0.x, -self.l/2+pos0.y)
		p3=(-self.l/2 +pos0.x, self.l/2+pos0.y)
		self.item_canvas = self.arena.create_polygon((p1,p2,p3) , fill='orange')
		self.forma = self.arena.type(self.item_canvas)

	def _move_forma(self, delta):
		pass

	def pos(self):

		pos = self.arena.coords(self.item_canvas)
		x = pos[0] - (self.l/2)
		y = pos[1]
		pos = Ponto2D(x,y)
		return pos

	def ang(self):
		return self.ang


	def move(self, delta):
		pass

	def __repr__(self):
		s = 'info robo:\n\n' 
		s += "nome: {}\ntipo:{}\nid:{}".format(self.nome,self.forma,self.item_canvas)
		return s
	