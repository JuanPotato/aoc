fn solve(input_str: &str) -> (i32, String) {
    let mut twos = 0;
    let mut threes = 0;

    for w in input_str.lines() {
        let mut alphabet = [0i32; 128];

        for b in w.bytes() {
            alphabet[b as usize] += 1;
        }

        twos += alphabet.contains(&2) as i32;
        threes += alphabet.contains(&3) as i32;
    }

    let mut part2 = String::new();

    for w1 in input_str.lines() {
        for w2 in input_str.lines() {
            let s = w1
                .as_bytes()
                .iter()
                .zip(w2.as_bytes().iter())
                .map(|(b1, b2)| (*b1 != *b2) as i32)
                .sum::<i32>();

            if s == 1 {
                part2 = w1
                    .chars()
                    .zip(w2.chars())
                    .filter_map(|(c1, c2)| if c1 == c2 { Some(c1) } else { None })
                    .collect();
                break;
            }
        }
    }

    (twos * threes, part2)
}

fn main() {
    let input = include_str!("../input/day2.input");
    let answer = solve(input);

    println!("{:?}", answer);
    assert_eq!(answer, (6723, "prtkqyluiusocwvaezjmhmfgx".into()));
}
