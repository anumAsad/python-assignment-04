import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()
        
        # Create a grid of blue cells
        self.cells = []
        for row in range(CANVAS_HEIGHT // CELL_SIZE):
            for col in range(CANVAS_WIDTH // CELL_SIZE):
                left_x = col * CELL_SIZE
                top_y = row * CELL_SIZE
                right_x = left_x + CELL_SIZE
                bottom_y = top_y + CELL_SIZE
                cell = self.canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')
                self.cells.append(cell)

        # Create eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')

        # Bind mouse motion event to move the eraser
        self.canvas.bind('<Motion>', self.move_eraser)
    
    def move_eraser(self, event):
        # Get mouse coordinates
        mouse_x = event.x
        mouse_y = event.y

        # Move eraser
        self.canvas.coords(self.eraser, mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)

        # Erase cells that overlap with eraser
        for cell in self.cells:
            coords = self.canvas.coords(cell)
            if (coords[0] < mouse_x + ERASER_SIZE and coords[2] > mouse_x and
                coords[1] < mouse_y + ERASER_SIZE and coords[3] > mouse_y):
                self.canvas.itemconfig(cell, fill='white')

def main():
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
