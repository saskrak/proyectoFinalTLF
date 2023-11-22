import re

# Definir expresiones regulares para cada tipo de token
expresion_numero_natural = r'\b[0-9]+\b'
expresion_numero_real = r'\b[0-9]+(\.[0-9]+)?\b' 
expresion_identificador = r'\b[a-zA-Z_][a-zA-Z0-9_]{0,9}\b' 
expresion_palabra_reservada = r'\b(if|else|while|for|func|return)\b' #mal
expresion_operador_aritmetico = r'[\+\-\*/]'
expresion_operador_comparacion = r'[=<>]=?|!='
expresion_operador_logico = r'(&&|\|\||!)' 
expresion_operador_asignacion = r'='
expresion_operador_incremento_decremento = r'\+\+|\-\-' 
expresion_parentesis = r'[\(\)]'
expresion_llaves = r'[{}]'
expresion_terminal = r';'
expresion_separador = r','
expresion_hexadecimal = r'\b[0-9A-Fa-f]+\b'
expresion_cadena_caracteres = r'"[^"]*"'
expresion_comentario_linea = r'\/\/.*$' 
expresion_comentario_bloque = r'\/\*[\s\S]*?\*\/'

# Diccionario para mapear expresiones regulares a descripciones de tokens
expresiones_token = {
    expresion_numero_natural: "Número Natural",
    expresion_numero_real: "Número Real",
    expresion_identificador: "Identificador",
    expresion_palabra_reservada: "Palabra Reservada",
    expresion_operador_aritmetico: "Operador Aritmético",
    expresion_operador_comparacion: "Operador de Comparación",
    expresion_operador_logico: "Operador Lógico",
    expresion_operador_asignacion: "Operador de Asignación",
    expresion_operador_incremento_decremento: "Operador de Incremento/Decremento",
    expresion_parentesis: "Paréntesis",
    expresion_llaves: "Llaves",
    expresion_terminal: "Terminal",
    expresion_separador: "Separador",
    expresion_hexadecimal: "Número Hexadecimal",
    expresion_cadena_caracteres: "Cadena de Caracteres",
    expresion_comentario_linea: "Comentario de Línea",
    expresion_comentario_bloque: "Comentario de Bloque"
}

def analizar_token(entrada):
    for expresion, descripcion in expresiones_token.items():
        match = re.fullmatch(expresion, entrada)
        if match:
            longitud = len(match.group(0))
            if longitud == len(entrada):
                if entrada == "if" or entrada == "else" or entrada == "while" or entrada == "for" or entrada == "func" or entrada == "return":
                    return f"'{entrada}' es una Palabra Reservada "
                elif descripcion == "Identificador" and longitud  > 10:
                    return "Token no reconocido."
                else:
                    return f"'{entrada}' es un {descripcion}."
    return "Token no reconocido."


while True:
    entrada = input("Si desea salir escriba 'salir' o si no continue ")
    if entrada == "salir":
        break  # Sal del bucle si se ingresa "salir"
    else:
        # Realiza alguna operación o procesamiento con la entrada
        entrada_usuario = input("Ingrese un token: ")
        mensaje = analizar_token(entrada_usuario)
        print(mensaje)


