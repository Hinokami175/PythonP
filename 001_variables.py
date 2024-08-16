#variables
#variable tipo string
my_variable ="My String Variable"
print(my_variable)
##variable tipo int
my_int_variable =8
print(my_int_variable)
##conversion de una variable de tipo int a String
my_int_to_str_variable=str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
#variable tipo boolean
my_bool_variable = False
print(my_bool_variable)
##concatenaciónd de variables en un print
print(my_variable,my_int_variable,my_bool_variable)
#prueba rara de del print de un type de un print
#algunas funciones del sistemafuncion lenght
print(len(my_variable))
print("Este es el valor de:",my_bool_variable)
#VARIABLES EN UNA SOLA linea Cuidado con abusar de esta sintaxis
name, surname,alias,age= "juan","diez","JUANJI",35
print("me llamo",name,surname,". mi edad es", age,". y mi alias es",alias)
# inputs
""""
first_name= input("Cual es tu nombre")
age = input("Cual es tu edad?")
print(first_name)
print(age)
"""

name =35
age ="brais"
print(name)
print(age)
#fozamos el tipo?
address: str ="Mi dirección"
address=32
print(type(address))
age:int = input("edad del dante?:")
print(type(age))