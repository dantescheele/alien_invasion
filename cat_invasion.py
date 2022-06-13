import sys # Tools within sys are used to exit the game when the player quits
import pygame

from settings import Settings
from puppy import Puppy

class CatInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Cat Invasion")
        
        self.puppy = Puppy(self)

        # Set the background color.
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            self.puppy.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ci = CatInvasion()
    ci.run_game()