from os import system
system("cls")
import random
import csv

planilla_de_cliente = []
sectores_disponibles = ("concepcion", "chiguayante", "talcahuano", "hualpen", "san pedro")

def registrar_pedido():
    while True:
        id_cliente = random.randint(111111,999999)
        nombre_cliente = input("Ingrese el nombre del cliente\n==> ")
        longitud_nombre = len(nombre_cliente)
        print()
        apellido_cliente = input("Ingrese el apellido del cliente\n==> ")
        longitud_apellido = len(apellido_cliente)
        print()
        while nombre_cliente.isalpha() == False or longitud_nombre<3 or apellido_cliente.isalpha() == False or longitud_apellido<3:
            print()
            print("[ERROR] [EL NOMBRE Y APELLIDO DEBEN SER NUMERICOS][EL NOMBRE Y APELLIDO NO PUEDEN SER MENOR A 3 CARACTERES]")
            print()
            nombre_cliente = input("Ingrese el nombre del cliente\n==> ")
            longitud_nombre = len(nombre_cliente)
            print()
            apellido_cliente = input("Ingrese el apellido del cliente\n==> ")
            longitud_apellido = len(apellido_cliente)
            print()
        direccion_cliente = input("Ingrese la direccion del cliente (calle y numero)\n==> ")
        print()
        print(f"Sectores disponibles: {sectores_disponibles}")
        sector_cliente = input("Ingrese el sector del cliente\n==> ")
        print()
        while sector_cliente not in sectores_disponibles:
            print()
            print("[ERROR] [DEBE INGRESAR UNO DE LOS SECTORES DISPONIBLES]")
            print()
            print(f"Sectores disponibles: {sectores_disponibles}")
            sector_cliente = input("Ingrese el sector del cliente\n==> ")
            print()
        try:
            dispensadores_6lts = int(input("Ingrese le cantidad de dispensadores de 6 litros que desea\t==> "))
            dispensadores_10lts = int(input("Ingrese le cantidad de dispensadores de 10 litros que desea\t==> "))
            dispensadores_20lts = int(input("Ingrese le cantidad de dispensadores de 20 litros que desea\t==> "))
            cantidad_dispensadores = dispensadores_6lts + dispensadores_10lts + dispensadores_20lts
            print()
            while cantidad_dispensadores==0:
                print()
                print("[ERROR] [DEBE INGRESAR UN PEDIDO SUPERIOR A 0 UNIDADES]")
                print()
                dispensadores_6lts = int(input("Ingrese le cantidad de dispensadores de 6 litros que desea\t==> "))
                dispensadores_10lts = int(input("Ingrese le cantidad de dispensadores de 10 litros que desea\t==> "))
                dispensadores_20lts = int(input("Ingrese le cantidad de dispensadores de 20 litros que desea\t==> "))
                cantidad_dispensadores = dispensadores_6lts + dispensadores_10lts + dispensadores_20lts
                print()
        except ValueError:
            print()
            print("[ERROR] [DEBE INGRESAR UN VALOR NUMERICO]")
            print()
            continue

        pedido_cliente = {
            "ID": id_cliente,
            "Nombre": nombre_cliente + (f" {apellido_cliente}"),
            "Direccion": direccion_cliente,
            "Sector": sector_cliente,
            "Disp.6lts": dispensadores_6lts,
            "Disp.10lts": dispensadores_10lts,
            "Disp.20lts": dispensadores_20lts
        }
        planilla_de_cliente.append(pedido_cliente)
        print("[PEDIDO DEL CLIENTE REGISTRADO CON EXITO]")
        break

def listar_todos_los_pedidos():
    if not planilla_de_cliente:
        print("[LA PLANILLA DE PEDIDOS SE ENCUENTRA VACIA]")
    for pedido_cliente in planilla_de_cliente:
        print(pedido_cliente)

def imprimir_hoja_de_ruta():
    print(f"Sectores disponibles: {sectores_disponibles}")
    sector_hdr = input("Ingrese su sector para imprimir la hoja de ruta\n==> ")
    if sector_hdr not in sectores_disponibles:
        print("[ERROR] [EL SECTOR INGRESADO NO ES VALIDO]")
    elif sector_hdr in sectores_disponibles:
        with open(f"hoja_de_ruta_{sector_hdr}.csv", "w", newline="") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(["ID", "Nombre", "Direccion", "Sector", "Disp.6lts", "Disp.10lts", "Disp.20lts"])
            for pedido_cliente in planilla_de_cliente:
                if pedido_cliente["Sector"]==sector_hdr:
                    escritor_csv.writerow([pedido_cliente["ID"], pedido_cliente["Nombre"], pedido_cliente["Direccion"], pedido_cliente["Sector"], pedido_cliente["Disp.6lts"], pedido_cliente["Disp.10lts"], pedido_cliente["Disp.20lts"]])
        print(f"[LA HOJA DE RUTA {sector_hdr} HA SIDO GENERADA CON EXITO]")

def buscar_pedido_por_id():
    while True:
        if not planilla_de_cliente:
            print("[LA PLANILLA DE PEDIDOS SE ENCUENTRA VACIA]")
            break
        else:
            try:
                id_buscar = int(input("Ingrese la ID a buscar\n==> "))
            except ValueError:
                print()
                print("[ERROR] [DEBE INGRESAR UN VALOR NUMERICO]")
                print()
                continue
            for pedido_cliente in planilla_de_cliente:
                if pedido_cliente["ID"]!=id_buscar:
                    print("[ERROR] [LA ID INGRESADA NO SE ENCUENTRA DISPONIBLE]")
                    return
                elif pedido_cliente["ID"]==id_buscar:
                    print(pedido_cliente)
            break






def programa_principal(): 
    while True:
        from os import system
        system("cls")
        try:
            print()
            opciones = int(input("[CleanWasser]\n1. Registrar pedido\n2. Listar todos los pedidos\n3. Imprimir hoja de ruta\n4. Buscar pedido por ID\n5. Salir de la aplicacion\n==> "))
            print()
            while opciones<1 or opciones>5:
                print()
                print("[ERROR] [LA OPCION DEBE SER 1, 2, 3, 4 o 5]")
                print()
                opciones = int(input("[CleanWasser]\n1. Registrar pedido\n2. Listar todos los pedidos\n3. Imprimir hoja de ruta\n4. Buscar pedido por ID\n5. Salir de la aplicacion\n==> "))
                print()
        except ValueError:
            print()
            print("[ERROR] [DEBE INGRESAR UN VALOR NUMERICO]")
            print()
            continue

        if opciones==1:
            registrar_pedido()
        elif opciones==2:
            listar_todos_los_pedidos()
        elif opciones==3:
            imprimir_hoja_de_ruta()
        elif opciones==4:
            buscar_pedido_por_id()
        elif opciones==5:
            break
        print()
        input("Ingrese cualquier tecla para continuar\n==> ")
            
if __name__ == "__main__":
    programa_principal()