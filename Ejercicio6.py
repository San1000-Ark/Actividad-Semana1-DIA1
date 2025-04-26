#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número sec
secret_number=int(input("Adivina el numero: "))

if secret_number<28:
    print("INCORRECTO: El numero es mayor")
elif secret_number>28:
    print("INCORRECTO: El numero es menor") 
elif secret_number==28:
    print("CORRECTO: ADIVINASTE EL NUMERO")