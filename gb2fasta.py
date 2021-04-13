"""algorithm converting GenBank (full) file to fasta file"""

__authors__ = "Jules Garreau"
__contact__ = "jules.garreau00@gmail.com"
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__  = "10/02/21"

import tkinter

import functions as fct

screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("Genbank to Fasta Converter")

menubar = tkinter.Menu(screen)
menu1 = tkinter.Menu(menubar, tearoff=0)
menu1.add_command(label="Open", command=lambda : fct.openGBfile())
menubar.add_cascade(label="File", menu=menu1)

bouton1 = tkinter.Button(screen, text="Convert to Fasta as Full sequence",
          command=lambda : fct.gb2fasta(fct.gb))
bouton2 = tkinter.Button(screen, text = "Save as...",
          command=lambda : fct.savefile())

bouton1.pack()
bouton2.pack()
screen.config(menu=menubar)

screen.mainloop()
