//! Chapter 1 (Part II) -- RUSTLINGS-STYLE EXERCISE (Rust edition)
//!
//! Four deliberate bugs are hiding below (in
//! simple_linear_regression_fit, predict, mse, and kmeans_assign). Find
//! and fix each one so every `#[test]` passes. Do not edit the tests.
//!
//! Build & run: rustc --edition 2021 --test exercise01_buggy.rs -o /tmp/isl_ex01_buggy_test && /tmp/isl_ex01_buggy_test

fn simple_linear_regression_fit(xs: &[f64], ys: &[f64]) -> (f64, f64) {
    // BUG: uses raw sums instead of centering around the means first --
    // wrong whenever xbar != 0.
    let n = xs.len() as f64;
    let num: f64 = xs.iter().zip(ys).map(|(x, y)| x * y).sum();
    let den: f64 = xs.iter().map(|x| x * x).sum();
    let b1 = num / den;
    let xbar = xs.iter().sum::<f64>() / n;
    let ybar = ys.iter().sum::<f64>() / n;
    let b0 = ybar - b1 * xbar;
    (b0, b1)
}

fn predict(xs: &[f64], _b0: f64, b1: f64) -> Vec<f64> {
    // BUG: forgets the intercept term entirely.
    xs.iter().map(|x| b1 * x).collect()
}

fn mse(y_true: &[f64], y_pred: &[f64]) -> f64 {
    // BUG: computes mean ABSOLUTE error, not mean SQUARED error.
    let n = y_true.len() as f64;
    y_true.iter().zip(y_pred).map(|(t, p)| (t - p).abs()).sum::<f64>() / n
}

fn kmeans_assign(points: &[(f64, f64)], centroids: &[(f64, f64)]) -> Vec<usize> {
    // BUG: only compares the x-coordinate, ignoring y entirely.
    points
        .iter()
        .map(|&(px, _py)| {
            centroids
                .iter()
                .map(|&(cx, _cy)| (px - cx).abs())
                .enumerate()
                .fold((0usize, f64::INFINITY), |(bi, bd), (i, d)| {
                    if d < bd {
                        (i, d)
                    } else {
                        (bi, bd)
                    }
                })
                .0
        })
        .collect()
}

fn online_mean_update(old_mean: f64, new_x: f64, n: u64) -> f64 {
    // Correct.
    old_mean + (new_x - old_mean) / n as f64
}

fn main() {
    let points = [(0.0, 0.0), (0.2, 0.1), (0.0, 5.0), (0.1, 5.1)];
    let centroids = [(0.0, 0.0), (0.0, 5.0)];
    println!(
        "K-means assignments: {:?}  <-- should distinguish the two y-clusters!",
        kmeans_assign(&points, &centroids)
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_simple_linear_regression_fit() {
        let xs = [1.0, 2.0, 3.0, 4.0, 5.0];
        let ys = [3.0, 5.0, 7.0, 9.0, 11.0];
        let (b0, b1) = simple_linear_regression_fit(&xs, &ys);
        assert!((b0 - 1.0).abs() < 1e-6, "b0 = {b0}");
        assert!((b1 - 2.0).abs() < 1e-6, "b1 = {b1}");
    }

    #[test]
    fn test_predict() {
        let preds = predict(&[0.0, 1.0, 2.0], 1.0, 2.0);
        assert_eq!(preds, vec![1.0, 3.0, 5.0]);
    }

    #[test]
    fn test_mse() {
        let m = mse(&[1.0, 2.0, 3.0], &[1.0, 2.0, 5.0]);
        assert!((m - 4.0 / 3.0).abs() < 1e-9, "got {m}");
    }

    #[test]
    fn test_kmeans_assign() {
        let points = [(0.0, 0.0), (0.2, 0.1), (0.0, 5.0), (0.1, 5.1)];
        let centroids = [(0.0, 0.0), (0.0, 5.0)];
        assert_eq!(kmeans_assign(&points, &centroids), vec![0, 0, 1, 1]);
    }

    #[test]
    fn test_online_mean_update() {
        assert!((online_mean_update(5.0, 15.0, 2) - 10.0).abs() < 1e-9);
    }
}
