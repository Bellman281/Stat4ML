//! Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Rust edition), Exercise 3
//! Part II: Introduction to Statistical Learning
//!
//! Three deliberate bugs are hiding below (in online_variance_update,
//! variance_from_state, and pseudo_label_accuracy). Find and fix each
//! one so every `#[test]` passes. Do not edit the tests.
//!
//! Build & run: rustc --edition 2021 --test exercise03_buggy.rs -o /tmp/ex03_buggy_test && /tmp/ex03_buggy_test

#[derive(Clone, Copy)]
struct WelfordState {
    n: u64,
    mean: f64,
    m2: f64,
}

fn online_variance_update(state: WelfordState, new_x: f64) -> WelfordState {
    // BUG: reuses `delta` (from the OLD mean) a second time instead of
    // computing `delta2` from the updated mean.
    let n = state.n + 1;
    let delta = new_x - state.mean;
    let mean = state.mean + delta / n as f64;
    let m2 = state.m2 + delta * delta;
    WelfordState { n, mean, m2 }
}

fn variance_from_state(state: WelfordState) -> f64 {
    // BUG: uses the (n-1) sample-variance correction instead of
    // population variance m2/n.
    if state.n > 1 {
        state.m2 / (state.n - 1) as f64
    } else {
        0.0
    }
}

fn pseudo_label_accuracy(teacher_preds: &[i32], true_labels: &[i32]) -> f64 {
    // BUG: forgets to divide by the total count.
    let matches = teacher_preds.iter().zip(true_labels).filter(|(p, t)| p == t).count();
    matches as f64
}

fn semi_supervised_combined_accuracy(labeled_acc: f64, labeled_frac: f64, pseudo_acc: f64, unlabeled_frac: f64) -> f64 {
    // Correct.
    labeled_frac * labeled_acc + unlabeled_frac * pseudo_acc
}

fn main() {
    let acc = pseudo_label_accuracy(&[1, 0, 1, 1, 0], &[1, 0, 0, 1, 0]);
    println!("pseudo_label_accuracy (buggy) = {acc}");
    let _ = semi_supervised_combined_accuracy(0.95, 0.1, acc, 0.9);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_online_variance() {
        let stream = [4.0, 6.0, 8.0, 2.0, 10.0];
        let mut state = WelfordState { n: 0, mean: 0.0, m2: 0.0 };
        for &x in &stream {
            state = online_variance_update(state, x);
        }
        let var = variance_from_state(state);
        assert!((var - 8.0).abs() < 1e-9, "got {var}");
    }

    #[test]
    fn test_pseudo_label_accuracy() {
        let acc = pseudo_label_accuracy(&[1, 0, 1, 1, 0], &[1, 0, 0, 1, 0]);
        assert!((acc - 0.8).abs() < 1e-9, "got {acc}");
    }
}
