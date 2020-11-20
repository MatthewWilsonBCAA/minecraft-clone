SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

FRAME_RATE = 15

CHUNK_SIZE = 32

UPGRADE_COST = 5

BLOCK_LIST = [
    ["Dirt", "images/dirt.png", (30, 30), 1],
    ["Grass", "images/grass.png", (30, 55), 2],
    ["Stone", "images/stone.png", (30, 80), 3],
    ["Red Ore", "images/red-ore.png", (30, 105), 4],
    ["Blue Ore", "images/blue-ore.png", (30, 130), 5]
]
#0, just background
#1, upgrade pickaxe
UI_LIST = [
    [(200, 160), (100, 80), 2],
    [(220, 100), (SCREEN_WIDTH - 110, 50), 0],
    [(50, 50), (SCREEN_WIDTH - 175, 75), 1]
]
