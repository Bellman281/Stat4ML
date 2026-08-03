//! Chapter 0 -- RUSTLINGS-STYLE EXERCISE (Rust edition), Exercise 3
//! Part I: Statistics Foundation for ML
//!
//! Two deliberate bugs are hiding below (in trace, and in the
//! discriminant inside eigenvalues_2x2). Find and fix each one so every
//! `#[test]` passes. Do not edit the tests.
//!
//! Build & run: rustc --edition 2021 --test exercise03_buggy.rs -o /tmp/ex03_buggy_test && /tmp/ex03_buggy_test

type Mat2 = [[f64; 2]; 2];

fn trace(a: &Mat2) -> f64 {
    // BUG: sums all four entries of A instead of just the two diagonal
    // entries (see ch00_text.tex Section 5, trace(A) = a11 + a22).
    a[0][0] + a[0][1] + a[1][0] + a[1][1]
}

fn det2x2(a: &Mat2) -> f64 {
    // Correct.
    a[0][0] * a[1][1] - a[0][1] * a[1][0]
}

fn eigenvalues_2x2(a: &Mat2) -> (f64, f64) {
    let tr = trace(a);
    let d = det2x2(a);
    // BUG: discriminant should be trace(A)^2 - 4*det(A), not
    // trace(A)^2 - det(A) -- see ch00_text.tex Section 5, Theorem 5.1.
    let disc = (tr * tr - d).sqrt();
    ((tr + disc) / 2.0, (tr - disc) / 2.0)
}

fn eigenvector_for_eigenvalue_2x2(a: &Mat2, lam: f64) -> [f64; 2] {
    // Correct (not part of this exercise).
    let (aa, b, c, d) = (a[0][0], a[0][1], a[1][0], a[1][1]);
    let v = if b.abs() > 1e-12 {
        [b, lam - aa]
    } else {
        [lam - d, c]
    };
    let norm = (v[0] * v[0] + v[1] * v[1]).sqrt();
    [v[0] / norm, v[1] / norm]
}

fn main() {
    let a: Mat2 = [[0.8, 0.3], [0.2, 0.7]];
    let (lam1, lam2) = eigenvalues_2x2(&a);
    println!("eigenvalues = {lam1}, {lam2}  <-- should be 1.0 and 0.5, check trace()!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_trace() {
        let a: Mat2 = [[0.8, 0.3], [0.2, 0.7]];
        assert!((trace(&a) - 1.5).abs() < 1e-9, "got {}", trace(&a));
    }

    #[test]
    fn test_eigenvalues() {
        let a: Mat2 = [[0.8, 0.3], [0.2, 0.7]];
        let (lam1, lam2) = eigenvalues_2x2(&a);
        assert!((lam1 - 1.0).abs() < 1e-6, "lam1={lam1}");
        assert!((lam2 - 0.5).abs() < 1e-6, "lam2={lam2}");
        assert!((lam1 + lam2 - trace(&a)).abs() < 1e-9);
        assert!((lam1 * lam2 - det2x2(&a)).abs() < 1e-9, "lam1*lam2={} det={}", lam1 * lam2, det2x2(&a));
    }

    #[test]
    fn test_eigenvector() {
        let a: Mat2 = [[0.8, 0.3], [0.2, 0.7]];
        let (lam1, _) = eigenvalues_2x2(&a);
        let v1 = eigenvector_for_eigenvalue_2x2(&a, lam1);
        let av1 = [a[0][0] * v1[0] + a[0][1] * v1[1], a[1][0] * v1[0] + a[1][1] * v1[1]];
        assert!((av1[0] - lam1 * v1[0]).abs() < 1e-6);
        assert!((av1[1] - lam1 * v1[1]).abs() < 1e-6);
    }
}
