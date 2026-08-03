//! Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Rust edition)
//! Part I: Statistics Foundation for ML
//!
//! Every function below is fully implemented -- but FIVE contain a
//! deliberate bug that violates something from ch01_text.tex. Find and
//! fix each one so every `#[test]` below passes. Do not edit the tests.
//!
//! Build & run the tests with:
//!   rustc --edition 2021 --test exercise01_buggy.rs -o /tmp/exercise01_buggy_test && /tmp/exercise01_buggy_test
//!
//! Just like `rustlings run`, keep re-compiling and re-running after each
//! fix until every test shows `ok`.

fn sample_space_two_coins() -> Vec<&'static str> {
    vec!["HH", "HT", "TH", "TT"]
}

fn is_valid_probability_function(p: &[f64], _sample_space: &[&str], tol: f64) -> bool {
    // BUG: only checks the sum -- forgets non-negativity (Axiom 1).
    (p.iter().sum::<f64>() - 1.0).abs() < tol
}

fn complement_probability(p_a: f64) -> f64 {
    // BUG: should be 1.0 - p_a.
    p_a
}

fn union_probability(p_a: f64, p_b: f64, p_a_and_b: f64) -> f64 {
    // BUG: forgets to subtract the intersection (inclusion-exclusion).
    p_a + p_b
}

fn conditional_probability(p_a_and_b: f64, p_b: f64) -> f64 {
    // Correct.
    p_a_and_b / p_b
}

fn bayes_theorem(p_b_given_a: f64, p_a: f64, p_b: f64) -> f64 {
    // BUG: forgets to divide by P(B).
    p_b_given_a * p_a
}

fn bayes_theorem_partition(p_b_given_ai: &[f64], p_ai: &[f64]) -> Vec<f64> {
    // Correct.
    let denom: f64 = p_b_given_ai.iter().zip(p_ai).map(|(pb, pa)| pb * pa).sum();
    p_b_given_ai
        .iter()
        .zip(p_ai)
        .map(|(pb, pa)| pb * pa / denom)
        .collect()
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

fn simulate_coin_law_of_large_numbers(p_heads: f64, n_tosses: u64, seed: u64) -> f64 {
    // BUG: ignores p_heads, always thresholds at 0.5.
    let mut rng = Lcg::new(seed);
    let mut heads = 0u64;
    for _ in 0..n_tosses {
        if rng.next_f64() < 0.5 {
            heads += 1;
        }
    }
    heads as f64 / n_tosses as f64
}

fn main() {
    let ss = sample_space_two_coins();
    println!("Two-coin sample space: {:?}", ss);
    let fair = vec![0.25, 0.25, 0.25, 0.25];
    println!(
        "Fair distribution valid? {}",
        is_valid_probability_function(&fair, &ss, 1e-9)
    );
    let freq = simulate_coin_law_of_large_numbers(0.2, 1000, 42);
    println!("empirical P(heads) with p=0.2: {freq:.4}  <-- should be near 0.2, not 0.5!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sample_space() {
        assert_eq!(sample_space_two_coins(), vec!["HH", "HT", "TH", "TT"]);
    }

    #[test]
    fn test_is_valid_probability_function_rejects_negative() {
        let ss = sample_space_two_coins();
        let invalid = vec![0.5, -0.1, 0.3, 0.3]; // negative prob!
        assert!(
            !is_valid_probability_function(&invalid, &ss, 1e-9),
            "a probability vector with a negative entry must be rejected (Kolmogorov Axiom 1)"
        );
    }

    #[test]
    fn test_complement_probability() {
        assert!((complement_probability(0.3) - 0.7).abs() < 1e-9);
    }

    #[test]
    fn test_union_probability() {
        assert!((union_probability(0.5, 0.4, 0.2) - 0.7).abs() < 1e-9);
    }

    #[test]
    fn test_conditional_probability() {
        assert!((conditional_probability(0.2, 0.4) - 0.5).abs() < 1e-9);
    }

    #[test]
    fn test_bayes_theorem() {
        assert!((bayes_theorem(0.4, 0.5, 0.4) - 0.5).abs() < 1e-9);
    }

    #[test]
    fn test_bayes_theorem_partition() {
        let post = bayes_theorem_partition(&[0.9, 0.2], &[0.01, 0.99]);
        let denom = 0.9 * 0.01 + 0.2 * 0.99;
        assert!((post[0] - (0.9 * 0.01 / denom)).abs() < 1e-6);
    }

    #[test]
    fn test_simulate_coin_law_of_large_numbers() {
        let freq = simulate_coin_law_of_large_numbers(0.2, 200_000, 42);
        assert!((freq - 0.2).abs() < 0.05, "got {freq}, expected near 0.2");
    }
}
