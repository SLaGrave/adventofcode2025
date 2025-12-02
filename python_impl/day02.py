
def load_data(data_location):
    """Loads data from a txt file.
    
    Reads the line, splits by commas, then saves as a pair of ints on either
    side of the dash.
    """
    with open(data_location, "r") as f:
        data = f.read()
    data = data.split(",")
    data = [q.strip() for q in data]
    data = [q.split("-") for q in data]
    return data


def check_id(item):
    # if str(item)[0] == "0":
    #     return False
    if len(str(item))%2 != 0:
        return True
    half_len = int(len(str(item))/2)
    if str(item)[:half_len] == str(item)[half_len:]:
        return False
    return True


def check_id_two(item):
    substring = ""
    item = str(item)
    for idx, letter in enumerate(item):
        if idx == len(item)-1:
            return True
        substring = f"{substring}{letter}"
        if len(item.replace(substring, ""))==0:
            return False


def part_n(data, method):
    counter = 0
    possible_ids = list()
    for begin, end in data:
        possible_ids.extend(range(int(begin), int(end)+1))
    for pid in possible_ids:
        if not method(pid):
            counter += pid
    return counter


def run(data_location = "../inputs/day02.txt"):
    data = load_data(data_location)
    print(part_n(data.copy(), check_id))
    print(part_n(data.copy(), check_id_two))


if __name__ == "__main__":
    run()
