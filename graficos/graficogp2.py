import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np

# Conexión a la base
conexion = sqlite3.connect('encuesta.db')

# Leer datos solo del participante 5
df = pd.read_sql_query("""
SELECT pregunta, respuesta
FROM respuestas
WHERE id_participante = 5
""", conexion)

if df.empty:
    print("⚠️ No hay respuestas para el participante con id = 5.")
else:
    plt.figure(figsize=(10, 6))

    # Crear gráfico simple de columnas
    plt.bar(df['pregunta'], df['respuesta'], width=0.5)

    plt.title("Respuestas del participante 5")
    plt.xlabel("Preguntas")
    plt.ylabel("Respuestas")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

conexion.close()
