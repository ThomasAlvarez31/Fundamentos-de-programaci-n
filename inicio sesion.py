'''#Lista de usuario permitido
usuarios=["die.mancilla@duocuc.cl","nacho.bittner@duocuc.cl"]
#Inicio de sesion de los trabajadores

while True:
    print("<---Empresas Calfun--->")
    print("1.-Iniciar Sesion")
    print("2.-Salir.")
    try: 
        opcion_usuario=int(input("Seleccione su opcion -->: "))
    except ValueError:
        print("Ingresa un valor valido!")
        print("");
    if opcion_usuario==1:
        print("Has elegido iniciar sesion")
        ingreso_usuario=input("Ingresa tu Correo usuario: ")
        if ingreso_usuario in usuarios:
            print("!Inicio de sesion Exitoso!")
            break
        else:
            print("!Inicio de sesion Denegado, vuelve a intentarlo")
            print("")
    elif opcion_usuario==2:
        print("Has elegido salir");
        break
    else:
        print("Ingresa una opcion valida!");
'''
while True:
    print("<---Empresas Calfun--->")
    print("1.-Iniciar Sesion")
    print("2.-Salir.")
    try: 
        opcion_usuario=int(input("Seleccione su opcion -->: "))
    except ValueError:
        print("Ingresa un valor valido!")
        print("");
    if opcion_usuario==1:
        usuario = input(">")
        contraseña = input(">")
        if usuario == ("nacho.bittner@duocuc.cl") and (contraseña == "1234"):
            print("Inicio de sesion exitoso!")
            break
    elif opcion_usuario==2:
        print("Has elegido salir");
        break
    else:
        print("Ingresa una opcion valida!");