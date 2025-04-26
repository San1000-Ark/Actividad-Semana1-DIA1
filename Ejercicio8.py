#Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:

peso=float(input("Ingresa el peso de la persona: "))
altura=float(input("Ingresa la altura de la persona: "))

imc=peso/(altura**2)
print(imc)

def clasificacion_imc(imc):
    if imc< 18.5:
        return("Bajo peso")
    elif 18.5<= imc <25:
        return ("Peso normal")
    elif 25> imc <29.9:
        return ("Sobrepeso")
    elif imc >= 30:
        return("Obesidad")
    
print("El IMC de la persona es: "+ str(imc))
print("Clasificacion como persona con: "+ clasificacion_imc(imc))
