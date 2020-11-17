from classes import *
from itertools import islice 
import json
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()
try:
    with open("world.json", "r") as file:
        data = json.load()
        chunk_one = Chunk((0, 0), True, data['one'])
        chunk_two = Chunk((800, 0), False, data['two'])
        chunk_three = Chunk((0, 800), False, data['three'])
        chunk_four = Chunk((800, 800), False, data['four'])
        chunk_five = Chunk((-800, 0), False, data['five'])
        chunk_six = Chunk((-800, -800), False, data['six'])
        chunk_seven = Chunk((0, -800), False, data['seven'])
        chunk_eight = Chunk((800, -800), False, data['eight'])
        chunk_nine = Chunk((-800, 800), False, data['nine'])
except:
    chunk_one = Chunk((0, 0), True)
    chunk_two = Chunk((800, 0), False)
    chunk_three = Chunk((0, 800), False)
    chunk_four = Chunk((800, 800), False)
    chunk_five = Chunk((-800, 0), False)
    chunk_six = Chunk((-800, -800), False)
    chunk_seven = Chunk((0, -800), False)
    chunk_eight = Chunk((800, -800), False)
    chunk_nine = Chunk((-800, 800), False)
all_sprites = pygame.sprite.Group()

chunk_list = [chunk_one, chunk_two, chunk_three, chunk_four, chunk_five, chunk_six, chunk_seven, chunk_eight, chunk_nine]
for chunk in chunk_list:
    for block in chunk.blocks:
        all_sprites.add(block)
running = True
x = 0
y = 0
is_build = False
while running:
    screen.fill((0, 0, 0))
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_b:
                is_build = not is_build
        if event.type == MOUSEBUTTONDOWN: 
            x,y = event.pos
        else:
            x = 0
            y = 0

    speed = -2
    hit_id = []
    for sprite in all_sprites:
        if pressed_keys[K_UP]:
            sprite.rect.move_ip(0, -speed)
            if hasattr(sprite, "id") and sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                hit_id.append(1)
        if pressed_keys[K_DOWN]:
            sprite.rect.move_ip(0, speed)
            if hasattr(sprite, "id") and sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                hit_id.append(2)
        if pressed_keys[K_LEFT]:
            sprite.rect.move_ip(-speed, 0)
            if hasattr(sprite, "id") and sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                hit_id.append(3)
        if pressed_keys[K_RIGHT]:
            sprite.rect.move_ip(speed, 0)
            if hasattr(sprite, "id") and sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                hit_id.append(4)
        if sprite.rect.collidepoint(x, y) and hasattr(sprite, "id"):
            if abs(player.rect.x - x) < 100 and abs(player.rect.y - y) < 100:
                if sprite.id != 0 and is_build == False:
                    sprite.change_block(0)
                elif sprite.id == 0 and is_build == True:
                    sprite.change_block(1)
            
    for sprite in all_sprites:
        if 1 in hit_id:
            sprite.rect.move_ip(0, speed)
        if 2 in hit_id:
            sprite.rect.move_ip(0, -speed)
        if 3 in hit_id:
            sprite.rect.move_ip(speed, 0)
        if 4 in hit_id:
            sprite.rect.move_ip(-speed, 0)
        if hasattr(sprite, "id") and sprite.id != 0:
            screen.blit(sprite.surf, sprite.rect)
    screen.blit(player.surf, player.rect)
    pygame.display.flip()
    clock.tick(FRAME_RATE)
    
# with open('world.json', 'w') as file:
#     data = []
#     for chunk in chunk_list:
#         temp_rows = 
#         for row in temp_rows:
#             for block in row:
#                 temp_row.append(block.id)
#         data.append()