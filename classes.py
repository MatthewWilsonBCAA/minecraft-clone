import pygame
from constants import *
import random
from chunks import chunk_styles, files
pygame.init()
font = pygame.font.SysFont('Consolas', 20)
small_font = pygame.font.SysFont('Consolas', 13)
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

class UI(pygame.sprite.Sprite):
    def __init__(self, size, pos, type):
        super(UI, self).__init__()
        self.type = type
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=pos)
        if self.type == 0:
            self.surf.fill((0, 0, 0))
        elif self.type == 1:
            self.surf = pygame.image.load(r"images/pickaxe.png").convert_alpha()
        elif self.type == 2:
            self.surf.fill((0, 0, 0))
            self.blocks = []
            for block in BLOCK_LIST:
                self.blocks.append(BlockImage(block[0], block[1], block[2], block[3]))

class BlockImage(pygame.sprite.Sprite):
    def __init__(self, name, image, pos, id):
        self.name = name
        self.id = id
        self.surf = pygame.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect(center=pos)

    def set_block(self):
        return self.id 
    
        
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
    def upgrade_pick(self):
        if self.inventory['4'] >= self.pickaxe - UPGRADE_COST:
            self.inventory['4'] -= self.pickaxe - UPGRADE_COST
            self.pickaxe += 1
class Block(pygame.sprite.Sprite):
    def __init__(self, pos, id):
        super(Block, self).__init__()
        if id >= 0:
            self.change_block(id)
        elif id == -2:
            self.change_block(random.randint(3, 6))
        elif id == -3:
            self.change_block(random.randint(1, 2))
        else:
            self.change_block(random.randint(0, 3))
        self.rect = self.surf.get_rect(center=pos)
        self.g_position = pos
        self.rend = 0
    def change_block(self, id):
        self.id = id
        if self.id == 1:
            self.surf = pygame.image.load(BLOCK_LIST[0][1]).convert_alpha()
            self.hp = 25
        elif self.id == 2:
            self.surf = pygame.image.load(BLOCK_LIST[1][1]).convert_alpha()
            self.hp = 2
        elif self.id == 3:
            self.surf = pygame.image.load(BLOCK_LIST[2][1]).convert_alpha()
            self.hp = 52
        elif self.id == 4:
            self.surf = pygame.image.load(BLOCK_LIST[3][1]).convert_alpha()
            self.hp = 55
        elif self.id == 5:
            self.surf = pygame.image.load(BLOCK_LIST[4][1]).convert_alpha()
            self.hp = 60
        elif self.id == 6:
            self.surf = pygame.image.load(BLOCK_LIST[5][1]).convert_alpha()
            self.hp = 57
        else:
            self.surf = pygame.image.load(r"images/ground.png").convert_alpha()
            self.hp = 0
    def check_render(self, prev_block, next_block, ver_block, bot_block, px, py, dist):
        if dist > REND_DIST - 25:
            self.surf.fill((25, 25, 25, 10), special_flags=pygame.BLEND_SUB)
        else:
        if prev_block and prev_block.id == 0 and self.rect.x > px:
            return True
        elif next_block and next_block.id == 0 and self.rect.x < px:
            return True
        elif ver_block and ver_block.id == 0 and self.rect.y > py:
            return True
        elif bot_block and bot_block.id == 0 and self.rect.y < py:
            return True
        elif not prev_block and not bot_block:
            return True
        else:
            return False

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