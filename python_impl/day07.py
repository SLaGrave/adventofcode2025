
def load_data(data_location):
    """Loads data from a txt file.
    
    Read lines, strip each one, and return as a list
    """
    with open(data_location, "r") as f:
        data = [list(q.strip()) for q in f.readlines()]
    return data


def part_one(data):
    counter = 0
    beams = set([data[0].index("S")])
    for row in data:
        if row == 1: continue
        new_beams = set()
        for beam in beams:
            if row[beam] == "^":
                new_beams.add(beam-1)
                new_beams.add(beam+1)
                counter += 1
            else:
                new_beams.add(beam)
        beams = new_beams
    return counter


def part_two(data):
    timelines = [0]* len(data)
    timelines[data[0].index("S")] += 1
    for row in data:
        new_timelines = timelines.copy()
        for idx, item in enumerate(row):
            if item == "^":
                value = timelines[idx]
                new_timelines[idx] = 0
                new_timelines[idx-1] += value
                new_timelines[idx+1] += value
        timelines = new_timelines
    return sum(timelines)


def run(data_location = "../inputs/day07.txt"):
    data = load_data(data_location)
    print(part_one(data.copy()))
    print(part_two(data.copy()))


if __name__ == "__main__":
    run()
