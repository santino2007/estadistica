import sqlite3
import tkinter as tk
from tkinter import Menu, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#--------------------------------------------------------------
basedatos = "encuesta.db"
#--------------------------------------------------------------
def obtener_preguntas_y_respuestas():
    conexion = sqlite3.connect(basedatos)
    cursor = conexion.cursor()

    cursor.execute("SELECT id_curso FROM cursos WHERE curso='3' AND seccion='A'")
    curso = cursor.fetchone()
    if not curso:
        conexion.close()
        return {}

    id_curso = curso[0]
    cursor.execute("SELECT id_participante FROM participantes WHERE id_curso=?", (id_curso,))
    alumnos = [fila[0] for fila in cursor.fetchall()]
    if not alumnos:
        conexion.close()
        return {}

    datos = {}
    for alumno in alumnos:
        cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE id_participante=?", (alumno,))
        filas = cursor.fetchall()
        for pregunta, respuesta in filas:
            if pregunta not in datos:
                datos[pregunta] = []
            if respuesta:
                datos[pregunta].append(respuesta.strip())

    conexion.close()
    return datos

def mostrar_grafico(frame, pregunta, respuestas):
    for w in frame.winfo_children():
        w.destroy()

    conexion = sqlite3.connect(basedatos)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT respuesta, COUNT(*) 
        FROM respuestas 
        WHERE pregunta=? 
        AND id_participante IN (
            SELECT id_participante FROM participantes 
            WHERE id_curso IN (
                SELECT id_curso FROM cursos WHERE curso='3' AND seccion='A'
            )
        )
        GROUP BY respuesta
    """, (pregunta,))
    resultados = cursor.fetchall()
    conexion.close()

    if not resultados:
        messagebox.showinfo("Sin datos", "No hay respuestas para esta pregunta.")
        return

    etiquetas = [r[0] if r[0] else "(sin respuesta)" for r in resultados]
    valores = [r[1] for r in resultados]

    if all(e.lower() in ["si", "sí", "no"] for e in etiquetas):
        tipo = "binaria"
    elif all(v.isdigit() for v in etiquetas):
        tipo = "numerica"
    elif any(len(e) > 25 for e in etiquetas):
        tipo = "texto_largo"
    elif len(etiquetas) <= 6:
        tipo = "opciones"
    else:
        tipo = "general"

    fig, ax = plt.subplots(figsize=(6, 4))

    if tipo == "binaria":
        ax.pie(valores, labels=etiquetas, autopct='%1.1f%%')
        ax.set_title(pregunta)
    elif tipo == "numerica":
        ax.plot(etiquetas, valores, marker="o")
        ax.set_xlabel("Valor")
        ax.set_ylabel("Cantidad")
        ax.set_title(pregunta)
    elif tipo == "texto_largo":
        ax.barh(etiquetas, valores)
        ax.set_title(pregunta)
    else:
        ax.bar(etiquetas, valores)
        ax.set_ylabel("Cantidad")
        ax.set_title(pregunta)
        ax.set_xticklabels(etiquetas, rotation=35, ha='right', fontsize=8)

    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

class MenuApp:
    def __init__(self, master, preguntas):
        self.master = master
        self.preguntas = preguntas
        self.crear_menu()

        self.area = tk.Frame(master, bg="#f8f8f8")
        self.area.pack(fill="both", expand=True)

    def crear_menu(self):
        barra_menu = Menu(self.master)
        self.master.config(menu=barra_menu)

        menu_preguntas = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Preguntas", menu=menu_preguntas)

        for pregunta in sorted(self.preguntas.keys()):
            texto = pregunta if len(pregunta) < 50 else pregunta[:47] + "..."
            menu_preguntas.add_command(
                label=texto,
                command=lambda q=pregunta: mostrar_grafico(self.area, q, self.preguntas[q])
            )

        barra_menu.add_command(label="Salir", command=self.master.quit)

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Encuesta del curso 3°A")
        self.root.geometry("950x650")

        preguntas = obtener_preguntas_y_respuestas()
        if not preguntas:
            messagebox.showinfo("Sin datos", "No se encontraron respuestas de 3A.")
            self.root.destroy()
            return

        self.menu_app = MenuApp(self.root, preguntas)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()