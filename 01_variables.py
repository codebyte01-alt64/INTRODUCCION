""""
Que es una variable?
Una variable es un espacio en la memoria que se utiliza para almacenar un valor.
Podemos pensar en una variable como una caja que contiene un valor.
Podemos asignar un valor a una variable utilizando el operador de asignación (=).
"""
# Por ejemplo, podemos crear una variable llamada "mi_variable" y asignarle el valor 10.

mi_variable = 10  # Asignamos el valor 10 a la variable mi_variable

# Ahora podemos imprimir el valor de la variable mi_variable en la consola

print(mi_variable)  # Imprime el valor de la variable mi_variable, que es 10

# También podemos cambiar el valor de la variable mi_variable

mi_variable = 20  # Asignamos un nuevo valor, 20, a la variable mi_variable

print(mi_variable)  # Imprime el nuevo valor de la variable mi_variable, que es 20

# ejemplo de variable con string

my_string_variable = "My String Variable" # Asignamos un string a la variable MyVariable

print(my_string_variable)  # Imprime el valor de la variable MyVariable, que es "My String Variable"

# ejemplo con entero

my_int_variable = 42  # Asignamos un entero a la variable MyIntVariable

print(my_int_variable)  # Imprime el valor de la variable MyIntVariable, que es 42

# ejemplo de variable entero a string

my_int_to_string = str(my_int_variable)  # Convertimos el entero a string

print(my_int_to_string)  # Imprime el valor de la variable MyIntToString, que es "42"

print(type(my_int_to_string))  # Imprime el tipo de dato de la variable MyIntToString, que es <class 'str'>

# ejemplo con float

my_float_variable = 3.14  # Asignamos un número de punto flotante a la variable MyFloatVariable

print(my_float_variable)  # Imprime el valor de la variable MyFloatVariable, que es 3.14

# ejemplo con boolean  

my_bool_variable = True  # Asignamos un valor booleano a la variable MyBoolVariable

print(my_bool_variable)  # Imprime el valor de la variable MyBoolVariable, que es True

# ejemplo con None

my_none_variable = None  # Asignamos el valor None a la variable MyNoneVariable

print(my_none_variable)  # Imprime el valor de la variable MyNoneVariable, que es None

# ejemplo con lista

my_list_variable = [1, 2, 3, 4, 5]  # Asignamos una lista a la variable MyListVariable

print(my_list_variable)  # Imprime el valor de la variable MyListVariable, que es [1, 2, 3, 4, 5]

# ejemplo con tupla

my_tuple_variable = (1, 2, 3)  # Asignamos una tupla a la variable MyTupleVariable

print(my_tuple_variable)  # Imprime el valor de la variable MyTupleVariable, que es (1, 2, 3)

# ejemplo con diccionario

my_dict_variable = {'key1': 'value1', 'key2': 'value2'}  # Asignamos un diccionario a la variable MyDictVariable

print(my_dict_variable)  # Imprime el valor de la variable MyDictVariable, que es {'key1': 'value1', 'key2': 'value2'}

# ejemplo con set

my_set_variable = {1, 2, 3}  # Asignamos un conjunto a la variable MySetVariable

print(my_set_variable)  # Imprime el valor de la variable MySetVariable, que es {1, 2, 3}

# ejemplo con set de float

my_float_set_variable = {9.8, 3.14, 2.7}  # Asignamos un conjunto de números de punto flotante a la variable MyFloatSetVariable 

print(my_float_set_variable)  # Imprime el valor de la variable MyFloatSetVariable, que es {9.8, 3.14, 2.7}

# ejemplo con variable de tipo complejo

my_complex_variable = 1 + 2j  # Asignamos un número complejo a la variable MyComplexVariable

print(my_complex_variable)  # Imprime el valor de la variable MyComplexVariable, que es 1 + 2j

# tipos de impresión de variables concatenacion  de variables

print(my_string_variable, my_int_to_string, my_bool_variable) # imprime las variables solicitadas en una sola línea como una cadena

print("Este es el valor de:", my_int_variable)  # Imprime el texto "Este es el valor de:" seguido del valor de la variable my_int_variable)

# Algunas Funciones del sistema 

print(len(my_string_variable))  # Imprime la longitud de la cadena my_string_variable

print(type(my_string_variable))  # Imprime el tipo de dato de la variable my_string_variable, que es <class 'str'>

print(type(my_int_to_string))  # Imprime el tipo de dato de la variable my_int_to_string, que es <class 'str'>

# Variables en una sola línea

name,  surname, alias, age = "german", "hernandez", "Piboxor", 47  # Asignamos valores a las variables name y surname en una sola línea

print("Me llamo: ", name, surname, "Y mi alias es: ", alias, "Mi edad es: ", age, "Años")  # Imprime los valores de las variables name, surname, alias y age en una sola línea

# funcion input para recibir datos del usuario

first_name = input("Ingrese su nombre: ")  # Solicita al usuario que ingrese su nombre y lo almacena en la variable first_name
age = input("Ingrese su edad: ")  # Solicita al usuario que ingrese su edad y lo almacena en la variable age

print("Hola", first_name, "tienes", age, "años")  # Imprime un saludo al usuario con su nombre y edad

# Forzamos el tipo de dato

address: str = input("Ingrese su dirección: ")  # Solicita al usuario que ingrese su dirección y lo almacena en la variable address como una cadena de texto

address = 25  # Asignamos un valor entero a la variable address, lo que sobrescribe el valor ingresado por el usuario

print("Su dirección es:", address)  # Imprime el valor de la variable address, que ahora es un entero

