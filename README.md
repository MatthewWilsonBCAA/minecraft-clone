# minecraft-clone
going to be a top-down minecraft clone, using Pygame

# controls
Use WASD to move your character, use numbers 1-5 to select what block you want to build with, use B to toggle between Build Mode and Mine Mode, and use any mouse click to interact with the grid.

# blocks
There are 5 different blocks in the game: Dirt, Grass, Stone, Red (Iron) Ore, and Blue (Cobalt) Ore. Do note that Stone and the Ores require multiple mouse clicks to successfully mine them.

# main.py
This file pulls from the other files, and runs the game. It mainly focuses on the physics and input
management.

# classes.py
This file stores the various sprite classes found in the game. Also stores the input constants.

# constants.py
This file stores commonly-used values.

# chunks.py
This file interpets given chunk files (stores as .txt files), and makes them availabe to the
rest of the game.

# the .json files
These files store the player's save data, with world.json storing the chunks' states, inventory.json
storing how many of each block type the player is holding, and stats.json storing the player's current
hp, pickaxe tier, axe tier, sword tier, and their position relative to the center of the world.

# starting over / creating new worlds
To generate a new world, simply delete the world.json file (you can back the current one up if you wish). To change between worlds with backups, you could rename ones you are not using, just note the program only reads whatever file is named world.json. If the program cannot find a file named world.json, it will generate a new world. This process can be used to have seperate characters also.