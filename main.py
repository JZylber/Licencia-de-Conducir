import csv

Sede = dict[str, str]
# Las sedes arrancan con los siguientes campos salvo impresiones que se agrega en el programa
# Sede = {
#     'nombre': str,
#     'actividad': str,
#     'direccion': str,
#     'barrio': str,
#     'impresiones': int
# }

def cargar_csv(nombreArchivo: str) -> list[list[str]]:
    with open(nombreArchivo, encoding="utf8") as archivo:
        lector = csv.reader(archivo)
        datos = []
        lector.__next__()
        for fila in lector:
            datos.append(fila)
    return datos

def generar_sedes(datos: list[list[str]]) -> list[Sede]:
    sedes = []
    for fila in datos:
        sede = {}
        sede['nombre'] = fila[4]
        sede['actividad'] = fila[5].replace('.', '')
        sede['direccion'] = f"{fila[10]} {fila[11]}"
        sede['barrio'] = fila[13]
        sedes.append(sede)
    return sedes

def seleccionar_desde_opciones(opciones: dict[str, list[Sede]]) -> Sede:
    for opcion in opciones.keys():
        print(f"- {opcion}")
    seleccion = ""
    while seleccion not in opciones.keys():
        seleccion = input("Seleccione una opción: ")
        if seleccion not in opciones.keys():
            print("Opción inválida")   
    sedes = opciones[seleccion]
    sede =  ""
    if len(sedes) > 1:
        for i, sede in enumerate(sedes):
            print(f"{i+1}. {sede['nombre']}")
        seleccion = -1
        while seleccion < 0 or seleccion >= len(sedes):
            seleccion = int(input("Seleccione una sede: ")) - 1
            if seleccion < 0 or seleccion >= len(sedes):
                print("Opción inválida")
        sede = sedes[seleccion]
    else:
        sede = sedes[0]
    return sede

def mostrar_sede(sede: Sede):
    print(f"Nombre: {sede['nombre']}")
    print(f"Actividad: {sede['actividad']}")
    print(f"Dirección: {sede['direccion']}")
    print(f"Barrio: {sede['barrio']}")

def main():
    datos = cargar_csv('licencias-de-conducir.csv')
    sedes = generar_sedes(datos)
    por_barrio = sedes_por_barrio(sedes)
    por_actividad = sedes_por_actividad(sedes)
    corriendo = True
    while(corriendo):
        print("Menú")
        print("1. Sedes por barrio")
        print("2. Sedes por actividad")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            sede = seleccionar_desde_opciones(por_barrio)
            mostrar_sede(sede)
            marcar_impresion(sede)
        elif opcion == '2':
            sede = seleccionar_desde_opciones(por_actividad)
            mostrar_sede(sede)
            marcar_impresion(sede)
        elif opcion == '3':
            corriendo = False
        else:
            print("Opción inválida")
    for sede in sedes:
        print(f"{sede['nombre']}: {sede['impresiones'] if 'impresiones' in sede else 0} vistas")

main()