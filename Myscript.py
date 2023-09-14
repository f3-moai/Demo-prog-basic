#-Declaracion y condiciones-
#a = 9
#b = 8
#c = "Edad"
#if a != b or a > b:
#    print("Condicion cumplida, numero:  " + str(b))
#else:
#    print("NO SE CUMPLIO LA CONDICIÓN, numero:  " + str(a))

#-Repetitivas-
#i = 0
#while i < 5:
#    print("Hola")
#    i += 1

#-Funciones-
#def miFuncion():
#    nombre = "David"
#    return "Hola " + nombre + "!"
    
#resultado = miFuncion()
#print(resultado) 

#def suma(numero1,numero2):
#    return numero1 + numero2

#resultado = suma(15, 5)
#print(resultado)

#-Listas-
#miLista = [3,"Hola",True]
#miLista[2] = ":V"
#print(miLista[2])
#miLista2 = [1,2,3,4,5,6,7]
#indice = 0
#for elemento in miLista2:
#    miLista2[indice] += 5
#    indice += 1
#print(miLista2)

def delvorverPositivos(arreglo):
    positivos = []
    for elem in arreglo:
        if elem > 0:
            positivos.append(elem)
    return positivos
    
Resultado = delvorverPositivos([-5,-6,-5,-80,100])
print(Resultado)