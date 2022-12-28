fn day5_part2(input: &str) -> i64 {
    let mut numbers = input
        .split_whitespace()
        .map(|n| i64::from_str_radix(n, 10).unwrap())
        .collect::<Vec<i64>>();

    let mut index: i64 = 0;
    let mut steps = 0;

    loop {
        if (index as usize) < numbers.len() && index >= 0 {
            let offset = numbers[index as usize];

            numbers[index as usize] += if offset >= 3 { -1 } else { 1 };
            index += offset;
            steps += 1;
        } else {
            break;
        }
    }

    steps
}
