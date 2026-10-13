# Chapter 8 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (relu_grad, grad_W).

relu_grad <- function(zs) {
  # BUG: ReLU's derivative is 1 for z > 0 and 0 otherwise; this is backwards.
  as.numeric(zs <= 0)
}
grad_logits <- function(p, y) p - y
grad_W <- function(delta, x) {
  # BUG: the outer product is delta[i]*x[j] (delta %o% x), not delta %o% delta.
  delta %o% delta
}

softmax <- function(zs) { e <- exp(zs - max(zs)); e / sum(e) }
.loss_of_W <- function(W, x, y) {
  z <- as.vector(W %*% x)
  p <- softmax(z)
  -sum(y * log(p))
}

run_tests <- function() {
  failures <- c()
  check <- function(name, cond, detail = "") {
    cond <- isTRUE(cond)
    cat(sprintf("[%s] %s%s\n", if (cond) "PASS" else "FAIL", name,
                if (nchar(detail)) paste0(": ", detail) else ""))
    if (!cond) failures[[length(failures) + 1]] <<- name
  }

  check("relu_grad", all(relu_grad(c(-1, 0, 2)) == c(0, 0, 1)),
        paste("got", paste(relu_grad(c(-1, 0, 2)), collapse = ",")))

  p <- c(0.7, 0.2, 0.1); y <- c(1, 0, 0)
  check("grad_logits", all(abs(grad_logits(p, y) - c(-0.3, 0.2, 0.1)) < 1e-9),
        paste("got", paste(format(grad_logits(p, y)), collapse = ",")))

  # analytic dL/dW vs finite differences for z = W x
  W <- matrix(c(0.1, -0.2, 0.0, 0.3, -0.1, 0.1), nrow = 3, byrow = TRUE)
  x <- c(1.0, 2.0)
  delta <- grad_logits(softmax(as.vector(W %*% x)), y)
  G <- grad_W(delta, x)
  eps <- 1e-6
  ok <- isTRUE(all(dim(G) == dim(W)))
  if (ok) {
    for (i in 1:nrow(W)) for (j in 1:ncol(W)) {
      Wp <- W; Wp[i, j] <- Wp[i, j] + eps
      Wm <- W; Wm[i, j] <- Wm[i, j] - eps
      num <- (.loss_of_W(Wp, x, y) - .loss_of_W(Wm, x, y)) / (2 * eps)
      if (abs(G[i, j] - num) > 1e-4) ok <- FALSE
    }
  }
  check("grad_W matches numeric dL/dW", ok)

  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
