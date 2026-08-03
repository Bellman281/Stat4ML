//! Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Rust edition)
//! Part I: Statistics Foundation for ML
//!
//! Four deliberate bugs are hiding below (in variance, correlation,
//! normal_mgf_theoretical, and normal_mgf_monte_carlo). Find and fix each
//! one so every `#[test]` passes. Do not edit the tests.
//!
//! Build & run: rustc --edition 2021 --test exercise02_buggy.rs -o /tmp/ex02_buggy_test && /tmp/ex02_buggy_test

fn expected_value(values: &[f64], probs: &[f64]) -> f64 {
    // Correct.
    values.iter().zip(probs).map(|(v, p)| v * p).sum()
}

fn variance(values: &[f64], probs: &[f64]) -> f64 {
    // BUG: returns E[X^2], forgets to subtract (E[X])^2.
    let sq: Vec<f64> = values.iter().map(|v| v * v).collect();
    expected_value(&sq, probs)
}

fn covariance(x_values: &[f64], y_values: &[f64], joint_probs: &[f64]) -> f64 {
    // Correct.
    let ex: f64 = x_values.iter().zip(joint_probs).map(|(x, p)| x * p).sum();
    let ey: f64 = y_values.iter().zip(joint_probs).map(|(y, p)| y * p).sum();
    let exy: f64 = x_values
        .iter()
        .zip(y_values)
        .zip(joint_probs)
        .map(|((x, y), p)| x * y * p)
        .sum();
    exy - ex * ey
}

fn correlation(cov_xy: f64, var_x: f64, var_y: f64) -> f64 {
    // BUG: divides by the variances instead of the standard deviations.
    cov_xy / (var_x * var_y)
}

fn normal_mgf_theoretical(t: f64, mu: f64, sigma2: f64) -> f64 {
    // BUG: missing "/2" in the exponent.
    (mu * t + sigma2 * t * t).exp()
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

fn standard_normal_pair(rng: &mut Lcg) -> (f64, f64) {
    let u1 = rng.next_f64().max(1e-12);
    let u2 = rng.next_f64();
    let r = (-2.0 * u1.ln()).sqrt();
    let theta = 2.0 * std::f64::consts::PI * u2;
    (r * theta.cos(), r * theta.sin())
}

fn normal_mgf_monte_carlo(t: f64, mu: f64, sigma2: f64, n: u64, seed: u64) -> f64 {
    // BUG: forgets to scale by sqrt(sigma2) -- always samples as if
    // sigma2 were 1.
    let _ = sigma2;
    let mut rng = Lcg::new(seed);
    let mut total = 0.0;
    let mut count: u64 = 0;
    while count < n {
        let (z1, z2) = standard_normal_pair(&mut rng);
        for z in [z1, z2] {
            if count >= n {
                break;
            }
            let x = mu + z;
            total += (t * x).exp();
            count += 1;
        }
    }
    total / n as f64
}

fn main() {
    let mc = normal_mgf_monte_carlo(0.4, 2.0, 4.0, 1000, 7);
    println!("MGF Monte Carlo estimate: {mc:.4}  <-- should be near 3.06, check sigma scaling!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_expected_value() {
        let xs = [0.0, 1.0, 2.0, 3.0];
        let ps = [1.0 / 8.0, 3.0 / 8.0, 3.0 / 8.0, 1.0 / 8.0];
        assert!((expected_value(&xs, &ps) - 1.5).abs() < 1e-9);
    }

    #[test]
    fn test_variance() {
        let xs = [0.0, 1.0, 2.0, 3.0];
        let ps = [1.0 / 8.0, 3.0 / 8.0, 3.0 / 8.0, 1.0 / 8.0];
        assert!((variance(&xs, &ps) - 0.75).abs() < 1e-9);
    }

    #[test]
    fn test_covariance() {
        let x_vals = [0.0, 0.0, 1.0, 1.0];
        let y_vals = [0.0, 1.0, 0.0, 1.0];
        let joint = [0.4, 0.1, 0.1, 0.4];
        assert!((covariance(&x_vals, &y_vals, &joint) - 0.15).abs() < 1e-9);
    }

    #[test]
    fn test_correlation() {
        assert!((correlation(0.16, 0.25, 0.25) - 0.64).abs() < 1e-9);
    }

    #[test]
    fn test_normal_mgf_theoretical() {
        let theo = normal_mgf_theoretical(0.4, 2.0, 4.0);
        let expected = (2.0f64 * 0.4 + 4.0 * 0.4 * 0.4 / 2.0).exp();
        assert!((theo - expected).abs() < 1e-9);
    }

    #[test]
    fn test_normal_mgf_monte_carlo() {
        let mc = normal_mgf_monte_carlo(0.4, 2.0, 4.0, 300_000, 7);
        let expected = (2.0f64 * 0.4 + 4.0 * 0.4 * 0.4 / 2.0).exp();
        assert!((mc - expected).abs() < 0.15, "got {mc}, expected near {expected}");
    }
}
