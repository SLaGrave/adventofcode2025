import ast


def load_data(data_location):
    """Loads data from a txt file.
    
    Read lines, strip each one, and return as a list
    """
    with open(data_location, "r") as f:
        data = [ast.literal_eval(f"[{q.strip()}]") for q in f.readlines()]
    return data


def area(loc1, loc2):
    return (abs(loc1[0]-loc2[0])+1) * (abs(loc1[1]-loc2[1])+1)


def part_one(data):
    counter = 0
    for idx1, loc1 in enumerate(data):
        for idx2, loc2 in enumerate(data[idx1+1:]):
            a = area(loc1, loc2)
            if a > counter: counter = a
    return counter


def part_two(data):
    # I hate this one...
    return -1


def run(data_location = "../inputs/day09.txt"):
    data = load_data(data_location)
    print(part_one(data.copy()))
    print(part_two(data.copy()))


if __name__ == "__main__":
    run()
