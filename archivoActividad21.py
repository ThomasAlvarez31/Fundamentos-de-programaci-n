from archivoActividad import *
import csv
trabajadores = []
sueldos = []
datos = []
def registro_trabajador():
        global trabajador
        global cargo
        global sueldoBruto
        nombre = input("Ingrese el nombre de su trabajador: ")
        apellido = input("Ingrese el apellido del trabajador: ")
        cargo = input("Ingrese el cargo del trabajador: ")
        sueldoBruto = int(input("Ingrese el suedo bruto del trabajador"))
        trabajador = nombre + " " +  apellido
        trabajadores.append(trabajador)
        descuentos(sueldoBruto)
        datos.append([trabajador,cargo,sueldoBruto,desc_salud,desc_afp,liquido_a_pagar])
while True:
    print("1.Registrar trabajador")
    print("2.Listar todos los trabajadores")
    print("3.Imprimir planilla de sueldos")
    print("4.Salir del programa")
    try:
        decision = int(input());
    except:
        print("Error ingrese una opcion valida")
    if decision == 1:
        print("Registro de trabajador")
        registro_trabajador()
        
    if decision == 2:
        print(trabajadores)
    if decision == 3:
        print("Usted quiere imprimir la planilla de sueldos")
        imprimir_planilla()
    if decision == 4:
        break
    if decision > 4:
        print("Ingrese una opcion valida porfavor")