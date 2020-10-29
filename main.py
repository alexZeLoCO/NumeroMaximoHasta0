n=int(input("Introduzca un número: "))      #SOLICITA VALOR
max = n     #INICIALIZA MAYOR (EL PRIMERO SIEMPRE ES MAYOR)
contador = 1        #ALMACENARÁ LA POSICIÓN DEL NÚMERO EN LA SUCESIÓN

if n ==0:       #SI EL PRIMERO ES 0
    print("Ningún número diferente a 0 se ha introducido.")
            #OUTPUT
else:       #SI NO
    while n!=0:     #MIENTRAS N NO SEA 0
        contador=contador+1     #ACTUALIZA POSICIÓN VALOR
        n=int(input("Introduzca un número: "))      #SOLICITA NÚMERO
        if n>max and n!=0:      #SI EL NÚMERO NO ES 0 Y ES MAYOR AL MAYOR
            contadormax = contador     #ALMACENA POSICIÓN DE VALOR MÁXIMO
            max = n     #ACTUALIZAR MAYOR

        #OUTPUT
    print ("El mayor número introducido fue el:",max,". En posición:",contadormax)