//! Chapter 0 -- RUSTLINGS-STYLE EXERCISE (Rust edition), Exercise 1
//! Part I: Statistics Foundation for ML
//!
//! Three deliberate bugs are hiding below (in transpose, det2x2, and
//! inverse2x2). Find and fix each one so every `#[test]` passes. Do not
//! edit the tests.
//!
//! Build & run: rustc --edition 2021 --test exercise01_buggy.rs -o /tmp/ex01_buggy_test && /tmp/ex01_buggy_test

type Mat2 = [[f64; 2]; 2];

fn matmul(a: &Mat2, b: &Mat2) -> Mat2 {
    // Correct.
    let mut c = [[0.0; 2]; 2];
    for i in 0..2 {
        for j in 0..2 {
            for t in 0..2 {
                c[i][j] += a[i][t] * b[t][j];
            }
        }
    }
    c
}

fn transpose(a: &Mat2) -> Mat2 {
    // BUG: returns A unchanged -- forgets to swap row/column indices
    // (see ch00_text.tex Definition 4.1).
    *a
}

fn det2x2(a: &Mat2) -> f64 {
    // BUG: computes a*d + b*c instead of a*d - b*c (sign error -- see
    // ch00_text.tex Section 2).
    a[0][0] * a[1][1] + a[0][1] * a[1][0]
}

fn inverse2x2(a: &Mat2) -> Mat2 {
    // BUG: forgets to divide by det(A) -- returns just the adjugate
    // matrix [[d,-b],[-c,a]] (see ch00_text.tex Section 3).
    [[a[1][1], -a[0][1]], [-a[1][0], a[0][0]]]
}

fn main() {
    let a: Mat2 = [[1.0, 2.0], [3.0, 4.0]];
    let inv_a = inverse2x2(&a);
    println!("A^-1 (buggy) = {inv_a:?}");
}

#[cfg(test)]
mod tests {
    use super::*;

    fn approx_eq(a: &Mat2, b: &Mat2, tol: f64) -> bool {
        (0..2).all(|i| (0..2).all(|j| (a[i][j] - b[i][j]).abs() < tol))
    }

    #[test]
    fn test_matmul() {
        let a: Mat2 = [[1.0, 2.0], [3.0, 4.0]];
        let b: Mat2 = [[5.0, 6.0], [7.0, 8.0]];
        assert!(approx_eq(&matmul(&a, &b), &[[19.0, 22.0], [43.0, 50.0]], 1e-9));
    }

    #[test]
    fn test_transpose_matches_matmul_identity() {
        let a: Mat2 = [[1.0, 2.0], [3.0, 4.0]];
        let b: Mat2 = [[5.0, 6.0], [7.0, 8.0]];
        let ab = matmul(&a, &b);
        let lhs = transpose(&ab);
        let rhs = matmul(&transpose(&b), &transpose(&a));
        assert!(approx_eq(&lhs, &rhs, 1e-9), "lhs={lhs:?} rhs={rhs:?}");
    }

    #[test]
    fn test_det_multiplicative() {
        let a: Mat2 = [[1.0, 2.0], [3.0, 4.0]];
        let b: Mat2 = [[5.0, 6.0], [7.0, 8.0]];
        let ab = matmul(&a, &b);
        let (da, db, dab) = (det2x2(&a), det2x2(&b), det2x2(&ab));
        assert!((da * db - dab).abs() < 1e-9, "da*db={} dab={}", da * db, dab);
    }

    #[test]
    fn test_inverse() {
        let a: Mat2 = [[1.0, 2.0], [3.0, 4.0]];
        let inv_a = inverse2x2(&a);
        let check = matmul(&a, &inv_a);
        assert!(approx_eq(&check, &[[1.0, 0.0], [0.0, 1.0]], 1e-9), "got {check:?}");
    }
}
