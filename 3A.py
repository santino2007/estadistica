import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conexion = sqlite3.connect("encuesta.db")
cursor = conexion.cursor()

cursor.execute("SELECT id_participante,pregunta,respuesta  FROM respuestas WHERE id_participante like 5")
info=cursor.fetchall()
#tod la info de la base de dato de 3A
for fila in info:
    print("-------------------------------------")
    print(fila)

#uso de telefono en fuera de la escuela y dentro
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 81 ")
info2=cursor.fetchall()
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 82")
info3=cursor.fetchall()
for fila2 in info2:
    print("------------------------------------")
    print(fila2)
    print(info3)

#edad
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 78 ")
info4=cursor.fetchall()
for fila3 in info4:
    print("---------------------------------------")
    print(info4)

#si o no
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 79 ")
info5=cursor.fetchall()
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 85 ")
info6=cursor.fetchall()
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 86 ")
info7=cursor.fetchall()
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 93 ")
info8=cursor.fetchall()
for fila4 in info5:
    print("------------------------------------------")
    print(fila4)
    print(info6)
    print(info7)
    print(info8) 

#marca temporal
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 77 ")
info9=cursor.fetchall()
for fila5 in info9:
    print("-----------------")
    print(fila5)

#precupacion de uso del telefono y iA
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 92 ")
info10=cursor.fetchall()
for fila6 in info10:
    print("--------------------------------------")
    print(fila6)


#pregunta repodidas con pablas
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 88 ")
info11=cursor.fetchall()
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 89 ")
info12=cursor.fetchall()
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 94 ")
info13=cursor.fetchall()
cursor.execute("SELECT pregunta,respuesta FROM respuestas  WHERE id_respuesta = 95 ")
info14=cursor.fetchall()
for fila7 in info11:
    print("--------------------------------")
    print(fila7)
    print(info12)
    print(info13)
    print(info14)




cursor.execute("SELECT * FROM participantes")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")

cursor.execute("SELECT curso, seccion FROM cursos WHERE seccion='B'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------") 

cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE id_participante=1")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")

cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE id_participante=8")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")
    
cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE respuesta='Si'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")
    
cursor.execute("SELECT id_participante FROM participantes WHERE id_curso='5'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")
    
cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE respuesta='Mas de 9 Horas'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")
    
cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE respuesta='16'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
print("----------------------------------------------------------------------------------------------------------------------------------")
    
cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE pregunta='¿Que opinas sobre ella?'")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)