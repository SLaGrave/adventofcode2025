use std::env;

mod day01;
mod utils;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() <= 2 {
        println!("Provide more arguments!");
        return;
    }

    let day = &args[1].parse::<i32>().unwrap();
    let input_path = &args[2];

    match day {
        1 => {
            day01::run(&input_path);
        }
        _ => {
            println!("Unimplmented day!");
        }
    }
}
