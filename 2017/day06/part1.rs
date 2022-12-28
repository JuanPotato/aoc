fn day6_part1(input: &str) -> i64 {
    use std::collections::HashSet;
    let mut states = HashSet::with_capacity(100);

    let mut state = [0u8; 16];
    println!("{:?}", &state);

    for (i, n) in input
        .split_whitespace()
        .map(|n| u8::from_str_radix(n, 10).unwrap())
        .enumerate()
    {
        state[i] = n;
    }

    let len = state.len();
    let mut cycles = 0;

    loop {
        let max_index = state
            .iter()
            .enumerate()
            .rev()
            .max_by_key(|e| e.1)
            .unwrap()
            .0;
        let max = state[max_index];
        state[max_index] = 0;

        for i in 0..max {
            state[(max_index + 1 + i as usize) % len] += 1;
        }

        cycles += 1;

        if !states.insert(state) {
            break;
        }
    }

    cycles
}
