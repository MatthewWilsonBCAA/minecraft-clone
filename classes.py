import pygame
from constants import *
import random
from chunks import chunk_styles
pygame.init()
font = pygame.font.SysFont('Consolas', 30)
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_t,
    K_f,
    K_g,
    K_h,
    KEYDOWN,
    QUIT,
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(round(SCREEN_WIDTH/2), round(SCREEN_HEIGHT/2)))

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, id):
        super(Block, self).__init__()
        if id >= 0:
            self.change_block(id)
        else:
            self.change_block(random.randint(0, 3))
        self.rect = self.surf.get_rect(center=pos)
        self.g_position = pos
    def change_block(self, id):
        self.id = id
        if self.id == 1:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((255, 255, 5))
        elif self.id == 2:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((0, 255, 0))
        elif self.id == 3:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((125, 125, 125))
        else:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((0, 20, 0))

class Chunk():
    def __init__(self, pos):
        self.blocks = []
        for y in range(CHUNK_SIZE):
            for x in range(CHUNK_SIZE):
                # print(str(x) + ", " + str(y))
                self.blocks.append(Block((x*25, y*25), chunk_styles["ring_one"][y][x]))
