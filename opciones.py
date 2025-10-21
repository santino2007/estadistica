import tkinter as tk
from tkinter import Menu, Text, messagebox, Tk

def on_click():
    messagebox.showinfo("Información", "Botón clickeado")

class MenuApp:
    def __init__(self, master):
        self.master = master
        self.create_menu()
        self.text_area = Text(master, wrap='word', height=20, width=50)
        self.text_area.pack(side='left', fill='both', expand=True)
        
    def create_menu(self):
        barra_menu = Menu(self.master)
        self.master.config(menu=barra_menu)
        
        # Submenú de preguntas
        menu_preguntas = Menu(barra_menu, tearoff=0)
        
        barra_menu.add_cascade(label="Preguntas y respuestas", menu=menu_preguntas)
        menu_preguntas.add_command(label="Todo", command=on_click)
        menu_preguntas.add_command(label="Preguntas si o no", command=on_click)
        menu_preguntas.add_command(label="preguntas numericas", command=on_click)
        menu_preguntas.add_command(label="preguntas 1 a 5/10", command=on_click)
        menu_preguntas.add_command(label="preguntas abiertas", command=on_click)
        
        
        # Comandos adicionales
        barra_menu.add_command(label="Salir", command=self.master.quit)
        
        

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Recuperatorio")
        self.menu_app = MenuApp(self.root)
        
    def run(self):
        self.root.mainloop()
                
if __name__ == "__main__":
    app = App()
    app.run()
