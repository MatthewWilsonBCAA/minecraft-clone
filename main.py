from classes import *
from itertools import islice 
import json
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
try:
    with open("inventory.json", "r") as file:
        inven = json.load(file)
except:
    inven = {}
player = Player(inven)
try:
    with open("world.json", "r") as file:
        data = json.load(file)
        chunk_one = Chunk((0, 0), True, 'one', data['one'])
        chunk_two = Chunk((800, 0), False, 'two', data['two'])
        chunk_three = Chunk((0, 800), False, 'three', data['three'])
        chunk_four = Chunk((800, 800), False, 'four', data['four'])
        chunk_five = Chunk((-800, 0), False, 'five', data['five'])
        chunk_six = Chunk((-800, -800), False, 'six', data['six'])
        chunk_seven = Chunk((0, -800), False, 'seven', data['seven'])
        chunk_eight = Chunk((800, -800), False, 'eight', data['eight'])
        chunk_nine = Chunk((-800, 800), False, 'nine', data['nine'])
except:
    chunk_one = Chunk((0, 0), True, 'one')
    chunk_two = Chunk((800, 0), False, 'two')
    chunk_three = Chunk((0, 800), False, 'three')
    chunk_four = Chunk((800, 800), False, 'four')
    chunk_five = Chunk((-800, 0), False, 'five')
    chunk_six = Chunk((-800, -800), False, 'six')
    chunk_seven = Chunk((0, -800), False, 'seven')
    chunk_eight = Chunk((800, -800), False, 'eight')
    chunk_nine = Chunk((-800, 800), False, 'nine')
all_sprites = pygame.sprite.Group()

chunk_list = [chunk_one, chunk_two, chunk_three, chunk_four, chunk_five, chunk_six, chunk_seven, chunk_eight, chunk_nine]
for chunk in chunk_list:
    for block in chunk.blocks:
        all_sprites.add(block)
running = True
x = 0
y = 0
is_build = False
selected_block = 0
while running:
    screen.fill((0, 0, 0))
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_1] and '1' in player.inventory:
        selected_block = 1
    elif pressed_keys[K_2] and '2' in player.inventory:
        selected_block = 2
    elif pressed_keys[K_3] and '3' in player.inventory:
        selected_block = 3
    elif pressed_keys[K_4] and '4' in player.inventory:
        selected_block = 4
    elif pressed_keys[K_5] and '5' in player.inventory:
        selected_block = 5

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
                    player.add_item(sprite.id, 1)
                    sprite.change_block(0)
                elif sprite.id == 0 and is_build == True and selected_block != 0 and player.inventory[selected_block] > 0:
                    sprite.change_block(selected_block)
                    player.inventory[selected_block] -= 1
                print(selected_block)
            
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

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))
with open('inventory.json', 'w') as file:
    json.dump(player.inventory, file)
with open('world.json', 'w') as file:
    keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    z = 0
    data = {'one': [], 'two': [], 'three': [], 'four': [], 'five': [], 'six': [], 'seven': [], 'eight': [], 'nine': []}
    for chunk in chunk_list:
        rows = list(split(chunk.blocks, 32))
        for row in rows:
            temp_row = []
            for block in row:

                temp_row.append(block.id)
            data[keys[z]].append(temp_row)
        z += 1
    json.dump(data, file)