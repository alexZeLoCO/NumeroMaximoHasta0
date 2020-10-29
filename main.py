n=int(input("Introduzca un número: "))      #SOLICITA VALOR
max = n     #INICIALIZA MAYOR (EL PRIMERO SIEMPRE ES MAYOR)
if n ==0:       #SI EL PRIMERO ES 0
    print("Ningún número diferente a 0 se ha introducido.")
            #OUTPUT
else:       #SI NO
    while n!=0:     #MIENTRAS N NO SEA 0
        n=int(input("Introduzca un número: "))      #SOLICITA NÚMERO
        if n>max and n!=0:      #SI EL NÚMERO NO ES 0 Y ES MAYOR AL MAYOR
            max = n     #ACTUALIZAR MAYOR

        #OUTPUT
    print ("El mayor número introducido fue el:",max)