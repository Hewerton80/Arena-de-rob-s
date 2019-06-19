import tkinter as tk

def processa_teclado(ev):
    if ev.char == 'q':
        canvas.coords(item_poligono, [100,100,160,40,160,100])
    if ev.char == 'a':
        canvas.coords(item_poligono2, [300-100,300-40,300+100,300+40])

l = 400
a = 400

root = tk.Tk()
root.title('Exemplos Canvas')
root.geometry('500x500+100+100')
canvas = tk.Canvas(root, width=l, height=a, borderwidth=0, highlightthickness=0, bg='yellow')
canvas.pack()

# polígono
item_poligono = canvas.create_polygon((50,50), (80,20), (80,50) , fill='orange')
item_poligono2 = canvas.create_oval(300-50, 300-20, 300+50, 300+20, fill='cyan', outline='orange')

print(type(item_poligono))
# digite 'q' para aumentar o tamanho do polígono
canvas.bind('<Key>', processa_teclado)
canvas.focus_set()
root.mainloop()