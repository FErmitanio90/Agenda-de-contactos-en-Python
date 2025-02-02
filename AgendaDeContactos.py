def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Por favor, escriba el nombre completo del contacto: ")
    
    # Verificar si el contacto ya existe
    if nombre in agenda:
        confirmar = input(f"El contacto '{nombre}' ya existe. ¿Desea sobrescribirlo? (s/n): ").strip().lower()
        if confirmar != 's':
            print("No se ha modificado el contacto.")
            return

    telefono = input("Por favor, escriba el teléfono del contacto: ")
    email = input("Por favor, escriba el email del contacto: ")

    agenda[nombre] = {"Teléfono": telefono, "Email": email}
    print(f"¡Se ha agregado el contacto '{nombre}' exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    
    if nombre in agenda:
        confirmar = input(f"¿Está seguro de que desea eliminar '{nombre}'? (s/n): ").strip().lower()
        if confirmar == 's':
            del agenda[nombre]
            print(f"El contacto '{nombre}' ha sido eliminado.")
        else:
            print("El contacto no se eliminó.")
    else:
        print(f"No se ha encontrado el contacto '{nombre}'.")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que está buscando: ")
    
    if nombre in agenda:
        print("\n--- Contacto encontrado ---")
        print(f"Nombre: {nombre}") 
        print(f"Teléfono: {agenda[nombre]['Teléfono']}")
        print(f"Email: {agenda[nombre]['Email']}")
        print("-" * 30)
    else:
        print(f"El contacto '{nombre}' no está en la agenda.")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos:")
        print("-" * 30)
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info['Teléfono']}")
            print(f"Email: {info['Email']}")
            print("-" * 30)
    else:
        print("La agenda está vacía aún.")

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor, elija una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliste de la agenda de contactos. ¡Hasta luego!")
            break
        else:
            print("Por favor, elija una opción válida (del 1 al 5).")

agenda_contactos()
