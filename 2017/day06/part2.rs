fn day6_part2(input: &str) -> i64 {
    use std::collections::HashMap;
    let mut states = HashMap::with_capacity(1000);

    let mut state = [0u8; 16];

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

        if let Some(old_cycle) = states.insert(state, cycles) {
            return cycles - old_cycle;
        }
    }

    cycles - states.get(&state).unwrap()
}
