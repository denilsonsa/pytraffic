import os
import sys
class dev_null:
    def write(self,s):
        pass

sys.stderr=dev_null()
sys.stdout=dev_null()
os.environ['LANG']='C'
from gi import pygtkcompat; pygtkcompat.enable(); pygtkcompat.enable_gtk(version="3.0"); import gtk
import Game
Game.Game()
gtk.main()
