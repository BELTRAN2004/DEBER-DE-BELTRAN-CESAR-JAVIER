# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Barcelona"

# Agregar una nueva clave-valor para "telefono"
informacion_personal["telefono"] = "123-456-789"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "987-654-321"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
