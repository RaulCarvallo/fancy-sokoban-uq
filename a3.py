
from tkinter import messagebox, filedialog
from typing import Callable
from model import SokobanModel, Tile, Entity
from a2_support import *
from a3_support import *

# Write your classes and functions here

'''Initialize Pygame'''



# root = tk.Tk()
# root.title('Extra Fancy Sokoban')
# play_game = tk.Label(root, text='Exta Fancy Sokoban')# create a label widget as a child of 'root'
# play_game.pack()


# main_page = tk.Label(frame, text="Main", bg="yellow")
# main_page.pack(side=tk.RIGHT)

# title_game = tk.Label(frame, text="Title", bg="purple")
# title_game.pack(side=tk.RIGHT)


class FancyGameView(AbstractGrid):
    images={}
    def __init__(self, master: tk.Frame | tk.Tk, dimensions: tuple[int, int], size:
tuple[int, int], **kwargs) -> None:
        super().__init__(
            self,
            master,
            dimensions,
            size,
            **kwargs
        )


class display(FancyGameView):
    def clear(self):
        """ Clears all child widgets off the canvas. """
        self.delete("all")

    def __init__ (self, maze: Grid, entities: Entities, player_position: Position):
        pass
    
    def get_image(image_name: str, size: tuple[int, int], cache: dict[str, ImageTk.PhotoImage] = None) -> Image:
        image = Image.open('Ca3\images\banner.png')

class FancyStatsView(AbstractGrid):
    def __init__(self) -> None:
        pass

class Shop:
    def __init__(self) -> None:
        pass

    
class FancySokobanView:
    def __init__(self, master: tk.Tk, dimensions: tuple[int, int], size: tuple[int,
int]) -> None:
        pass
        
        
class ExtraFancySokoban:
    def __init__(self, root: tk.Tk, maze_file: str) -> None:
        self._model = SokobanModel(maze_file)
        self._view = FancySokobanView(root, self._model.get_dimensions, (300,500))
        pass

def play_game(root: tk.Tk, maze_file: str) -> None:
    ExtraFancySokoban(root, maze_file)    
    root.mainloop()
def main() -> None:
    root = tk.Tk()
    play_game(root, "maze_files/maze1.txt")

    """ The main function. """
    pass  # Write your main code here


if __name__ == "__main__":
    main()
