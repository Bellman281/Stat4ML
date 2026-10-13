# Chapter 8 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (cross_entropy, ce_grad).

softmax <- function(zs) { e <- exp(zs - max(zs)); e / sum(e) }

cross_entropy <- function(p, y) {
  # BUG: cross-entropy is -sum(y*log(p)); the leading minus sign is missing.
  sum(y * log(p))
}
ce_grad <- function(p, y) {
  # BUG: the gradient at the logits is p - y, not y - p (ch08_text.tex Sec 2).
  y - p
}

run_tests <- function() {
  failures <- c()
  check <- function(name, cond, detail = "") {
    cond <- isTRUE(cond)
    cat(sprintf("[%s] %s%s\n", if (cond) "PASS" else "FAIL", name,
                if (nchar(detail)) paste0(": ", detail) else ""))
    if (!cond) failures[[length(failures) + 1]] <<- name
  }
  z <- c(2.0, 0.5, -1.0); y <- c(1, 0, 0); p <- softmax(z)

  L <- cross_entropy(p, y)
  check("cross_entropy", abs(L - (-log(p[1]))) < 1e-9, sprintf("got %s", format(L)))

  g <- ce_grad(p, y)
  expected <- p - y
  check("ce_grad == p - y", all(abs(g - expected) < 1e-9), paste("got", paste(format(g), collapse = ",")))

  eps <- 1e-6
  for (k in seq_along(z)) {
    zp <- z; zp[k] <- zp[k] + eps
    zm <- z; zm[k] <- zm[k] - eps
    num <- (cross_entropy(softmax(zp), y) - cross_entropy(softmax(zm), y)) / (2 * eps)
    check(sprintf("grad[%d] matches numeric", k), abs(g[k] - num) < 1e-4,
          sprintf("%.6f vs %.6f", g[k], num))
  }
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
