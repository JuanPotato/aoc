use std::collections::HashSet;

fn solve(input_str: &str) -> (i32, i32) {
    let nums: Vec<i32> = input_str.lines().map(|s| s.parse::<i32>().unwrap()).collect();

    let part1 = nums.iter().sum();

    let mut freqs = HashSet::with_capacity(nums.len());
    let mut part2 = 0;
    for n in nums.iter().cycle() {
        if !freqs.insert(part2) {
            break;
        }
        part2 += n;
    }

    (part1, part2)
}

fn main() {
    let input = include_str!("../input/day1.input");
    let answer = solve(input);
    
    println!("{:?}", answer);
    assert_eq!(answer, (508, 549));
}
