fn day4_part1(input: &str) -> i64 {
    input.split('\n').map(|l| is_valid(l) as i64).sum()
}

fn is_valid(input: &str) -> bool {
    let mut words = input.split_whitespace().collect::<Vec<&str>>();
    words.sort();
    let before_len = words.len();
    words.dedup();

    before_len == words.len()
}
