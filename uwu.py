# Definir la gramática
gramatica = {
    'S': ['E'],
    'E': ['E+T', 'T'],
    'T': ['T*F', 'F'],
    'F': ['(E)', 'id']
}

# Definir la tabla de análisis
tabla_analisis = {
    ('E', 'id'): ('T', 'E'),
    ('E', '('): ('T', 'E'),
    ('T', 'id'): ('F', 'T'),
    ('T', '('): ('F', 'T'),
    ('F', 'id'): ('id',),
    ('F', '('): ('(E)',)
}

def analisis_sintactico(cadena):
    pila = ['$', 'S']  # Pila inicial con el símbolo de inicio
    entrada = cadena + '$'
    indice = 0

    while len(pila) > 0:
        simbolo_actual = pila[-1]
        token_actual = entrada[indice]

        if simbolo_actual == token_actual:
            pila.pop()
            indice += 1
        elif simbolo_actual in gramatica:
            producciones = gramatica[simbolo_actual]
            coincidencia = False

            for produccion in producciones:
                if (simbolo_actual, token_actual) in tabla_analisis and \
                        tabla_analisis[(simbolo_actual, token_actual)] == tuple(produccion.split()):
                    coincidencia = True
                    break

            if coincidencia:
                pila.pop()
                produccion_reversa = produccion.split()[::-1]

                for simbolo in produccion_reversa:
                    pila.append(simbolo)
            else:
                print("Error de sintaxis")
                return False
        else:
            print("Error de sintaxis")
            return False

    if simbolo_actual == '$' and token_actual == '$':
        print("La cadena es válida")
        return True
    else:
        print("Error de sintaxis")
        return False

# Ejemplo de uso
cadena = 'id+(id*id)$'  # Cadena de prueba
analisis_sintactico(cadena)
