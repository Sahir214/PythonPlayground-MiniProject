# Stone , Paper , Scissor game  

import random

No=random.randint(1,3)
if No==1:
    bot = "s "
elif No==2:
    bot = "p"
else :
    bot = "c"  
      
you=input("Your Turn: (Choose any of this:Stone(s)/paper(p)/scissor(c))\t")
def game(bot,you):
    if bot==you:
       return None
    elif bot=="s":
        if you== "c":
            return False
        else :
            return True
    elif bot=="p":
        if you== "s":
            return False
        else :
            return True            
    elif bot=="c":
        if you== "p":
            return False
        else :
            return True
a=game(bot,you)
print(f"Bot chosen:\t {bot}")
print(f"You chosen:\t {you}")

if a==None:
    print("Match is Tie!")
elif a==True :
    print("You win this Match !")
else :
    print("Sorry! try Again , You Loose!")        
