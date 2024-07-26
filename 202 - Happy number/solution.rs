use std::collections::HashSet;

impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let mut visited: HashSet<i32> = HashSet::new();
        let mut current_value = n;
        while !visited.contains(&current_value) {
            visited.insert(current_value);
            current_value = {
                let mut rest = current_value;
                let mut sum = 0;
                while rest != 0 {
                    let digit = rest % 10;
                    sum += digit * digit;
                    rest /= 10;
                }
                sum
            };
        }
        current_value == 1
    }
}
