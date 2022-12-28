use std::fmt::Write;

fn rev(vec: &mut [u8], start: usize, len: usize) {
    let v_len = vec.len();

    for i in 0..(len / 2) {
        let i1 = (start + i) % v_len;
        let i2 = (start + (len - i) - 1) % v_len;

        let temp = vec[i1];
        vec[i1] = vec[i2];
        vec[i2] = temp;
    }
}

fn day10_part2(input: &str) -> String {
    let mut lengths = input
        .trim()
        .chars()
        .map(|n| n as usize)
        .collect::<Vec<usize>>();

    lengths.extend([17, 31, 73, 47, 23].iter());

    let mut list = (0..256).map(|x| x as u8).collect::<Vec<u8>>();
    let mut pos = 0;
    let mut skip = 0;

    for _ in 0..64 {
        for len in &lengths {
            rev(&mut list, pos, *len);
            pos = (pos + len + skip) % list.len();
            skip = (skip + 1) % list.len();
        }
    }

    let hash = list.chunks(16)
        .map(|c| c[1..].iter().fold(c[0], |h, &n| h ^ n))
        .collect::<Vec<u8>>();

    let mut s = String::with_capacity(32);

    for x in hash {
        write!(s, "{:02x}", x).unwrap();
    }

    s
}
