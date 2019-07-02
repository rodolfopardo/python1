numero = int(input("Ingrese el numero:"))
numero2 = int(input("Ingrese el segundo numero:"))
proceso = input("¿Desea sumar o restar?")

if proceso == "sumar":
      resultado = numero + numero2
      print("La suma es igual a:",resultado)
else:
      resultado = numero - numero2
      print("La resta es igual a:", resultado)


