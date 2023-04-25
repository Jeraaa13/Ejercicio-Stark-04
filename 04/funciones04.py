import re

def extraer_iniciales(nombre:str):
    """
    Recibe un nombre de tipo string
    Y extrae las iniciales del nombre seguidas por un punto
    si hay the lo omite y si hay un guion lo reemplaza por un espacio en blanco
    devuelve por ejemplo para Howard the duck H.D.
    """
    if not nombre:
        return "N/A"
    
    nombre = nombre.replace("-", " ")

    nombre = nombre.replace("the", "")

    iniciales = re.findall("[A-Z]", nombre)
    iniciales = ".".join(iniciales) + "."
    return iniciales

def definir_iniciales_nombre(diccionario:dict):
    """
    Recibe un diccionario, valida que sea tipo dict y que contenga la clave "nombre"
    La funcion agrega una nueva clave al dict llamada "iniciales" y el valor se obtiene de la funcion extraer_iniciales
    si encuentra algun error retona False en caso contrario True
    """
    if type(diccionario) != type(dict()) or "nombre" not in diccionario:
        return False
    else:
        iniciales = extraer_iniciales(diccionario["nombre"])
        diccionario["iniciales"] = iniciales
        return True
    
def agregar_iniciales_nombre(lista:list):
    """
    Recibe una lista tipo list
    Valida que sea tipo list, y que contenga al menos un elemento
    La funcion le pasa cada heroe a la funcion definir_iniciales_nombre()
    En caso de que la funcion antes nombrada retorne False, informa:‘El origen de datos no contiene el formato correcto’
    Si no devuelve True si finalizo con exito
    """
    if type(lista) == type(list()) and len(lista) > 0:
        for elemento in lista:
            bool = definir_iniciales_nombre(elemento)
            if bool == False:
                print("El origen de datos no contiene el formato correcto")
                return False
        return True
    else:
        return False
    
def stark_imprimir_nombres_con_iniciales(lista:list):
    """
    Recibe una lista tipo list
    Utiliza la funcion agregar_iniciales_al_nombre() para añadir las iniciales a los diccionarios
    Luego imprime la lista completa de los nombres junto a las iniciales
    Valida que sea la lista sea tipo list, y que contenga al menos un elemento
    """
    if type(lista) == type(list()) and len(lista) > 0:
        agregar_iniciales_nombre(lista)
        for elemento in lista:
            print("* {0} ({1})".format(elemento["nombre"], elemento["iniciales"]))
    
#2.1
def generar_codigo_heroe(id:int, genero:str) -> str:
    """
    Recibe una id de heroe tipo entero y un genero tipo str
    Genera un string por ej: GENERO-000…000ID
    Se valida que el id sea numerico, y que el genero no se encuentre vacio y este dentro de los valores esperados
    En caso de no pasar las validaciones retonra N/A
    """
    if type(id) == type(int()) and not genero.isnumeric() and genero in ["M", "F", "NB"]:
        id = str(id)
        id = id.zfill(8)
        id_heroe = "{0}-{1}".format(genero, id)
        return id_heroe
    else:
        return "N/A"

#2.2
def agregar_codigo_heroe(diccionario:dict, id:int):
    """
    Recibe un diccionario tipo dict, y una id tipo entero
    Agrega al diccionario una clave codigo_heroe y le asigna un valor usando la funcion generar_codigo_heroe()
    Valida que el diccionario no este vacio, y que el codigo recibido tenga exactamente 10 caracteres
    Retorna True si valida correctamente, y si no False
    """
    identificador = generar_codigo_heroe(id, diccionario["genero"])
    if len(diccionario) > 0 and len(identificador) == 10:
        diccionario["codigo_heroe"] = identificador
        return True
    else:
        return False
    
def stark_generar_codigo_heroes(lista:list):
    """
    Recibe una lista tipo list
    itera por la lista y le agrega una id a cada diccionario
    una vez finaliza imprime por pantalla un mensaje como: 
    Se asignaron X códigos
     * El código del primer héroe es: M-00000001
    ...
    * El código del del último héroe es: M-00001224
    la funcion valida que la lista no este vacia, que todos los elementos sean tipo dict, y que contenga la clave genero
    """
    contcodigos = 0
    flagprimerheroe = True
    if len(lista) > 0:
        for elemento in lista:
            if type(elemento) == type(dict()) and "genero" in elemento:
                contcodigos += 1
                agregar_codigo_heroe(elemento, contcodigos)
                if flagprimerheroe:
                    primer_heroe = elemento
                    flagprimerheroe = False
            else:
                break
        print("Se asignaron {0} códigos\n*El código del primer héroe es: {1}\n*El código del del último héroe es: {2}".format(contcodigos, primer_heroe["codigo_heroe"],elemento["codigo_heroe"] ))
    else:
        print("El origen de datos no contiene el formato correcto")

#3.1
def sanitizar_entero(numero_str:str):
    """
    Recibe un string numerico entero
    valida que sea un numero entero positivo
        Si contiene carácteres no numéricos retornar -1
        Si el número es negativo se deberá retornar un -2
        Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
    Retorna un numero entero
    """
    numero_str = numero_str.strip()
    if numero_str.isdigit():
        numero_int = int(numero_str)
        if numero_int < 0:
            return -2
        else:
            return numero_int
    else:
        return -1

def sanitizar_flotante(numero_str:str):
    """
    Recibe un string numerico fltante
    valida que sea un numero flotante positivo
        Si contiene carácteres no numéricos retornar -1
        Si el número es negativo se deberá retornar un -2
        Si ocurren otros errores que no permiten convertirlo a flotante entonces se deberá retornar -3
    Retorna un numero flotante
    """
    numero_str = numero_str.strip()
    for caracter in numero_str:
        if caracter.isdigit() or caracter == ".":
            numero_float = float(numero_str)
            if numero_float < 0:
                return -2
            else:
                return numero_float
        else:
            return -1

def sanitizar_string(valor_str:str, valor_por_defecto:str="-"):
    """
    Recibe un valor_str que es un string que representa el texto a validar, un valor_por_defecto que es un string
    que representa un valor por defecto (inicializar con -)
    La funcion determina si es solo texto, si se encuentra numero retorna "N/A"
    si contiene una barra "/" se reemplaza por un espacio
    si el parametro recibido es solo texto se retorna en todo minusculas
    si el parametro se encuentra vacio y nos pasaron un valor_por_defecto se retorna el valor por defecto convertido a minusculas
    y quita los espacios en blanco
    """
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    if not valor_str:
        return valor_por_defecto.lower()
    
    if valor_str.isalpha():
        valor_str = valor_str.replace("/", " ")
        return valor_str.lower()
    else:
        return "N/A"
    
#3.4
def sanitizar_dato(diccionario:dict, clave:str, tipo_dato:str):
    """
    Recibe un diccionario, una clave tipo str que representa el dato a sanitizas(que este en el diccionario) y un tipo de dato que representa el tipo de dato a sanitizar
    Valida que tipo_dato sea o string o entero o flotante si no se encuentran informa: "Tipo de dato no reconocido"
    valida que la clave excista dentro del diccionario en caso de que no informa: "La clave especificada no existe en el diccionario"
    Retorna True si sanitizo algun dato y False en caso contrario 
    """
    tipo_dato = tipo_dato.lower()
    if clave in diccionario:
        if tipo_dato == "entero":
            valor_sanitizado = sanitizar_entero(diccionario[clave])
            diccionario[clave] = valor_sanitizado
            return True
        elif tipo_dato == "flotante":
            valor_sanitizado = sanitizar_flotante(diccionario[clave])
            diccionario[clave] = valor_sanitizado
            return True
        elif tipo_dato == "string":
            valor_sanitizado = sanitizar_string(diccionario[clave])
            diccionario[clave] = valor_sanitizado
            return True
        else:
            print("Tipo de dato no reconocido")
            return False
    else:
        print("La clave especificada no existe en el diccionario")
        return False

#3.5
def stark_normalizar_datos(lista:list):
    """
    Recibe una lista tipo list
    valida que la lista no este vacia
    Sanitiza los valores, "altura", "peso", "color_ojos", "color_pelo", "fuerza" e "inteligencia"
    Una vez finalizado muestra el mensaje "Datos normalizados"
    """
    if len(lista) > 0:
        for elemento in lista:
            sanitizar_dato(elemento, "altura", "flotante")
            sanitizar_dato(elemento, "peso", "flotante")
            sanitizar_dato(elemento, "color_ojos", "string")
            sanitizar_dato(elemento, "color_pelo", "string")
            sanitizar_dato(elemento, "fuerza", "entero")
            sanitizar_dato(elemento, "inteligencia", "string")
            elemento["altura"] = convertir_cm_a_mtrs(elemento["altura"])
        print("Datos normalizados")
    else:
        print("ERROR: Lista de heroes vacia")

#4.1
def generar_indice_nombres(lista:list):
    """
    Recibe una lista tipo list
    Itera la lista y genera una lista donde cada elemento es el nombre de todos los personajes separado
    por ejemplo ["Howard", "the", "Duck"]
    valida La lista contenga al menos un elemento, Todos los elementos sean del tipo diccionario, todos los elementos contengan la clave ‘nombre’
    si encuentra un error se informa: ‘El origen de datos no contiene el formato correcto"
    """
    if len(lista) > 0:
        lista_nombres = []
        for elemento in lista:
            if type(elemento) == type(dict()) and "nombre" in elemento:
                lista_nombres += elemento["nombre"].split(" ")
            else:
                break
        return lista_nombres
    else:
        print("El origen de datos no contiene el formato correcto")

def stark_imprimir_indice_nombre(lista:list):
    """
    Recibe una lista tipo list
    Muesta por pantalla el indice generado por la funcion generar_indice_nombre() con todos los nombres separados por un guion
    Por ejemplo: Howard-the-duck-Rocket-Raccoon-Wolverine...
    """
    lista_nombres = generar_indice_nombres(lista)
    lista_nombres = "-".join(lista_nombres)
    print(lista_nombres)

#5.1
def convertir_cm_a_mtrs(valor_cm:float):
    """
    Recibe un numero del tipo float que representa los cm
    La funcion retorna el numero recibido, convertido a metros
    Valida que el numero recibido sea positivo
    """
    if valor_cm > 0:
        valor_mtrs = valor_cm / 100
        valor_mtrs = round(valor_mtrs, 2)
        return valor_mtrs
    else:
        return -1

#5.2
def generar_separador(patron:str, largo:int, imprimir:bool=True) -> str:
    """
    Recibe un patron que es un cararcter que se utilizara como patron para generar el separador,
    Recibe un largo que es un número que representa la cantidad de caracteres que va ocupar el separador.
    Recibe imprimir que es un parámetro opcional del tipo booleano (por default definir en True)
    La funcion genera un string que contenga el patron repitiendo como la cantidad recibida como parametro
    Si el parámetro booleano recibido se encuentra en False se deberá solo retornar el separador generado. Si se encuentra en True antes de retornarlo, imprimirlo por pantalla
    Valida que el parametro patron tenga al menos un caracter y como maximo dos y que el largo sea un entero entre 1 y 235 inclusive
    En caso de no verificar las validaciones devuelve "N/A"
    """
    if len(patron) > 0 and len(patron) < 3 and largo > 0 and largo < 236:
        separador = patron * largo
    else:
        return "N/A"
    
    if imprimir:
        print(separador)
    
    return separador

#5.3
def generar_encabezado(titulo:str) -> str:
    """
    Recibe un titulo, un str que representa el titulo de una seccion en la ficha
    La funcion devuelve un str que contenga el titulo envuelto entre dos separadores(estimar el largo segun tu pantalla)
    La funcion conviete el titulo a mayusculas
    ejemplo:
    ********************************************************************************
    PRINCIPAL
    ********************************************************************************
    """
    titulo = titulo.upper()
    separador = generar_separador("*", 170, False)
    encabezado = "{0}\n{1}\n{2}\n".format(separador, titulo, separador)
    return encabezado

#5.4
def imprimir_ficha_heroe(heroe:dict) -> str:
    """
    Recibe un heroe tipo dict
    Y a traves de la funcion generar_encabezado() genera un encabezado para cada categoria del heroe(PRINCIPAL,FISICO,SEÑAS PARTICULARES)
    Y al final junto los tres encabezados y los muestra
    """
    principal = generar_encabezado("PRINCIPAL")
    fisico = generar_encabezado("FISICO")
    señas_particulares = generar_encabezado("SEÑAS PARTICULARES")
    ficha_principal = "{0}\nNOMBRE DEL HÉROE: {1}\nIDENTIDAD SECRETA: {2}\nCONSULTORA: {3}\nCÓDIGO DE HEROE: {4}\n".format(principal, heroe["nombre"], heroe["identidad"],heroe["empresa"],heroe["codigo_heroe"])
    ficha_fisico = "{0}\nALTURA: {1} Mtrs.\nPESO: {2} Kg.\nFUERZA: {3} N\n".format(fisico,heroe["altura"],heroe["peso"],heroe["fuerza"])
    ficha_señas_particulares = "{0}\nCOLOR DE OJOS: {1}\nCOLOR DE PELO: {2}\n".format(señas_particulares,heroe["color_ojos"],heroe["color_pelo"])
    ficha = "{0}{1}{2}".format(ficha_principal, ficha_fisico, ficha_señas_particulares)
    print(ficha)

def stark_navegar_fichas(lista:list) -> str:
    """
    Recibe una lista con heroes
    Y muestra la ficha de cada uno usando la funcion imprimir_ficha_heroe()
    Y a traves de opciones el usuario puede ir moviendose entre fichas de izquierda a derecha, y salir
    """
    i = 0
    imprimir_ficha_heroe(lista[0])
    opciones = "Ingrese una de las siguientes opciones:\n        [1] Ir a la izquierda      [2] Ir a la derecha      [S] Salir\n"
    while True:
        opcion = input("{0}".format(opciones)).upper()
        
        if opcion == "1":
            i -= 1
            if i < 0:
                i = len(lista) - 1
            imprimir_ficha_heroe(lista[i])
        
        elif opcion == "2":
            i += 1
            if i > len(lista) - 1:
                i = 0
            imprimir_ficha_heroe(lista[i])
        
        elif opcion == "S":
            break

        else:
            opcion = input("{0}".format(opciones)).upper()

#6.1
def imprimir_menu():
    """
    No recibe nada
    Genera un separador "-" de 170 caracteres de largo utilizando la funcion generar_separador()
    y imprime un menu de opciones
    """
    separador = generar_separador("-", 170, False)
    menu = "1 - Imprimir la lista de nombres junto con sus iniciales\n2 - Generar códigos de héroes\n3 - Normalizar datos\n4 - Imprimir índice de nombres\n5 - Navegar fichas\nS - Salir\n{0}\n".format(separador)
    print(menu)

def stark_menu_principal():
    """
    Imprime el menu utilizando la funcion imprimir_menu()
    y le pide una opcion al usuario
    y la retorna
    """
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    return opcion

def stark_marvel_app_3(lista:list):
    """
    La funcion se encarga de la ejecucion del programa
    """
    while True:
        opcion = stark_menu_principal()
        if opcion == "1":
            stark_imprimir_nombres_con_iniciales(lista)
        elif opcion == "2":
            stark_generar_codigo_heroes(lista)
        elif opcion == "3":
            stark_normalizar_datos(lista)
        elif opcion == "4":
            stark_imprimir_indice_nombre(lista)
        elif opcion == "5":
            stark_navegar_fichas(lista)
        elif opcion == "S":
            break
        else:
            opcion = stark_menu_principal()