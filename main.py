from arena_tk import *

if __name__ == "__main__":
	p=5
	w=128*p
	h=90*p
	
	root = tk.Tk()
	root.title('Arena de Robos')
	root.geometry('{}x{}+300+200'.format(w,h))

	h=h-(h*0.1)
	
	arena = ArenaTK(root,'arenas/arena3.txt',w,h,p)
	arena.pack()

	# cria robôs/sensores

	#arena.adiciona_robo(r1)
	#arena.adiciona_robo(r2)

	#arena.ativa_controle_robo(r1.nome)

	root.mainloop()