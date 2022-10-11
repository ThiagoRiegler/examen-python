from operator import indexOf


seleccion = 1
vec = []
while seleccion != 0:
    print("------------------------------------------------")
    print("0: Finalizar")
    print("1: Añadir un elemento al vector")
    print("2: Eliminar un elemento del vector")
    print("3: Buscar un numero ingresado por teclado")
    print("4: Ordenar ascendentemente el vector")
    print("5: Calcular el promedio del vector")
    print("6: Indicar el numero minimo y mayor")
    seleccion = int(input("Ingrese la opcion que desea realizar: "))

    if seleccion == 1:
        print("------------------------------------------------")
        num = int(input("Ingrese un numero para agregar: "))
        vec.append(num)
        print(vec)

    if seleccion == 2:
        print("------------------------------------------------")
        if(len(vec) != 0):
            num = int(input("Ingrese un numero para eliminar: "))
            if(vec.__contains__(num)):
                vec.remove(num)
                print(vec)
            else:
                print("No se encuentra el numero en el vector")
        else:
            print("El vector esta vacio")

    if seleccion == 3:
        print("------------------------------------------------")
        if(len(vec) != 0):
            num = int(input("Ingrese un numero para buscar: "))
            if(vec.__contains__(num)):
                i = vec.index(num)
                if(i > 0):
                    print(vec[i-1])
                print(vec[i])
                if(i < (len(vec)-1)):
                    print(vec[i+1])
            else:
                print("No se encuentra el numero en el vector")
        else:
            print("El vector esta vacio")

    if seleccion == 4:
        vec.sort()
        print(vec)

    if seleccion == 5:
        sum = 0
        i = 0
        j = 0
        for i in range(len(vec)):
            sum = sum + vec[i]
        prom = sum/len(vec)
        print("Promedio:", prom)
        
        for j in range(len(vec)):
            if vec[j] < prom:
                print("Menor que el promedio:", vec[j])
            elif vec[j] > prom:
                print("Mayor que el promedio:", vec[j])
            else:
                print("Igual que el promedio:", vec[j])
    
    if seleccion == 6:
        vec.sort()
        print("Numero menor:", vec[0])
        print("Numero mayor:", vec[len(vec)-1])