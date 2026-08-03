//! Chapter 0 -- RUSTLINGS-STYLE EXERCISE (Rust edition), Exercise 2
//! Part I: Statistics Foundation for ML
//!
//! Two deliberate bugs are hiding in lu_decompose_2x2 (wrong pivot for
//! l21, and a u22 that forgets to subtract the update term). Find and
//! fix each one so every `#[test]` passes. Do not edit the tests.
//!
//! Build & run: rustc --edition 2021 --test exercise02_buggy.rs -o /tmp/ex02_buggy_test && /tmp/ex02_buggy_test

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

fn lu_decompose_2x2(a: &Mat2) -> (Mat2, Mat2) {
    let (a11, a12, a21, a22) = (a[0][0], a[0][1], a[1][0], a[1][1]);
    let (u11, u12) = (a11, a12);
    // BUG: divides by a22 (wrong pivot) instead of a11 -- see
    // ch00_text.tex Section 6.1, l21 = a21 / a11.
    let l21 = a21 / a22;
    // BUG: forgets to subtract l21 * u12 -- returns a22 unchanged
    // instead of the Schur-complement update u22 = a22 - l21 * u12.
    let u22 = a22;
    let l: Mat2 = [[1.0, 0.0], [l21, 1.0]];
    let u: Mat2 = [[u11, u12], [0.0, u22]];
    (l, u)
}

fn reconstruct(l: &Mat2, u: &Mat2) -> Mat2 {
    // Correct.
    matmul(l, u)
}

fn main() {
    let a: Mat2 = [[4.0, 3.0], [6.0, 3.0]];
    let (l, u) = lu_decompose_2x2(&a);
    println!("L = {l:?}, U = {u:?}  <-- check against ch00_text.tex Section 6.1");
}

#[cfg(test)]
mod tests {
    use super::*;

    fn approx_eq(a: &Mat2, b: &Mat2, tol: f64) -> bool {
        (0..2).all(|i| (0..2).all(|j| (a[i][j] - b[i][j]).abs() < tol))
    }

    #[test]
    fn test_lu() {
        let a: Mat2 = [[4.0, 3.0], [6.0, 3.0]];
        let (l, u) = lu_decompose_2x2(&a);
        assert!(approx_eq(&l, &[[1.0, 0.0], [1.5, 1.0]], 1e-9), "L={l:?}");
        assert!(approx_eq(&u, &[[4.0, 3.0], [0.0, -1.5]], 1e-9), "U={u:?}");
    }

    #[test]
    fn test_reconstruct() {
        let a: Mat2 = [[4.0, 3.0], [6.0, 3.0]];
        let (l, u) = lu_decompose_2x2(&a);
        assert!(approx_eq(&reconstruct(&l, &u), &a, 1e-9));
    }
}
