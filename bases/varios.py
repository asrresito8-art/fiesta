
def nuevoTema(tema):
  print(f"================== {tema} ============")

  #ESTO ES PARA GENERAR UNA MAQUINA DE JUGOS.
def menu():

     opcion = -1
     while not opcion ==0:
         
          print("======================================")
          print("bienvenido a esta tienda de frutas")
          print("=============================================")
          print("elige una opcion")
          print("1. juego de naranja")
          print("2. juego de guayaba")
          print("3. juego de zanhoria")
          print("4. juego de jugo de fresa")
          print("0. salir")
          print("elige una opcion")

          opcion = int (input())
          print(f"opcion elegida:{opcion}")
   
          evaluar_opcion_2(opcion)

def evaluar_opcion_1(opcion):
     if opcion==1:
               print("preparando jugo de naranja")
     elif opcion==2:
               print("prparando jugo de guayaba")
     elif opcion ==3:
               print("preparando un jugo de zahahoria")
     elif opcion ==4:
               print("preparando jugo de fresa")
     else:
          pass
     a = input()
def evaluar_opcion_2(opcion):
     match opcion:
          case 1:
               print("preparando jugo de naranja")
          case 2:
               print("prparando jugo de guayaba")
          case 3:
               print("preparando un jugo de zahahoria")
          case 4:
               print("preparando jugo de fresa")
          case _:
               pass
     a = input()

def factorial(numero):
     resultado =1
     if numero < 0:
           return"no se puede calcular el factorial"
     for i in range(1,numero + 1):
            resultado = resultado * i
     return resultado

