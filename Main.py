from Features.Auth import *
from Features.Menu import *
import tkinter

auth = Auth()
menu = Menu()

root = tkinter.Tk()
root.withdraw()
root.update()

name = auth.login(False,False)
menu.showMenu(name,False,root)
