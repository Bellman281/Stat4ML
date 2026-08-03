"""
Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Python edition)
Part I: Statistics Foundation for ML

Every function below is fully implemented -- but FIVE of them contain a
deliberate bug that violates something from ch01_text.tex (an axiom, a
theorem, or a formula). Your job is NOT to write new code from scratch: it
is to find and fix each bug so that every test in `run_tests()` passes.

How to work through this file (just like Rustlings):
  1. Run it:  python3 exercise01_buggy.py
  2. Read the first assertion failure -- it names the broken function and
     shows expected vs. actual output.
  3. Fix ONLY that function.
  4. Re-run. Repeat until you see "All tests passed!".

Do not change the test harness (`run_tests`) or the function signatures --
only the buggy function bodies.
"""
import random


def sample_space_two_coins():
    return ["HH", "HT", "TH", "TT"]


def is_valid_probability_function(p, sample_space, tol=1e-9):
    # BUG: only checks that probabilities sum to 1 -- forgets to check
    # non-negativity (Kolmogorov's Axiom 1, ch01_text.tex Section 2.2) and
    # forgets to check that the keys of `p` match `sample_space` exactly.
    return abs(sum(p.values()) - 1.0) < tol


def complement_probability(p_a):
    # BUG: returns P(A) instead of P(A^c) = 1 - P(A).
    return p_a


def union_probability(p_a, p_b, p_a_and_b):
    # BUG: classic inclusion-exclusion mistake -- forgets to subtract the
    # intersection. P(A u B) = P(A) + P(B) - P(A n B), NOT P(A) + P(B).
    return p_a + p_b


def conditional_probability(p_a_and_b, p_b):
    # This one is correct: P(A|B) = P(A n B) / P(B).
    return p_a_and_b / p_b


def bayes_theorem(p_b_given_a, p_a, p_b):
    # BUG: forgets to divide by P(B). Bayes' rule is
    # P(A|B) = P(B|A) * P(A) / P(B), not just P(B|A) * P(A).
    return p_b_given_a * p_a


def bayes_theorem_partition(p_b_given_ai, p_ai):
    # This one is correct.
    denom = sum(pb * pa for pb, pa in zip(p_b_given_ai, p_ai))
    return [pb * pa / denom for pb, pa in zip(p_b_given_ai, p_ai)]


def simulate_coin_law_of_large_numbers(p_heads, n_tosses, seed=0):
    # BUG: uses a fixed threshold of 0.5 instead of the requested p_heads,
    # so the simulation ignores its own parameter.
    rng = random.Random(seed)
    heads = sum(1 for _ in range(n_tosses) if rng.random() < 0.5)
    return heads / n_tosses


# --------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# --------------------------------------------------------------------------
def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol if isinstance(expected, float) else got == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    ss = sample_space_two_coins()
    check("sample_space_two_coins", ss, ["HH", "HT", "TH", "TT"])

    fair = {o: 0.25 for o in ss}
    invalid = {"HH": 0.5, "HT": -0.1, "TH": 0.3, "TT": 0.3}  # negative prob!
    check("is_valid_probability_function(fair)",
          is_valid_probability_function(fair, ss), True)
    check("is_valid_probability_function(invalid, has negative prob)",
          is_valid_probability_function(invalid, ss), False)

    check("complement_probability(0.3)", complement_probability(0.3), 0.7)
    check("union_probability(0.5, 0.4, 0.2)", union_probability(0.5, 0.4, 0.2), 0.7)
    check("conditional_probability(0.2, 0.4)", conditional_probability(0.2, 0.4), 0.5)
    # P(A)=0.5, P(B)=0.4, P(B|A) = P(AnB)/P(A) = 0.2/0.5 = 0.4 => P(A|B) should be 0.5
    check("bayes_theorem", bayes_theorem(0.4, 0.5, 0.4), 0.5)

    post = bayes_theorem_partition([0.9, 0.2], [0.01, 0.99])
    expected_denom = 0.9 * 0.01 + 0.2 * 0.99
    check("bayes_theorem_partition[0]", round(post[0], 6),
          round(0.9 * 0.01 / expected_denom, 6))

    freq = simulate_coin_law_of_large_numbers(0.2, 200_000, seed=42)
    check("simulate_coin_law_of_large_numbers(p=0.2) converges near 0.2",
          round(freq, 1), 0.2, tol=0.05)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
