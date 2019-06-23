from arena_tk import *

if __name__ == "__main__":
	def apaga_campos():
		
		e_nome.delete(0, tk.END)
		e_x.delete(0, tk.END)
		e_y.delete(0, tk.END)
		e_ori.delete(0, tk.END)
		arena.focus_set()

	
	w=640# larguar da tela = 640
	h=600# altura da tela = 600
	p=int(w/64)
	
	root = tk.Tk()
	root.title('Arena de Robos')
	root.geometry('{}x{}+300+50'.format(w,h))
	h=h-(h*0.2)
	
	arena = ArenaTK(root,'arenas/arena3.txt',w,h,p)
	inf = tk.Label(root,textvariable=arena.info)
	inf.config(font=("Helvetica", 9),bd=10,bg='#ffffff',relief=tk.SUNKEN)

	e_nome = tk.Entry(root)
	nome = tk.Label(root,text='Nome:',font=("Helvetica", 9))

	e_x = tk.Entry(root)
	x = tk.Label(root,text='x:',font=("Helvetica", 9))

	e_y = tk.Entry(root)
	y = tk.Label(root,text='y:',font=("Helvetica", 9))
        
	e_ori = tk.Entry(root)
	ori = tk.Label(root,text='Orientação:',font=("Helvetica", 9))

	b = tk.Button(root,text='Adicionar robô')
	b.config(command= lambda: arena.cria_robo(e_nome.get(),e_x.get(),e_y.get(),e_ori.get()  ))
	


	arena.bind('<Button-1>', arena.ativa_controle_robo)
	
	arena.focus_set()
	arena.bind('<Key>', arena.processa_teclado)

	arena.grid(row=0,column=0,columnspan=6)
	inf.grid(row=1,column=0,columnspan=6,stick='e w')

	e_nome.grid(row=3,column=0)
	nome.grid(row=2,column=0)

	e_x.grid(row=3,column=1)
	x.grid(row=2,column=1)

	e_y.grid(row=3,column=2)
	y.grid(row=2,column=2)

	e_ori.grid(row=3,column=3)
	ori.grid(row=2,column=3)

	b.grid(row=4,column=0,columnspan=6, stick='n e w')




	root.mainloop()