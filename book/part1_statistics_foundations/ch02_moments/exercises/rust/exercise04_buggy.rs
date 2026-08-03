//! Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Rust edition), Exercise 4
//! Part I: Statistics Foundation for ML
//!
//! Three deliberate bugs are hiding below (in first_derivative_at_zero,
//! second_derivative_at_zero, and variance_from_derivatives). Find and
//! fix each one so every `#[test]` passes. Do not edit the tests.
//!
//! Build & run: rustc --edition 2021 --test exercise04_buggy.rs -o /tmp/ex04_buggy_test && /tmp/ex04_buggy_test

fn mgf_normal(t: f64, mu: f64, sigma2: f64) -> f64 {
    // Correct.
    (mu * t + sigma2 * t * t / 2.0).exp()
}

fn first_derivative_at_zero(mu: f64, sigma2: f64, h: f64) -> f64 {
    // BUG: forgets the factor of 2 in the denominator.
    (mgf_normal(h, mu, sigma2) - mgf_normal(-h, mu, sigma2)) / h
}

fn second_derivative_at_zero(mu: f64, sigma2: f64, h: f64) -> f64 {
    // BUG: forgets the "-2*M(0)" term.
    (mgf_normal(h, mu, sigma2) + mgf_normal(-h, mu, sigma2)) / (h * h)
}

fn variance_from_derivatives(mu: f64, sigma2: f64, h: f64) -> f64 {
    // BUG: forgets to subtract (E[X])^2.
    second_derivative_at_zero(mu, sigma2, h)
}

fn main() {
    println!("first_derivative_at_zero (buggy) = {}", first_derivative_at_zero(2.0, 4.0, 1e-4));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_first_derivative() {
        let d1 = first_derivative_at_zero(2.0, 4.0, 1e-4);
        assert!((d1 - 2.0).abs() < 1e-3, "got {d1}");
    }

    #[test]
    fn test_second_derivative() {
        let d2 = second_derivative_at_zero(2.0, 4.0, 1e-4);
        assert!((d2 - 8.0).abs() < 1e-2, "got {d2}");
    }

    #[test]
    fn test_variance_from_derivatives() {
        let v = variance_from_derivatives(2.0, 4.0, 1e-4);
        assert!((v - 4.0).abs() < 1e-2, "got {v}");
    }
}
