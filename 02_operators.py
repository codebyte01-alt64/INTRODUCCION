# Operadores arítméticos y de cadenas en Python
# Vamos a ver cómo funcionan los operadores aritméticos y de cadenas en Python

print(3 + 4)  # Suma: Imprime el resultado de la suma de 3 y 4, que es 7
print(10 - 5)  # Resta: Imprime el resultado de la resta de 10 menos 5, que es 5
print(2 * 3)  # Multiplicación: Imprime el resultado de la multiplicación de 2 por 3, que es 6
print(8 / 2)  # División: Imprime el resultado de la división de 8 entre 2, que es 4.0
print(5 % 2)  # Módulo: Imprime el residuo de la división de 5 entre 2, que es 1
print(2 ** 3)  # Exponente: Imprime el resultado de 2 elevado a la potencia de 3, que es 8
print(10 // 3)  # División entera: Imprime el resultado de la división entera de 10 entre 3, que es 3
print(2 ** 3 + 5 - 6 * 2 / 4  // 2)  # Operaciones combinadas: Imprime el resultado de la expresión, que es 8 + 5 - 3 = 10.0

print("Hola " + "Python")  # Concatenación de cadenas: Imprime "HolaPython" al unir las dos cadenas
print("Hola " * 3)  # Repetición de cadenas: Imprime "Hola" tres veces, resultando en "HolaHolaHola"
print("Hola " + " " + "Python")  # Concatenación con espacio: Imprime "Hola Python" al unir las cadenas con un espacio
print("Hola " * 2 + " " + "Python")  # Repite "Hola" dos veces y concatena con " Python", resultando en "HolaHola Python"
print("Hola " + str(3))  # Concatenación de cadena y número: Convierte el número 3 a cadena y lo une a "Hola", resultando en "Hola3"
print("Hola " + str(3) + " " + "Python")  # Convierte el número 3 a cadena y lo une a "Hola" y "Python", resultando en "Hola3 Python"
print("Hola " * (2 ** 3))  # Repite "Hola" ocho veces (2 elevado a 3), resultando en "Hola" repetido ocho veces

my_float = 2.5 * 2
print("Hola " * int(my_float))  # Convierte el resultado de 2.5 * 2 a entero (5) y lo repite, resultando en "Hola" repetido cinco veces
print("Hola " * int(2.5 * 2))  # Repite "Hola" cinco veces, ya que 2.5 * 2 es 5.0 y se convierte a entero

# Operadores de comparación en Python

print(3 == 3)  # Igualdad: Imprime True porque 3 es igual a 3
print(3 != 4)  # Desigualdad: Imprime True porque 3 no es igual a 4
print(3 < 4)  # Menor que: Imprime True porque 3 es menor que 4
print(4 > 3)  # Mayor que: Imprime True porque 4 es mayor que 3
print(3 <= 3)  # Menor o igual que: Imprime True porque 3 es igual a 3
print(4 >= 3)  # Mayor o igual que: Imprime True porque 4 es mayor que 3
print(3 == 3.0)  # Igualdad entre entero y flotante: Imprime True porque 3 es igual a 3.0
print(3 == "3")  # Igualdad entre entero y cadena: Imprime False porque 3 (entero) no es igual a "3" (cadena)
print(3 != 3.0)  # Desigualdad entre entero y flotante: Imprime False porque 3 es igual a 3.0

print("Hola" > "Python")  # Comparación de cadenas: Imprime False porque "Hola" es menor que "Python" en orden lexicográfico
print("Hola" < "Python")  # Comparación de cadenas: Imprime True porque "Hola" es menor que "Python" en orden lexicográfico
print("Hola" == "Hola")  # Igualdad de cadenas: Imprime True porque ambas cadenas son iguales
print("Hola" != "Python")  # Desigualdad de cadenas: Imprime True porque "Hola" no es igual a "Python"
print("Hola" <= "Hola")  # Menor o igual que: Imprime True porque "Hola" es igual a "Hola"
print("Hola" >= "Python")  # Mayor o igual que: Imprime False porque "Hola" es menor que "Python"
print("Hola" == "hola")  # Comparación de cadenas con diferente capitalización: Imprime False porque "Hola" no es igual a "hola"
print("Hola" == "Hola ")  # Comparación de cadenas con espacio: Imprime False porque "Hola" no es igual a "Hola "
print("Hola" == "Hola".upper())  # Comparación de cadenas con mayúsculas: Imprime False porque "Hola" no es igual a "HOLA"
print("Hola" == "Hola".lower())  # Comparación de cadenas con minúsculas: Imprime True porque "Hola" es igual a "Hola"
print(len("Hola") == 4)  # Longitud de cadena: Imprime True porque la longitud de "Hola" es 4
print(len("aaaa") >= len("aaaa")) # Longitud de cadenas: Imprime True porque la longitud de "aaaa" es igual a la de "aaaa"

# Operadores lógicos en Python

print(3 > 4 and "Hola" > "Python")  # AND lógico: Imprime False porque 3 no es mayor que 4
print(3 < 4 and "Hola" > "Python") # AND lógico: Imprime False porque "Hola" no es mayor que "Python"
print(3 < 4 or "Hola" > "Python") # OR lógico: Imprime True porque 3 es menor que 4
print(3 > 4 or "Hola" < "Python") ## OR lógico: Imprime False porque 3 no es mayor que 4 y "Hola" no es menor que "Python"
print(not (3 < 4))  # NOT lógico: Imprime False porque 3 es menor que 4, y negarlo da False







