# Sistema de gestión de biblioteca con listas paralelas (versión con match case)
titulos = []
ejemplares = []

opcion = 0

while opcion != 8:
    print("\n--- MENÚ DE BIBLIOTECA ---")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion.isdigit():
        opcion = int(opcion)
    else:
        print("Debe ingresar un número válido.")
        opcion = 0

    match opcion:
        case 1:
            cant = input("¿Cuántos títulos iniciales desea ingresar?: ")
            if cant.isdigit():
                cant = int(cant)
                if cant > 0:
                    for i in range(cant):
                        titulo = input(f"Ingrese el título {i+1}: ").strip()
                        
                        if titulo == "":
                            print("El título no puede estar vacío. No se agregó.")
                            ejemplares.append(0)  # Mantiene la sincronía
                        else:
                            # Validar duplicados
                            existe = False
                            for t in titulos:
                                if t.lower() == titulo.lower():
                                    existe = True
                            if existe:
                                print("Ese título ya estaba cargado, no se agregó.")
                                ejemplares.append(0)  # Mantiene la sincronía
                            else:
                                titulos.append(titulo)
                                ejemplares.append(0)  # Inicialmente sin copias
                else:
                    print("Debe ingresar un número mayor que 0.")
            else:
                print("Debe ingresar un número válido.")

        case 2:
            if len(titulos) == 0:
                print("Primero debe ingresar títulos (opción 1).")
            else:
                for i in range(len(titulos)):
                    copias = input(f"Ingrese la cantidad de ejemplares para '{titulos[i]}': ")
                    while not copias.isdigit() or int(copias) < 0:
                        copias = input("Cantidad inválida. Ingrese un número entero mayor o igual a 0: ")
                    ejemplares[i] = int(copias)

        case 3:
            if len(titulos) == 0:
                print("No hay libros cargados.")
            else:
                print("\n--- CATÁLOGO ---")
                for i in range(len(titulos)):
                    print(f"{titulos[i]} - {ejemplares[i]} ejemplares")

        case 4:
            if len(titulos) == 0:
                print("No hay libros cargados.")
            else:
                buscar = input("Ingrese el título a consultar: ").strip().lower()
                if buscar == "":
                    print("Debe ingresar un título válido.")
                else:
                    encontrado = False
                    for i in range(len(titulos)):
                        if titulos[i].lower() == buscar:
                            print(f"'{titulos[i]}' tiene {ejemplares[i]} ejemplares.")
                            encontrado = True
                    if not encontrado:
                        print("Título no encontrado en el catálogo.")

        case 5:
            print("\n--- LIBROS AGOTADOS ---")
            agotados = False
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(titulos[i])
                    agotados = True
            if not agotados:
                print("No hay libros agotados.")

        case 6:
            nuevo_titulo = input("Ingrese el nuevo título: ").strip()
            
            if nuevo_titulo == "":
                print("El título no puede estar vacío. No se agregó.")
            else:
                existe = False
                for t in titulos:
                    if t.lower() == nuevo_titulo.lower():
                        existe = True

                if existe:
                    print("Ese título ya existe en el catálogo, no se agregó.")
                else:
                    copias = input("Ingrese la cantidad de ejemplares: ")
                    while not copias.isdigit() or int(copias) < 0:
                        copias = input("Cantidad inválida. Ingrese un número entero mayor o igual a 0: ")
                    copias = int(copias)

                    titulos.append(nuevo_titulo)
                    ejemplares.append(copias)
                    print("Libro agregado correctamente.")

        case 7:
            if len(titulos) == 0:
                print("No hay libros cargados.")
            else:
                print("\n--- ACTUALIZAR EJEMPLARES ---")
                for i in range(len(titulos)):
                    print(f"{i+1}. {titulos[i]} - {ejemplares[i]} ejemplares")

                sel = input("Seleccione el número del libro: ")
                if sel.isdigit():
                    sel = int(sel) - 1
                    if 0 <= sel < len(titulos):
                        accion = input("¿Préstamo (p) o Devolución (d)?: ").lower()
                        if accion == "p":
                            cant = input("¿Cuántos ejemplares desea prestar?: ")
                            while not cant.isdigit() or int(cant) <= 0:
                                cant = input("Cantidad inválida. Ingrese un número mayor a 0: ")
                            cant = int(cant)
                            if ejemplares[sel] >= cant:
                                ejemplares[sel] -= cant
                                print(f"Préstamo de {cant} ejemplar(es) registrado.")
                            else:
                                print(f"No se puede prestar {cant}. Solo hay {ejemplares[sel]} disponibles.")
                            
                        elif accion == "d":
                            ejemplares[sel] += 1
                            print("Devolución registrada.")
                        else:
                            print("Opción inválida.")
                    else:
                        print("Número de libro inválido.")
                else:
                    print("Debe ingresar un número válido.")

        case 8:
            print("Saliendo del sistema...")

        case _:
            print("Opción no válida. Intente de nuevo.")
