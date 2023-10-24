
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
        self._cache = {}

   ##################
    Entities = dict[Tuple[int, int], Entity]:

    def display(self, maze: Grid, entities: Entities, player_position: Position ):
        
        self.clear()
        
        # step 1 = draw the tiles from the maze
        for row_num, row in enumerate(maze):
            for col_num, tile in enumerate(row):
                position = (row_num, col_num)
                if str(tile) == " ":
                    image_name = "images/Floor.png"
                if str(tile) == "W":
                    image_name = "images/W.png"
                if str(tile) == "G":
                    image_name = "images/G.png"
                if str(tile) == "X":
                    image_name = "images/X.png"
                else: 
                    image_name = f"images/{str(tile)}.png"
                image = get_image(image_name, self.get_cell_size(), self._cache)
                self.create_image(self.get_midpoint(position), image=image)

        # go over the entities and create images for those
        # one for loop over the dictionary (look into .items method for dictionaries)

    
        for entity in entities:
            entity_position = entity.get_position()  # Assuming there's a method to get entity position
            entity_image_name = entity.get_image_name()  # Assuming there's a method to get entity image name
            entity_image = get_image(entity_image_name, self.get_cell_size(), self._cache)
            self.create_image(self.get_midpoint(entity_position), image=entity_image)
            

        # draw the player at the player position (not a for loop, just draw the player at player_position)
        image = get_image(image_name("images/P.png"), self.get_cell_size(), self._cache)
        self.create_image(self.get_midpoint(player_position), image=i)





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

        

    def get_tile_position(self,tile_position) -> Position:
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
    
    def draw_stats(self, moves_remaining: int, strength: int, money: int) -> None:
        pass        

class Shop(tk.Frame):

    def __init__(self, master: tk.Frame) -> None:
        pass
    
    def create_buyable_item( self, item: str, amount: int, callback: Callable[[], None]
) -> None:
        pass
    
class FancySokobanView:
    def __init__(self, master: tk.Tk, dimensions: tuple[int, int], size: tuple[int,
int]) -> None:
        self._game_view = FancyGameView(master, dimensions, size)
        self._game_view.pack()

    def display_game(self, maze: Grid, entities: Entities, player_position: Position ):
        self._game_view.display(maze, entities, player_position)
    
    def display_stats(self, moves: int, strength: int, money: int) -> None:
        pass

    def create_shop_items( self, shop_items: dict[str, int], button_callback:Callable[[str], None] | None = None ) -> None:
        pass

class ExtraFancySokoban:
    def __init__(self, root: tk.Tk, maze_file: str) -> None:
        self._model = SokobanModel(maze_file)
        self._view = FancySokobanView(root, self._model.get_dimensions(), (MAZE_SIZE, MAZE_SIZE))
        root.title('Extra Fancy Sokoban')
        ## add image banner using get_image function inside the root parameter
        img = get_image('images/banner.png', (MAZE_SIZE+SHOP_WIDTH,BANNER_HEIGHT))
        label = tk.Label(root, image = img)
        label.pack()
        self.redraw()
        pass
    
    def redraw(self) -> None:
        self._view.display_game(self._model.get_maze(), self._model.get_entities(), self._model.get_player_position())
    
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
