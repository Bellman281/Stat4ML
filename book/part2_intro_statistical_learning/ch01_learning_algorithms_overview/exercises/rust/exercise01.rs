//! Chapter 1 exercise -- Learning Algorithms Overview (Rust edition)
//! Part II: Introduction to Statistical Learning
//!
//! HOMEWORK: implement one small example of each of three learning
//! paradigms: supervised (closed-form simple linear regression),
//! unsupervised (a K-means assignment step), online (running mean).
//!
//! Build & run the tests with:
//!   rustc --edition 2021 --test exercise01.rs -o /tmp/isl_exercise01_test && /tmp/isl_exercise01_test

/// Fit y = b0 + b1*x by ordinary least squares. Returns (b0, b1).
fn simple_linear_regression_fit(xs: &[f64], ys: &[f64]) -> (f64, f64) {
    // TODO: b1 = sum((x-xbar)*(y-ybar)) / sum((x-xbar)^2); b0 = ybar - b1*xbar
    todo!("simple_linear_regression_fit")
}

/// Return [b0 + b1*x for x in xs].
fn predict(xs: &[f64], b0: f64, b1: f64) -> Vec<f64> {
    // TODO
    todo!("predict")
}

/// Mean squared error.
fn mse(y_true: &[f64], y_pred: &[f64]) -> f64 {
    // TODO
    todo!("mse")
}

/// Unsupervised learning step: for each point (x,y), return the index of
/// the nearest centroid (Euclidean distance).
fn kmeans_assign(points: &[(f64, f64)], centroids: &[(f64, f64)]) -> Vec<usize> {
    // TODO
    todo!("kmeans_assign")
}

/// Online learning step: incremental mean update.
fn online_mean_update(old_mean: f64, new_x: f64, n: u64) -> f64 {
    // TODO: old_mean + (new_x - old_mean) / n
    todo!("online_mean_update")
}

fn main() {
    let xs = [1.0, 2.0, 3.0, 4.0, 5.0];
    let ys = [2.1, 3.9, 6.2, 7.8, 10.1];
    let (b0, b1) = simple_linear_regression_fit(&xs, &ys);
    let preds = predict(&xs, b0, b1);
    println!("Fitted line: y = {b0:.3} + {b1:.3} x, MSE = {:.4}", mse(&ys, &preds));

    let points = [(0.0, 0.0), (0.2, 0.1), (5.0, 5.0), (5.1, 4.9)];
    let centroids = [(0.0, 0.0), (5.0, 5.0)];
    println!("K-means assignments: {:?}", kmeans_assign(&points, &centroids));

    let stream = [4.0, 6.0, 8.0, 2.0, 10.0];
    let mut mean = stream[0];
    for (i, &x) in stream[1..].iter().enumerate() {
        let n = (i + 2) as u64;
        mean = online_mean_update(mean, x, n);
    }
    let batch_mean: f64 = stream.iter().sum::<f64>() / stream.len() as f64;
    println!("Final running mean = {mean:.4} (batch mean = {batch_mean:.4})");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_simple_linear_regression_fit() {
        // y = 1 + 2x exactly, not centered at x=0.
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
        assert!((m - 4.0 / 3.0).abs() < 1e-9);
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
