"""
Chapter 8 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (relu_grad, grad_W). Fix one function at a time until all
tests pass. Do not edit run_tests(). The final test checks that grad_W really
is dL/dW for a one-layer softmax classifier, via finite differences.
"""
# level: research
import math


def relu_grad(zs):
    # BUG: ReLU's derivative is 1 for z > 0 and 0 otherwise; this is backwards.
    return [0.0 if z > 0 else 1.0 for z in zs]


def grad_logits(p, y):
    return [pk - yk for pk, yk in zip(p, y)]


def grad_W(delta, x):
    # BUG: the outer product is delta[i]*x[j]; this multiplies by delta[j],
    # which is not even well-defined when len(delta) != len(x).
    return [[delta[i] * delta[j] for j in range(len(x))] for i in range(len(delta))]


# --- helpers used only by the test (a 1-layer softmax classifier) ---
def _softmax(zs):
    m = max(zs); e = [math.exp(z - m) for z in zs]; s = sum(e)
    return [ei / s for ei in e]


def _loss_of_W(W, x, y):
    z = [sum(W[i][j] * x[j] for j in range(len(x))) for i in range(len(W))]
    p = _softmax(z)
    return -sum(yk * math.log(pk) for pk, yk in zip(p, y))


def run_tests():
    failures = []

    def check(name, cond, detail=""):
        print(f"[{'PASS' if cond else 'FAIL'}] {name}{(': ' + detail) if detail else ''}")
        if not cond:
            failures.append(name)

    check("relu_grad", relu_grad([-1.0, 0.0, 2.0]) == [0.0, 0.0, 1.0],
          f"got {relu_grad([-1.0, 0.0, 2.0])}")

    p = [0.7, 0.2, 0.1]; y = [1.0, 0.0, 0.0]
    gl = grad_logits(p, y)
    check("grad_logits", all(abs(a - b) < 1e-9 for a, b in zip(gl, [-0.3, 0.2, 0.1])),
          f"got {gl}")

    # analytic dL/dW vs finite differences for z = W x
    W = [[0.1, -0.2], [0.0, 0.3], [-0.1, 0.1]]
    x = [1.0, 2.0]
    z = [sum(W[i][j] * x[j] for j in range(len(x))) for i in range(len(W))]
    delta = grad_logits(_softmax(z), y)
    G = grad_W(delta, x)
    eps = 1e-6
    ok = True
    for i in range(len(W)):
        for j in range(len(x)):
            Wp = [row[:] for row in W]; Wp[i][j] += eps
            Wm = [row[:] for row in W]; Wm[i][j] -= eps
            num = (_loss_of_W(Wp, x, y) - _loss_of_W(Wm, x, y)) / (2 * eps)
            if abs(G[i][j] - num) > 1e-4:
                ok = False
    check("grad_W matches numeric dL/dW", ok)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
