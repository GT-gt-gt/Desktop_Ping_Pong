import tkinter
import threading
import os
import time

class window(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        creatwin(self.name)

def creatwin(name):
    win = tkinter.Tk()
    win.title(name)
    win.overrideredirect(True)
    win.mainloop()

player1 = window("player1")
player2 = window("player2")
ball = window("ball")

player1.start()
player2.start()
ball.start()

os.exit()