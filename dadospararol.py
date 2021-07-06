#tirada de dados
import random #importa el modulo random para la funcion .randint
tot=0
n=int(input("Cuantos dados tiras:"))
d=int(input("Tipo de dado: "))
m=int(input("Modificador:"))
tot=0
if d==4 or d==6 or d==8 or d==10 or d==12 or d==20:#tipo de dados validos
    while n>0:
      n=n-1
      x=random.randint(1,d) #funcion random que da interger
      tot=tot+x+m #me da la suma de todos los x. no es necesario poner for in x
      print(x)
else:
      print("Elige 4,6,8,10,12,20")
print("Total:",tot)
