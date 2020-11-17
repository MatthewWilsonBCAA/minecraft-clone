import pygame
from constants import *
import random
from chunks import chunk_styles, files
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
        elif id == -2:
            self.change_block(random.randint(3, 5))
        elif id == -3:
            self.change_block(random.randint(1, 2))
        else:
            self.change_block(random.randint(0, 3))
        self.rect = self.surf.get_rect(center=pos)
        self.g_position = pos
    def change_block(self, id):
        self.id = id
        if self.id == 1:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((135, 125, 0))
        elif self.id == 2:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((0, 255, 0))
        elif self.id == 3:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((125, 125, 125))
        elif self.id == 4:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((175, 125, 125))
        elif self.id == 5:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((125, 125, 175))
        else:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((0, 20, 0))

class Chunk():
    def __init__(self, pos, spawn_chunk):
        self.blocks = []
        if spawn_chunk:
            self.chunk_type = files[0]
            self.mirrored_chance = 1
        else:
            self.chunk_type = files[random.randint(0, len(files)-1)]
            self.mirrored_chance = random.randint(1, 2)
        for y in range(CHUNK_SIZE):
            for x in range(CHUNK_SIZE):
                # print(str(x) + ", " + str(y))
                if self.mirrored_chance == 1:
                    self.blocks.append(Block((x*25 + pos[0] , y*25 + pos[1]), chunk_styles[self.chunk_type][y][x]))
                else:
                    self.blocks.append(Block((x*25 + pos[0] , y*25 + pos[1]), chunk_styles[self.chunk_type][x][y]))
