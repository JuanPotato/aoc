use std::collections::HashMap;

fn get_def<'a, K, V>(map: &'a HashMap<K, V>, key: &'a K, def: V) -> V
where
    K: std::cmp::Eq,
    K: std::hash::Hash,
    V: std::marker::Copy,
{
    let is_set = map.get(key).is_some();

    if is_set { *map.get(key).unwrap() } else { def }
}

fn day8_part1(input: &str) -> i64 {
    let mut map: HashMap<&str, i64> = HashMap::new();

    for line in input.trim().split('\n') {
        let parts = line.split(' ').collect::<Vec<&str>>();

        let cond_left: i64 = get_def(&map, &parts[4], 0);
        let cond_right: i64 = parts[6].parse().unwrap();

        let compare = match parts[5] {
            "<" => i64::lt,
            ">" => i64::gt,
            "<=" => i64::le,
            ">=" => i64::ge,
            "==" => i64::eq,
            "!=" => i64::ne,
            _ => panic!(),
        };

        if !compare(&cond_left, &cond_right) {
            continue;
        }

        let inc = parts[1] == "inc";

        let mut var = get_def(&map, &parts[0], 0);
        let addend: i64 = parts[2].parse().unwrap();

        var += addend * if inc { 1 } else { -1 };

        map.insert(parts[0], var);
    }

    *map.values().max().unwrap()
}
