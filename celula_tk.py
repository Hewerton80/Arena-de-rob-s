from itens_tk import *

class CelulaTK(ItemTK):
	def __init__(self,pos,tam,detectada,livre):
		self.pos = pos
		self.tam = tam
		self.detectada = detectada
		self.livre = livre
	
	def _inicializa_forma(self):
		x1=self.pos[0]*self.tam
		y1=self.pos[1]*self.tam
		x2=x1+self.tam
		y2=y1+self.tam
	
		cor = '#ffffff' if self.livre else '#000000'
		bloco = 'branco' if self.livre else 'preto'
		self.item_canvas = self.arena.create_rectangle(x1, y1, x2, y2,width=0, fill="#888888",tag=(bloco,'bloco'))
		#self.oculta()

	def _move_forma(self, delta):
		pass


