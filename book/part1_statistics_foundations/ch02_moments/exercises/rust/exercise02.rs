//! Chapter 2 exercise -- Moments (Rust edition)
//! Part I: Statistics Foundation for ML
//!
//! HOMEWORK: implement each `todo!()` below using only ch02_text.tex.
//!
//! Build & run the tests with:
//!   rustc --edition 2021 --test exercise02.rs -o /tmp/exercise02_test && /tmp/exercise02_test

/// E[X] for a discrete random variable with support `values` and matching
/// probabilities `probs`.
fn expected_value(values: &[f64], probs: &[f64]) -> f64 {
    // TODO
    todo!("expected_value")
}

/// Var(X) = E[X^2] - (E[X])^2. Reuse expected_value.
fn variance(values: &[f64], probs: &[f64]) -> f64 {
    // TODO
    todo!("variance")
}

/// Cov(X,Y) = E[XY] - E[X]E[Y], given the joint distribution as parallel
/// slices x_values[i], y_values[i], joint_probs[i].
fn covariance(x_values: &[f64], y_values: &[f64], joint_probs: &[f64]) -> f64 {
    // TODO
    todo!("covariance")
}

/// rho = Cov(X,Y) / (sqrt(var_x) * sqrt(var_y))
fn correlation(cov_xy: f64, var_x: f64, var_y: f64) -> f64 {
    // TODO
    todo!("correlation")
}

/// Closed-form MGF of N(mu, sigma2): exp(mu*t + sigma2*t^2/2)
fn normal_mgf_theoretical(t: f64, mu: f64, sigma2: f64) -> f64 {
    // TODO
    todo!("normal_mgf_theoretical")
}

/// Deterministic LCG PRNG (no external crates needed).
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

/// Box-Muller: turn 2 uniform(0,1) draws into 2 independent standard
/// normal draws. Provided for you -- not part of the exercise.
fn standard_normal_pair(rng: &mut Lcg) -> (f64, f64) {
    let u1 = rng.next_f64().max(1e-12);
    let u2 = rng.next_f64();
    let r = (-2.0 * u1.ln()).sqrt();
    let theta = 2.0 * std::f64::consts::PI * u2;
    (r * theta.cos(), r * theta.sin())
}

/// Estimate E[e^{tX}] for X ~ N(mu, sigma2) via Monte Carlo.
fn normal_mgf_monte_carlo(t: f64, mu: f64, sigma2: f64, n: u64, seed: u64) -> f64 {
    // TODO: sample n draws of X = mu + sqrt(sigma2)*Z (Z standard normal,
    // via standard_normal_pair) and return the average of exp(t*x).
    todo!("normal_mgf_monte_carlo")
}

fn main() {
    let xs = [0.0, 1.0, 2.0, 3.0];
    let ps = [1.0 / 8.0, 3.0 / 8.0, 3.0 / 8.0, 1.0 / 8.0];
    let mu = expected_value(&xs, &ps);
    let var = variance(&xs, &ps);
    println!("E[X] = {mu}, Var(X) = {var}  (Binomial(3,0.5): expect mean 1.5, var 0.75)");

    let x_vals = [0.0, 0.0, 1.0, 1.0];
    let y_vals = [0.0, 1.0, 0.0, 1.0];
    let joint = [0.4, 0.1, 0.1, 0.4];
    let cov = covariance(&x_vals, &y_vals, &joint);
    let var_x = variance(&[0.0, 1.0], &[0.5, 0.5]);
    println!("Cov(X,Y) = {cov}, corr = {}", correlation(cov, var_x, var_x));

    let (mu_n, sigma2_n, t) = (2.0, 4.0, 0.4);
    let theo = normal_mgf_theoretical(t, mu_n, sigma2_n);
    let mc = normal_mgf_monte_carlo(t, mu_n, sigma2_n, 200_000, 7);
    println!("Normal MGF at t={t}: theoretical={theo:.5}, Monte Carlo={mc:.5}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_expected_value_and_variance() {
        let xs = [0.0, 1.0, 2.0, 3.0];
        let ps = [1.0 / 8.0, 3.0 / 8.0, 3.0 / 8.0, 1.0 / 8.0];
        assert!((expected_value(&xs, &ps) - 1.5).abs() < 1e-9);
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
