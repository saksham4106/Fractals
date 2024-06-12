from tkinter import *
import random
import time
import threading

class point:
    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y
        self.point()

    def point(self):
        c.create_oval(self.x, self.y, self.x + 2, self.y + 2, fill = "white", outline = "")


def generatePoints():
    init_v = point(250, 250)
    for i in range(10000000):
        dest = vertices[random.randint(0, 2)]
        new_v = point((init_v.x + dest.x) / 2,(init_v.y + dest.y)  /2)
        init_v = new_v
        #time.sleep(0.1)
win = Tk()
c = Canvas(win, width = 500, height = 500)
c.pack()
#250,50  100,350,   400,350
v1 = point(250, 50)
v2 = point(100,350)
v3 = point(400,350)

vertices = [v1, v2, v3]

thread1 = threading.Thread(target=generatePoints)
thread1.start()

win.mainloop()
