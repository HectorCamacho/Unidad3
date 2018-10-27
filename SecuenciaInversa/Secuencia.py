pila = []

print("Ingresa 5 caracteres:")

digite0= input(pila.append(" "))
digite1= input(pila.append(" "))
digite2= input(pila.append(" "))
digite3= input(pila.append(" "))
digite4= input(pila.append(" "))

pila.append(digite0)
pila.append(digite1)
pila.append(digite2)
pila.append(digite3)
pila.append(digite4)

print ("Mensaje Normal:",pila)
Mensaje = ""

while (len(pila)>0):
    Mensaje+=pila.pop()

print("Mensaje Inverso",Mensaje)