from Auth import *
from Menu import *

auth = Auth()
menu = Menu()

name = auth.login(False,False)
menu.showMenu(name,False)
