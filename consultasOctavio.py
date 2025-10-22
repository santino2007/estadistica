import sqlite3
conexion=sqlite3.connect("encuesta.db")
cursor = conexion.cursor()

print("conexion establecida con exito")

cursor.execute("SELECT * FROM participantes")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")

cursor.execute("SELECT curso, seccion FROM cursos WHERE curso ='3' AND seccion='A'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------") 

cursor.execute("SELECT participantes.id_curso, participantes.id_participante, respuestas.id_respuesta, respuestas.pregunta, respuestas.respuesta FROM participantes JOIN respuestas ON participantes.id_participante = respuestas.id_participante WHERE particiantes.id_curso='5'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")

cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE id_participante=8 AND curso='3' AND seccion='A'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")
    
cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE respuesta='Si' AND  curso='3' AND seccion='A'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")
    
cursor.execute("SELECT id_participante FROM participantes WHERE curso='3' AND seccion='A'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")
    
cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE respuesta='Mas de 9 Horas'AND curso='3' AND seccion='A'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")
    
cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE respuesta='16' AND curso='3' AND seccion='A'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")
    
cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE pregunta='¿Que opinas sobre ella?' AND curso='3' AND seccion='B'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)



conexion.close()