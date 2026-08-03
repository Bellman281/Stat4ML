//! Reference solution for exercise04.rs (Chapter 2, Exercise 4)

fn mgf_normal(t: f64, mu: f64, sigma2: f64) -> f64 {
    (mu * t + sigma2 * t * t / 2.0).exp()
}

fn first_derivative_at_zero(mu: f64, sigma2: f64, h: f64) -> f64 {
    (mgf_normal(h, mu, sigma2) - mgf_normal(-h, mu, sigma2)) / (2.0 * h)
}

fn second_derivative_at_zero(mu: f64, sigma2: f64, h: f64) -> f64 {
    let m0 = mgf_normal(0.0, mu, sigma2);
    (mgf_normal(h, mu, sigma2) - 2.0 * m0 + mgf_normal(-h, mu, sigma2)) / (h * h)
}

fn variance_from_derivatives(mu: f64, sigma2: f64, h: f64) -> f64 {
    let d1 = first_derivative_at_zero(mu, sigma2, h);
    let d2 = second_derivative_at_zero(mu, sigma2, h);
    d2 - d1 * d1
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
