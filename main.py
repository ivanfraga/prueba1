import numpy as np

matriz = np.zeros((100,100))
arreglo1= np.zeros(10)
rangoA= 10
rangoB= 100
print("Digite su nemero de cedula digito por digito")

for a in range (rangoA):
    arreglo1[a]= int(input("Digito "+str(a+1)+": "))

for b in range (rangoB):
    for c in range (rangoB):
        z=(c%10)
        matriz[b][c]=arreglo1[z]

print(matriz)


def sumColum (matriz):
    C=int(input("Digite la columna que quiere sumar: "))
    suma= 0
    for b in range (rangoB):
        for c in range (rangoB):
            if(c==(C-1)):
                suma += matriz[b][c]
    #print("La suma de esa columna es: "+str(suma))
    return suma


def sumfil(matriz):
    D=int(input("Digite la fila que quiere sumar: "))
    suma2 =0
    for b in range (rangoB):
        if(b==(D-1)):
            for c in range (rangoB):
                suma2 += matriz[b][c]

    #print("La suma de esa fila es: "+str(suma2))
    return suma2


def sumdiagons (matriz):
    diago1=0;
    suma3= 0
    for a in range (rangoB):
        for b in range (rangoB):
            if (b==diago1):
                suma3 += matriz[a][b]
        diago1 += 1

    diago2=99
    suma4= 0
    for a in range (rangoB):
        for b in range (rangoB):
            if (b==diago2):
                suma4 += matriz[a][b]
        diago2 -= 1
    sumat=suma3+suma4

    #print("la suma de las diagonales es: "+str(sumat))
    return sumat


def multicolum (matriz):
    C=int(input("Digite la columna que quiere multiplicar: "))
    suma5= 1
    for b in range (rangoB):
        for c in range (rangoB):
            if(c==(C-1)):
                suma5 *= matriz[b][c]
    #print("La multiplicación de esa columna es: "+str(suma5))
    return suma5


def multifil (matriz):
    D=int(input("Digite la fila que quiere multiplicar: "))
    suma2 =1
    for b in range (rangoB):
        if(b==(D-1)):
            for c in range (rangoB):
                suma2 *= matriz[b][c]

    #print("La multiplicación de esa fila es: "+str(suma2))
    return suma2


def multidiago (matriz):
    diago2=99
    suma4= 1
    for a in range (rangoB):
        for b in range (rangoB):
            if (b==diago2):
                suma4 *= matriz[a][b]
        diago2 -= 1

    #print("la multiplicación de la diagonal es: "+str(suma4))
    return suma4

print("Ejercicios a resolver\n")
opcion=1
while(opcion != 0):
    print("1.- Sumar los elementos de una determinada columna. ")
    print("2.- Sumar los elementos de una determinada fila")
    print("3.- Sumar los elementos de las diagonales")
    print("4.- Multiplicar los elementos de una determinada columna")
    print("5.- Multiplicar los elementos de una determinada fila")
    print("6.- Multiplicar los elementos de las diagonal")
    print("0.- Salir")

    opcion=int(input("Opcion: "))

    if(opcion == 1):
        print("La suma de esa columna es: " + str(sumColum(matriz)))
    elif(opcion == 2):
        print("La suma de esa fila es: "+str(sumfil(matriz)))
    elif(opcion == 3):
        print("la suma de las diagonales es: " + str(sumdiagons(matriz)))
    elif(opcion == 4):
        print("La multiplicación de esa columna es: " + str(multicolum(matriz)))
    elif(opcion == 5):
        print("La multiplicación de esa fila es: " + str(multifil(matriz)))
    elif(opcion == 6):
        print("la multiplicación de la diagonal es: " + str(multidiago(matriz)))
    elif (opcion == 0):
        print("Gracias")
