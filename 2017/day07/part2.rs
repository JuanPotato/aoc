#[derive(Debug)]
struct Tower {
    name: String,
    weight: i64,
    load: i64,
    total_load: i64,
    children: Option<Vec<usize>>, // indexes
    parent: Option<usize>, // index
}

fn calc_load(i: usize, towers: &mut [Tower]) -> i64 {
    let mut load = 0;

    if let Some(ref children) = towers[i].children.clone() {
        for c in children {
            load += calc_load(*c, towers) + towers[*c].weight;
        }
    }

    towers[i].load = load;
    towers[i].total_load = towers[i].load + towers[i].weight;

    return towers[i].load;
}

fn get_parent(generations: usize, i: usize, towers: &[Tower]) -> usize {
    let mut cur = i;

    for _ in 0..generations {
        match towers[cur].parent {
            Some(n) => cur = n,
            None => break,
        }
    }

    return cur;
}

fn find_odd_child(i: usize, towers: &[Tower]) -> (usize, i64) {
    if let Some(ref children) = towers[i].children {
        let weights: Vec<i64> = children.iter().map(|c| towers[*c].total_load).collect();

        let right = if weights[0] == weights[1] {
            weights[0]
        } else {
            weights[2]
        };

        let mut odd: i64 = -1;

        for c in 0..children.len() {
            if towers[children[c]].total_load != right {
                odd = c as i64;
                break;
            }
        }

        if odd == -1 {
            return (i, right);
        } else {
            return (children[odd as usize], right);
        }
    } else {
        return (i, towers[i].total_load);
    }
}

fn day7_part2(input: &str) -> i64 {
    use std::collections::HashMap;

    let mut towers_map: HashMap<&str, usize> = HashMap::with_capacity(1100);
    // Array of name -> index in vector
    let mut towers: Vec<Tower> = Vec::with_capacity(1100);

    let lines: Vec<&str> = input.trim().split('\n').collect();

    for line in &lines {
        let parts = line.split(|c| !char::is_alphanumeric(c))
            .filter(|x| x.len() > 0)
            .collect::<Vec<&str>>();

        let mut tower = Tower {
            name: parts[0].to_string(),
            weight: parts[1].parse().unwrap(),
            load: -1,
            total_load: -1,
            children: None,
            parent: None,
            // Oh
        };

        if parts.len() < 3 {
            tower.load = 0;
        }

        towers_map.insert(parts[0], towers.len());
        towers.push(tower);
    }

    for (i, line) in lines.iter().enumerate() {
        let parts = line.split(|c| !char::is_alphanumeric(c))
            .filter(|x| x.len() > 0)
            .collect::<Vec<&str>>();

        if parts.len() < 3 {
            continue;
        }

        let children: Vec<usize> = parts[2..]
            .iter()
            .map(|n| *towers_map.get(n).unwrap())
            .collect();

        for c in &children {
            towers[*c].parent = Some(i);
        }

        towers[i].children = Some(children);
    }

    let toparent = get_parent(towers.len(), 0, &towers);
    calc_load(toparent, &mut towers);

    let mut old_odd = find_odd_child(toparent, &towers);
    let mut odd = find_odd_child(old_odd.0, &towers);

    while odd.0 != old_odd.0 {
        old_odd = odd;
        odd = find_odd_child(old_odd.0, &towers);
    }

    old_odd.1 - towers[old_odd.0].load
}
