"""This class handles sprite sheets.

This was taken from www.scriptefun.com/transcript-2-using
sprite-sheets-and-drawing-the-background
I've added some code to fail if the file wasn't found..
Note: When calling images_at the rect is the format:
(x, y, x + offset, y + offset)
"""

import pygame


class Spritesheet:
    """Class the create sprites from a sprite sheet."""

    def __init__(self, filename):
        """Get the sprite sheet file."""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except TypeError:
            message = 'Unable to load spritesheet image:' + filename
            raise message

    def image_at(self, rectangle, colorkey=None):
        """Load image from x,y,x+offset,y+offset."""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey=None):
        """Load multiple images, supply a list of coordinates."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey=None):
        """Load a strip of images and returns them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

# if __name__ == "__main__":
#     STEP = 20
#     TILES = "ressource/floor-tiles-20x20.png"
#     FLOOR = (1 * STEP, 0 * STEP, STEP, STEP)
#     WALL = (12 * STEP, 5 * STEP, STEP, STEP)
#     EXIT = (8 * STEP, 1 * STEP, STEP, STEP)

#     screen = pygame.display.set_mode((300, 300))
#     loop = True
#     while loop:
#         for event in pygame.event.get():
#             if event.type == 12:  # pygame.QUIT:
#                 loop = False
#         ss = Spritesheet("ressource/floor-tiles-20x20.png")
#         # image = ss.image_at((0, 0, 20, 20))
#         image = ss.image_at(EXIT)
#         screen.blit(image, (0, 0))

#         img_list = ss.load_strip((0, 0, STEP, STEP), 8)
#         screen.blit(img_list[2], (50, 0))
#         screen.blit(img_list[6], (55, 15))

#         pygame.display.flip()
