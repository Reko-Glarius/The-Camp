"""
Nombre del Creador: Ricardo Aliste G. (Reko)
Fecha: 12/05/2016
Descripcion: Juego hecho en python con TKinter; estilo de de libro "Crea tu Propia Historia"
"""

from tkinter import *

def autor (root):
    archi=open('autor.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        Label(root,text= li[:-1],bg="goldenrod3").pack()
    archi.close()
""" Funciones en las que se lee el respectivo .txt para luego mostrar el texto en la ventana """
def a (t1):
    archi=open('a.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        Label(t1,text= li[:-1],bg="goldenrod3").pack()
    archi.close()
def aa (t2):
    archi=open('aa.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        Label(t2,text= li[:-1],bg="goldenrod3").pack()
    archi.close()
def ab (t3):
    archi=open('ab.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        Label(t3,text= li[:-1],bg="goldenrod3").pack()
    archi.close()
def aaa (t4):
    archi=open('aaa.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        Label(t4,text= li[:-1],bg="goldenrod3").pack()
    archi.close()
def aab (t5):
    archi=open('aab.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        Label(t5,text= li[:-1],bg="goldenrod3").pack()
    archi.close()
def aba (t6):
    archi=open('aba.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        Label(t6,text= li[:-1],bg="goldenrod3").pack()
    archi.close()
def abb (t7):
    archi=open('abb.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        Label(t7,text= li[:-1],bg="goldenrod3").pack()
    archi.close()

""" Configuracion de cada ventana creable """
def primera():
    t1 = Toplevel(root)
    t1.geometry('400x700')
    t1.config(bg="goldenrod3")
    t1.title("The Camp-DEMO 0.0.1")
    Label(t1,text=a(t1)).pack
    Button(t1,text="May",bg="goldenrod4", command= a1).pack()
    Button(t1,text="Lukas",bg="goldenrod4", command=a2).pack()
    t1.grab_set()
    root.withdraw()
def a1():
    t2 = Toplevel(root)
    t2.geometry('400x850')
    t2.config(bg="goldenrod3")
    t2.title("The Camp-DEMO 0.0.1")
    Label(t2,text=aa(t2)).pack
    Button(t2,text="Levantarse Rapido",bg="goldenrod4", command=a1a).pack()
    Button(t2,text="Levantarse Lento",bg="goldenrod4", command=a1b).pack()
    t2.grab_set()
def a2():
    t3 = Toplevel(root)
    t3.geometry('400x850')
    t3.config(bg="goldenrod3")
    t3.title("The Camp-DEMO 0.0.1")
    Label(t3,text=ab(t3)).pack
    Button(t3,text="Usar laLinerna en Ray",bg="goldenrod4", command=a2a).pack()
    Button(t3,text="Irse sin Ray",bg="goldenrod4", command=a2b).pack()
    t3.grab_set()
def a1a():
    t4 = Toplevel(root)
    t4.geometry('400x700')
    t4.config(bg="goldenrod3")
    t4.title("The Camp-DEMO 0.0.1")
    Label(t4,text=aaa(t4)).pack
    Button(t4,text="Salir",bg="goldenrod4", command=exit).pack()
    t4.grab_set()
def a1b():
    t5 = Toplevel(root)
    t5.geometry('400x900')
    t5.config(bg="goldenrod3")
    t5.title("The Camp-DEMO 0.0.1")
    Label(t5,text=aab(t5)).pack
    Button(t5,text="Salir",bg="goldenrod4", command=exit).pack()
    t5.grab_set()
def a2a():
    t6 = Toplevel(root)
    t6.geometry('400x700')
    t6.config(bg="goldenrod3")
    t6.title("The Camp-DEMO 0.0.1")
    Label(t6,text=aba(t6)).pack
    Button(t6,text="Salir",bg="goldenrod4", command=exit).pack()
    t6.grab_set()
def a2b():
    t7 = Toplevel(root)
    t7.geometry('400x700')
    t7.config(bg="goldenrod3")
    t7.title("The Camp-DEMO 0.0.1")
    Label(t7,text=abb(t7)).pack
    Button(t7,text="Salir",bg="goldenrod4", command=exit).pack()
    t7.grab_set()

""" Configuracion de la ventana inicial (Equivale al menu) """
root= Tk()
logo=PhotoImage(file="logo.png")
Label(image=logo).pack()
root.config(bg="goldenrod3")
root.title("The Camp-DEMO 0.0.1")
root.geometry("200x200")
Button(root, text="Nueva Partida",bg="goldenrod4", command=primera).pack()
Button(root, text="Salir",bg="goldenrod4", command=exit).pack()
Label(root, text=autor(root), bg="goldenrod3").pack()
root.mainloop()
