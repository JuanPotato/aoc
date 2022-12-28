fn day2_part2(input: &str) -> u32 {
    input
        .split("\n")
        .map(|l| {
            l.split_whitespace()
                .map(|n| u32::from_str_radix(n, 10).unwrap())
                .collect::<Vec<u32>>()
        })
        .map(|ref l| {
            'outer: for n in l {
                for m in l {
                    if m > n && m % n == 0 {
                        return m / n;
                    }
                }
            }
            0
        })
        .sum()
}
