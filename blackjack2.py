import tkinter as tk
from tkinter import *
import random
from PIL import Image,ImageTk

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
c.create_text(60,525,text=(f'YOU HAVE ${z}'),fill="black",font=('impact'))
c.create_text(800,525,text=(f"CURRENT BET ${y}"),fill="black",font=('impact'))





def getSprite(h,j):
    img = Image.open("Deck.png").convert("RGBA")
    xi = h*49
    yi = j*65
    img2 = img.crop([xi,yi,xi+49,yi+65])
    return ImageTk.PhotoImage(img2)



def results():
    if playertotal[0]>dealercards[0]:
        print("Player Wins!!")
        f = (int(bet[1])*2)
        money[1] = f+int(money[1])
        print(f'you now have-> ${money[1]}')
    if playertotal[0]<dealercards[0]:
         print("you lose!")
         money[1] = int(money[1]) - int(bet[1])
         print(f'you now have-> ${money[1]}')
         



def dealer():
     a = random.randint(16,21)
     print(f'the dealer has {a}')
     dealercards[0] = a
     results()
def blackjack():
    a=random.sample(numbers,k=1)
    b=random.sample(suits,k=1)
    for h in a:
         h=int(a[0])-1
         print(h)
    if b[0]=="clubs":
         j=0
    print(f"Your card is the {a[0]} of {b[0]}")
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
    image = tk.PhotoImage(file="Deck.png")
    deck=[]
    deck.append(getSprite(h,j))
    img = c.create_image(32,48,image=deck[0])
    
    
    print(f'Your total ->{playertotal}')
    if playertotal[0]>21:
        print("BUST!!!!!")
    z = input("hit or stay\n>")
    if z =="hit":
            blackjack()
    if z =="stay":
            dealer()
    return ImageTk.PhotoImage(img2)  

blackjack()






c.pack()
w.mainloop()