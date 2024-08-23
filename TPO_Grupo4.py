import json

# Función para crear un espectáculo y agregarlo a la lista de espectáculos
def crear_espectaculo(espectaculos, nombre, fecha, hora, capacidad):
    espectaculo = {
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "capacidad": capacidad,
        "asientos": [[0 for _ in range(capacidad)] for _ in range(capacidad)]  # Matriz de asientos (0 = libre, 1 = ocupado)
    }
    espectaculos.append(espectaculo)
    print(f"Espectáculo '{nombre}' creado con éxito.")


# Función para mostrar todos los espectáculos disponibles
def mostrar_espectaculos(espectaculos):
    for i, espectaculo in enumerate(espectaculos):
        print(f"{i + 1}. {espectaculo['nombre']} - {espectaculo['fecha']} {espectaculo['hora']}")

# Función para vender una entrada, actualiza la matriz de asientos y registra la venta
def vender_entrada(espectaculos, espectaculo_id, fila, columna):
    try:
        espectaculo = espectaculos[espectaculo_id]
        if espectaculo['asientos'][fila][columna] == 0:
            espectaculo['asientos'][fila][columna] = 1
            print("Entrada vendida correctamente.")
        else:
            print("El asiento ya está ocupado.")
    except IndexError:
        print("El asiento no existe.")

# Función para mostrar los asientos disponibles de un espectáculo específico
def mostrar_asientos_disponibles(espectaculos, espectaculo_id):
    try:
        espectaculo = espectaculos[espectaculo_id]
        print("Asientos (0 = libre, 1 = ocupado):")
        for fila in espectaculo['asientos']:
            print(fila)
    except IndexError:
        print("Espectáculo no encontrado.")

# Función recursiva para buscar un espectáculo por nombre
def buscar_espectaculo_recursivo(espectaculos, nombre, indice=0):
    if indice >= len(espectaculos):
        return None
    if espectaculos[indice]['nombre'] == nombre:
        return indice
    return buscar_espectaculo_recursivo(espectaculos, nombre, indice + 1)

# Función para guardar los espectáculos en un archivo
def guardar_espectaculos(espectaculos, archivo="espectaculos.json"):
    with open(archivo, "w") as file:
        json.dump(espectaculos, file)
    print("Espectáculos guardados correctamente.")

# Función para cargar los espectáculos desde un archivo
def cargar_espectaculos(archivo="espectaculos.json"):
    try:
        with open(archivo, "r") as file:
            espectaculos = json.load(file)
        print("Espectáculos cargados correctamente.")
        return espectaculos
    except FileNotFoundError:
        print("No se encontró el archivo. Iniciando con una lista vacía.")
        return []

# Función principal
def main():
    espectaculos = cargar_espectaculos()

    while True:
        print("\nMenú:")
        print("1. Crear espectáculo")
        print("2. Mostrar espectáculos")
        print("3. Vender entrada")
        print("4. Mostrar asientos disponibles")
        print("5. Buscar espectáculo")
        print("6. Guardar y salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del espectáculo: ")
            fecha = input("Fecha (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")
            capacidad = int(input("Capacidad del estadio: "))
            crear_espectaculo(espectaculos, nombre, fecha, hora, capacidad)
        elif opcion == "2":
            mostrar_espectaculos(espectaculos)
        elif opcion == "3":
            mostrar_espectaculos(espectaculos)
            espectaculo_id = int(input("Seleccione el ID del espectáculo: ")) - 1
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))
            vender_entrada(espectaculos, espectaculo_id, fila, columna)
        elif opcion == "4":
            mostrar_espectaculos(espectaculos)
            espectaculo_id = int(input("Seleccione el ID del espectáculo: ")) - 1
            mostrar_asientos_disponibles(espectaculos, espectaculo_id)
        elif opcion == "5":
            nombre = input("Nombre del espectáculo a buscar: ")
            indice = buscar_espectaculo_recursivo(espectaculos, nombre)
            if indice is not None:
                print(f"Espectáculo encontrado en la posición: {indice + 1}")
            else:
                print("Espectáculo no encontrado.")
        elif opcion == "6":
            guardar_espectaculos(espectaculos)
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
