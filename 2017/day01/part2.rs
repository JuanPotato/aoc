fn day1_part2(input: &str) -> u32 {
    let mut sum = 0;
    let digits: Vec<char> = input.chars().collect();

    for i in 0..digits.len() {
        if digits[i] == digits[(i + digits.len() / 2) % digits.len()] {
            sum += digits[i].to_digit(10).unwrap();
        }
    }

    sum
}
