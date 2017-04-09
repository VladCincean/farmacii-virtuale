from controller import Controller
from UI import UI

file = input("Filename: ")
try:
    ctrl = Controller(file)
    ui = UI(ctrl)
#     a, b = ctrl.getWalk(0,1)
#     print(a)
#     print(b)
    ui.run()
except IOError as ioe:
    print("IOError: " + str(ioe))
    