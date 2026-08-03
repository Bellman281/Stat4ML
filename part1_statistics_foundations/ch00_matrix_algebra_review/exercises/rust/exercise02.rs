//! Chapter 0 exercise 2 -- Matrix Algebra Review: LU decomposition
//! Part I: Statistics Foundation for ML
//!
//! HOMEWORK: implement each `todo!()` using Doolittle's method for a 2x2
//! matrix, as worked out in ch00_text.tex Section 6.1 (Matrix
//! Decompositions).
//!
//! Build & run: rustc --edition 2021 exercise02.rs -o /tmp/ex02 && /tmp/ex02
//! Reference solution: solutions/exercise02_solution.rs

type Mat2 = [[f64; 2]; 2];

fn matmul(a: &Mat2, b: &Mat2) -> Mat2 {
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
    // TODO: Doolittle's method.
    //   u11 = a11, u12 = a12
    //   l21 = a21 / a11
    //   u22 = a22 - l21 * u12
    // See ch00_text.tex Section 6.1 (and its editorial note on the
    // "u11=14" typo -- don't reproduce it here).
    todo!("lu_decompose_2x2")
}

fn reconstruct(l: &Mat2, u: &Mat2) -> Mat2 {
    // TODO: L @ U.
    todo!("reconstruct")
}

fn main() {
    let a: Mat2 = [[4.0, 3.0], [6.0, 3.0]]; // same example as ch00_text.tex
    let (l, u) = lu_decompose_2x2(&a);
    println!("L = {l:?}");
    println!("U = {u:?}");
    let a_check = reconstruct(&l, &u);
    println!("L @ U = {a_check:?}  -- should equal A = {a:?}");
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
