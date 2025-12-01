
def load_data():
    with open("../inputs/day01.txt", "r") as f:
        data = [q.strip() for q in f.readlines()]
    return data


def part_one(data):
    dial = 50
    counter = 0
    for turn in data:
        if turn[0] == "R": turn = turn[1:]
        else: turn = f"-{turn[1:]}"
        turn = int(turn)
        dial = (dial + turn) % 100
        if dial == 0: counter += 1
    return counter


def part_two(data):
    dial = 50
    counter = 0
    for turn in data:
        if turn[0] == "L": sign = -1
        else: sign = 1
        turn = int(turn[1:])
        for _ in range(turn):
            dial += sign*1
            dial %= 100
            if dial == 0: counter += 1
    return counter


if __name__ == "__main__":
    data = load_data()
    print(part_one(data.copy()))
    print(part_two(data.copy()))
