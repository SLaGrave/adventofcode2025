
def load_data(data_location):
    """Loads data from a txt file.
    
    Read lines, strip each one, and return as a list
    """
    with open(data_location, "r") as f:
        data = [q.strip() for q in f.readlines()]
    values = data[:-1]
    values = [[x for x in q.split(" ") if x != ""] for q in values]
    ops = data[-1].split(" ")
    ops = [q for q in ops if q != ""]
    return values, ops


def part_one(values, ops):
    counter = 0
    for x in range(len(ops)):
        my_values = list()
        for row in values:
            my_values.append(row[x])
        s = ops[x].join(my_values)
        counter += eval(s)

    return counter


def part_two(data_location):
    counter = 0
    with open(data_location, "r") as f:
        data = f.readlines()
    data = [q.replace("\n", "") for q in data]
    cols = list()
    for x in range(len(data[0])):
        s = ""
        for row in data:
            s += row[x]
        cols.insert(0, s)
    
    print(cols)

    my_items = list()
    for item in cols:
        item = item.strip()
        if item == "":
            print(my_items)
            my_items = list()
            continue
        try:
            my_items.append(str(eval(item)))
        except:
            my_items.append(str(eval(item[:-1])))
            counter += eval(item[-1].join(my_items))

    return counter


def run(data_location = "../inputs/day04.txt"):
    values, ops = load_data(data_location)
    print(part_one(values.copy(), ops.copy()))
    print(part_two(data_location))


if __name__ == "__main__":
    run()
