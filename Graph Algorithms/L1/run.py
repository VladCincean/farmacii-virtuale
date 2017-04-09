'''
Created on 19 mar. 2016

@author: Vlad
'''
from controller import Controller
from UI import UI

while True:
    fName = input("filename: ")
    try:
        ctrl = Controller(fName)
        ui = UI(ctrl)
        ui.run()
        #print(str(ctrl.graph()))
        break
        
    except IOError:
        print("Error! Cannot open file.")
        