import tkinter as tk
from PIL import Image,ImageTk

#settings:
x = 0 # Sprite Sheet Column (0-3)
y = 3 # Sprite Sheet Row (0-7)

w = tk.Tk()
w.attributes("-topmost",True)
w.geometry("400x300")

c = tk.Canvas(width=380,height=280)
c.pack()
i=0
def getSprite(x,y):
    img = Image.open("Deck.png").convert("RGBA")
    xi = x*50
    yi = y*65
    img2 = img.crop([xi,yi,xi+50,yi+65])
    return ImageTk.PhotoImage(img2)    
image = tk.PhotoImage(file="Deck.png")
deck=[]
deck.append( getSprite(x,y))
img = c.create_image(32,48,image=deck[0])

w.mainloop()