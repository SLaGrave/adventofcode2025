
def load_data(data_location):
    """Loads data from a txt file.
    
    Read lines, strip each one, and return as a list
    """
    with open(data_location, "r") as f:
        data = [q.strip() for q in f.readlines()]
    return data


def part_one(data):
    return -1


def part_two(data):
    return -1


def run(data_location = "../inputs/day12.txt"):
    data = load_data(data_location)
    print(part_one(data.copy()))
    print(part_two(data.copy()))


if __name__ == "__main__":
    run()
