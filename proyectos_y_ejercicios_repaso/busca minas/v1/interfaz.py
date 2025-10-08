import tkinter as tk
from tkinter import messagebox
import logica

class BuscaminasGUI:
    def __init__(self, root, tamano, num_minas):
        self.root = root
        self.tamano = tamano
        self.num_minas = num_minas

        # Crear tableros
        self.tablero_real = logica.Crear_tablero(tamano)
        self.tablero_visible = logica.Crear_tablero(tamano)
        logica.minas(self.tablero_real, num_minas)

        self.botones = []
        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea la cuadrícula de botones."""
        for i in range(self.tamano):
            fila_botones = []
            for j in range(self.tamano):
                btn = tk.Button(self.root, text=" ", width=3, height=1,
                                command=lambda x=i, y=j: self.revelar(x, y))
                btn.bind("<Button-3>", lambda event, x=i, y=j: self.poner_bandera(x, y))
                btn.grid(row=i, column=j)
                fila_botones.append(btn)
            self.botones.append(fila_botones)

    def actualizar_tablero(self):
        """Actualiza la interfaz según el tablero visible."""
        for i in range(self.tamano):
            for j in range(self.tamano):
                valor = self.tablero_visible[i][j]
                btn = self.botones[i][j]

                if valor == ' ':
                    btn.config(text=" ", bg="SystemButtonFace")
                elif valor == 'M':
                    btn.config(text="💣", bg="red")
                else:
                    colores = {
                        '1': 'blue',
                        '2': 'green',
                        '3': 'red',
                        '4': 'purple',
                        '5': 'maroon'
                    }
                    btn.config(text=valor, fg=colores.get(valor, 'black'), bg="lightgray")

    def revelar(self, fila, columna):
        """Revela una celda del tablero."""
        if self.tablero_visible[fila][columna] == '🚩':
            return

        if not logica.seleccionar_celda(self.tablero_real, self.tablero_visible, fila, columna):
            self.actualizar_tablero()
            messagebox.showinfo("Fin del juego", "💥 ¡Pisaste una mina!")
            self.root.destroy()
            return

        self.actualizar_tablero()

        if logica.win(self.tablero_real, self.tablero_visible):
            messagebox.showinfo("Victoria", "🎉 ¡Ganaste!")
            self.root.destroy()

    def poner_bandera(self, fila, columna):
        """Pone o quita una bandera en la celda."""
        actual = self.botones[fila][columna]['text']
        if actual == '🚩':
            self.botones[fila][columna].config(text=" ")
            self.tablero_visible[fila][columna] = ' '
        elif self.tablero_visible[fila][columna] == ' ':
            self.botones[fila][columna].config(text="🚩")
            self.tablero_visible[fila][columna] = '🚩'

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Buscaminas 🧨")

    # Puedes cambiar el tamaño o dificultad acá:
    app = BuscaminasGUI(root, tamano=8, num_minas=10)

    root.mainloop()