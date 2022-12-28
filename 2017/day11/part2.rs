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

fn day11_part2(input: &str) -> usize {
    let mut n = 0;
    let mut nw = 0;
    let mut ne = 0;
    let mut s = 0;
    let mut sw = 0;
    let mut se = 0;

    let mut max = 0;

    for x in input.trim().split(',') {
        match x {
            "n" => n += 1,
            "nw" => nw += 1,
            "ne" => ne += 1,
            "s" => s += 1,
            "sw" => sw += 1,
            "se" => se += 1,
            _ => {}
        }

        equalize!(n, s);
        equalize!(ne, sw);
        equalize!(nw, se);
        merge!(se, sw, s);
        merge!(ne, nw, n);
        merge!(ne, s, se);
        merge!(nw, s, sw);
        merge!(se, n, ne);
        merge!(sw, n, nw);

        let m = n + ne + nw + s + se + sw;
        if m > max {
            max = m;
        }
    }

    max
}
