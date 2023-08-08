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
        self.game.title('Rock, Paper, Scissor - Shoot!')  # Set the game title
        width = 760
        height = 490
        self.game.geometry(f"{width}x{height}")
        self.game.minsize(760, 490)  # set min size that the menu have to be


if __name__ == '__main__':
    game = tk.Tk()
    app = MAIN(game)
    game.mainloop()
    # play_rps() commented out game before it still works like this
