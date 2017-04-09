from controller import Controller
from UI import UI

file = input("Filename: ")
try:
    ctrl = Controller(file)
    ui = UI(ctrl)
    ui.run()
except IOError as ioe:
    print("IOError: " + str(ioe))
    