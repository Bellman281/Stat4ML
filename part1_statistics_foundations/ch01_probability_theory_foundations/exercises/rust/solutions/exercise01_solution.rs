//! Chapter 1 -- reference solution (Rust).
//! Build & test: rustc --edition 2021 --test exercise01_solution.rs -o /tmp/ex01_sol && /tmp/ex01_sol
//! Run demo:     rustc --edition 2021 exercise01_solution.rs -o /tmp/ex01_sol_bin && /tmp/ex01_sol_bin

fn sample_space_two_coins() -> Vec<&'static str> {
    vec!["HH", "HT", "TH", "TT"]
}

fn is_valid_probability_function(p: &[f64], _sample_space: &[&str], tol: f64) -> bool {
    if p.iter().any(|&v| v < 0.0) {
        return false;
    }
    (p.iter().sum::<f64>() - 1.0).abs() < tol
}

fn complement_probability(p_a: f64) -> f64 {
    1.0 - p_a
}

fn union_probability(p_a: f64, p_b: f64, p_a_and_b: f64) -> f64 {
    p_a + p_b - p_a_and_b
}

fn conditional_probability(p_a_and_b: f64, p_b: f64) -> f64 {
    p_a_and_b / p_b
}

fn bayes_theorem(p_b_given_a: f64, p_a: f64, p_b: f64) -> f64 {
    p_b_given_a * p_a / p_b
}

fn bayes_theorem_partition(p_b_given_ai: &[f64], p_ai: &[f64]) -> Vec<f64> {
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
    let mut rng = Lcg::new(seed);
    let mut heads = 0u64;
    for _ in 0..n_tosses {
        if rng.next_f64() < p_heads {
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
        let invalid = vec![0.5, -0.1, 0.3, 0.3];
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
