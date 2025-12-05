
def load_data(data_location):
    """Loads data from a txt file.
    
    Read lines, strip each one, split into fresh and available ingredients,
    make fresh a list of lists, and make all int-strings actually ints.
    """
    with open(data_location, "r") as f:
        data = [q.strip() for q in f.readlines()]
        fresh = list()
        available = list()
        first_half_of_list = True
        for item in data:
            if item == "":
                first_half_of_list = False
                continue
            if first_half_of_list:
                tmp = item.split("-")
                fresh.append([int(tmp[0]), int(tmp[1])])
            else:
                available.append(int(item))
    return fresh, available


def part_one(fresh, available):
    counter = 0
    for item in available:
        for pair in fresh:
            if item >= pair[0] and item <= pair[1]:
                counter += 1
                break
    return counter


def sub_part_two(fresh):
    """Goes through the fresh list and tries to fold ranges into each other
    wherever possible. Needs to be run several times."""
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
        new_fresh = sub_part_two(fresh)
        if new_fresh == fresh:
            counter = 0
            for item in fresh:
                counter += item[1] - item[0] + 1
            return counter
        fresh = new_fresh


def run(data_location = "../inputs/day05.txt"):
    fresh, available = load_data(data_location)
    print(part_one(fresh.copy(), available.copy()))
    print(part_two(fresh.copy()))


if __name__ == "__main__":
    run()
