fn day1_part1(input: &str) -> u32 {
    let mut sum = 0;
    let chars: Vec<char> = input.chars().collect();

    for digits in chars.windows(2) {
        if digits[0] == digits[1] {
            sum += digits[0].to_digit(10).unwrap();
        }
    }

    if chars[0] == chars[input.len() - 1] {
        sum += chars[0].to_digit(10).unwrap();
    }

    sum
}
