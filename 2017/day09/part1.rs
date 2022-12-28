fn day9_part1(input: &str) -> i64 {
    let mut score = 0;
    let mut level = 0;
    let mut garbage = false;
    let mut skip = false;

    for c in input.trim().chars() {
        if skip {
            skip = false;
            continue;
        }

        match c {
            '!' => skip = true,

            '<' => garbage = true,

            '>' => garbage = false,

            '{' => {
                if !garbage {
                    level += 1;
                }
            }

            '}' => {
                if !garbage {
                    score += level;
                    level -= 1;
                }
            }

            _ => continue,
        }
    }

    score
}
