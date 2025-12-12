import ast

class Machine:
    def __init__(self, s: str):
        self.lights = ""
        self.buttons = list()
        self.joltages = list()
        parts = s.split(" ")
        for idx, part in enumerate(parts):
            if idx == 0:
                self.lights = ast.literal_eval(part.replace("[", "'").replace("]", "'"))
            elif idx == len(parts)-1:
                self.joltages = ast.literal_eval(part.replace("{", "[").replace("}", "]"))
            else:
                self.buttons.append(ast.literal_eval(part.replace("(", "[").replace(")", "]")))

    def part_one(self):
        return -1
    
    def part_two(self):
        return -1


def load_data(data_location):
    """Loads data from a txt file.
    
    Read lines, strip each one, and return as a list
    """
    with open(data_location, "r") as f:
        data = [Machine(q.strip()) for q in f.readlines()]
    return data


def run(data_location = "../inputs/day10.txt"):
    data = load_data(data_location)
    print(sum([machine.part_one() for machine in data]))
    print(sum([machine.part_two() for machine in data]))


if __name__ == "__main__":
    run()
