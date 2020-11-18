import pygame
from constants import *
import random
from chunks import chunk_styles, files
pygame.init()
font = pygame.font.SysFont('Consolas', 20)
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_b,
    K_f,
    K_g,
    K_h,
    K_w,
    K_a,
    K_s,
    K_d,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN
)

class Player(pygame.sprite.Sprite):
    def __init__(self, inventory, hp, pickaxe, axe, sword):
        super(Player, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(round(SCREEN_WIDTH/2), round(SCREEN_HEIGHT/2)))
        self.inventory = inventory
        self.hp = hp
        self.pickaxe = pickaxe
        self.axe = axe
        self.sword = sword
    def add_item(self, item_id, amount):
        self.inventory[str(item_id)] += amount
    def remove_item(self, item_id, amount):
        self.inventory[str(item_id)] -= amount

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
            self.surf = pygame.image.load(r"dirt.png").convert_alpha()
            self.hp = 25
        elif self.id == 2:
            self.surf = pygame.image.load(r"grass.png").convert_alpha()
            self.hp = 2
        elif self.id == 3:
            self.surf = pygame.image.load(r"stone.png").convert_alpha()
            self.hp = 52
        elif self.id == 4:
            self.surf = pygame.image.load(r"red-ore.png").convert_alpha()
            self.hp = 55
        elif self.id == 5:
            self.surf = pygame.image.load(r"blue-ore.png").convert_alpha()
            self.hp = 60
        else:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((0, 20, 0))
            self.hp = 0

class Chunk():
    def __init__(self, pos, spawn_chunk, name, data=None):
        self.blocks = []
        self.name = name
        if spawn_chunk:
            self.chunk_type = files[0]
            self.mirrored_chance = 1
        else:
            self.chunk_type = files[random.randint(0, len(files)-1)]
            self.mirrored_chance = random.randint(1, 2)
        for y in range(CHUNK_SIZE):
            for x in range(CHUNK_SIZE):
                # print(str(x) + ", " + str(y))
                if data:
                    self.blocks.append(Block((x*25 + pos[0] , y*25 + pos[1]), data[y][x]))
                else:
                    if self.mirrored_chance == 1:
                        self.blocks.append(Block((x*25 + pos[0] , y*25 + pos[1]), chunk_styles[self.chunk_type][y][x]))
                    else:
                        self.blocks.append(Block((x*25 + pos[0] , y*25 + pos[1]), chunk_styles[self.chunk_type][x][y]))
