tasks = []
ultimo_id = 0

def agregar_tarea(tasks):
    global ultimo_id
    titulo = input("Ingresa el titulo de la tarea: ")
    ultimo_id += 1
    tarea = {
        "id" : ultimo_id,
        "title" : titulo,
        "completed" : False
    }
    tasks.append(tarea)

def mostrar_tareas(tasks):
    if not tasks:
        print("No hay tareas registradas.")
    else:
        print(f"{'ID':<5} {'TITULO':<30} {'ESTADO':<12}")
        print("-" * 50)
    for tarea in tasks:
        task_id = tarea["id"]
        titulo = tarea["title"]
        estado = tarea["completed"]
        if not estado:
            estado = "Pendiente"
        else:
            estado = "Completada"
        print(f"{task_id:<5} {titulo:<30} {estado:<12}")

def actualizar_tarea(tasks):
    try:
        id_ingresado = int(input("Ingresa el id de la tarea que deseas completar: "))
        for tarea in tasks:
            if tarea["id"] == id_ingresado:
                tarea["completed"] = not tarea["completed"]
                print(f"El estado de la tarea se actualizó correctamente.")
                break
        else:
            print("La tarea no se encontró")
    except ValueError:
        print("Error, debes ingresar un número entero")

def eliminar_tarea(tasks):
    try:
        id_ingresado = int(input("Ingresa el id de la tarea que deseas eliminar: "))
        for index, tarea in enumerate(tasks):
            if tarea["id"] == id_ingresado:
                del tasks[index]
                print("Tarea eliminada con exito. ")
                break
        else:
            print("La tarea no se encontró. ")
    except ValueError:
        print("Error, debes ingresar un número entero")

while True:
    print("Menú de opciones: ")
    opcion = int(input("1. Agregar tarea\n" \
                       "2. Listar tarea\n" \
                       "3. Cambiar estado de tarea\n"
                       "4. Eliminar tarea\n" \
                       "5. Salir\n"))
    
    match opcion:
        case 1:
            agregar_tarea(tasks)
        case 2:
            mostrar_tareas(tasks)
        case 3:
            actualizar_tarea(tasks)
        case 4:
            eliminar_tarea(tasks)
        case 5:
            break
        case _:
            print("Opcion no valida")
