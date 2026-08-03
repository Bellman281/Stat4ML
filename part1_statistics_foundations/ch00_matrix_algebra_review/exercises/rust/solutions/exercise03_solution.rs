//! Reference solution for exercise03.rs (Chapter 0, Exercise 3)

type Mat2 = [[f64; 2]; 2];

fn trace(a: &Mat2) -> f64 {
    a[0][0] + a[1][1]
}

fn det2x2(a: &Mat2) -> f64 {
    a[0][0] * a[1][1] - a[0][1] * a[1][0]
}

fn eigenvalues_2x2(a: &Mat2) -> (f64, f64) {
    let tr = trace(a);
    let d = det2x2(a);
    let disc = (tr * tr - 4.0 * d).sqrt();
    ((tr + disc) / 2.0, (tr - disc) / 2.0)
}

fn eigenvector_for_eigenvalue_2x2(a: &Mat2, lam: f64) -> [f64; 2] {
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
    println!("eigenvalues = {lam1}, {lam2}  (expect 1.0 and 0.5)");
    println!("trace(A) = {}, sum of eigenvalues = {}", trace(&a), lam1 + lam2);
    println!("det(A) = {}, product of eigenvalues = {}", det2x2(&a), lam1 * lam2);

    let v1 = eigenvector_for_eigenvalue_2x2(&a, lam1);
    let av1 = [a[0][0] * v1[0] + a[0][1] * v1[1], a[1][0] * v1[0] + a[1][1] * v1[1]];
    println!("A @ v1 = {av1:?}, lambda1 * v1 = [{}, {}]  -- should match", lam1 * v1[0], lam1 * v1[1]);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_trace() {
        let a: Mat2 = [[0.8, 0.3], [0.2, 0.7]];
        assert!((trace(&a) - 1.5).abs() < 1e-9);
    }

    #[test]
    fn test_eigenvalues() {
        let a: Mat2 = [[0.8, 0.3], [0.2, 0.7]];
        let (lam1, lam2) = eigenvalues_2x2(&a);
        assert!((lam1 - 1.0).abs() < 1e-6, "lam1={lam1}");
        assert!((lam2 - 0.5).abs() < 1e-6, "lam2={lam2}");
        assert!((lam1 + lam2 - trace(&a)).abs() < 1e-9);
        assert!((lam1 * lam2 - det2x2(&a)).abs() < 1e-9);
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
