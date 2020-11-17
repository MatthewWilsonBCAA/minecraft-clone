from classes import *
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()

all_sprites = pygame.sprite.Group()
chunk_one = Chunk((0, 0), True)
chunk_two = Chunk((800, 0), False)
chunk_three = Chunk((0, 800), False)
chunk_four = Chunk((800, 800), False)
chunk_five = Chunk((-800, 0), False)
chunk_six = Chunk((-800, -800), False)
chunk_seven = Chunk((0, -800), False)
chunk_list = [chunk_one, chunk_two, chunk_three, chunk_four, chunk_five, chunk_six, chunk_seven]
for chunk in chunk_list:
    for block in chunk.blocks:
        all_sprites.add(block)
running = True
while running:
    screen.fill((0, 0, 0))
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
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
    