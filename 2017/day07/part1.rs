fn day7_part1(input: &str) -> String {
    use std::collections::HashMap;

    let mut towers = HashMap::with_capacity(1000);

    for line in input.trim().split("\n") {
        let parts = line.split(|c| !char::is_alphanumeric(c))
            .filter(|x| x.len() > 0)
            .collect::<Vec<&str>>();

        let carried = if parts.len() > 2 {
            Some(
                parts[2..]
                    .iter()
                    .map(|x| x.to_string())
                    .collect::<Vec<String>>(),
            )
        } else {
            None
        };

        towers.insert(parts[0].to_string(), carried);
    }

    let mut to_remove = Vec::with_capacity(towers.len());

    for (_, carrying_option) in &towers {
        if let &Some(ref carrying) = carrying_option {
            for name in carrying {
                to_remove.push(name.clone());
            }
        }
    }

    for name in &to_remove {
        towers.remove(name);
    }

    towers.keys().last().unwrap().to_string()
}
