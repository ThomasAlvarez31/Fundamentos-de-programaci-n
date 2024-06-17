import time
import os
from menu_de_opciones import menu
while True:
    try: 
        #Limpiar pantalla
        os.system("cls")
        print("<---Empresas Calfun--->")
        print("1.-Iniciar Sesion")
        print("2.-Salir")
        opcion_usuario=int(input("\nSeleccione su opcion --> "))
        os.system("cls")
    except ValueError:
        print("Ingreso un valor invalido, por favor vuelva a intentarlo...")
        time.sleep(2)
    #Inicio sesion
    if opcion_usuario==1:
        print ("Ingrese su correo")
        usuario = input("--> ")
        print ("Ingrese su contraseña")
        contraseña = input("--> ")
        if usuario == ("nacho.bittner@duocuc.cl") and (contraseña == "1234"):
            print("Inicio de sesion exitoso!")
            break
    #Salir
    elif opcion_usuario==2:
        print("Has elegido salir");
        #Funcion exit(), fuerza al programa a finalizar la ejecucion
        exit()
    else:
        print("Ingreso una opcion invalida, por favor vuelva a intentarlo...");
        time.sleep(2)
menu()
#Actualizado