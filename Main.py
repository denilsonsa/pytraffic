import extra_path
import os
import sys
os.environ['LANG']='C'
from gi import pygtkcompat; pygtkcompat.enable(); pygtkcompat.enable_gtk(version="3.0"); import gtk
import Game
Game.Game()
gtk.main()
