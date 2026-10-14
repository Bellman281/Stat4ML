"""Chapter 1 -- reference solution (Proof)."""
# level: proof
import math


def hoeffding_tail(n, eps):
    return 2 * math.exp(-2 * n * eps ** 2)


def confidence_width(n, delta):
    return math.sqrt(math.log(2 / delta) / (2 * n))


def finite_class_bound(emp_risk, m, n, delta):
    return emp_risk + math.sqrt((math.log(m) + math.log(2 / delta)) / (2 * n))


def main():
    print("hoeffding_tail(100,0.1):", hoeffding_tail(100, 0.1))
    print("confidence_width(200)  :", confidence_width(200, 0.05))
    print("finite_class_bound     :", finite_class_bound(0.1, 1000, 500, 0.05))


if __name__ == "__main__":
    main()
