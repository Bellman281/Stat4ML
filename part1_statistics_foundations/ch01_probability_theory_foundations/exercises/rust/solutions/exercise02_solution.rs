//! Reference solution for exercise02.rs (Chapter 1, Exercise 2)

fn choose3(x: i64) -> f64 {
    match x {
        0 | 3 => 1.0,
        1 | 2 => 3.0,
        _ => 0.0,
    }
}

fn pmf_three_coins(x: i64) -> f64 {
    choose3(x) * 0.5f64.powi(3)
}

fn cdf_three_coins(x: f64) -> f64 {
    let k = x.floor() as i64;
    (0..4).filter(|&i| i <= k).map(pmf_three_coins).sum()
}

fn inverse_transform_sample(u: f64) -> f64 {
    -u.ln()
}

fn exponential_pdf(y: f64) -> f64 {
    if y >= 0.0 {
        (-y).exp()
    } else {
        0.0
    }
}

struct Lcg {
    state: u64,
}
impl Lcg {
    fn new(seed: u64) -> Self {
        Lcg { state: seed ^ 0x2545F4914F6CDD1D }
    }
    fn next_f64(&mut self) -> f64 {
        self.state = self
            .state
            .wrapping_mul(6364136223846793005)
            .wrapping_add(1442695040888963407);
        ((self.state >> 11) as f64) / ((1u64 << 53) as f64)
    }
}

fn main() {
    let total: f64 = (0..4).map(pmf_three_coins).sum();
    println!("sum of pmf over x=0..3: {total}  (should be 1.0)");

    println!("F_X(2.5) = {}  (should be 7/8 = 0.875)", cdf_three_coins(2.5));
    println!("F_X(-1) = {}, F_X(3.5) = {}", cdf_three_coins(-1.0), cdf_three_coins(3.5));

    let mut rng = Lcg::new(7);
    let n = 200_000;
    let mean: f64 = (0..n)
        .map(|_| inverse_transform_sample(rng.next_f64().max(1e-12)))
        .sum::<f64>()
        / n as f64;
    println!("mean of {n} inverse-transform samples: {mean:.4}  (Exponential(1) mean is 1.0)");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_pmf() {
        assert!((pmf_three_coins(0) - 1.0 / 8.0).abs() < 1e-9);
        assert!((pmf_three_coins(1) - 3.0 / 8.0).abs() < 1e-9);
        let total: f64 = (0..4).map(pmf_three_coins).sum();
        assert!((total - 1.0).abs() < 1e-9);
    }

    #[test]
    fn test_cdf() {
        assert!((cdf_three_coins(2.5) - 7.0 / 8.0).abs() < 1e-9);
        assert!((cdf_three_coins(-1.0) - 0.0).abs() < 1e-9);
        assert!((cdf_three_coins(3.5) - 1.0).abs() < 1e-9);
    }

    #[test]
    fn test_inverse_transform_mean() {
        let mut rng = Lcg::new(7);
        let n = 200_000;
        let mean: f64 = (0..n)
            .map(|_| inverse_transform_sample(rng.next_f64().max(1e-12)))
            .sum::<f64>()
            / n as f64;
        assert!((mean - 1.0).abs() < 0.15, "got {mean}");
    }
}
