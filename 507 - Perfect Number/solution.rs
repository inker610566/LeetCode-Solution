impl Solution {
    pub fn check_perfect_number(num: i32) -> bool {
        if num == 1 {
            return false;
        }
        let mut divisor_sum = 1;
        let mut divisor = 2;
        while divisor * divisor < num {
            if num % divisor == 0 {
                divisor_sum += divisor + num / divisor;
            }
            divisor += 1;
        }
        if divisor * divisor == num {
            divisor_sum += divisor;
        }
        return divisor_sum == num;
    }
}
