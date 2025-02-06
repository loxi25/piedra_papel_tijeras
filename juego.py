print("seleccione un numero")

print("1. piedra")
print("2. papel")
print("3. tijeras")

n=input("selecciona el objeto que desees")
z=random(1.0,2.0,3.0)
if  n==z:
    r=empate
if  n==1 and z==2:
    r=perdiste
if  n==1 and z==3:
    r=ganaste
if  n==2 and z==3:
    r=perdiste
if  n==2 and z==1:
    r=ganaste
if  n==3 and z==2:
    r=ganaste
if  n==3 and z==1:
    r=perdiste
