from varios import nuevoTema, menu, factorial

print("hola mundo")
# esto es un comentario

"""
esto es un comentario
de
multiples lineas
"""



# ------------- variables -------------.

#tipos de variables.

nuevoTema("variables")

#int : variable entera.

numero = 6
print("numero:", numero)

# float : variable flotante.

temperatura = 22.7
print("temperatura:", temperatura)

# str : variable de nombres o palabras.

nombre = " ´johana de paz´ "
print("nombre:", nombre)

# bool : variable boleana.

fuma = True
print("fuma:", fuma)

# -------------operadores------------
nuevoTema("operadores")

nuevoTema("aritmeticos")

numero1 = 20
numero2 = 3
print("numero1:", numero1)
print("numero2:", numero2)
print("numero1 + numero2", numero1 + numero2)   # suma 
print("numero1 - numero2", numero1 - numero2)   # resta
print("numero1 * numero2", numero1 * numero2)   # multiplicacion
print("numero1 / numero2", numero1 / numero2)   # divicion
print("numero1 % numero2", numero1 % numero2)   # prcentaje 
print("numero1 ** numero2", numero1 ** numero2) # potencia

nuevoTema("logicos")

# Esta forma de escrivir el codigo es para cambiar la estructura.
# se llama string litera. ((f"{}}: {}"))
# SON IGUALDADES DEL SISTEMA BOLEANO (SIERTO O FALSO)
print(f"{numero1} > {numero2}: {numero1 > numero2}") # MENOR QUE 
print(f"{numero1} < {numero2}: {numero1 < numero2}") # MAYOR QUE
print(f"{numero1} >= {numero2}: {numero1 >= numero2}") # MENOR O IGUAL QUE
print(f"{numero1} <= {numero2}: {numero1 <= numero2}") # MAYOR O IGUAL QUE
print(f"{numero1} == {numero2}: {numero1 == numero2}") # IGUAL IGUAL QUE

# ------------- lista ------------
nuevoTema("lista")

frutas = ["kiwis", "manzanas", "melonoes", "limones", "piñas", "platanos", "naranjas"]
print("frutas: ", frutas)

varios = [23, 457.23, True, "adquiel", frutas]
print ("varios: ", varios)

print("frutas[3]:", frutas[3])           # iprime el 4to dato    
print("frutas[1:5]:", frutas[1:5])       # imprime de 2do al 5to dato
print("frutas[1:5:2]", frutas[1:5:2])    # imprime el 2do y el 3ro tercero

print("frutas[:4]", frutas[:4])          # imprime de 1ro al 3ro  
print("frutas[4:]", frutas[4:])          # imprime 4to asta que termine

print("tamaño de la lista ´len(frutas´:", len(frutas))
print("ultimo elemento de la lista ´frutas[len(frutas) -1]´:", len(frutas))

print(frutas[len(frutas) -1])
print("utimo elemento de la lista ´frutas[-1]´:", frutas[-1])
print("penultimo elemento de la lista ´frutas[-2]´:", frutas[-2])
print("antepenultimo elemento de la lista ´frutas[-3]´:", frutas[-3])
 
print("agregando un elemento a la lista")
print("frutas.append(´mangos´): ", frutas.append("mangos"))
print("frutas: ", frutas)

print("eliminandoi un elemento a la lista")
print("frutas.remove(´kiwis´): ", frutas.remove("kiwis"))
print("frutas:" , frutas)

print("ordenar la lista")
print("frutas.sort(): ", frutas.sort())
print("frutas: ", frutas)

print("invertir la lista")
print("frutas.reverse():", frutas.reverse())
print("frutas: ", frutas)

# ------------- instruciones de contro ------------
nuevoTema("instruciones de contro")

nuevoTema("---for")

for i in range(6):
    print(i)
    print(".----")
for i in range(3,6):
    print (i)
    print(".----")
for i in range(1,20,2): 
    print(i)

nuevoTema("con listas")

for  fruta in frutas: #UTILISAMOS FOR PARA HACER UNA LISTA
    print(frutas)
for indice, fruta in enumerate (frutas):
    print(f"{indice},- {frutas}")


nuevoTema("for de una sola linea")
[print(frutas) for frutas in frutas]


nuevoTema("con en continue")
for i in range (8):
     if i >2 and i <5:
          continue
     print(i)

nuevoTema("con en break")
for i in range (8):
     if i >2:
          break
     print(i)
nuevoTema("while")
menu()

# ------------- instruciones de celeccion ------------
nuevoTema("instruciones de de seleccion")
nuevoTema("if-else")

entrego_proyecto= True
el_proyecto_funciona= True
calificacion = 30
if calificacion >= 70:
    print(f"el alumno esta reprobado su calificacion fue {calificacion} :(")
else:
        if entrego_proyecto and el_proyecto_funciona:
            print("puede que pase")
        else:
            print(f" El alumno esta reprobado su calificacion fue {calificacion}:)")

valor= []

if not 0:
     print("la condicion es falsa")

if not False:
     print("la condicion es falsa")

if not None:
     print("la condicion es falsa")

if not []:
     print("la condicion es falsa con Lista vacia")

nuevoTema("funcion")
numero=-1
resultado =factorial(numero)
print(F"El factorial de {numero} es: {resultado}")

#=====DICCIONARIO
nuevoTema("Diccionario")

persona={
     'nombre':'Jose Luis',
     'edad':22,
     'fuma': True,
     'estructura': 1.80,
     'hobbies':['Toma', 'Leer', 'Pintar']
}

print('---Accediendo a los elementos de un diccionario')
print('persina:', persona)
print('persona.get("nombre"):', persona.get("nombre"))          
# NO OCUPAR ESTA FORMA DE AXEDER A OBJETOS.
#print('persona.get("nombre"):', persona.get¨["nombre"]) 

print("---Accediendo a las claves")
print('persona.kkeys():', persona.keys())

print("---Accediendo a los valores")
print('persona.values():', persona.values())

print("---Accediendo a elementos")
print('persona.items():', persona.items())

print("---Accediendo a clase valor")
for clave, valor in persona.items():
     print(f"{clave}: {valor}")

print("---Modificando valores")
persona.update({'nombre':'Jose Luis'}) #cupdate on un update modificamos el contenido
print(persona)

print("---Obtener un valor y borrar la clave")
result = persona.pop('nombre')  #pop 
print(persona)


print("---Borrando el contenido")
persona.clear() # borramos el contenido 
print(persona)