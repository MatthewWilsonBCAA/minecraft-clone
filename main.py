from classes import *
from itertools import islice 
import json
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Matt's Top Down Minecraft")
icon = pygame.image.load(BLOCK_LIST[random.randint(0, len(BLOCK_LIST) - 1)][1])
pygame.display.set_icon(icon)
try:
    with open("stats.json", "r") as file:
        data = json.load(file)
        hp = data['hp']
        pickaxe = data['pickaxe']
        axe = data['axe']
        sword = data['sword']
        x_pos = data['x_pos']
        y_pos = data['y_pos']
except:
    hp = 10
    pickaxe = 10
    axe = 10
    sword = 10
    x_pos = 0
    y_pos = 0
try:
    with open("inventory.json", "r") as file:
        inven = json.load(file)
except:
    inven = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0}
player = Player(inven, hp, pickaxe, axe, sword)
pos_list = [
    (0+x_pos, 0+y_pos),
    (800+x_pos, 0+y_pos),
    (0+x_pos, 800+y_pos),
    (800+x_pos, 800+y_pos),
    (-800+x_pos, 0+y_pos),
    (-800+x_pos, -800+y_pos),
    (0+x_pos, -800+y_pos),
    (800+x_pos, -800+y_pos),
    (-800+x_pos, 800+y_pos)
]
try:
    with open("world.json", "r") as file:
        data = json.load(file)
        chunk_one = Chunk(pos_list[0], True, 'one', data['one'])
        chunk_two = Chunk(pos_list[1], False, 'two', data['two'])
        chunk_three = Chunk(pos_list[2], False, 'three', data['three'])
        chunk_four = Chunk(pos_list[3], False, 'four', data['four'])
        chunk_five = Chunk(pos_list[4], False, 'five', data['five'])
        chunk_six = Chunk(pos_list[5], False, 'six', data['six'])
        chunk_seven = Chunk(pos_list[6], False, 'seven', data['seven'])
        chunk_eight = Chunk(pos_list[7], False, 'eight', data['eight'])
        chunk_nine = Chunk(pos_list[8], False, 'nine', data['nine'])
except:
    chunk_one = Chunk(pos_list[0], True, 'one')
    chunk_two = Chunk(pos_list[1], False, 'two')
    chunk_three = Chunk(pos_list[2], False, 'three')
    chunk_four = Chunk(pos_list[3], False, 'four')
    chunk_five = Chunk(pos_list[4], False, 'five')
    chunk_six = Chunk(pos_list[5], False, 'six')
    chunk_seven = Chunk(pos_list[6], False, 'seven')
    chunk_eight = Chunk(pos_list[7], False, 'eight')
    chunk_nine = Chunk(pos_list[8], False, 'nine')
all_sprites = pygame.sprite.Group()

chunk_list = [chunk_one, chunk_two, chunk_three, chunk_four, chunk_five, chunk_six, chunk_seven, chunk_eight, chunk_nine]
for chunk in chunk_list:
    for block in chunk.blocks:
        all_sprites.add(block)

ui_group = pygame.sprite.Group()
for param in UI_LIST:
    obj = UI(param[0], param[1], param[2])
    ui_group.add(obj)   

running = True
x = 0
y = 0
is_build = False
selected_block = 0
checked_light_blocks = False
light_timer = 0
lit_spots = []

dist_b = [] #used for block lighting only

while running:
    screen.fill((0, 0, 0))
    pressed_keys = pygame.key.get_pressed()
    # if pressed_keys[K_1] and '1' in player.inventory:
    #     selected_block = 1
    # elif pressed_keys[K_2] and '2' in player.inventory:
    #     selected_block = 2
    # elif pressed_keys[K_3] and '3' in player.inventory:
    #     selected_block = 3
    # elif pressed_keys[K_4] and '4' in player.inventory:
    #     selected_block = 4
    # elif pressed_keys[K_5] and '5' in player.inventory:
    #     selected_block = 5

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
    rend_r = []
    #light_timer += 1
    #if light_timer > 5:
    checked_light_blocks = False
        #light_timer = 0
    lit_spots.clear()
    for sprite in all_sprites:
        if sprite.id == 7 and not checked_light_blocks:
            lit_spots.append((sprite.rect.x, sprite.rect.y))
        if pressed_keys[K_w]:
            sprite.rect.move_ip(0, -speed)
            if hasattr(sprite, "id") and sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                hit_id.append(1)
        if pressed_keys[K_s]:
            sprite.rect.move_ip(0, speed)
            if hasattr(sprite, "id") and sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                hit_id.append(2)
        if pressed_keys[K_a]:
            sprite.rect.move_ip(-speed, 0)
            if hasattr(sprite, "id") and sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                hit_id.append(3)
        if pressed_keys[K_d]:
            sprite.rect.move_ip(speed, 0)
            if hasattr(sprite, "id") and sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                hit_id.append(4)
        if sprite.rect.collidepoint(x, y) and hasattr(sprite, "id") and not hasattr(sprite, "name"):
            dist = ((player.rect.x - x) ** 2 + (player.rect.y - y)  ** 2) ** 0.5
            if not pygame.sprite.collide_rect(player, sprite) and dist < 125:
                if sprite.id != 0 and is_build == False:
                    sprite.hp -= player.pickaxe
                    if sprite.hp <= 0:
                        player.add_item(sprite.id, 1)
                        sprite.change_block(0)
                    checked_light_blocks = False
                elif sprite.id == 0 and is_build == True and selected_block != 0 and player.inventory[str(selected_block)] > 0:
                    checked_light_blocks = False
                    sprite.change_block(selected_block)
                    player.remove_item(selected_block, 1)
    prev_sprite = False
    next_sprite = False
    ver_sprite = False
    bot_sprite = False
    for sprite in all_sprites:
        if 1 in hit_id:
            sprite.rect.move_ip(0, speed)
        if 2 in hit_id:
            sprite.rect.move_ip(0, -speed)
        if 3 in hit_id:
            sprite.rect.move_ip(speed, 0)
        if 4 in hit_id:
            sprite.rect.move_ip(-speed, 0)
            
        
        if sprite.rect.x > 0 and sprite.rect.x < SCREEN_WIDTH and sprite.rect.y > 0 and sprite.rect.y < SCREEN_HEIGHT:
            if sprite.id == 7:
                screen.blit(sprite.surf, sprite.rect)
            else:
                dist_b.clear()
                dist_b.append(((player.rect.x - sprite.rect.x) ** 2 + (player.rect.y - sprite.rect.y)  ** 2) ** 0.5)
                for cor in lit_spots:
                    if abs(cor[0] - sprite.rect.x) < REND_DIST + 50:
                        d = ((cor[0] - sprite.rect.x) ** 2 + (cor[1] - sprite.rect.y)  ** 2) ** 0.5
                        if d < REND_DIST + 50: dist_b.append(d)
                sprite.surf.set_alpha(sprite.check_render(dist_b))
                screen.blit(sprite.surf, sprite.rect)
                
    
    for sprite in ui_group:
        screen.blit(sprite.surf, sprite.rect)
        if sprite.type == 1:
            screen.blit(small_font.render("Pick Lv" + str(player.pickaxe), True, (255, 255, 0)), (sprite.rect.x, sprite.rect.y-20))
            if sprite.rect.collidepoint(x, y):
                player.upgrade_pick()
        if sprite.type == 2:
            for ui in sprite.blocks:
                screen.blit(ui.surf, ui.rect)
                if ui.rect.collidepoint(x, y):
                    selected_block = ui.id
    screen.blit(font.render("Tools and Upgrades", True, (255, 255, 0)), (SCREEN_WIDTH-200, 0))
    screen.blit(player.surf, player.rect)
    checked_light_blocks = True

    z = 1
    for block in BLOCK_LIST:
        text = block[0]
        pos = (block[2][0] + 15, block[2][1])
        if selected_block == z:
            text = '->' + text
        text += ": " + str(player.inventory[str(z)])
        screen.blit(font.render(text, True, (255, 255, 0)), pos)
        z += 1


    if is_build:
        screen.blit(font.render("Building...", True, (255, 255, 0)), (30, 10))
    else:
        screen.blit(font.render("Mining...", True, (255, 255, 0)), (30, 10))


    pygame.display.flip()
    clock.tick(FRAME_RATE)

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

with open('stats.json', 'w') as file:
    x_pos = chunk_one.blocks[0].rect.x + 12
    y_pos = chunk_one.blocks[0].rect.y + 12
    data = {'hp': player.hp, 'pickaxe': player.pickaxe, 'axe': player.axe, 'sword': player.sword, 'x_pos': x_pos, 'y_pos': y_pos}
    json.dump(data, file)


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