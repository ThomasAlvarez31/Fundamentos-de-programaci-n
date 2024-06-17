import time
#Listas
trabajadores = []
datos = []
datos_ceo = []
datos_desarrollador = []
datos_analista = []
#Calculo de Desc. Salud, Desc. AFP y liquido a pagar
def descuentos(sueldo_bruto):
    global desc_salud
    global desc_afp
    global liquido_a_pagar
    #Desc. Salud
    desc_salud = int(sueldo_bruto * 0.07)
    #Desc. AFP
    desc_afp = int(sueldo_bruto * 0.12)
    #Liquido a pagar
    liquido_a_pagar = sueldo_bruto-(desc_salud+desc_afp)
#Registro
def registro_trabajador():
        global trabajador
        global cargo
        global sueldo_bruto
        global contador_ceo
        global contador_desarrollador
        global contador_analista
        nombre = input("Ingrese el nombre de su trabajador: ")
        apellido = input("Ingrese el apellido del trabajador: ")
        cargo = input("Ingrese el cargo del trabajador: ")
        sueldo_bruto = int(input("Ingrese el suedo bruto del trabajador: "))
        trabajador = nombre + " " +  apellido
        trabajadores.append(trabajador)
        descuentos(sueldo_bruto)
        datos.append(trabajador)
        datos.append(str(sueldo_bruto))
        datos.append(str(desc_salud))
        datos.append(str(desc_afp))
        datos.append(str(liquido_a_pagar))
        print (cargo.upper())
        if cargo.upper() == "CEO":
            datos.append(cargo.upper())
            datos_ceo.append(trabajador)
            datos_ceo.append(cargo.upper())
            datos_ceo.append(str(sueldo_bruto))
            datos_ceo.append(str(desc_salud))
            datos_ceo.append(str(desc_afp))
            datos_ceo.append(str(liquido_a_pagar))
            return
        elif cargo.capitalize() == "Desarrollador":
            datos.append(cargo.capitalize())
            datos_desarrollador.append(trabajador)
            datos_desarrollador.append(cargo.capitalize())
            datos_desarrollador.append(str(sueldo_bruto))
            datos_desarrollador.append(str(desc_salud))
            datos_desarrollador.append(str(desc_afp))
            datos_desarrollador.append(str(liquido_a_pagar))
            return
        elif cargo.capitalize() == "Analista de datos":
            datos.append(cargo.capitalize())
            datos_analista.append(trabajador)
            datos_analista.append(cargo.capitalize())
            datos_analista.append(str(sueldo_bruto))
            datos_analista.append(str(desc_salud))
            datos_analista.append(str(desc_afp))
            datos_analista.append(str(liquido_a_pagar))
        else:
            print ("Su cargo esta mal redactado, por favor vuelva a intentarlo")
            time.sleep(2)
def imprimir_planilla():
    #Contador
    contador = 0
    #Escribir archivo_csv
    with open('registro.txt','w',newline='') as archivo_txt:
        archivo_txt.write("Trabajador , Cargo, Sueldo Bruto, Desc. Salud, Desc. AFP, Liquido a pagar\n")
        for dato in datos:
            archivo_txt.write(dato)
            contador = contador + 1
            if contador % 6 == 0:
                archivo_txt.write("\n")
                continue
            archivo_txt.write(" , ")
def imprimir_ceo():
    #Contador
    contador = 0
    #Escribir archivo_csv
    with open('registro_ceo.txt','w',newline='') as archivo_txt:
        archivo_txt.write("Trabajador , Cargo, Sueldo Bruto, Desc. Salud, Desc. AFP, Liquido a pagar\n")
        print (datos_ceo)
        for dato in datos_ceo:
            archivo_txt.write(dato)
            contador = contador + 1
            if contador % 6 == 0:
                archivo_txt.write("\n")
                continue
            archivo_txt.write(" , ")
def imprimir_desarrollador():
    #Contador
    contador = 0
    #Escribir archivo_csv
    with open('registro_desarrollador.txt','w',newline='') as archivo_txt:
        archivo_txt.write("Trabajador , Cargo, Sueldo Bruto, Desc. Salud, Desc. AFP, Liquido a pagar\n")
        for dato in datos_desarrollador:
            archivo_txt.write(dato)
            contador = contador + 1
            if contador % 6 == 0:
                archivo_txt.write("\n")
                continue
            archivo_txt.write(" , ")
def imprimir_analista():
    #Contador
    contador = 0
    #Escribir archivo_csv
    with open('registro_analista.txt','w',newline='') as archivo_txt:
        archivo_txt.write("Trabajador , Cargo, Sueldo Bruto, Desc. Salud, Desc. AFP, Liquido a pagar\n")
        for dato in datos_analista:
            archivo_txt.write(dato)
            contador = contador + 1
            if contador % 6 == 0:
                archivo_txt.write("\n")
                continue
            archivo_txt.write(" , ")