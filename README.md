# Advent of Code 2025 🎄

[Advent of Code 2025](adventofcode.com/2025) in a variety(?) of languages - currently just Python3.

## Usage

If you want to run the Python 3 implementation, I have a script (`pyaoc25.py`)
that will run any day on any input. Use the command:

```sh
$ python pyaoc25.py <day> <input_path>
# Example command
$ python pyaoc25.py 1 inputs/day01.txt
```

## Notes on days

### Day 01

My solution to Part two is very naive - if there were much larger values in my
input, my runtime may have been massive. But everything seems to be working out,
so I don't really care too much right now. Might go back and optimize it a bit
later...

### Day 03

So I ended up solving Part 2 while doing Part 1. I have been reading these
problems at night, and then actually coding the solution in the morning. Last
night I could see the solution to Day 3 for two steps, but I wanted to
generalize it. That's what led to the recursive function in my repo. I was so
happy when Part 2 was simply more digits!

### Day 06

This code directly uses python's `eval`, so be careful what input files you give
it.
