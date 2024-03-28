#Convertiremos de metros a kilómetros y a centímetros
#Segun solicite el usuario

distancia=float(input('Escriba la cantidad en metros: '))
opcion=input('\n A qué unidad quieres convertir?'
             '\n a. Convertir a kilómetros'
             '\n b. Convertir a centímetros' 
             '\n c. Convertir a metros \n')

if opcion=='a':
    total=distancia/1000
    print('La cantidad convertidad en kilómetros es: ',total)
elif opcion=='b':
    total=distancia*100
    print('La cantidad convertida en centímetro', total)
elif opcion=='c':
    total=distancia*1
    print('La cantidad convertida en metros', total)
else:
    print('Opcion no válida')