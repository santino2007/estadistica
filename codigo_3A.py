
from tkinter import Tk, Menu, Text, messagebox

def on_click():
    messagebox.showinfo("information", "button clicked")

class Menuapp:
    def __init__(self, master):
        self.master = master
        self.create_menu()
        self.text_area = Text(master, wrap='word', height=280, width=300)
        self.text_area.pack(side='left', fill='both', expand=True)
    
    def create_menu(self):
        barra_menu = Menu(self.master)
        self.master.config(menu=barra_menu)

        menu_cursos = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="cursos", menu=menu_cursos)
        menu_cursos.add_command(label="curso 1", command=on_click)
        menu_cursos.add_command(label="curso 2", command=on_click)
        menu_cursos.add_command(label="curso 3", command=on_click)
        menu_cursos.add_command(label="curso 4", command=on_click)
        menu_cursos.add_command(label="curso 5", command=on_click)
        
        commands= [("salir", self.master.quit)]
        for (text, commands) in commands:
            barra_menu.add_command(label=text, command=commands)
        
class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("recuperatorio")
        self.menu_app = Menuapp(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()