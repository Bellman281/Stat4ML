"""
Chapter 8 exercise -- one step of backpropagation (Research tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch08_text.tex Section 3. These are the
three pieces of a backward pass:
  - relu_grad  : the local derivative of ReLU (1 where z>0, else 0).
  - grad_logits: the delta at the logits of a softmax+cross-entropy head, p - y.
  - grad_W     : dL/dW for a linear layer z = W x, which is the outer product
                 delta (x)^T  ->  grad_W[i][j] = delta[i] * x[j].

Vectors are lists; a matrix is a list of row-lists.
Run with:  python3 exercise10.py
Reference solution: solutions/exercise10_solution.py
"""
# level: research


def relu_grad(zs):
    """Element-wise ReLU derivative: 1.0 where z > 0, else 0.0."""
    raise NotImplementedError("TODO: relu_grad")


def grad_logits(p, y):
    """Delta at the logits of a softmax+CE head: p - y."""
    raise NotImplementedError("TODO: grad_logits")


def grad_W(delta, x):
    """Outer product delta (x)^T: a matrix with grad_W[i][j] = delta[i]*x[j]."""
    raise NotImplementedError("TODO: grad_W")


def main():
    print("relu_grad  :", relu_grad([-1.0, 0.0, 2.0]))
    p = [0.7, 0.2, 0.1]; y = [1.0, 0.0, 0.0]
    delta = grad_logits(p, y)
    print("grad_logits:", delta)
    print("grad_W     :", grad_W(delta, [1.0, 2.0]))


if __name__ == "__main__":
    main()
