from tkinter import *   # Importa o módulo tkinter
from tkinter import ttk # Importa o módulo ttk do tkinter, que possui widgets mais "modernos"

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()                     # Janela principal
root.title("Feet to Meters")    # Titulo da janela

mainframe = ttk.Frame(root, padding="3 3 12 12")        # Frame principal da janela
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))    # Cria o grid no frame principal, sticky é a "Âncora" que prende o frame as direções
mainframe.columnconfigure(0, weight=1)                  # Faz com que apenas o espaço vazio do frame mude de tamanho(para colunas)
mainframe.rowconfigure(0, weight=1)                     # Faz com que apenas o espaço vazio do frame mude de tamanho(para linhas)

feet = StringVar()   # Variável para armazenar o valor em pés entrado pelo usuário
meters = StringVar() # Variável para armazenar o valor em metros convertido pelo programa

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)   # Cria o widget para a entrada de texto, inserido no widget mainframe, com tamanho de 7 caracteres -
feet_entry.grid(column=2, row=1, sticky=(W, E))                 # - usando a variável "feet". Posiciona o widget na coluna 2, liinha 1, âncorado a esquerda e a direita

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))              # Widget responsável pelo label que mostra o resultado da variável "meters"
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)  #

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
