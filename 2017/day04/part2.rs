fn day4_part2(input: &str) -> i64 {
    input.split('\n').map(|l| is_valid(l) as i64).sum()
}

fn is_valid(input: &str) -> bool {
    let mut words = input
        .split_whitespace()
        .map(|w| {
            let mut letters = w.chars().collect::<Vec<char>>();
            letters.sort();

            letters.iter().collect::<String>()
        })
        .collect::<Vec<String>>();

    words.sort();
    let before_len = words.len();
    words.dedup();

    before_len == words.len()
}
