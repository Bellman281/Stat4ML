//! Reference solution for exercise03.rs (Chapter 1, Exercise 3)

fn independence_check(p_a: f64, p_b: f64, p_a_and_b: f64, tol: f64) -> bool {
    (p_a_and_b - p_a * p_b).abs() < tol
}

fn intersection_with_complement(p_a: f64, p_b_and_a: f64) -> f64 {
    p_a - p_b_and_a
}

fn exponential_cdf(y: f64) -> f64 {
    if y >= 0.0 {
        1.0 - (-y).exp()
    } else {
        0.0
    }
}

fn probability_integral_transform_mean(n: u64, seed: u64) -> f64 {
    let mut rng = Lcg::new(seed);
    let mut total = 0.0;
    for _ in 0..n {
        let u = rng.next_f64().max(1e-12);
        let x = -u.ln();
        total += exponential_cdf(x);
    }
    total / n as f64
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
    println!(
        "independent (0.5, 0.4, 0.2): {}  (expect true)",
        independence_check(0.5, 0.4, 0.2, 1e-9)
    );
    println!(
        "independent (0.5, 0.4, 0.3): {}  (expect false)",
        independence_check(0.5, 0.4, 0.3, 1e-9)
    );

    println!(
        "P(A n B^c), A=0.5,B=0.4,AnB=0.3: {}  (expect 0.2)",
        intersection_with_complement(0.5, 0.3)
    );

    println!("exponential_cdf(0) = {}  (expect 0)", exponential_cdf(0.0));
    println!("exponential_cdf(1) = {:.4}  (expect ~0.6321)", exponential_cdf(1.0));

    let mean = probability_integral_transform_mean(200_000, 7);
    println!("probability_integral_transform_mean = {mean:.4}  (Uniform(0,1) mean is 0.5)");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_independence() {
        assert!(independence_check(0.5, 0.4, 0.2, 1e-9));
        assert!(!independence_check(0.5, 0.4, 0.3, 1e-9));
    }

    #[test]
    fn test_intersection_with_complement() {
        assert!((intersection_with_complement(0.5, 0.3) - 0.2).abs() < 1e-9);
    }

    #[test]
    fn test_exponential_cdf() {
        assert!((exponential_cdf(0.0) - 0.0).abs() < 1e-9);
        assert!((exponential_cdf(1.0) - (1.0 - (-1.0f64).exp())).abs() < 1e-9);
    }

    #[test]
    fn test_probability_integral_transform_mean() {
        let mean = probability_integral_transform_mean(200_000, 7);
        assert!((mean - 0.5).abs() < 0.15, "got {mean}");
    }
}
