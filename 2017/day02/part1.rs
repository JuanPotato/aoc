fn day2_part1(input: &str) -> u32 {
    input
        .split("\n")
        .map(|l| {
            l.split_whitespace()
                .map(|n| u32::from_str_radix(n, 10).unwrap())
                .collect::<Vec<u32>>()
        })
        .map(|l| {
            l.iter().cloned().max().unwrap() - l.iter().min().unwrap()
        })
        .sum()
}
