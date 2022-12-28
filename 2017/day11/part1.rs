macro_rules! equalize {
    ($a:ident, $b:ident) => {
        if $a < $b {
            $b -= $a;
            $a = 0;
        } else {
            $a -= $b;
            $b = 0;
        }
    }
}

macro_rules! merge {
    ($a:ident, $b:ident, $c:ident) => {
        if $a < $b {
            $b -= $a;
            $c += $a;
            $a = 0;
        } else {
            $a -= $b;
            $c += $b;
            $b = 0;
        }
    }
}

fn day11_part1(input: &str) -> usize {
    let (mut n, mut nw, mut ne, mut s, mut sw, mut se) = input.trim().split(',').fold(
        (0, 0, 0, 0, 0, 0),
        |mut acc, x| {
            match x {
                "n" => acc.0 += 1,
                "nw" => acc.1 += 1,
                "ne" => acc.2 += 1,
                "s" => acc.3 += 1,
                "sw" => acc.4 += 1,
                "se" => acc.5 += 1,
                _ => {}
            }

            acc
        },
    );

    equalize!(n, s);

    equalize!(ne, sw);
    equalize!(nw, se);

    merge!(se, sw, s);
    merge!(ne, nw, n);

    merge!(ne, s, se);
    merge!(nw, s, sw);
    merge!(se, n, ne);
    merge!(sw, n, nw);

    n + ne + nw + s + se + sw
}
