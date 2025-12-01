
def load_data(data_location = "../inputs/day01.txt"):
    """Loads data from a txt file.
    
    Read lines, strip each one, and return as a list
    """
    with open(data_location, "r") as f:
        data = [q.strip() for q in f.readlines()]
    return data


def part_one(data):
    counter = 0
    dial = 50
    for turn in data:
        # Transform into integer
        # "L50" -> -50
        # "R109" -> 109
        turn = int(turn[1:]) if turn[0] == "R" else int(f"-{turn[1:]}")
        dial = (dial + turn) % 100
        if dial == 0: counter += 1
    return counter


def part_two(data):
    counter = 0
    dial = 50
    for turn in data:
        sign = 1 if turn[0] == "R" else -1
        turn = int(turn[1:])
        for _ in range(turn):
            dial = (dial + sign) % 100
            if dial == 0: counter += 1
    return counter


if __name__ == "__main__":
    data = load_data()
    print(part_one(data.copy()))
    print(part_two(data.copy()))
