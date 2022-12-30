use regex::Regex;
use std::collections::hash_map::Entry;
use std::collections::HashMap;

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord, Clone, Copy)]
enum ClothSquare {
    NonOverlapping(i32),
    Overlapping,
}

struct Claim {
    id: i32,
    x: i32,
    y: i32,
    w: i32,
    h: i32,
}

fn solve(input_str: &str) -> (usize, i32) {
    let re_num = Regex::new(r"-?\d+").unwrap();

    let mut claims = Vec::new();
    for l in input_str.lines() {
        let mut matches = re_num
            .find_iter(l)
            .map(|m| m.as_str().parse::<i32>().unwrap());

        let id = matches.next().unwrap();
        let x = matches.next().unwrap();
        let y = matches.next().unwrap();
        let w = matches.next().unwrap();
        let h = matches.next().unwrap();
        claims.push(Claim { id, x, y, w, h });
    }

    let mut cloth: HashMap<(i32, i32), ClothSquare> = HashMap::with_capacity(1000);

    for c in &claims {
        for px in c.x..(c.x + c.w) {
            for py in c.y..(c.y + c.h) {
                match cloth.entry((px, py)) {
                    Entry::Occupied(mut o) => {
                        *o.get_mut() = ClothSquare::Overlapping;
                    }
                    Entry::Vacant(v) => {
                        v.insert(ClothSquare::NonOverlapping(c.id));
                    }
                }
            }
        }
    }

    let part1 = cloth
        .values()
        .filter(|&&v| v == ClothSquare::Overlapping)
        .count();

    let mut safe_claims = HashMap::new();
    for v in cloth.values() {
        if let ClothSquare::NonOverlapping(id) = v {
            *safe_claims.entry(*id).or_insert(0) += 1;
        }
    }

    let mut part2 = 0;
    for c in &claims {
        let count = *safe_claims.get(&c.id).unwrap_or(&0);
        if c.w * c.h == count {
            part2 = c.id;
            break;
        }

    }

    (part1, part2)
}

fn main() {
    let input = include_str!("../input/day3.input");
    let answer = solve(input);

    println!("{:?}", answer);
    assert_eq!(answer, (109143, 506));
}
