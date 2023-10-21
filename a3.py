
from tkinter import Label, messagebox, filedialog
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
            master,
            dimensions,
            size,
            **kwargs
        )

    def display(self, maze: Grid, entities: Entities, player_position: Position ):
        
        game_display = FancyGameView()
        game_display.clear()
        tile_positions = [(x, y) for x in range(0, game_display.width, self.get_cell_size()[0]) 
                        for y in range(0, game_display.height, self.get_cell_size()[1])]
        pass

# Clear the game view

    def clear(self):
        """ Clears all child widgets off the canvas. """
        self.delete("all")


# Define tile and entity positions
entity_positions = []
entity_positions = [(entity_x, entity_y) for entity_x, entity_y in entity_positions]

def pixel_to_cell(self, x: int, y: int) -> tuple[int, int]:
    cell_width, cell_height = self.get_cell_size()
    return y // cell_height, x // cell_width


def get_player_position(self) -> Position:
    """ Returns the player's current position. """
    return self._player_position

def entity_positions(
    self,
    position: tuple[int, int],
    text: str,
    font=None
    ) -> None:


# Create a  tile images

        

    def get_tile_position(self,tile_position) -> Positon:
        """ Returns the tile's current position. """
        tile_positions = []
        tile_positions = [(tile_x, tile_y) for tile_x, tile_y in tile_positions]

        for tile_x, tile_y in tile_positions:
            tile_image = get_image(tile_x, tile_y, "tile")  # Use the get_image function to create tile images
            # game_display.render_image(tile_image, tile_x, tile_y)
    #     return self._tile_position


# Create and render entity images
# for entity_x, entity_y in entity_positions:
#     entity_image = get_image(entity_x, entity_y, "entity")  # Use the get_image function to create entity images
#     game_display.render_image(entity_image, entity_x, entity_y)

# Update the display to show the rendered images
# pygame.display.update()

# Game loop, event handling, and other game logic here
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# Quit the game and clean up
# pygame.quit()



def __init__ (self, maze: Grid, entities: Entities, player_position: Position):
    pass

class FancyStatsView(AbstractGrid):
    def __init__(self, master: tk.Tk | tk.Frame) -> None:
        pass
    
    def initial_position(self, x: int, y: int) -> tuple[int, int]:
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
        root.title('Extra Fancy Sokoban')
        ## add image banner using get_image function inside the root parameter
        img = get_image('images/banner.png', (923,105))
        label = tk.Label(root, image = img)
        label.pack()
        root.mainloop()
        pass
    
    def redraw(self) -> None:
        pass
    
    def handle_keypress(self, event: tk.Event) -> None:
        pass


def play_game(root: tk.Tk, maze_file: str) -> None:
    ExtraFancySokoban(root, maze_file)    
    root.mainloop()

def main() -> None:
    root = tk.Tk()
    play_game(root, "maze_files/maze1.txt")
    """ The main function. """
    pass

if __name__ == "__main__":
    main()
