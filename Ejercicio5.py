#Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

cuenTotal=int(input("Ingresa la cuenta total de tu pedido: "))
print("Los porcentajes de propinas son:")
print("10%")
print("15%")
print("20%")
Porcentajes=int(input("Ingrese el porcentaje que quiere dar"))
propina=cuenTotal*(Porcentajes/100)
print(propina)

    
