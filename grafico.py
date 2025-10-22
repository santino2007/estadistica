import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conexion = sqlite3.connect('encuesta.db')

df = pd.read_sql_query("""
SELECT pregunta, respuesta
FROM respuestas
WHERE id_participante = 5
""", conexion)

if df.empty:
    print("⚠️ No hay respuestas para el participante con id = 5.")
else:
    plt.figure(figsize=(10, 6))
    plt.barh(df['pregunta'], df['respuesta'])
    plt.title("Respuestas del participante 5 3A")
    plt.xlabel("Valor de respuesta")
    plt.ylabel("Preguntas")
    plt.tight_layout()
    plt.show()

conexion.close()
