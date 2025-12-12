use crate::utils;

fn load_data(data_location: &str) -> Vec<i32> {
    let mut ints: Vec<i32> = Vec::new();
    let lines = utils::read_lines(data_location);
    for mut sign in lines {
        let n = sign.split_off(1);
        let mut i_n = n.parse::<i32>().unwrap();
        if sign == "L" {
            i_n *= -1;
        }
        ints.push(i_n);
    }
    return ints;
}

fn part_one(data_location: &str) -> i32 {
    let data: Vec<i32> = load_data(data_location);
    let mut counter: i32 = 0;
    let mut dial: i32 = 50;
    for turn in data {
        dial = (dial + turn) % 100;
        if dial == 0 {
            counter += 1;
        }
    }
    return counter;
}

fn part_two(data_location: &str) -> i32 {
    let data: Vec<i32> = load_data(data_location);
    let mut counter: i32 = 0;
    let mut dial: i32 = 50;
    for turn in data {
        let sign = turn/turn.abs();  // Get just the sign of the turn value
        for _ in 0..turn.abs() {
            dial = (dial + sign) % 100;
            if dial == 0 {
                counter += 1;
            }
        }
    }
    return counter;
}

pub fn run(data_location: &str) {
    println!("{}", part_one(data_location));
    println!("{}", part_two(data_location));
}
