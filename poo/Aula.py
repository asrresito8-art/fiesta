
from blessed import Terminal

from Estudiante import Estudiante
from Materia import Materia

term= Terminal()

class Aula:
    def __init__ (self, nombre, grupo, ):
        self.nombre = nombre 
        self.grupo = grupo
        self.estudiantes =[]

    def inscribir_estudiantes(self, estudiante):
       self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
          print(f"{term.orange}--------Estudiantes escritos en el grupo"\
                 f"{self.grupo}------------------{term.normal}")
          for indice, estudiante in enumerate(self.estudiantes):
             print (f"{indice}.-{estudiante}")

    def __str__(self):
     return f"{term.bold_red}{self.grupo}{term.normal} "\
        f"ubicado en el {term.green}{self.nombre}{term.normal}"

def main():
    #print("Dentro de main")
    M7A = Aula("Laboratorio 3", "M7A")
    #print(f"M7A: {M7A}")

    paulina=Estudiante("Paulina", "Rubio", "Ramirez")
    jennifer=Estudiante("Jennifer", "Villareal", "Aparicio")
    
    M7A.inscribir_estudiantes(paulina)
    M7A.inscribir_estudiantes(jennifer)

    programacion = Materia("Programacion Avanzada")
    paulina.anexar_marteria(programacion)
    programacion.ingresar_calificaciones(30 , 25 , 10)

    M7A.mostrar_estudiantes()

    paulina.mostrar_calificaciones()

if __name__ == "__main__":
    main()
