import tkinter as tk
from tkinter import *

w = tk.Tk()
w.attributes('-topmost',True)
w.geometry("865x556")
c = tk.Canvas(width=860,height=555,background="#005b13",bd="2")
def sex():
    print("sex")


b=Button(w,text="sex!",command=sex).pack()



c.pack()
w.mainloop()