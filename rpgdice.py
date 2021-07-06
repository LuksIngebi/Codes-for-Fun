#throw dice
import random #import random module .randint
tot=0
n=int(input("How many dice:"))
d=int(input("Kind of dice: "))
m=int(input("Modifier:"))
tot=0
if d==4 or d==6 or d==8 or d==10 or d==12 or d==20:#valid dice
    while n>0:
      n=n-1
      x=random.randint(1,d) #random fucntion for integer
      tot=tot+x+m #total value
      print(x)
else:
      print("Chose 4,6,8,10,12,20")
print("Total:",tot)
