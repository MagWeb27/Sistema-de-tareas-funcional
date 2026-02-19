import json
import os

# Configuración del archivo de persistencia
NOMBRE_ARCHIVO = "tareas.json"

def cargar_datos():
    """Carga las tareas desde el archivo JSON si existe."""
    if os.path.exists(NOMBRE_ARCHIVO):
        try:
            with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def guardar_datos(tasks):
    """Guarda la lista de tareas actual en el archivo JSON."""
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def obtener_siguiente_id(tasks):
    """Calcula el siguiente ID basado en el máximo actual para evitar duplicados."""
    if not tasks:
        return 1
    return max(tarea["id"] for tarea in tasks) + 1

def agregar_tarea(tasks):
    titulo = input("Ingresa el título de la tarea: ")
    if not titulo.strip():
        print("Error: El título no puede estar vacío.")
        return

    tarea = {
        "id": obtener_siguiente_id(tasks),
        "title": titulo,
        "completed": False
    }
    tasks.append(tarea)
    guardar_datos(tasks)
    print(f"Tarea '{titulo}' agregada con éxito.")

def mostrar_tareas(tasks):
    if not tasks:
        print("\nNo hay tareas registradas.")
    else:
        print(f"\n{'ID':<5} {'TITULO':<50} {'ESTADO':<12}")
        print("-" * 50)
        for tarea in tasks:
            estado = "Completada" if tarea["completed"] else "Pendiente"
            print(f"{tarea['id']:<5} {tarea['title']:<50} {estado:<12}")
    print()

def actualizar_tarea(tasks):
    try:
        id_ingresado = int(input("Ingresa el ID de la tarea a completar/pendiente: "))
        for tarea in tasks:
            if tarea["id"] == id_ingresado:
                tarea["completed"] = not tarea["completed"]
                guardar_datos(tasks)
                print("Estado actualizado correctamente.")
                return
        print("La tarea no se encontró.")
    except ValueError:
        print("Error: Debes ingresar un número entero.")

def editar_tarea(tasks):
    try:
        id_ingresado = int(input("Ingresa el ID de la tarea que deseas editar el nombre: "))
        for tarea in tasks:
            if tarea["id"] == id_ingresado:
                nuevo_titulo = input("Ingresa el nuevo nombre de la tarea: ")
                tarea["title"] = nuevo_titulo
                guardar_datos(tasks)
                print("Nombre actualizado correctamente.")
                return
        print("La tarea no se encontró.")
    except ValueError:
        print("Error: Debes ingresar un número entero.")

def eliminar_tarea(tasks):
    try:
        id_ingresado = int(input("Ingresa el ID de la tarea que deseas eliminar: "))
        for i, tarea in enumerate(tasks):
            if tarea["id"] == id_ingresado:
                tasks.pop(i)
                guardar_datos(tasks)
                print("Tarea eliminada con éxito.")
                return
        print("La tarea no se encontró.")
    except ValueError:
        print("Error: Debes ingresar un número entero.")

# --- FLUJO PRINCIPAL ---

tasks = cargar_datos()

while True:
    print("--- MENÚ DE OPCIONES ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Cambiar estado (Check/Uncheck)")
    print("4. Eliminar tarea")
    print("5. Editar tarea")
    print("6. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    match opcion:
        case "1":
            agregar_tarea(tasks)
        case "2":
            mostrar_tareas(tasks)
        case "3":
            actualizar_tarea(tasks)
        case "4":
            eliminar_tarea(tasks)
        case "5":
            editar_tarea(tasks)
        case "6":
            print("¡Hasta luego!")
            break
        case _:
            print("Opción no válida, intenta de nuevo.")