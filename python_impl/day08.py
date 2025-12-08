import ast
import math


def load_data(data_location):
    """Loads data from a txt file.
    
    Read lines, strip each one, and return as a list
    """
    with open(data_location, "r") as f:
        data = [ast.literal_eval(f"[{q.strip()}]") for q in f.readlines()]
    return data


def calc_dist(loc1, loc2):
    total = 0
    for idx in range(len(loc1)):
        total += (loc1[idx]-loc2[idx])**2
    return math.sqrt(total)


def part_one(locations, num_closest = 1000, num_product = 3):
    networks = list()
    # Create distances
    distances = list()
    for idx1, loc1 in enumerate(locations):
        networks.append(set([idx1]))  # Append to networks
        for idx2 in range(idx1+1, len(locations)):
            loc2 = locations[idx2]
            distances.append((calc_dist(loc1, loc2), (idx1, idx2)))
    # Order distances & trim
    distances = sorted(distances, key = lambda dist: dist[0])
    distances = distances[:num_closest]
    # Combine networks
    for d in distances:
        a, b = d[1]
        new_networks = [set([a, b])]
        for net in networks:
            if a in net or b in net:
                new_networks[0].update(net)
            else:
                new_networks.append(net)
        networks = new_networks
    # Start getting answer
    networks = [len(q) for q in networks]
    networks = sorted(networks, reverse=True)
    networks = networks[:num_product]
    return math.prod(networks)


def part_two(locations):
    networks = list()
    # Create distances
    distances = list()
    for idx1, loc1 in enumerate(locations):
        networks.append(set([idx1]))  # Append to networks
        for idx2 in range(idx1+1, len(locations)):
            loc2 = locations[idx2]
            distances.append((calc_dist(loc1, loc2), (idx1, idx2)))
    # Order distances & trim
    distances = sorted(distances, key = lambda dist: dist[0])
    # Combine networks
    for d in distances:
        a, b = d[1]
        new_networks = [set([a, b])]
        for net in networks:
            if a in net or b in net:
                new_networks[0].update(net)
            else:
                new_networks.append(net)
        networks = new_networks
        if len(networks) == 1:
            return locations[a][0] * locations[b][0]
    return -1


def run(data_location = "../inputs/day08.txt"):
    data = load_data(data_location)
    print(part_one(data.copy()))
    print(part_two(data.copy()))


if __name__ == "__main__":
    run()