from tkinter import *

class Paint:
	pass

def desenha_livremente(evento):
	if acao.get() == 'Desenho livre':
		print('Mouse em {}, {}'.format(evento.x, evento.y,end=' | '))
		raio = 3
		canvas.create_oval(evento.x-raio, evento.y-raio, evento.x+raio, evento.y+raio, fill='#000000')

def preenche(evento):
	if acao.get() == 'Preenche':
		print('Mouse em {}, {}'.format(evento.x, evento.y,end=' | '))
		canvas = evento.widget
		item = canvas.find_overlapping(evento.x+1, evento.y+1,evento.x-1, evento.y-1)
		print(item)
		if len(item) == 0:
			canvas.config( bg='#00ff00')
		elif len(item) == 1:
			if canvas.type(item) == 'line':
				canvas.itemconfig(item, fill='#ff5500')
			else:
				canvas.itemconfig(item, fill='#ff0000',outline='#ff0000')
		elif len(item) > 1:
			for i in item:
				if canvas.type(item) == 'line':
					canvas.itemconfig(i, fill='#ff00ff')
				else:
					canvas.itemconfig(i, fill='#ff0000',outline='#ff0000')

def recebeCordPont(evento):
	if acao.get() == 'Desenha linha':
		print('Mouse em {}, {}'.format(evento.x, evento.y,end=' | '))
		if px1.get() == 0 and py1.get() == 0:
			px1.set(evento.x)
			py1.set(evento.y)
		elif px2.get() == 0 and py2.get() == 0:
			px2.set(evento.x)
			py2.set(evento.y)
			fazLinha()

def fazLinha():
	canvas.create_line(px1.get(), py1.get(),px2.get() , py2.get(),fill='#0000ff',width=3)
	px1.set(0)
	py1.set(0)
	px2.set(0)
	py2.set(0)

def mudaAcao(action):
	print('ação: {}'.format(action))

	l = Label(root, textvar=acaoText)
	acaoText.set('Ação: {}'.format(action))
	l.grid(row=31,column=1)
	acao.set(action)

	if action == 'Limpa tela':
		limpaTela()

def escolheEvento(evento):


	if acao.get() == 'Preenche':
		preenche(evento)
	elif acao.get() == 'Desenha linha':

		recebeCordPont(evento)
	elif acao.get() == 'Seleciona item':
		selecionaItem(evento)


def mostraCords(evento):
	#print('Mouse em {}, {}'.format(evento.x, evento.y,end=' | '))
	l = Label(root, textvar=cords)
	cords.set(' Posição: {}, {}px  '.format(evento.x, evento.y))
	l.grid(row=31,column=0)

def selecionaItem(evento):
	item = canvas.find_overlapping(evento.x+1, evento.y+1,evento.x-1, evento.y-1)
	
	l = Label(root, textvar=itemText)
	if len(item)  > 0:
		i = item[len(item)-1]
		itemText.set('Item: {}'.format(canvas.type(i)))
	else:
		itemText.set('Item:')
	l.grid(row=31,column=2)

def limpaTela():
	canvas.delete(ALL)
	canvas.config(bg='#ffffff')


root = Tk()
root.title('Projeto de Paint')
root.geometry('500x500+100+100')

px1=IntVar()
py1=IntVar()
px2=IntVar()
py2=IntVar()
w=380
h=460

v=IntVar()
cords=StringVar()
acao = StringVar()
acaoText = StringVar()
itemText = StringVar()

r1 = Radiobutton(root, text="Desenho livre",variable=v, value=1, justify=LEFT)
r2 = Radiobutton(root, text="Preenche", variable=v,value=2, justify=LEFT)
r3 = Radiobutton(root, text="Desenha linha", variable=v,value=3, justify=LEFT)
r4 = Radiobutton(root, text="Seleciona item", variable=v,value=4, justify=LEFT)
r5 = Radiobutton(root, text="Limpa tela", variable=v,value=5, justify=LEFT)

r1.config(command=lambda:mudaAcao('Desenho livre'))
r2.config(command=lambda:mudaAcao('Preenche'))
r3.config(command=lambda:mudaAcao('Desenha linha'))
r4.config(command=lambda:mudaAcao('Seleciona item'))
r5.config(command=lambda:mudaAcao('Limpa tela'))

r1.grid(row=0,column=5)
r2.grid(row=1,column=5)
r3.grid(row=2,column=5)
r4.grid(row=3,column=5)
r5.grid(row=4,column=5)


canvas = Canvas(root, width=w, height=h, borderwidth=0, highlightthickness=0, bg='#ffffff')
canvas.create_oval(300-50, 300-20, 300+50, 300+20, fill='cyan',outline='#ffffff')
canvas.create_oval(100-20, 300-70, 100+20, 300+70, fill='#ff00ff', outline='#ffffff')
canvas.create_polygon((50,50), (110,35), (150,200) , fill='orange')

canvas.bind('<Motion>', mostraCords)
canvas.bind('<B1-Motion>', desenha_livremente)
canvas.bind('<Button-1>', escolheEvento)


canvas.grid(row=0,column=0,columnspan=5, rowspan=15 )



root.mainloop()