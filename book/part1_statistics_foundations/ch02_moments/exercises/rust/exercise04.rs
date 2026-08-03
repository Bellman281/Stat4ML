//! Chapter 2 exercise 4 -- MGF derivatives give moments
//! Part I: Statistics Foundation for ML
//!
//! HOMEWORK: implement each `todo!()` using only ch02_text.tex Section 3
//! (moment generating functions, and E[X^n] = M_X^(n)(0)) and the
//! Normal MGF formula. Use central finite differences:
//!   M'(0)  ~= (M(h) - M(-h)) / (2h)
//!   M''(0) ~= (M(h) - 2 M(0) + M(-h)) / h^2
//!
//! Build & run: rustc --edition 2021 exercise04.rs -o /tmp/ex04 && /tmp/ex04
//! Reference solution: solutions/exercise04_solution.rs

fn mgf_normal(t: f64, mu: f64, sigma2: f64) -> f64 {
    // Provided for you.
    (mu * t + sigma2 * t * t / 2.0).exp()
}

fn first_derivative_at_zero(mu: f64, sigma2: f64, h: f64) -> f64 {
    // TODO
    todo!("first_derivative_at_zero")
}

fn second_derivative_at_zero(mu: f64, sigma2: f64, h: f64) -> f64 {
    // TODO
    todo!("second_derivative_at_zero")
}

fn variance_from_derivatives(mu: f64, sigma2: f64, h: f64) -> f64 {
    // TODO: Var(X) = E[X^2] - (E[X])^2.
    todo!("variance_from_derivatives")
}

fn main() {
    let (mu, sigma2, h) = (2.0, 4.0, 1e-4);

    let d1 = first_derivative_at_zero(mu, sigma2, h);
    println!("M_X'(0) ~= {d1:.6}  (theoretical E[X] = mu = {mu})");

    let d2 = second_derivative_at_zero(mu, sigma2, h);
    println!("M_X''(0) ~= {d2:.6}  (theoretical E[X^2] = sigma2+mu^2 = {})", sigma2 + mu * mu);

    let var = variance_from_derivatives(mu, sigma2, h);
    println!("Var(X) via derivatives ~= {var:.6}  (theoretical Var(X) = sigma2 = {sigma2})");
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
