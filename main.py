import webbrowser
import tkinter as tk
from functools import partial

gui = tk.Tk()
gui.title("PyDesktopChess")
gui.geometry('400x600')
gui.configure(bg='#DDDDFF')
gui.resizable(0,0)

def start_chess(sec:str,add:str):
    webbrowser.open('https://www.chess.com/play/online/new?action=createLiveChallenge&base='+str(sec)+'&timeIncrement='+str(add))

title = tk.Label(gui,text='\nPyDesktopChess\nPress the button and start\nAuthor : NaoCoding\n------------------------------------------------',font=('Times New Roman',20),bg='#DDDDFF').pack()
title2 = tk.Label(gui,text='Bullet Chess',font=('Times New Roman',20),bg='#DDDDFF').pack()

bullet = tk.Button(gui,text="   1 Min Bullet Chess  ",font=('Times New Roman',15),command = partial(start_chess,60,0)).pack()
bullet2 = tk.Button(gui,text="1 / 1 Min Bullet Chess",font=('Times New Roman',15),command = partial(start_chess,60,1)).pack()



title3 = tk.Label(gui,text='------------------------------------------------\nBlitz Chess',font=('Times New Roman',20),bg='#DDDDFF').pack()

blitz = tk.Button(gui,text="   3 Min Blitz Chess   ",font=('Times New Roman',15),command = partial(start_chess,180,0)).pack()
blitz2 = tk.Button(gui,text="3 / 2 Min Blitz Chess ",font=('Times New Roman',15),command = partial(start_chess,180,2)).pack()

title4 = tk.Label(gui,text='------------------------------------------------\nRapid Chess',font=('Times New Roman',20),bg='#DDDDFF').pack()

blitz3 = tk.Button(gui,text="   10 Min Rapid Chess    ",font=('Times New Roman',15),command = partial(start_chess,600,0)).pack()
blitz4 = tk.Button(gui,text="15 / 10 Min Rapid Chess",font=('Times New Roman',15),command = partial(start_chess,900,10)).pack()



gui.mainloop()



