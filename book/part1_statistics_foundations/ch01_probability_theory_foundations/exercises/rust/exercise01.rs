//! Chapter 1 exercise -- Probability Theory Foundations (Rust edition)
//! Part I: Statistics Foundation for ML
//!
//! HOMEWORK: implement each `todo!()` below using only the definitions
//! from ch01_text.tex. This file is written for advanced developers who
//! want the probability toolkit implemented in a systems language.
//!
//! Build & run the tests with:
//!   rustc --edition 2021 --test exercise01.rs -o /tmp/exercise01_test && /tmp/exercise01_test
//!
//! (If you have a full Cargo project instead, `cargo test` works the same
//! way -- this single-file layout just avoids requiring network access to
//! fetch crates.)

/// Return the sample space of tossing two fair coins.
fn sample_space_two_coins() -> Vec<&'static str> {
    vec!["HH", "HT", "TH", "TT"]
}

/// Check whether `p` (probabilities, in the same order as `sample_space`)
/// satisfies Kolmogorov's axioms: every value >= 0, and the values sum to
/// 1 within `tol`. Assumes `p.len() == sample_space.len()`.
fn is_valid_probability_function(p: &[f64], _sample_space: &[&str], tol: f64) -> bool {
    // TODO: check non-negativity AND that the sum is within `tol` of 1.0.
    todo!("is_valid_probability_function")
}

/// P(A^c) = 1 - P(A)
fn complement_probability(p_a: f64) -> f64 {
    // TODO
    todo!("complement_probability")
}

/// Inclusion-exclusion: P(A u B) = P(A) + P(B) - P(A n B)
fn union_probability(p_a: f64, p_b: f64, p_a_and_b: f64) -> f64 {
    // TODO
    todo!("union_probability")
}

/// P(A | B) = P(A n B) / P(B)
fn conditional_probability(p_a_and_b: f64, p_b: f64) -> f64 {
    // TODO
    todo!("conditional_probability")
}

/// Bayes' rule: P(A | B) = P(B|A) * P(A) / P(B)
fn bayes_theorem(p_b_given_a: f64, p_a: f64, p_b: f64) -> f64 {
    // TODO
    todo!("bayes_theorem")
}

/// Full Bayes' theorem over a partition A_1..A_k of the sample space.
/// Returns posterior[i] = P(A_i | B).
fn bayes_theorem_partition(p_b_given_ai: &[f64], p_ai: &[f64]) -> Vec<f64> {
    // TODO: use the law of total probability for the denominator.
    todo!("bayes_theorem_partition")
}

/// A tiny linear-congruential PRNG so this exercise has zero external
/// dependencies. Not cryptographically anything -- just deterministic.
struct Lcg {
    state: u64,
}
impl Lcg {
    fn new(seed: u64) -> Self {
        Lcg { state: seed ^ 0x2545F4914F6CDD1D }
    }
    /// Returns a value uniformly distributed in [0, 1).
    fn next_f64(&mut self) -> f64 {
        // Numerical Recipes LCG constants.
        self.state = self
            .state
            .wrapping_mul(6364136223846793005)
            .wrapping_add(1442695040888963407);
        ((self.state >> 11) as f64) / ((1u64 << 53) as f64)
    }
}

/// Simulate `n_tosses` coin tosses with P(heads) = p_heads and return the
/// empirical proportion of heads.
fn simulate_coin_law_of_large_numbers(p_heads: f64, n_tosses: u64, seed: u64) -> f64 {
    // TODO: draw n_tosses values from Lcg::next_f64(), count how many are
    // < p_heads, return count as f64 / n_tosses as f64.
    todo!("simulate_coin_law_of_large_numbers")
}

fn main() {
    let ss = sample_space_two_coins();
    println!("Two-coin sample space: {:?}", ss);
    let fair = vec![0.25, 0.25, 0.25, 0.25];
    println!(
        "Fair distribution valid? {}",
        is_valid_probability_function(&fair, &ss, 1e-9)
    );

    let (p_a, p_b, p_ab) = (0.5, 0.4, 0.2);
    println!("P(A^c) = {}", complement_probability(p_a));
    println!("P(A u B) = {}", union_probability(p_a, p_b, p_ab));
    println!("P(A | B) = {}", conditional_probability(p_ab, p_b));
    println!("Bayes P(A|B) = {}", bayes_theorem(p_ab / p_a, p_a, p_b));

    for n in [10u64, 1_000, 100_000] {
        let freq = simulate_coin_law_of_large_numbers(0.5, n, 42);
        println!("n={n:>7}: empirical P(heads) = {freq:.4}");
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sample_space() {
        assert_eq!(sample_space_two_coins(), vec!["HH", "HT", "TH", "TT"]);
    }

    #[test]
    fn test_is_valid_probability_function() {
        let ss = sample_space_two_coins();
        let fair = vec![0.25, 0.25, 0.25, 0.25];
        assert!(is_valid_probability_function(&fair, &ss, 1e-9));

        let invalid = vec![0.5, -0.1, 0.3, 0.3]; // negative prob!
        assert!(!is_valid_probability_function(&invalid, &ss, 1e-9));
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
