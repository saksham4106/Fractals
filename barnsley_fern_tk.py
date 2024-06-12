from tkinter import *
import random
import time
import threading
import numpy.matlib
import numpy as np


class point:
    def __init__(self, x, y) -> None:
        self.x = (x+5) * 50
        self.y = (10-y) * 50
        self.draw()


    def draw(self):
        print(self.x, self.y)
        c.create_oval(self.x, self.y, self.x + 2, self.y + 2, fill = "white", outline = "")
    

def generatePoints():
    x = 0
    y = 0
    xn = 0
    yn = 0
    for i in range(100000):
        r = random.randint(1,100)
        if r <= 1:
            xn = 0
            yn = 0.16 * y
        if 1 <= r <= 86:
            xn = 0.85 * x + 0.04 * y
            yn = -0.04 * x + 0.85 * y + 1.6
        if 86 <= r <= 93:
            xn = 0.2 * x - 0.26 * y
            yn = 0.23 * x + 0.22 * y + 1.6
        if 93 <= r <= 100:
            xn = -0.15 * x + 0.28 * y
            yn = 0.26 * x + 0.24 * y + 0.44

        x = xn
        y = yn

        #time.sleep(0.1)
win = Tk()
c = Canvas(win, width = 500, height = 500)
c.pack()

thread1 = threading.Thread(target=generatePoints)
thread1.start()

win.mainloop()
