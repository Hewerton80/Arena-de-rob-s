from robo_tipo_2 import *
from itens_tk import *
from geometria import *
class RoboTipo2TK(ItemTK,RoboTipo2):
	def __init__(self,nome):
		RoboTipo2.__init__(self,nome)
		self.l = 25 #base do triângulo (que é igual a sua altura)
		self.vertices = [(self.l/2 , 0),(-self.l/2 , -self.l/2),(-self.l/2 , self.l/2)] 

	def _inicializa_forma(self): 
		p0 = Ponto2D(50,50)
		pol =  Poligono(self.vertices,p0,self.ang)
		print('cordenadas dos vertices do poligôno no canvas: {}'.format(pol))
		p1=(pol.vertices[0].x, pol.vertices[0].y)
		p2=(pol.vertices[1].x, pol.vertices[1].y)
		p3=(pol.vertices[2].x, pol.vertices[2].y)
		
		self.item_canvas = self.arena.create_polygon((p1,p2,p3) , fill='orange')
		self.forma = self.arena.type(self.item_canvas)

	def processa_teclado(self,evento):
		tecla = evento.char
		if tecla == 'w':
			self.move((Robo.DELTA,0),'frente')
		if tecla == 's':
			self.move((-Robo.DELTA,0),'frente')

	def pos(self):

		pos = self.arena.coords(self.item_canvas)
		x = pos[0] - (self.l/2)
		y = pos[1]
		pos = Ponto2D(x,y)
		return pos

	def ang(self):
		return self.ang

	def move(self,vet_des,sentido):
		if sentido == 'frente':
			pol =  Poligono(self.vertices,self.pos(),self.ang)
			pol.move(vet_des)
			print('cordenadas dos vertices do poligôno no canvas: {}'.format(pol.pos))
			self._move_forma( (pol.pos.x,pol.pos.y) )

	def _move_forma(self,vet_des):

		#pol =  Poligono(self.vertices, self.pos(), self.ang())
		p1=(self.vertices[0][0] + vet_des[0], self.vertices[0][1] + vet_des[1])
		p2=(self.vertices[1][0] + vet_des[0], self.vertices[1][1] + vet_des[1])
		p3=(self.vertices[2][0] + vet_des[0], self.vertices[2][1] + vet_des[1])
		self.arena.coords(self.item_canvas,[ p1[0], p1[1], p2[0], p2[1], p3[0], p3[1] ])
		

	def __repr__(self):
		s = 'info robo:\n\n' 
		s += "nome: {}\ntipo:{}\nid:{}".format(self.nome,self.forma,self.item_canvas)
		return s
	