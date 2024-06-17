import time
import os
from funciones import datos_ceo, datos_analista, datos_desarrollador
from funciones import registro_trabajador, imprimir_planilla, imprimir_ceo, imprimir_desarrollador, imprimir_analista, trabajadores, datos
def menu():
    #Menu de opciones
    while True:
        #Limpiar pantalla
        os.system("cls")
        #Menu
        print("1.Registrar trabajador")
        print("2.Listar todos los trabajadores")
        print("3.Imprimir planilla de sueldos")
        print("4.Salir del programa")
        try:
            decision = int(input("\n> "));
            os.system("cls")
        except:
            print("Ingreso una valor invalido, por favor vuelva a intentarlo...");
            time.sleep(2)
        if decision == 1:
            print("[ Registro de trabajador ]")
            registro_trabajador()
        elif decision == 2:
            print(trabajadores)
            input ("\nPresione 'Enter' para volver")
        elif decision == 3:
            try:
                print("Planilla de sueldos")
                print ("1.-Imprimir todos")
                print ("2.-Imprimir CEO")
                print ("3.-Imprimir Desarrollador")
                print ("4.-Imprimir Analista de datos")
                print ("5.-Salir")
                decision_2 = int(input("\n>"))
                if decision_2 == 1:
                    imprimir_planilla()
                elif decision_2 == 2:
                    if "CEO" in datos:
                        imprimir_ceo()
                        input ("\nPresione 'Enter' para volver")
                    else:
                        print ("No existe CEO en plantilla, porfavor vuelva a intentarlo...")
                        time.sleep(2)
                elif decision_2 == 3:
                    if "Desarrollador" in datos:
                        imprimir_desarrollador()
                        input ("\nPresione 'Enter' para volver")
                    else:
                        print ("No existe Desarrollador en plantilla, porfavor vuelva a intentarlo...")
                        time.sleep(2)
                elif decision_2 == 4:
                    if "Analista de datos" in datos:
                        imprimir_analista()
                        input ("\nPresione 'Enter' para volver")
                    else:
                        print ("No existe Analista de datos, porfavor vuelva a intentarlo...")
                        time.sleep(2)
                elif decision_2 == 5:
                    continue
                else:
                    print("Ingreso una opcion invalida, por favor vuelva a intentarlo...");
                    time.sleep(2)
            except ValueError:
                print("Ingreso una valor invalido, por favor vuelva a intentarlo...");
                time.sleep(2)
        elif decision == 4:
            exit()
        else:
            print("Ingreso una opcion invalida, por favor vuelva a intentarlo...");
            time.sleep(2)