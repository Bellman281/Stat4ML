//! Chapter 2 exercise 3 -- Variance of linear combinations, matrix covariance
//! Part I: Statistics Foundation for ML
//!
//! HOMEWORK: implement each `todo!()` using only ch02_text.tex Section 2
//! (Var(aX+bY)) and Section 4 (matrix notation for moments).
//!
//! Build & run: rustc --edition 2021 exercise03.rs -o /tmp/ex03 && /tmp/ex03
//! Reference solution: solutions/exercise03_solution.rs

type Mat2 = [[f64; 2]; 2];

fn var_sum_two(a: f64, b: f64, var_x: f64, var_y: f64, cov_xy: f64) -> f64 {
    // TODO: Var(aX+bY) = a^2 Var(X) + b^2 Var(Y) + 2ab Cov(X,Y).
    todo!("var_sum_two")
}

fn cov_matrix_2x2(var_x: f64, var_y: f64, cov_xy: f64) -> Mat2 {
    // TODO: [[Var(X1), Cov(X1,X2)], [Cov(X1,X2), Var(X2)]].
    todo!("cov_matrix_2x2")
}

/// M @ v for a 2x2 matrix and length-2 vector. Provided for you.
fn matvec(m: &Mat2, v: &[f64; 2]) -> [f64; 2] {
    [m[0][0] * v[0] + m[0][1] * v[1], m[1][0] * v[0] + m[1][1] * v[1]]
}

fn var_linear_combo(a_vec: &[f64; 2], cov_matrix: &Mat2) -> f64 {
    // TODO: Var(a^T X) = a^T Sigma a.
    todo!("var_linear_combo")
}

fn transform_covariance(r: &Mat2, sigma: &Mat2) -> Mat2 {
    // TODO: Var(RX) = R Sigma R^T.
    todo!("transform_covariance")
}

fn main() {
    let (var_x, var_y, cov_xy) = (2.0, 3.0, 0.5);
    let (a, b) = (1.5, -2.0);

    let direct = var_sum_two(a, b, var_x, var_y, cov_xy);
    println!("Var(aX+bY) directly = {direct}");

    let sigma = cov_matrix_2x2(var_x, var_y, cov_xy);
    println!("Cov(X) = {sigma:?}");
    let via_matrix = var_linear_combo(&[a, b], &sigma);
    println!("a^T Sigma a = {via_matrix}  -- should match the direct formula above");

    let r: Mat2 = [[1.0, 0.0], [1.0, 1.0]];
    let result = transform_covariance(&r, &sigma);
    println!("R Sigma R^T = {result:?}");
}

#[cfg(test)]
mod tests {
    use super::*;

    fn approx_eq(a: &Mat2, b: &Mat2, tol: f64) -> bool {
        (0..2).all(|i| (0..2).all(|j| (a[i][j] - b[i][j]).abs() < tol))
    }

    #[test]
    fn test_var_sum_two() {
        assert!((var_sum_two(1.5, -2.0, 2.0, 3.0, 0.5) - 13.5).abs() < 1e-9);
    }

    #[test]
    fn test_cov_matrix_and_linear_combo() {
        let sigma = cov_matrix_2x2(2.0, 3.0, 0.5);
        assert!(approx_eq(&sigma, &[[2.0, 0.5], [0.5, 3.0]], 1e-9));
        let via_matrix = var_linear_combo(&[1.5, -2.0], &sigma);
        assert!((via_matrix - 13.5).abs() < 1e-9, "got {via_matrix}");
    }

    #[test]
    fn test_transform_covariance() {
        let sigma = cov_matrix_2x2(2.0, 3.0, 0.5);
        let r: Mat2 = [[1.0, 0.0], [1.0, 1.0]];
        let result = transform_covariance(&r, &sigma);
        assert!(approx_eq(&result, &[[2.0, 2.5], [2.5, 6.0]], 1e-9), "got {result:?}");
    }
}
