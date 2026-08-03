//! Reference solution for exercise02.rs (Chapter 0, Exercise 2)

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
    let (a11, a12, a21, a22) = (a[0][0], a[0][1], a[1][0], a[1][1]);
    let (u11, u12) = (a11, a12);
    let l21 = a21 / a11;
    let u22 = a22 - l21 * u12;
    let l: Mat2 = [[1.0, 0.0], [l21, 1.0]];
    let u: Mat2 = [[u11, u12], [0.0, u22]];
    (l, u)
}

fn reconstruct(l: &Mat2, u: &Mat2) -> Mat2 {
    matmul(l, u)
}

fn main() {
    let a: Mat2 = [[4.0, 3.0], [6.0, 3.0]];
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
