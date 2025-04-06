# Trabajo con Archivos de Texto en Python

# --- Escritura de archivo ---
# Abrimos (o creamos) el archivo 'my_notes.txt' en modo escritura ('w')
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Hoy aprendí cómo manejar archivos en Python.\n")
    file.write("Es importante cerrar los archivos luego de usarlos.\n")
    file.write("Practicar con ejemplos me ayuda a entender mejor.\n")

# --- Lectura del archivo ---
# Abrimos el archivo en modo lectura ('r')
with open("my_notes.txt", "r") as file:
    # Leemos línea por línea usando un bucle
    for line in file:
        # Mostramos cada línea en la consola
        print(line.strip())  # .strip() elimina los saltos de línea al final

# Nota: Usamos 'with' para abrir archivos, lo cual asegura que se cierren automáticamente
