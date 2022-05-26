import subprocess as sp
import tkinter.messagebox
from tkinter import *
from random import randint
from pathlib import Path


diretorio = str(Path.home())
dir_arquivo = diretorio+str('\\Desktop\\Sorteio.txt')
dir_logo = 'logo.png'
bloco_notas = 'notepad.exe'


numeros = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
           [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
           [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
           [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]]


def gera_num():
    count = 1
    sorteio = []
    sorteio2 = ''
    jogos = entrada.get()
    if jogos.isnumeric():
        arquivo = open(dir_arquivo, 'a')
        jogos = int(jogos)
        for y in range(jogos):
            sorteio.clear()
            arquivo.write(f'Sorteio nº {count}:')
            arquivo.write('\n')
            count += 1
            for x in numeros:
                sorteio.append(randint(x[0], x[-1]))
                sorteio2 = str(sorteio)
            arquivo.write(sorteio2)
            arquivo.write('\n')
        arquivo.close()
        sp.Popen([bloco_notas, dir_arquivo])
    else:
        tkinter.messagebox.showinfo('Erro', 'Informar apenas números inteiros')


root = Tk()
root.geometry('220x180+400+300')
root.configure(background='#3CB371')
root.title('PySena')

fundo = PhotoImage(file=dir_logo)

fundo_label = Label(root, image=fundo)
fundo_label.place(x=0, y=0)

titulo = Label(root, text='Informe a quantidade de jogos')
titulo.configure(background='red')
titulo.place(x=20, y=120)

entrada = Entry(root, width=10)
entrada.place(x=20, y=152)

botao = Button(root, text='<Gerar Jogos>', command=gera_num)
botao.place(x=100, y=150)

texto = Label(root)
texto.place(x=80, y=180)

root.resizable(False, False)
root.mainloop()
