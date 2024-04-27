class Estudiante:
    def init(self, nombre, edad, nota):
        self.nombre=nombre
        self.edad=edad
        self.nota=nota
    def calcular_promedio(calificaciones):
        return sum(calificaciones) / len(calificaciones)
    nombre=input("Digite su nombre: ")
    edad=input("Digite su edad: ")
    Estudiante=(nombre, edad)
    
    def nota_mayor(calificaciones):
        return max(calificaciones)
    
    calificaciones = []
    continuar = 's'
    while continuar.lower() == 's':
        nota = int(input("Ingrese una calificación: "))
        calificaciones.append(nota)
        continuar = input("¿Desea ingresar otra calificación? (s/n): ")
    
    promedio = calcular_promedio(calificaciones)
    mayor = nota_mayor(calificaciones)
    
    print(f"La nota promedio es: {promedio}.")
    print(f"La nota mayor es: {mayor}.")
    
    print(f"Su nombre es {nombre} tiene {edad} años y la nota promedio esta en {promedio}.")
    
    if promedio >= 40:
        print("El estudiante pasa la materia.")
    else:
        print("El estudiante no pasa la materia.")