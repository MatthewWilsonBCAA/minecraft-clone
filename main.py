from classes import *
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()

all_sprites = pygame.sprite.Group()
chunk_one = Chunk((-2000, -2000))
for block in chunk_one.blocks:
    all_sprites.add(block)
running = True
while running:
    screen.fill((0, 0, 0))
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.blit(player.surf, player.rect)
    speed = -1
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
        screen.blit(sprite.surf, sprite.rect)
    pygame.display.flip()
    clock.tick(FRAME_RATE)
    