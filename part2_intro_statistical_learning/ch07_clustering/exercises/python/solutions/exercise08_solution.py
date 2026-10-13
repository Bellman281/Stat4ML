"""Chapter 7 -- reference solution (Proof)."""
# level: proof


def sq_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def inertia(data, labels, centroids):
    return sum(sq_dist(data[i], centroids[labels[i]]) for i in range(len(data)))


def assign_step(data, centroids):
    return [min(range(len(centroids)), key=lambda k: sq_dist(x, centroids[k])) for x in data]


def update_step(data, labels, K):
    out = []
    for k in range(K):
        members = [data[i] for i in range(len(data)) if labels[i] == k]
        if members:
            n = len(members)
            out.append([sum(p[0] for p in members) / n, sum(p[1] for p in members) / n])
        else:
            out.append([0.0, 0.0])
    return out


def main():
    data = [[0, 0], [1, 0], [10, 0], [11, 0]]
    cents = [[0, 0], [5, 0]]
    labels = assign_step(data, cents)
    print("labels       :", labels)
    print("J before     :", inertia(data, labels, cents))
    cents2 = update_step(data, labels, 2)
    print("new centroids:", cents2)
    print("J after      :", inertia(data, labels, cents2))


if __name__ == "__main__":
    main()
