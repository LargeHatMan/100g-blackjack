import random


numbers=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
suits = ["clubs",'spades','hearts','dimonds']

money=[0]
bet = [0]
playertotal = [0]
dealercards=[0]

x=input("starting Money \n>")
y=input("Bet amount \n>")
money.append(x)
bet.append(y)

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


    play = input("Would you like to play again?\n1=yes\n2=No\n>")
    if play=="1":
         playertotal[0]=0
         u = input("new bet \n>")
         bet[1]=int(u)
         blackjack()
    if play =="2":
         print("you where so close to winning it big time!")
         



def dealer():
     a = random.randint(16,21)
     print(f'the dealer has {a}')
     dealercards[0] = a
     results()
    
def blackjack():
    a=random.sample(numbers,k=1)
    b=random.sample(suits,k=1)
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
    playertotal[0]=(playertotal[0]+a[0])
    print(f'Your total ->{playertotal}')
    if playertotal[0]>21:
        print("BUST!!!!!")
    z = input("hit or stay\n>")
    if z =="hit":
            blackjack()
    if z =="stay":
            dealer()


blackjack()

