SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

FRAME_RATE = 30

CHUNK_SIZE = 32

UPGRADE_COST = 5

BLOCK_LIST = [
    ["Dirt", (30, 30)],
    ["Grass", (30, 45)],
    ["Stone", (30, 60)],
    ["Red Ore", (30, 75)],
    ["Blue Ore", (30, 90)]
]
#0, just background
#1, upgrade pickaxe
UI_LIST = [
    [(200, 160), (100, 80), 0],
    [(220, 100), (SCREEN_WIDTH - 110, 50), 0],
    [(50, 50), (SCREEN_WIDTH - 175, 75), 1]
]