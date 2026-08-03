//! Reference solution for exercise01.rs (Chapter 0, Exercise 1)

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

fn transpose(a: &Mat2) -> Mat2 {
    [[a[0][0], a[1][0]], [a[0][1], a[1][1]]]
}

fn det2x2(a: &Mat2) -> f64 {
    a[0][0] * a[1][1] - a[0][1] * a[1][0]
}

fn inverse2x2(a: &Mat2) -> Mat2 {
    let d = det2x2(a);
    [[a[1][1] / d, -a[0][1] / d], [-a[1][0] / d, a[0][0] / d]]
}

fn main() {
    let a: Mat2 = [[1.0, 2.0], [3.0, 4.0]];
    let b: Mat2 = [[5.0, 6.0], [7.0, 8.0]];

    let ab = matmul(&a, &b);
    println!("AB = {ab:?}");

    let lhs = transpose(&ab);
    let rhs = matmul(&transpose(&b), &transpose(&a));
    println!("(AB)^T = {lhs:?}, B^T A^T = {rhs:?}  -- should match (Theorem 4.1)");

    let (da, db, dab) = (det2x2(&a), det2x2(&b), det2x2(&ab));
    println!("det(A)*det(B) = {}, det(AB) = {dab}  -- should match (Theorem 2.1.8)", da * db);

    let inv_a = inverse2x2(&a);
    let check = matmul(&a, &inv_a);
    println!("A @ A^-1 = {check:?}  -- should be the 2x2 identity");
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
