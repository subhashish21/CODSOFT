import random
def timepass(comp, me):
    if(comp==me):
        return None
    elif(comp == 'r'):
        if(me == 'p'):
            return True
        elif(me == 's'):
            return False    
    elif(comp == 'p'):
        if(me == 's'):
            return True
        elif(me == 'r'):
            return False
    elif(comp == 's'):
        if(me == 'r'):
            return True
        elif(me == 'p'):
            return False            


print("comp turn: rock(r), paper(p)  or scissor(s)? ")
rand = random.randint(1, 3)
if(rand==1):
    comp = 'r'
elif(rand==2):
    comp = 'p'
elif(rand==3):
    comp ='s'   

me = input("my turn: rock(r), paper(p) or scissor(s)? ")
a = timepass(comp, me)
print(f"computer chose {comp}")
print(f"you chose {me}")
if(a==None):
    print("the game is a tie")
elif(a):
    print("you win")   
else:
    print("you lose!!")   
