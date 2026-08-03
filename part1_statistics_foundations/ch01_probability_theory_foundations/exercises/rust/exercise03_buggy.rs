//! Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Rust edition), Exercise 3
//! Part I: Statistics Foundation for ML
//!
//! Three deliberate bugs are hiding below (in independence_check,
//! exponential_cdf, and probability_integral_transform_mean). Find and
//! fix each one so every `#[test]` passes. Do not edit the tests.
//!
//! Build & run: rustc --edition 2021 --test exercise03_buggy.rs -o /tmp/ex03_buggy_test && /tmp/ex03_buggy_test

fn independence_check(p_a: f64, p_b: f64, p_a_and_b: f64, tol: f64) -> bool {
    // BUG: checks the disjoint-events additivity condition instead of
    // the independence condition -- see ch01_text.tex Section 4.
    (p_a_and_b - (p_a + p_b)).abs() < tol
}

fn intersection_with_complement(p_a: f64, p_b_and_a: f64) -> f64 {
    // Correct.
    p_a - p_b_and_a
}

fn exponential_cdf(y: f64) -> f64 {
    // BUG: returns the density e^{-y} instead of integrating it to get
    // the CDF 1 - e^{-y}.
    if y >= 0.0 {
        (-y).exp()
    } else {
        0.0
    }
}

fn probability_integral_transform_mean(n: u64, seed: u64) -> f64 {
    // BUG: forgets to apply exponential_cdf -- averages the raw
    // Exponential(1) samples, converging to 1.0 instead of 0.5.
    let mut rng = Lcg::new(seed);
    let mut total = 0.0;
    for _ in 0..n {
        let u = rng.next_f64().max(1e-12);
        let x = -u.ln();
        total += x;
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
    println!("independence_check (buggy) = {}", independence_check(0.5, 0.4, 0.2, 1e-9));
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
        assert!((exponential_cdf(0.0) - 0.0).abs() < 1e-9, "got {}", exponential_cdf(0.0));
        assert!(
            (exponential_cdf(1.0) - (1.0 - (-1.0f64).exp())).abs() < 1e-9,
            "got {}",
            exponential_cdf(1.0)
        );
    }

    #[test]
    fn test_probability_integral_transform_mean() {
        let mean = probability_integral_transform_mean(200_000, 7);
        assert!((mean - 0.5).abs() < 0.15, "got {mean}");
    }
}
