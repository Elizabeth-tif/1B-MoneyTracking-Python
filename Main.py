from User import *
from Menu import *

auth = User()
menu = Menu()

name = auth.login(False,False)
menu.showMenu(name,False)
