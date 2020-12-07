def repr_int(x):
    try:
        x = int(x)
        return True
    except ValueError:
        return False


chunk_styles = {}

files = [
    "mount_one.txt",
    "mount_two.txt",
    "thunderdome.txt",
    "graveyard.txt",
    "forest.txt",
]
for name in files:
    running = True
    with open(name) as file:
        chunk_styles[name] = []
        while running:
            cur_line = list(file.readline())
            if "E" in cur_line:
                running = False
            temp_list = []
            for i in cur_line:
                if repr_int(i):
                    temp_list.append(int(i))
                elif i == "s":
                    temp_list.append(-3)
                elif i == "o":
                    temp_list.append(-2)
                elif i == "n":
                    temp_list.append(-1)
                elif i == "t":
                    temp_list.append(-4)
            if temp_list:
                chunk_styles[name].append(temp_list)