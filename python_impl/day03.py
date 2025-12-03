
def load_data(data_location):
    """Loads data from a txt file.
    
    Read lines, strip each one, and return as a list
    """
    with open(data_location, "r") as f:
        data = [q.strip() for q in f.readlines()]
    return data


def find_largest(string, n=2, substring=""):
    # print(string, n, substring)
    if n==0:
        return int(substring)
    # Find largest single digit
    largest_digit = "1"
    for c in string[:len(string)-n+1]:
        if c > largest_digit:
            largest_digit = c
    largest_idx = string.index(largest_digit)
    return find_largest(string[largest_idx+1:], n=n-1, substring=f"{substring}{largest_digit}")


def part_one(data):
    counter = 0
    for bank in data:
        counter += find_largest(bank)
    return counter


def part_two(data):
    counter = 0
    for bank in data:
        counter += find_largest(bank, n=12)
    return counter


def run(data_location = "../inputs/day03.txt"):
    data = load_data(data_location)
    print(part_one(data.copy()))
    print(part_two(data.copy()))


if __name__ == "__main__":
    run()
