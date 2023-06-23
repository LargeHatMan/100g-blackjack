import tkinter as tk
from tkinter import *
import random
from PIL import Image,ImageTk
from tkinter import ttk
numbers=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
suits = ["clubs",'spades','hearts','dimonds']
money=[0]
bet = [0]
playertotal = [0]
dealercards=[0]


w = tk.Tk()
w.attributes('-topmost',True)
w.geometry("865x556")
card = PhotoImage(file = "card.png")
bg = PhotoImage(file = "bg.png")
c = tk.Canvas(width=860,height=555,background="#005b13",bd="2")
e1 =tk.Entry(w)
c.create_image(432,300,image=bg)
c.create_image(800,100,image=card)
c.create_text(420,40, text="Black jack!", fill="black", font=('Helvetica 15 bold'))
c.pack()



x=input("starting Money \n>")
y=input("Bet amount \n>")
z = int(x) -int(y)
money.append(z)
bet.append(y)
racks=c.create_text(60,525,text=(''),fill="black",font=('impact'))




def getSprite(h,j):
    img = Image.open("Deck.png").convert("RGBA")
    xi = h*49
    yi = j*65
    img2 = img.crop([xi,yi,xi+49,yi+65])
    return ImageTk.PhotoImage(img2)

def text():
     global racks
     c.delete(racks)
     racks=c.create_text(60,525,text=(f'YOU HAVE ${money[1]}'),fill="black",font=('impact'))
     bands=c.create_text(800,525,text=(f"CURRENT BET ${y}"),fill="black",font=('impact'))
def results():
    if playertotal[0]>dealercards[0]:
        print("Player Wins!!")
        f = (int(bet[1])*2)
        money[1] = f+int(money[1])
        print(f'you now have-> ${money[1]}')
        money.append(money[1])
        reset()
        text()
        

    if playertotal[0]<dealercards[0]:
         print("you lose!")
         money[1] = int(money[1]) - int(bet[1])
         print(f'you now have-> ${money[1]}')
         reset()
         text()
 

    
         
def reset():
     playertotal[0]=0
     dealercards[0]=0


def dealer():
     a = random.randint(16,23)
     print(f'the dealer has {a}')
     if a>21:
          print("the dealer BUSTED!")
          dealercards[0]=0
     else:
          dealercards[0] = a
     results()
def blackjack():
    a=random.sample(numbers,k=1)
    b=random.sample(suits,k=1)
    print(f"Your card is the {a[0]} of {b[0]}")
    h=0
    j=0
    if a[0] =="A":
         h=0
    if a[0] ==2:
         h=1
    if a[0] ==3:
         h=2
    if a[0] ==4:
         h=3
    if a[0] ==5:
         h=4
    if a[0] ==6:
         h=5
    if a[0] ==7:
         h=6
    if a[0] ==8:
         h=7
    if a[0] ==9:
         h=8
    if a[0] ==10:
         h=9
    if a[0] =="J":
         h=10
    if a[0] =="Q":
         h=11
    if a[0] =="K":
         h=12
    if b[0] == "clubs":
         j=0
    if b[0] == "dimonds":
         j=1
    if b[0] == "hearts":
         j=2
    if b[0] == "spades":
         j=3    
    if a[0] =="Q":
        a[0]=10
    if a[0] =="K":
        a[0]=10
    if a[0] =="J":
        a[0]=10
    if a[0] == "A":
        p=input("1 or 11?\n>")
        if p=="1":
            a[0]=1
        if p=="11":
            a[0]=11
    img = Image.open("Deck.png").convert("RGBA")
    xi = h*49
    yi = j*65
    img2 = img.crop([xi,yi,xi+49,yi+65])  
    playertotal[0]=(playertotal[0]+a[0])
    deck=[]
    deck.append(getSprite(h,j))
    img = c.create_image(400,500,image=deck[0])
    print(f'Your total ->{playertotal}')
    if playertotal[0]>21:
        print("BUST!!!!!")
        playertotal[0]=0
        print(f'Your total ->{playertotal}')
        dealer()
    hit = Button(w, text = "hit",command=blackjack,width=10,height=2)
    hit.place(x=500,y=450)
    stay = Button(w, text = "stay",command=dealer,width=10,height=2)
    stay.place(x=250,y=450)
    



text()
blackjack()


w.mainloop()