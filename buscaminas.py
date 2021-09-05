from random import randint
import sys

buscaminas=[]
buscaminas2=([[0.0,0.1,0.2,0.3,0.4],[1.0,1.1,1.2,1.3,1.4],[2.0,2.1,2.2,2.3,2.4],[3.0,3.1,3.2,3.3,3.4],[4.0,4.1,4.2,4.3,4.4]])
ceros=0
aciertos=0
x=0
y=0
print("\t\t\t****Buscaminas****")

print("REGLAS:\n** 1 = mina\n** 0 = safe\n** SOLO CUENTA CON UNA OPORTUNIDAD!\n** En caso de acertar el espacio se convertira en mina para evitar volverla a usar\n** Tiene que completar el numeroo de aciertos")

for i in range(5):
    buscaminas.append([0]*5)

for f in range(5):
    for c in range(5):
        buscaminas[f][c]=randint(0, 1)
print("\n\nEstas son las cordenadas de las posiciones para el buscaminas:\n")
for k in range(len(buscaminas2)):
    print(buscaminas2[k])

buscaminas2=buscaminas

for f in range(5):
    for c in range(5):
        if buscaminas[f][c]==0:
            ceros=ceros+1
print("\nNumero de aciertos: ",ceros)

while aciertos!=ceros:
    f=int(input("Ingrese la coordenada para la Fila [0-4]: "))
    c=int(input("Ingrese la coordenada para la Columna [0-4]: "))
    
    if buscaminas[f][c]==1:
        print("Perdiste!")
        print("Esta fue la matriz: \n")
        
        for x in range(len(buscaminas)):
            print(buscaminas[x])
            
        sys.exit()
    else:
        aciertos=aciertos+1

        buscaminas2[f][c]=1
print("Felicidades, ganaste!")
