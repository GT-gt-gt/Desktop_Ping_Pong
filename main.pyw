import win32api
import win32con
import win32gui
import time
import threading
from pynput.keyboard import Key, Listener
import random

# function
def p_move(handle, x, y):
    win32gui.MoveWindow(handle, x, win32gui.GetWindowRect(handle)[1] + y, 30, 250, False)

def b_move(x, y):
    win32gui.MoveWindow(b_handle, win32gui.GetWindowRect(b_handle)[0] + x, win32gui.GetWindowRect(b_handle)[1] + y, 30, 30, False)

def b_reset():
    win32gui.MoveWindow(b_handle, 725, 400, 50, 50, False)

def on_press(key):
    try:
        if key.char == "w":
            p_move(p1_handle, 20, -50)
        elif key.char == "s":
            p_move(p1_handle, 20, 50)
        elif key.char == "i":
            p_move(p2_handle, 1470, -50)
        elif key.char == "k":
            p_move(p2_handle, 1470, 50)
    except:
        pass

def on_release(key):
    global flag
    if key == Key.esc:
        flag = False
        return False

def ball_movement():
    global direction
    corr = win32gui.GetWindowRect(b_handle)
    p1_corr = win32gui.GetWindowRect(p1_handle)
    p2_corr = win32gui.GetWindowRect(p2_handle)
    if corr[0] <= 50 and corr[1] >= p1_corr[1] and corr[1] <= p1_corr[1]+250:
        direction[0] -= random.randint(0, 1)
        direction[0] *= -1
    elif corr[0] >= 1440 and corr[1] >= p2_corr[1] and corr[1] <= p2_corr[1]+250:
        direction[0] += random.randint(0, 1)
        direction[0] *= -1
    elif corr[0] <= 50 or corr[0] >= 1440:
        b_reset()
        direction = [random.randint(8, 10), random.randint(8, 10)]
        time.sleep(1)
    if corr[1] <= 20 or corr[1] >= 740:
        direction[1] *= -1
    b_move(direction[0], direction[1])
    time.sleep(0.02)

# listener thread
class lthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
key_listener = lthread()

# creat windows
win32api.ShellExecute(0, "open", "creat.pyw", "", "", 1)
time.sleep(1)

# get handle
p1_handle = win32gui.FindWindow("TkTopLevel", "player1")
p2_handle = win32gui.FindWindow("TkTopLevel", "player2")
b_handle = win32gui.FindWindow("TkTopLevel", "ball")

# main
if p1_handle and p2_handle and b_handle:

    # set to original position
    win32gui.MoveWindow(p1_handle, 20, 200, 30, 250, False)
    win32gui.MoveWindow(p2_handle, 1470, 200, 30, 250, False)
    win32gui.MoveWindow(b_handle, 725, 400, 30, 30, False)

    flag = True
    key_listener.start()
    direction = [random.randint(5, 8), random.randint(5, 8)]
    while flag:
        ball_movement()

win32api.ShellExecute(0, "open", "clear.pyw", "", "", 1)