# El simbolo # indica un comentario en Python

# Empezamos con un ejemplo sencillo que es un "Hola Mundo"

print("Hola Mundo")  # print(): Imprime el texto "Hola Mundo" en la consola

# Haremos lo mismo con un "hola Python"

print("Hola Python")  # Imprime el texto "Hola Python" en la consola

"""
Podemos realizar un comentario de varias líneas utilizando comillas triples.
Esto es útil para explicar el código o dejar notas.
Este es un comentario de varias líneas.
Podemos usar comillas triples para crear comentarios de varias líneas.
"""

'''
Otro ejemplo de comentario de varias líneas.
También podemos usar comillas simples para comentarios de varias líneas.
'''

# Vamos a ver cadenas de texto (strings) y cómo imprimirlas
# Las cadenas de texto son secuencias de caracteres encerradas entre comillas
# Podemos usar comillas dobles o simples para definir cadenas de texto

print("¡Hola, Python!")  # Imprime el texto "¡Hola, Python!" en la consola
print('¡Hola, Python!')  # También podemos usar comillas simples para cadenas de texto

# Las comillas dobles y simples son equivalentes en Python para definir cadenas de texto

# Podemos usar comillas triples para cadenas de texto que ocupan varias líneas

print("""Este es un ejemplo de una cadena de texto
que ocupa varias líneas.Podemos usar comillas triples para definir cadenas de texto
que abarcan varias líneas.""")  # Imprime una cadena de texto de varias líneas

# También podemos usar comillas simples triples para cadenas de texto de varias líneas

print('''Este es otro ejemplo de una cadena de texto
que ocupa varias líneas.Podemos usar comillas simples triples para definir cadenas de texto
que abarcan varias líneas.''')  # Imprime otra cadena de texto de varias líneas

# Ahora vamos a ver type y cómo funciona con diferentes tipos de datos

# Consultamos el tipo de dato de diferentes valores utilizando la función type()
# y lo imprimimos en la consola

print(type("Hola Python"))  # Imprime el tipo de dato de la cadena "Hola Python"
print(type(42))  # Imprime el tipo de dato del número entero 42
print(type(3.14))  # Imprime el tipo de dato del número de punto flotante o con decimal 3.14 float
print(type(1 + 2j))  # Imprime el tipo de dato del número complejo 1 + 2j
print(type([1, 2, 3]))  # Imprime el tipo de dato de una lista [1, 2, 3]
print(type((1, 2, 3)))  # Imprime el tipo de dato de una tupla (1, 2, 3)
print(type({'a': 1, 'b': 2}))  # Imprime el tipo de dato de un diccionario {'a': 1, 'b': 2}
print(type({1, 2, 3}))  # Imprime el tipo de dato de un set o conjunto {1, 2, 3}
print(type({9.8, 3.14, 2.7})) # imprime el tipo de datos set o conjunto con números de punto flotante
print(type(True))  # Imprime el tipo de dato del valor booleano True
print(type(None))  # Imprime el tipo de dato del valor None (nulo)

# Podemos usar type() para verificar el tipo de dato de una variable