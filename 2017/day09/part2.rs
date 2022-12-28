fn day9_part2(input: &str) -> i64 {
    let mut score = 0;
    let mut total_garbage = 0;
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

            '<' => {
                if garbage {
                    total_garbage += 1;
                }

                garbage = true;
            }

            '>' => garbage = false,

            '{' => {
                if !garbage {
                    level += 1;
                } else {
                    total_garbage += 1;
                }
            }

            '}' => {
                if !garbage {
                    score += level;
                    level -= 1;
                } else {
                    total_garbage += 1;
                }
            }

            _ => {
                if garbage {
                    total_garbage += 1;
                }
            }
        }
    }

    total_garbage
}
