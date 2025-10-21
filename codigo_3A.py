
from tkinter import Tk, Menu, Text, messagebox, filedialog

def on_click():
    messagebox.showinfo("information", "button clicked")

class Menuapp:
    def __init__(self, master):
        self.master = master
        self.create_menu()
        self.text_area = Text(master, wrap='word', height=280, width=300)
        self.text_area.pack(side='left', fill='both', expand=True)
    
    def abrir_archivo(self):
        archivo = filedialog.askdirectory(initialdir="/", title="secciona un archivo")
        if archivo: 
            print(f"se abrio un archivo:{archivo}")
            
        else:
            messagebox.INFO("no se pudo abrir el archivo")
    
    def create_menu(self):
        barra_menu = Menu(self.master)
        self.master.config(menu=barra_menu)

        menu_cursos = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="cursos", menu=menu_cursos)
        menu_cursos.add_command(label="3º A", command=self.abrir_archivo)
        menu_cursos.add_command(label="3º B", command=on_click)
        menu_cursos.add_command(label="3ª C", command=on_click)
        menu_cursos.add_command(label="3º D", command=on_click)
        menu_cursos.add_command(label="4º A", command=on_click)
        menu_cursos.add_command(label="4º B", command=on_click)
        
        
        
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