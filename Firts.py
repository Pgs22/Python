#fecha de entrega 12 octubre

#1 - Pregunta al usuario que introduzca el radio de un círculo y utiliza la fórmula del área (A = π * r^2) para calcular y mostrar el área.
#Math?? Buscar python documentation
# importamamos la libreria -->
import math
radio = (input("escribe radio"))
area = math.pi * math.pow(radio,2)
print("El area del circulo es", area)


#ejercicio 2: Utiliza la función input() para pedir al usuario 5 notas numéricas y muestra la nota media
#media = (nota1+nota2) / 5
for i in range(5): 
    print(i)

for i in range(1,10,2): #inicio + fin + saltade2en2
    print(i)

#ejercicio 3 (en lapagina12 documentacion de alexia)
#Pide al usuario dos palabras y muestra el número total de letras que ha escrito el usuario

#ejercicio 4: Pide al usuario una frase y dos letras. Utiliza la función replace para sustituir todas las instancias de la primera letra por la segunda a la frase.

#ejercicio 5: Pide al usuario que introduzca una cadena de texto y una palabra, y utiliza las funciones find y count para mostrar la primera ubicación de la palabra y cuántas veces aparece.

#ejercicio6:
# #Pide al usuario que introduzca su fecha de nacimiento en el formato DD/MM/AAAA y utiliza la función int para extraer y mostrar el año de nacimiento.
#pasos:pedir alusuario formato de fecha, (opcional) usando un while paraque cumpla si cumple elformato
#por ejemplo buscar posicion 3 y 6 si es una barra (opcional)
#siguiente paso:situarte en la posicion para extraer los datos,y luego imprimirlo


#El while nos permite hacer un else dentro,directamente añades el else cuando quieras

print("Hola DAW2")
#Para hacer operaciones tenemos que castear a integer, sino lo detecta como un texto
edad = int(input("Cuantos años tienes?")) #Nos guarda el valor por teclado en la variable edad
edadFutura = edad + 25
print ("Tengo ", edadFutura , " años.")