
def load_data(data_location):
    """Loads data from a txt file.
    
    Read lines, strip each one, and return as a list
    """
    with open(data_location, "r") as f:
        data = [q.strip() for q in f.readlines()]
        fresh = list()
        second = list()
        alnsd = True
        for item in data:
            if item == "":
                alnsd = False
                continue
            if alnsd:
                tmp = item.split("-")
                fresh.append([int(tmp[0]), int(tmp[1])])
            else:
                second.append(int(item))
    return fresh, second


def part_one(fresh, second):
    counter = 0
    for item in second:
        for pair in fresh:
            if item >= pair[0] and item <= pair[1]:
                counter += 1
                break
    return counter


def sub(fresh):
    maxes = list()
    for item in fresh:
        x, y = item
        got = False
        for idx, m in enumerate(maxes):
            dx, dy = m
            # Fully between, do nothing
            if x >= dx and x <= dy and y >= dx and y <= dy:
                got = True
                break
            # new upper
            elif x >= dx and x <= dy and y > dy:
                maxes[idx][1] = y
                got = True
                break
            # new lower
            elif x < dx and y >= dx and y <= dy:
                maxes[idx][0] = x
                got = True
                break
            # all new
            elif x < dx and y > dy:
                maxes[idx][0] = x
                maxes[idx][1] = y
                got = True
                break
        if not got:
            maxes.append(item)
    return maxes


def part_two(fresh):
    while True:
        print(fresh)
        new_fresh = sub(fresh)
        if new_fresh == fresh:
            counter = 0
            for item in fresh:
                counter += item[1] - item[0] + 1
            return counter
        fresh = new_fresh


def run(data_location = "../inputs/day05.txt"):
    fresh, second = load_data(data_location)
    print(part_one(fresh.copy(), second.copy()))
    print(part_two(fresh.copy()))


if __name__ == "__main__":
    run()
