fn day3_part1(input: i64) -> i64 {
    let coords = get_coords(input);
    coords.0.abs() + coords.1.abs()
}

fn get_coords(num: i64) -> (i64, i64) {
    // What this does is find the nearest square, move to a corner, then adjust the x or y
    let sqrt = (num as f64).sqrt().round() as i64;
    let base = sqrt * sqrt + 1;
    let dif = base - num;

    let mut x = 0;
    let mut y = 0;

    if sqrt % 2 == 0 {
        // even
        x = -sqrt / 2;
        y = -x;

        if dif > 0 {
            // if base > num
            x += dif;
        } else {
            // if base < num
            y += dif;
        }
    } else {
        x = sqrt / 2 + 1;
        y = -x + 1;

        if dif > 0 {
            // if base > num
            x -= dif;
        } else {
            // if base < num
            y -= dif;
        }
    }

    (x, y)
}
