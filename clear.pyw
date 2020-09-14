import win32gui
import win32con

p1_handle = win32gui.FindWindow("TkTopLevel", "player1")
p2_handle = win32gui.FindWindow("TkTopLevel", "player2")
b_handle = win32gui.FindWindow("TkTopLevel", "ball")
win32gui.PostMessage(p1_handle,win32con.WM_CLOSE,0,0)
win32gui.PostMessage(p2_handle,win32con.WM_CLOSE,0,0)
win32gui.PostMessage(b_handle,win32con.WM_CLOSE,0,0)