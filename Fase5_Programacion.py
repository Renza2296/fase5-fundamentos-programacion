
# ==========================================
# FASE 5 - FUNDAMENTOS DE PROGRAMACIÓN
# Problema 5 - Control de Horas Trabajadas
# ==========================================

# Función para calcular el total de horas
def calcular_total_horas(horas):
    total = sum(horas)
    return total


# Función para clasificar la jornada laboral
def clasificar_jornada(total_horas):
    if total_horas > 40:
        return "Sobretiempo"
    else:
        return "Horario Estándar"


# Matriz con nombre del recurso y horas trabajadas
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

matriz_recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 8, 8, 7],
    ["Luis", 10, 9, 9, 8, 10],
    ["María", 8, 8, 8, 8, 8]
]

print("==============================================")
print(" CONTROL DE HORAS TRABAJADAS SEMANALES ")
print("==============================================\n")

# Recorrer la matriz
for recurso in matriz_recursos:

    nombre = recurso[0]
    horas = recurso[1:]

    # Calcular total de horas
    total_horas = calcular_total_horas(horas)

    # Clasificar jornada
    clasificacion = clasificar_jornada(total_horas)

    # Mostrar resultados
    print(f"Recurso: {nombre}")
    print(f"Total de horas trabajadas: {total_horas}")

    print(f"Clasificación: {clasificacion}")
    print("----------------------------------------------")