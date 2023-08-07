"""
Rock Paper Scissors
-------------------------------------------------------------
"""
# imports for menu
import tkinter as tk
from functions import play_rps


# imports

# menu
class MAIN:  # main function for the gui
    def __init__(self, game_gui):
        """
        :param game_gui:
        """
        self.game = game_gui
        self.game.title('Rock, Paper, Scissors - Shoot!')  # Set the game title
        gui_width = 760
        gui_height = 490
        self.game.geometry(f"{gui_width}x{gui_height}")
        self.game.minsize(600, 400)


if __name__ == '__main__':
    game = tk.Tk()
    app = MAIN(game)
    game.mainloop()
    # play_rps() commented out game before it still works like this
