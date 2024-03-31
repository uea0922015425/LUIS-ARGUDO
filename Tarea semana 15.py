# Tarea semana 15
#Luis Argudo

# Crear un diccionario llamado informacion_personal con información ficticia
informacion_personal = {
    "Nombre": "Martin Carrion",
    "Edad": 40,
    "Ciudad": "Manta",
    "Profesion": "Bombero"
}
# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["Ciudad"] = "Manta"
# Agregar una nueva clave-valor que represente la "profesion" de la persona
informacion_personal["Profesion"] = "Bombero"
# Verificar si la clave "telefono" existe y, si no existe, agregarla con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "2540-306"
# Eliminar la clave "edad" del diccionario
del informacion_personal["Edad"]
# Imprimir el diccionario resultante en formato vertical
for key, value in informacion_personal.items():
    print(f"{key}: {value}")