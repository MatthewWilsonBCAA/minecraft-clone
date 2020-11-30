SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

FRAME_RATE = 60

CHUNK_SIZE = 32

UPGRADE_COST = 5
REND_DIST = 175
BLOCK_LIST = [
    ["Dirt", "images/dirt.png", (30, 30), 1, 25],
    ["Grass", "images/grass.png", (30, 55), 2, 2],
    ["Stone", "images/stone.png", (30, 80), 3, 52],
    ["Red Ore", "images/red-ore.png", (30, 105), 4, 55],
    ["Blue Ore", "images/blue-ore.png", (30, 130), 5, 60],
    ["Green Ore", "images/green-ore.png", (30, 155), 6, 57],
    ["Warm Rock", "images/warm-rock.png", (30, 180), 7, 40]
]
#0, just background
#1, upgrade pickaxe
UI_LIST = [
    [(200, 180), (100, 90), 2],
    [(220, 100), (SCREEN_WIDTH - 110, 50), 0],
    [(50, 50), (SCREEN_WIDTH - 175, 75), 1]
]
