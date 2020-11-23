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
    inven = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
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
    (-800+x_pos, 800+y_pos),
    (-1600+x_pos, -1600+y_pos),
    (-1600+x_pos, -800+y_pos),
    (-800+x_pos, -1600+y_pos),
    (-1600+x_pos, 0+y_pos),
    (0+x_pos, -1600+y_pos),
    (-1600+x_pos, 800+y_pos),
    (800+x_pos, -1600+y_pos),
    (-1600+x_pos, 1600+y_pos),
    (1600+x_pos, 1600+y_pos),
    (-800+x_pos, 1600+y_pos),
    (1600+x_pos, -800+y_pos),
    (0+x_pos, 1600+y_pos),
    (1600+x_pos, 0+y_pos),
    (800+x_pos, 1600+y_pos),
    (1600+x_pos, 800+y_pos),
    (1600+x_pos, 1600+y_pos)
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
        chunk_ten = Chunk(pos_list[9], False, 'ten', data['ten'])
        chunk_eleven = Chunk(pos_list[10], False, 'eleven', data['eleven'])
        chunk_twelve = Chunk(pos_list[11], False, 'twelve', data['twelve'])
        chunk_thirteen = Chunk(pos_list[12], False, 'thirteen', data['thirteen'])
        chunk_fourteen = Chunk(pos_list[13], False, 'fourteen', data['fourteen'])
        chunk_fifteen = Chunk(pos_list[14], False, 'fifteen', data['fifteen'])
        chunk_sixteen = Chunk(pos_list[15], False, 'sixteen', data['sixteen'])
        chunk_seventeen = Chunk(pos_list[16], False, 'seventeen', data['seventeen'])
        chunk_eighteen = Chunk(pos_list[17], False, 'eighteen', data['eighteen'])
        chunk_nineteen = Chunk(pos_list[18], False, 'nineteen', data['nineteen'])
        chunk_twenty = Chunk(pos_list[19], False, 'twenty', data['twenty'])
        chunk_twentyone = Chunk(pos_list[20], False, 'twentyone', data['twentyone'])
        chunk_twentytwo = Chunk(pos_list[21], False, 'twentytwo', data['twentytwo'])
        chunk_twentythree = Chunk(pos_list[22], False, 'twentythree', data['twentythree'])
        chunk_twentyfour = Chunk(pos_list[23], False, 'twentyfour', data['twentyfour'])
        chunk_twentyfive = Chunk(pos_list[24], False, 'twentyfive', data['twentyfive'])
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
    chunk_ten = Chunk(pos_list[0], False, 'ten')
    chunk_eleven = Chunk(pos_list[1], False, 'eleven')
    chunk_twelve = Chunk(pos_list[2], False, 'twelve')
    chunk_thirteen = Chunk(pos_list[3], False, 'thirteen')
    chunk_fourteen = Chunk(pos_list[4], False, 'fourteen')
    chunk_fifteen = Chunk(pos_list[14], False, 'fifteen')
    chunk_sixteen = Chunk(pos_list[15], False, 'sixteen')
    chunk_seventeen = Chunk(pos_list[16], False, 'seventeen')
    chunk_eighteen = Chunk(pos_list[17], False, 'eighteen')
    chunk_nineteen = Chunk(pos_list[18], False, 'nineteen')
    chunk_twenty = Chunk(pos_list[19], False, 'twenty')
    chunk_twentyone = Chunk(pos_list[20], False, 'twentyone')
    chunk_twentytwo = Chunk(pos_list[21], False, 'twentytwo')
    chunk_twentythree = Chunk(pos_list[22], False, 'twentythree')
    chunk_twentyfour = Chunk(pos_list[23], False, 'twentyfour')
    chunk_twentyfive = Chunk(pos_list[24], False, 'twentyfive')
all_sprites = pygame.sprite.Group()

chunk_list = [
    chunk_one,
    chunk_two,
    chunk_three,
    chunk_four,
    chunk_five,
    chunk_six,
    chunk_seven,
    chunk_eight,
    chunk_nine,
    chunk_ten,
    chunk_eleven,
    chunk_twelve,
    chunk_thirteen,
    chunk_fourteen,
    chunk_fifteen,
    chunk_sixteen,
    chunk_seventeen,
    chunk_eighteen,
    chunk_nineteen,
    chunk_twenty,
    chunk_twentyone,
    chunk_twentytwo,
    chunk_twentythree,
    chunk_twentyfour,
    chunk_twentyfive
    ]
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
cam = pygame.Vector2((0, 0))

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
    if pressed_keys[K_w]:
        player.rect.move_ip(0, -speed)
    if pressed_keys[K_s]:
        player.rect.move_ip(0, speed)
    if pressed_keys[K_a]:
        player.rect.move_ip(-speed, 0)
    if pressed_keys[K_d]:
        player.rect.move_ip(speed, 0)
    
    prev_sprite = False
    next_sprite = False
    ver_sprite = False
    bot_sprite = False
    
    for chunk in chunk_list:
        # three extra vars for tracking what block we are on
        z = 0
        v = 0
        b = 0
        for sprite in chunk.blocks:
            if pressed_keys[K_w]:
                if sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                    hit_id.append(1)
            if pressed_keys[K_s]:
                if sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                    hit_id.append(2)
            if pressed_keys[K_a]:
                if sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                    hit_id.append(3)
            if pressed_keys[K_d]:
                if sprite.id > 0 and pygame.sprite.collide_rect(player, sprite):
                    hit_id.append(4)
            if sprite.rect.collidepoint(x, y) and hasattr(sprite, "id") and not hasattr(sprite, "name"):
                dist = ((player.rect.x - x) ** 2 + (player.rect.y - y)  ** 2) ** 0.5
                if not pygame.sprite.collide_rect(player, sprite) and dist < 125:
                    if sprite.id != 0 and is_build == False:
                        sprite.hp -= player.pickaxe
                        if sprite.hp <= 0:
                            player.add_item(sprite.id, 1)
                            sprite.change_block(0)
                    elif sprite.id == 0 and is_build == True and selected_block != 0 and player.inventory[str(selected_block)] > 0:
                        sprite.change_block(selected_block)
                        player.remove_item(selected_block, 1)
            #if sprite.rect.x > -20 and sprite.rect.x < SCREEN_WIDTH + 20 and sprite.rect.y > -20 and sprite.rect.y < SCREEN_HEIGHT + 20:
            if prev_sprite and sprite.check_render(prev_sprite, next_sprite, ver_sprite, bot_sprite):
                screen.blit(sprite.surf, (sprite.rect.x + player.rect.x, sprite.rect.y + player.rect.y))
            prev_sprite = sprite
            if z < len(chunk.blocks) - 2:
                next_sprite = chunk.blocks[z + 2]
            if v > 32:
                ver_sprite = chunk.blocks[z - 31]
            else:
                ver_sprite = False
            if b < len(chunk.blocks) - 33:
                bot_sprite = chunk.blocks[z + 33]
            else:
                bot_sprite = False
            z += 1
            v += 1
            b += 1
    if 1 in hit_id:
        player.rect.move_ip(0, speed)
    if 2 in hit_id:
        player.rect.move_ip(0, -speed)
    if 3 in hit_id:
        player.rect.move_ip(speed, 0)
    if 4 in hit_id:
        player.rect.move_ip(-speed, 0)
                
    
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
    screen.blit(player.surf, (round(SCREEN_WIDTH/2), round(SCREEN_HEIGHT/2)))


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
    x_pos = cam.rect.x + 12
    y_pos = cam.rect.y + 12
    data = {'hp': player.hp, 'pickaxe': player.pickaxe, 'axe': player.axe, 'sword': player.sword, 'x_pos': x_pos, 'y_pos': y_pos}
    json.dump(data, file)


with open('inventory.json', 'w') as file:
    json.dump(player.inventory, file)


with open('world.json', 'w') as file:
    keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twentyone', 'twentytwo', 'twentythree', 'twentyfour', 'twentyfive']
    z = 0
    data = {'one': [], 'two': [], 'three': [], 'four': [], 'five': [], 'six': [], 'seven': [], 'eight': [], 'nine': [], 'ten': [], 'eleven': [], 'twelve': [], 'thirteen': [], 'fourteen': [], 'fifteen': [], 'sixteen': [], 'seventeen': [], 'eighteen': [], 'nineteen': [], 'twenty': [], 'twentyone': [], 'twentytwo': [], 'twentythree': [], 'twentyfour': [], 'twentyfive': []}
    for chunk in chunk_list:
        rows = list(split(chunk.blocks, 32))
        for row in rows:
            temp_row = []
            for block in row:
                temp_row.append(block.id)
            data[keys[z]].append(temp_row)
        z += 1
    json.dump(data, file)