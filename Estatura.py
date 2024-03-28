#El programa  evaluará estatura del usuario
#Si la estatura es menor que 160 cm print: Eres chaparrito
#Si la estatura está entre 160 cm y 175 cm print: Eres de estatura mediana
#Si la estatura es mayor a 175 cm imprimirá: Eres alto.
nombre=input("Escribe tu nombre: ")
estatura=int(input("Indica tu estatura: "))
if estatura<160:
    print(f'{nombre}, Eres chaparrito')
if estatura>=160 and estatura<175:
    print(f'{nombre}, Eres de estatura mediana')
else:
    print(f'{nombre}, Eres alto')