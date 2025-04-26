#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

numero1=int(input("Ingresa el numero1: "))
numero2=int(input("Ingresa el numero2: "))

if numero1>numero2:
    print("El numero1 es mayor que el numero2")
else:
    print("El numero2 es mayor que el numero1")
if numero2==numero1:
    print("Los dos numeros son iguales")
    