//! Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Rust edition), Exercise 2
//! Part I: Statistics Foundation for ML
//!
//! Three deliberate bugs are hiding below (in pmf_three_coins,
//! cdf_three_coins, and inverse_transform_sample). Find and fix each
//! one so every `#[test]` passes. Do not edit the tests.
//!
//! Build & run: rustc --edition 2021 --test exercise02_buggy.rs -o /tmp/ex02_buggy_test && /tmp/ex02_buggy_test

fn pmf_three_coins(x: i64) -> f64 {
    // BUG: forgets the binomial coefficient C(3,x) -- returns (1/2)^3
    // for every x (see ch01_text.tex Section 5).
    let _ = x;
    0.5f64.powi(3)
}

fn cdf_three_coins(x: f64) -> f64 {
    // BUG: uses strict "<" instead of "<=" -- an off-by-one that
    // under-counts at integer boundaries.
    let k = x.floor() as i64;
    (0..4).filter(|&i| i < k).map(pmf_three_coins).sum()
}

fn inverse_transform_sample(u: f64) -> f64 {
    // BUG: missing the leading minus sign -- see ch01_text.tex
    // Section 8, Y = -log(X).
    u.ln()
}

fn exponential_pdf(y: f64) -> f64 {
    // Correct (not part of this exercise).
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
    println!("pmf(1) (buggy) = {}", pmf_three_coins(1));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_pmf() {
        assert!((pmf_three_coins(0) - 1.0 / 8.0).abs() < 1e-9);
        assert!((pmf_three_coins(1) - 3.0 / 8.0).abs() < 1e-9, "got {}", pmf_three_coins(1));
        let total: f64 = (0..4).map(pmf_three_coins).sum();
        assert!((total - 1.0).abs() < 1e-9, "total={total}");
    }

    #[test]
    fn test_cdf() {
        assert!((cdf_three_coins(2.5) - 7.0 / 8.0).abs() < 1e-9, "got {}", cdf_three_coins(2.5));
        assert!((cdf_three_coins(-1.0) - 0.0).abs() < 1e-9);
        assert!((cdf_three_coins(3.5) - 1.0).abs() < 1e-9, "got {}", cdf_three_coins(3.5));
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
