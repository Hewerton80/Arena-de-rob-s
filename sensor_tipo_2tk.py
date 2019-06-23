from itens_tk import *
from sensor import *
class SensorTipo2Tk(ItemTK,Sensor):

	r = 40
	def __init__(self):
		Sensor.__init__(self)
	def _inicializa_forma(self):
		pos = self.robo.pos()
		cor = self.robo.cor
		self.robo.sensor_id = self.robo.arena.create_oval(pos.x-SensorTipo2Tk.r, pos.y-SensorTipo2Tk.r, pos.x+SensorTipo2Tk.r, pos.y+SensorTipo2Tk.r)
		self.robo.arena.itemconfig(self.robo.sensor_id, outline=cor, width = 2,tag='sensor')

	def _move_forma(self):
		pos = self.robo.pos()
		self.robo.arena.coords(self.robo.sensor_id,[ pos.x-SensorTipo2Tk.r, pos.y-SensorTipo2Tk.r, pos.x+SensorTipo2Tk.r, pos.y+SensorTipo2Tk.r ])
		self.obtem_medicaotk()

	def inicializa_sensor(self, robo):
		self.robo = robo
		print('Sensor inicializado no robo {}'.format(self.robo.nome))

	def obtem_medicaotk(self):
		novas_celulas = []
		pos = self.robo.pos()
		arenatk = self.robo.arena
		itens = arenatk.find_enclosed(pos.x-SensorTipo2Tk.r, pos.y-SensorTipo2Tk.r, pos.x+SensorTipo2Tk.r, pos.y+SensorTipo2Tk.r)
		for i in itens:
			tag = arenatk.gettags(i)
			tag = tag[0] if len(tag)>0 else False
			
			if (tag == 'branco' or tag == 'preto') and i not in self.celulas_detec:
				self.celulas_detec.append(i)
				novas_celulas.append(i)


			elif (tag == 'robo') and i not in self.robos_detec:
				self.robos_detec.append(i)
				print(tag)
		self.exibe(novas_celulas)

	def obtem_medicao(self):
		self.oculta()
		self.exibe(self.celulas_detec)
		

	#mostra as celulas detectdas
	def exibe(self,novas_celulas):
		arenatk = self.robo.arena
		
		for i in novas_celulas:
			tag = arenatk.gettags(i)
			tag = tag[0] if len(tag)>0 else False
			if tag == 'branco' and i in self.celulas_detec:
				arenatk.itemconfig(i, fill='#ffffff')

			elif tag == 'preto' and i in self.celulas_detec:
				arenatk.itemconfig(i, fill='#000000')


	def oculta(self):
		arenatk = self.robo.arena
		todos_os_blocos = arenatk.find_withtag('bloco')
		todos_os_sensores = arenatk.find_withtag('sensor')
		#deixa todos os ítens cinzas
		for i in todos_os_blocos:
			arenatk.itemconfig(i, fill='#888888')
		#desliga todos os outros sensores
		for s in todos_os_sensores:
			if s != self.robo.sensor_id:
				self.robo.arena.itemconfig(s,state='hidden')






