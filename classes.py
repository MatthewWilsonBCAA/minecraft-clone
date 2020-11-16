import pygame
from constants import *
import random
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
        self.id = id
        if self.id > 0:
            self.surf = pygame.Surface((25, 25))
            if self.id == 1:
                self.surf.fill((255, 255, 0))
            elif self.id == 2:
                self.surf.fill((0, 255, 0))
            self.rect = self.surf.get_rect(center=pos)
        else:
            self.surf = pygame.Surface((0, 0))
            self.surf.fill((255, 255, 0))
            self.rect = self.surf.get_rect(center=pos)
            self.id = 0
        self.g_position = pos

class Chunk():
    def __init__(self, pos):
        self.blocks = []
        for y in range(CHUNK_SIZE):
            for x in range(CHUNK_SIZE):
                self.blocks.append(Block((x*25, y*25), random.randint(-10, 2)))
