import pygame

class Puppy:
    """A class to manage the puppy."""

    def __init__(self, ci_game):
        """Initialize the puppy and its starting position."""
        self.screen = ci_game.screen
        self.screen_rect = ci_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/puppy.bmp')
        self.rect = self.image.get_rect()

        # Start each new puppy at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)