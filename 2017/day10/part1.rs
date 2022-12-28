fn rev(vec: &mut [i64], start: usize, len: usize) {
    let v_len = vec.len();

    for i in 0..(len / 2) {
        let i1 = (start + i) % v_len;
        let i2 = (start + (len - i) - 1) % v_len;

        let temp = vec[i1];
        vec[i1] = vec[i2];
        vec[i2] = temp;
    }
}

fn day10_part1(input: &str) -> i64 {
    let lengths = input
        .trim()
        .split(',')
        .map(|n| n.parse().unwrap())
        .collect::<Vec<usize>>();

    let mut list = (0..256).collect::<Vec<i64>>();
    let mut pos = 0;
    let mut skip = 0;

    for len in lengths {
        rev(&mut list, pos, len);
        pos += (len + skip) % list.len();
        skip += 1;
    }

    list[0] * list[1]
}
