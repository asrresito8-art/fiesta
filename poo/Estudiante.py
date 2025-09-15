class Estudiante:
    # constructor
    def __init__ (self, nombre, apellido_paterno, apellido_materno):
        self.nombre = nombre 
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.materias =[]

    def anexar_marteria(self,materia):
        self.materias.append(materia)

    def mostrar_calificaciones(self):
        for materia in self.materias:
            materia.mostrar_resultados()

    # toString representacion en texto de la clase
    def __str__(self):
        return  f" {self.nombre} {self.apellido_paterno}"