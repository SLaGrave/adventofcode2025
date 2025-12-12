
def load_devices(data_location):
    with open(data_location, "r") as f:
        data = [q.strip() for q in f.readlines()]
    devices = dict()
    for line in data:
        line = line.split(": ")
        devices[line[0]] = line[1].split(" ")
    return devices


def dfs(current, devices, path=list()):
    """Basic Depth First Search algorithm.
    
    Modified from here:
    https://www.geeksforgeeks.org/dsa/find-paths-given-source-destination/

    Returns
    -------
    counter : int
        Number of paths that lead from current to "out"
    """
    counter = 0
    path.append(current)
    if current == "out": counter += 1
    else:
        for output in devices[current]:
            counter += dfs(output, devices, path)
    path.pop()
    return counter


def part_one(devices):
    return dfs("you", devices)


def part_two(devices):
    return -1


def run(data_location = "../inputs/day11.txt"):
    devices = load_devices(data_location)
    print(part_one(devices.copy()), flush=True)
    print(part_two(devices.copy()), flush=True)


if __name__ == "__main__":
    run()
