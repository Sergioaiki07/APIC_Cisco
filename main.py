import func
print("Bienvenido seleccione una acción \n 1 - Estado de interfaces leaf 1 \n 2 - Estado de interfaces leaf 2 \n 3 - Bajar alguna interfaz")
print("Ingrese valor (1,2,3) ", end="")  # espera de ingreso
opcion = input()
#prueba del puerto 1/49 que esta up
if opcion == '1':
    estado = func.Estado_leaf('101') # llamo funcion del leaf 1 que tiene codigo 101
    total = int(estado.json()['totalCount']) #saco la cantidad de puertos que tiene el leaf
    print(' Total interfases :',estado.json()['totalCount'], '\n','ID  ,  Estado administrativo,  Modo , Auto Negociacion') # Imprimo la cabecera de la lista
    x = 0
    # while para recorer todo el json sacando datos nececitados
    while x < total:
        print(estado.json()['imdata'][x]['l1PhysIf']['attributes']['id'], '          ', estado.json()['imdata'][x]['l1PhysIf']['attributes']['adminSt'], '       ',estado.json()['imdata'][x]['l1PhysIf']['attributes']['mode'], '    ', estado.json()['imdata'][x]['l1PhysIf']['attributes']['autoNeg'])
        x += 1
if opcion == '2':
    estado = func.Estado_leaf('102') # llamo funcion del leaf 2 que tiene codigo 102
    total = int(estado.json()['totalCount'])#saco la cantidad de puertos que tiene el leaf
    print(' Total interfases :', estado.json()['totalCount'], '\n', 'ID  ,    Estado administrativo,  Modo , Auto Negociacion')
    x = 0
    while x < total:
        print(estado.json()['imdata'][x]['l1PhysIf']['attributes']['id'], '       ', estado.json()['imdata'][x]['l1PhysIf']['attributes']['adminSt'], '          ',estado.json()['imdata'][x]['l1PhysIf']['attributes']['mode'], '      ', estado.json()['imdata'][x]['l1PhysIf']['attributes']['autoNeg'])
        x += 1
if opcion == '3':
    print("Que leaf quiere modificar 1 o 2? ", end="")
    leaf = input()
    print("Que interfas quiere modificar formato X/XX? ", end="")
    interfaz = input()
    print("1 para subir 2 para bajar administrativamente ", end="")
    updown = input()
    est = func.adm_puerto(interfaz,updown,leaf) #envio datos para realizar la modificacion
    print(est)
    try:#utilizo esta funcion para poder determinar cuando se ingrese datos incorrectos en esta seccion
        if est.status_code == 200: #espero el codigo 200 si el cambio fuen realizado correctamente
            print("Cambios realizados correctamente, en unos segundos se reflejara en el controlador.")
        else:
            print("Ha ocurrido un erro , ", est)
    except:
        print()
else:
    print("Por favor elija una opción valida") # si se ingresa un dato incorrecto en el menu principal