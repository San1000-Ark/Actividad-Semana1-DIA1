#Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).
anno=int(input("Ingresa un año: "))

if anno%4!=0:
    print("El año no es bisiesto")
elif anno%4==0:
        print("El año es bisiesto")
elif anno%100==0:
    print("El año es bisiesto")
elif anno%400==0:
    print("El año es bisiesto")


    

