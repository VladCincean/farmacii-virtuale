'''
Created on 8 mai 2016

@author: Vlad
'''
from controller import Controller
from ui import UI

ctrl = Controller()
ui = UI(ctrl)
ui.run()
