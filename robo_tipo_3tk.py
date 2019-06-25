from robo_tipo_3 import *
from itens_tk import *
from geometria import *
from random import *
from sensor_tipo_2tk import *
from robo_tipo_2tk import *
class RoboTipo3TK(RoboTipo3):
	l = 20 #base do triângulo (que é igual a sua altura)
	vertices = [(l/2 , 0),(0,l/2),(-l/2 , l/2),(-l/2 ,-l/2),(0,-l/2)]
	

	def __init__(self,nome,x,y,ori):
		self.cor = None
		self.sensor = None
		self.sensor_id = None
		self.nome = nome
		
		x = float(x) if x else uniform(RoboTipo3TK.l, 640 - RoboTipo3TK.l)
		y = float(y) if y else uniform(RoboTipo3TK.l, 410 - RoboTipo3TK.l)
		ori = float(ori) if ori else uniform(0,360)
		pos0 = Ponto2D(x, y)
		pol = Poligono(RoboTipo3TK.vertices, pos0, ori )
		RoboTipo2.__init__(self,nome,pol)

	def _inicializa_forma(self): 
		print('cordenadas dos vertices do poligôno no canvas: {}'.format(self.forma))
		p1=(self.forma.vertices[0].x, self.forma.vertices[0].y)
		p2=(self.forma.vertices[1].x, self.forma.vertices[1].y)
		p3=(self.forma.vertices[2].x, self.forma.vertices[2].y)
		p4=(self.forma.vertices[3].x, self.forma.vertices[3].y)
		p5=(self.forma.vertices[4].x, self.forma.vertices[4].y)
		
		self.cor = '#'
		rgb = ['00','22','44','66','88','aa','cc','dd','ff']
		self.cor += rgb[randint(0,8)]
		self.cor += rgb[randint(0,8)]
		self.cor += rgb[randint(0,8)]
		print('cor: {}'.format(self.cor))
		self.item_canvas = self.arena.create_polygon((p1,p2,p3,p4,p5) , fill=self.cor,tag='robo', outline='#000000')
		#self.forma = self.arena.type(self.item_canvas)

	def processa_teclado(self,evento):
		tecla = evento.char
		if tecla == 'w':
			vet_des = Ponto2D.rotaciona((Robo.DELTA,0), self.forma.ang, (0,0))
			#print("vetor deslocamento: {}".format(vet_des))
			self.move(vet_des)

		elif tecla == 's':
			vet_des = Ponto2D.rotaciona((-Robo.DELTA,0), self.forma.ang, (0,0))
			#print("vetor deslocamento: {}".format(vet_des))
			self.move(vet_des)

		elif tecla == 'q':
			vet_des = Ponto2D.rotaciona((0,-Robo.DELTA), self.forma.ang, (0,0))
			#print("vetor deslocamento: {}".format(vet_des))
			self.move(vet_des)

		elif tecla == 'e':
			vet_des = Ponto2D.rotaciona((0,Robo.DELTA), self.forma.ang, (0,0))
			#print("vetor deslocamento: {}".format(vet_des))
			self.move(vet_des)

		elif tecla == 'd':
			self.rotaciona(Robo.ALPHA)

		elif tecla == 'a':
			self.rotaciona(-Robo.ALPHA)

	def pos(self):
		bico = self.arena.coords(self.item_canvas)
		pos = Ponto2D.rotaciona((-RoboTipo2TK.l/2,0), self.forma.ang, (0,0))
		x = bico[0] + pos.x
		y = bico[1] + pos.y
		pos = Ponto2D(x,y)
		return pos

	def ang(self):
		return self.forma.ang

	def move(self,vet_des):
		if not self.colide():
			self.forma.move(vet_des)
			#print('cordenadas dos vertices do poligôno no canvas: {}'.format(self.forma.pos))
			self._move_forma()
			self.sensor._move_forma()
	
	def rotaciona(self,ang):
		self.forma.rotaciona(ang)
		#print('cordenadas x,y do poligôno no canvas: {}'.format(self.forma.pos))
		self._move_forma()
		self.sensor._move_forma()

	def _move_forma(self):
		p1=(self.forma.vertices[0].x , self.forma.vertices[0].y )
		p2=(self.forma.vertices[1].x , self.forma.vertices[1].y )
		p3=(self.forma.vertices[2].x , self.forma.vertices[2].y )
		p4=(self.forma.vertices[3].x , self.forma.vertices[3].y )
		p5=(self.forma.vertices[4].x , self.forma.vertices[4].y )
		self.arena.coords(self.item_canvas,[ p1[0], p1[1], p2[0], p2[1], p3[0], p3[1],p4[0],p4[1],p5[0],p5[1] ])

	def adiciona_sensor(self):
		sensor = SensorTipo2Tk()
		sensor.inicializa_sensor(self)
		sensor._inicializa_forma()
		self.sensor = sensor

	def colide(self):
		p1=(self.forma.vertices[0].x , self.forma.vertices[0].y )#bico do robo
		arenatk = self.arena
		itens = arenatk.find_overlapping(p1[0]+0.1, p1[1]+0.1,p1[0]-0.1, p1[1]-0.1)
		print(itens)
		for i in itens:
			#print(i)
			tag = arenatk.gettags(i)
			tag = tag[0] if len(tag)>0 else False
			#print('tags do ítem que colidiu: {}\n'.format(tag))
			if tag == 'preto':
				return True
		return False
	def __repr__(self):
		s = 'info robo:\n\n' 
		s += "nome: {}\ntipo:{}\nid:{}".format(self.nome,self.forma,self.item_canvas)
		return s
	
