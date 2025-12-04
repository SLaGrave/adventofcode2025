
def load_data(data_location):
    """Loads data from a txt file.
    
    Read lines, strip each one, and return as a list
    """
    with open(data_location, "r") as f:
        data = [list(q.strip()) for q in f.readlines()]
    return data


def part_one(data):
    counter = 0
    height = len(data)
    width = len(data[0])
    new_data = list()
    for y in range(height):
        new_row = list()
        for x in range(width):
            if data[y][x] == ".":
                new_row.append(None)
                continue
            item = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if (dy == 0 and dx == 0) \
                    or (y + dy < 0) or (y + dy >= height) \
                    or (x + dx < 0) or (x + dx >= width):
                        continue
                    if data[y+dy][x+dx] == "@":
                        item += 1
            new_row.append(item)
        new_data.append(new_row)
    for y in range(height):
        for x in range(width):
            tmp = new_data[y][x]
            if tmp is None: continue
            if tmp < 4:
                counter += 1
    return counter


def part_two(data):
    counter = 0
    height = len(data)
    width = len(data[0])

    while True:
        new_data = list()
        for y in range(height):
            new_row = list()
            for x in range(width):
                if data[y][x] == ".":
                    new_row.append(None)
                    continue
                item = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if (dy == 0 and dx == 0) \
                        or (y + dy < 0) or (y + dy >= height) \
                        or (x + dx < 0) or (x + dx >= width):
                            continue
                        if data[y+dy][x+dx] == "@":
                            item += 1
                new_row.append(item)
            new_data.append(new_row)
        none_changed = True
        for y in range(height):
            for x in range(width):
                if new_data[y][x] is None:
                    data[y][x] = "."
                elif new_data[y][x] < 4:
                    counter += 1
                    data[y][x] = "."
                    none_changed = False
                else:
                    data[y][x] = "@"
        if none_changed:
            break

    return counter


def run(data_location = "../inputs/day04.txt"):
    data = load_data(data_location)
    print(part_one(data.copy()))
    print(part_two(data.copy()))


if __name__ == "__main__":
    run()
