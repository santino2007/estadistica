import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

base = "encuesta.db"

# ================================
# Obtener preguntas y respuestas
# ================================
def obtener_preguntas_y_respuestas():
    try:
        conexion = sqlite3.connect(base)
        cursor = conexion.cursor()

        # Verificar si las tablas necesarias existen
        tablas = [t[0] for t in cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")]
        requeridas = {"cursos", "participantes", "respuestas"}
        faltan = requeridas - set(tablas)
        if faltan:
            messagebox.showerror("Error", f"Faltan las tablas: {', '.join(faltan)}")
            conexion.close()
            return {}

        # Buscar el curso 3°A
        cursor.execute("SELECT id_curso FROM cursos WHERE curso='3' AND seccion='A'")
        curso = cursor.fetchone()
        if not curso:
            conexion.close()
            return {}

        id_curso = curso[0]

        # Obtener participantes de ese curso
        cursor.execute("SELECT id_participante FROM participantes WHERE id_curso=?", (id_curso,))
        alumnos = [fila[0] for fila in cursor.fetchall()]
        if not alumnos:
            conexion.close()
            return {}

        # Obtener todas las respuestas
        datos = {}
        for alumno in alumnos:
            cursor.execute("SELECT pregunta, respuesta FROM respuestas WHERE id_participante=?", (alumno,))
            for pregunta, respuesta in cursor.fetchall():
                if not pregunta:
                    continue
                if pregunta not in datos:
                    datos[pregunta] = []
                if respuesta:
                    datos[pregunta].append(str(respuesta).strip())

        conexion.close()
        return datos

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer la base de datos:\n{e}")
        return {}

# ================================
# Verificar si respuestas son numéricas
# ================================
def es_numerica(respuestas):
    if not respuestas:
        return False
    num = 0
    for r in respuestas:
        try:
            float(str(r).replace(",", "."))
            num += 1
        except:
            pass
    return (num / len(respuestas)) >= 0.6

# ================================
# Mostrar gráfico
# ================================
def mostrar_grafico(frame, pregunta, respuestas):
    for w in frame.winfo_children():
        w.destroy()

    if not respuestas:
        messagebox.showinfo("Sin datos", "No hay respuestas para esta pregunta.")
        return

    fig, ax = plt.subplots(figsize=(6, 4))
    fig.suptitle(pregunta, fontsize=10)

    # Tipo 1: Pregunta numérica → histograma
    if es_numerica(respuestas):
        numeros = []
        for r in respuestas:
            try:
                numeros.append(float(str(r).replace(",", ".")))
            except:
                pass
        if numeros:
            ax.hist(numeros, bins='auto', edgecolor='black')
            ax.set_xlabel("Valor")
            ax.set_ylabel("Frecuencia")
        else:
            ax.text(0.5, 0.5, "No se pudieron interpretar valores numéricos", ha='center')

    # Tipo 2: Pregunta Sí/No → gráfico circular
    elif all(str(r).lower() in ["sí", "si", "no"] for r in respuestas):
        si = sum(1 for r in respuestas if str(r).lower() in ["sí", "si"])
        no = sum(1 for r in respuestas if str(r).lower() == "no")
        ax.pie([si, no], labels=["Sí", "No"], autopct="%1.1f%%", startangle=90)
        ax.axis("equal")

    # Tipo 3: Opciones múltiples → barras horizontales
    elif len(set(respuestas)) <= 8:
        conteo = {}
        for r in respuestas:
            r = r if r else "(sin respuesta)"
            conteo[r] = conteo.get(r, 0) + 1
        etiquetas = list(conteo.keys())
        valores = list(conteo.values())
        ax.barh(etiquetas, valores)
        ax.set_xlabel("Cantidad")
        ax.set_ylabel("Opciones")
        ax.grid(axis='x', linestyle='--', alpha=0.6)

    # Tipo 4: Texto libre → palabras más frecuentes
    else:
        palabras = []
        for r in respuestas:
            palabras += [p.lower() for p in str(r).split() if len(p) > 3]
        conteo = {}
        for p in palabras:
            conteo[p] = conteo.get(p, 0) + 1
        if conteo:
            top = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:10]
            palabras_top = [x[0] for x in top]
            valores = [x[1] for x in top]
            ax.barh(palabras_top, valores)
            ax.set_xlabel("Frecuencia")
            ax.set_ylabel("Palabras")
            ax.grid(axis='x', linestyle='--', alpha=0.6)
        else:
            ax.text(0.5, 0.5, "Respuestas demasiado variadas o sin texto", ha='center')

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# ================================
# Interfaz principal
# ================================
def main():
    preguntas_y_respuestas = obtener_preguntas_y_respuestas()
    if not preguntas_y_respuestas:
        tk.Tk().withdraw()
        messagebox.showinfo("Sin datos", "No se encontraron respuestas del curso 3°A.")
        return

    ventana = tk.Tk()
    ventana.title("Encuesta del curso 3°A")
    ventana.geometry("900x600")

    panel_izq = tk.Frame(ventana, width=260)
    panel_izq.pack(side=tk.LEFT, fill=tk.Y, padx=6, pady=6)
    panel_der = tk.Frame(ventana)
    panel_der.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=6, pady=6)

    tk.Label(panel_izq, text="Preguntas del curso 3°A", font=("Segoe UI", 11, "bold")).pack(pady=6)

    canvas_btns = tk.Canvas(panel_izq)
    frame_btns = tk.Frame(canvas_btns)
    scroll = tk.Scrollbar(panel_izq, orient="vertical", command=canvas_btns.yview)
    canvas_btns.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    canvas_btns.pack(side="left", fill="both", expand=True)
    canvas_btns.create_window((0, 0), window=frame_btns, anchor="nw")

    def ajustar_scroll(_):
        canvas_btns.configure(scrollregion=canvas_btns.bbox("all"))
    frame_btns.bind("<Configure>", ajustar_scroll)

    area_grafico = tk.Frame(panel_der, relief=tk.RIDGE, borderwidth=1)
    area_grafico.pack(fill=tk.BOTH, expand=True)

    for pregunta in sorted(preguntas_y_respuestas.keys()):
        texto_btn = pregunta if len(pregunta) < 40 else pregunta[:37] + "..."
        ttk.Button(
            frame_btns,
            text=texto_btn,
            width=30,
            command=lambda q=pregunta: mostrar_grafico(area_grafico, q, preguntas_y_respuestas[q])
        ).pack(pady=3, padx=3, anchor="w")

    def limpiar():
        for w in area_grafico.winfo_children():
            w.destroy()
    ttk.Button(panel_izq, text="Limpiar gráfico", command=limpiar).pack(pady=8)

    ventana.mainloop()

if __name__ == "__main__":
    main()
