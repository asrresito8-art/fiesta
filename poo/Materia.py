
class Materia:
    def __init__ (self, nombre):
        self.nombre  = nombre
        self.horario =""
        self.temario =""
        self.calificaciones =[]

    def ingresar_calificaciones(self, numero1, numero2, numero3):
        self.calificaciones.append(numero1)
        self.calificaciones.append(numero2)
        self.calificaciones.append(numero3)
    
    def mostrar_resultados(self):
        for calif in self.calificaciones:
            print(calif, end="")
        print(f"promedio = {self.calcular_promedio()}")

    def calcular_promedio(self):
        resultado = 0
        for calif in self.calificaciones:
            resultado = resultado + calif
        resultado = resultado / len(self.calificaciones)
        return resultado
    def __str__(self):
        return ""
    