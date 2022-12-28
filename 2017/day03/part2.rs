const LEN: i64 = 17;
const RINGS: i64 = (LEN - 1) / 2;

fn day3_part2(input: i64) -> i64 {
    let mut plane = vec![0_i64; (LEN * LEN) as usize];

    set_num(&mut plane, 0, 0, 1);

    for i in 2..LEN * LEN {
        let (x, y) = get_coords(i);
        let sum = sum_around(&plane, x, y);

        if sum > input {
            return sum;
        }

        set_num(&mut plane, x, y, sum);
    }
}

fn get_num(arr: &[i64], x: i64, y: i64) -> i64 {
    arr[((y + RINGS) * LEN + (x + RINGS)) as usize]
}

fn set_num(arr: &mut [i64], x: i64, y: i64, num: i64) {
    arr[((y + RINGS) * LEN + (x + RINGS)) as usize] = num;
}

fn sum_around(arr: &[i64], x: i64, y: i64) -> i64 {
    let mut sum = 0;

    let a_x = x + RINGS;
    let a_y = y + RINGS;

    let left = a_x > 0;
    let right = a_x < LEN - 1;
    let up = a_y > 0;
    let down = a_y < LEN - 1;

    if left {
        sum += get_num(arr, x - 1, y);

        if up {
            sum += get_num(arr, x - 1, y - 1);
        }

        if down {
            sum += get_num(arr, x - 1, y + 1);
        }
    }

    if right {
        sum += get_num(arr, x + 1, y);

        if up {
            sum += get_num(arr, x + 1, y - 1);
        }

        if down {
            sum += get_num(arr, x + 1, y + 1);
        }
    }

    if up {
        sum += get_num(arr, x, y - 1);
    }

    if down {
        sum += get_num(arr, x, y + 1);
    }

    sum
}

fn print_arr(arr: &[i64], len: i64) {
    for i in 0..len {
        println!("{:?}", &arr[(i * len) as usize..((i + 1) * len) as usize]);
    }
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
