import csv
#Calculo de Desc. Salud, Desc. AFP y liquido a pagar
def descuentos(sueldo_bruto):
    global desc_salud
    global desc_afp
    global liquido_a_pagar
    #Desc. Salud
    desc_salud = sueldo_bruto / 0.07
    #Desc. AFP
    desc_afp = sueldo_bruto /0.12
    #Liquido a pagar
    liquido_a_pagar = sueldo_bruto-(desc_salud+desc_afp)

#Escribir en archivo_csv
with open('registro.csv','w',newline='') as archivo_csv:
    #Declarar escritura en archivo_csv 
    escritor_csv = csv.writer(archivo_csv)
    #Escribir filas de datos
    escritor_csv.writerows(datos)
def imprimir_planilla():
    #Leer archivo_csv
    with open('registro.csv','r',newline='') as archivo_csv:
        #Declarar lectura como diccionario
        lector_csv = csv.DictReader(archivo_csv)
        #Iteracion en cada fila del archivo_csv
        for fila in archivo_csv:
            nombre = fila['Nombre']
            cargo = fila['Cargo']
            sueldo_bruto = fila['Sueldo']
            desc_salud = fila['Desc. Salud']
            desc_afp = fila['Desc. AFP']
            liquido_a_pagar=fila['Liquido a pagar']
            #Imprimir planilla de sueldos
            print    ("Nombre    Cargo    Sueldo Bruto    Desc. Salud    Desc. AFP    Liquido a pagar")
            print (f"{nombre}    {cargo}    {sueldo_bruto}    {desc_salud}    {desc_afp}    {liquido_a_pagar}")
