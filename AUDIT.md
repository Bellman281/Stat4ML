# Content Audit

This audit covers every PDF that existed in the two source repositories
(`Stat4ML` and `Intro_Statistical_Learning`) before this reorganization,
found by extracting each PDF to text (`pdftotext -layout`) and reading it
in full (or, for a few of the longer/lower-priority files, spot-checking
the mathematically dense sections). It is organized into three parts:
structural issues (chapter numbering), confirmed typos/errors, and content
gaps. Where the source is a Beamer-generated PDF, a few items below could
be artifacts of `pdftotext` extraction rather than the original slide --
those are called out explicitly as "verify against the rendered PDF."

## 1. Chapter-numbering drift (Intro_Statistical_Learning)

The `Intro_Statistical_Learning` README lists 13 "basic course" chapters
by topic, but the PDF files actually committed to the repo use a
different, inconsistent numbering. This was the single biggest structural
issue found, and it directly motivated the "Separate parts, each
renumbered" chapter scheme used in `part2_intro_statistical_learning/`
(each chapter there is renumbered by topic order; the table below records
which original file backs which renumbered chapter).

| README topic order | README topic | File found on disk | Drift |
|---|---|---|---|
| 1 | Learning Algorithms Overview | `Chapter_1__Learning_Algorithms.pdf` | none |
| 2 | Regression, Cross-Validation | `Chapter_2__Cross_Validation.pdf` | file title only mentions CV, not regression |
| 3 | Logistic, Ridge, Lasso Regression | `Chapter_3__Regularization.pdf` | file covers logistic + ridge; Lasso is in the README topic list but the slides only sketch it (see gaps, below) |
| 4 | Recommendation Systems | *(none)* | missing entirely |
| 5 | Unsupervised Learning, PCA | `Chapter_5__Unsupervised_Learning.pdf` | none |
| 6 | EM Algorithm | `Chapter_7__EM_Algorithm.pdf` | **file numbered 7, not 6** |
| 7 | Clustering | `Chapter_8__Clustrering.pdf` | **file numbered 8, not 7**, plus filename typo ("Clustrering") |
| 8 | NN, Activation and Loss Functions | `Chapter_9__Activation_and_loss_functions.pdf` | **file numbered 9, not 8** |
| 9 | CNN | *(none)* | missing entirely |
| 10 | RNN, LSTM | *(none)* | missing entirely |
| 11 | Language Models and Tokenization | *(none)* | missing entirely |
| 12 | Transformers | `Chapter_11__Transformers.pdf` | **file numbered 11, not 12** |
| 13 | Large Language Models | *(none)* | missing entirely |
| Advanced 12 | Automatic Feature Extraction | `Chapter_12__Automatic_Feature_Extraction.pdf` | matches its own Advanced-course number, coincidentally |

Likely explanation: as chapters were recorded, the uploaded file numbers
were not kept in sync with the README's topic list whenever a planned
chapter (4, 9, 10, 11, 13) was skipped or reordered. Recommendation
adopted in this reorg: treat the README's topic order as authoritative,
renumber the chapter folders accordingly, and keep a note of the original
filename in each chapter's `README.md` (already done for every chapter in
`part2_intro_statistical_learning/`).

## 2. Confirmed typos and content errors

### Stat4ML slides (Part I)

- **Slide 1 (Probability Theory Foundation):**
  - "Bayaes's Rule" -> "Bayes's Rule" (p.23/49).
  - "identically disturbed" -> "identically distributed" (section header, p.35/49) -- easy to miss because it reads as a plausible English phrase.
  - "Whats is the sample space..." (x2, p.4/49) -> "What is the sample space...".
  - "Amazone's product page" -> "Amazon's product page" (p.5/49).
  - "The the pdf of Y is given by" (Theorem 7.2 statement, p.45/49) -> "Then the pdf of Y is given by".
  - Fixed in `part1_statistics_foundations/ch01_probability_theory_foundations/ch01_text.tex`.

- **Slide 2 (Moments):** "Recall that"average" is..." -- missing space/quote mark around "average" (p.5/37); stylistic only, fixed in the rewritten chapter text.

- **Slide 5, 6 (Convergence, MLE):** "disect the notation" -> "dissect the notation" (Slide 6, p.9/36). Also, on the same slide, one instance of the parameter vector is written as "q" instead of "θ" ("the parameter vector, q, is common for all variables", p.13/36) -- **verify against the rendered PDF**; every other occurrence on the same slide correctly uses θ, so this could be a `pdftotext` font-mapping artifact rather than an authored typo, but it reads oddly either way.

- **Slide 7 (Bayesian Estimation):** "θ̂MLE := argθ max p(Dθ)" is missing the conditioning bar -- should read `p(D|θ)` (p.7/17). **Verify against the rendered PDF**; this pattern (a dropped `|`) shows up in a few Beamer-to-text extractions and may not be present in the actual slide.

- **Homework 5:** "we should find the the probability..." -- duplicated word (p. of `STAT4ML_Homework5.pdf`).

- **`PreReq1_Matrix_Calculus.pdf` (Matrix Algebra prerequisite deck):**
  - **Real math bug (LU decomposition worked example):** for
    `A = [[4, 3], [6, 3]]`, Doolittle's method gives `u11 = a11 = 4`
    (the pivot is copied straight from `A`, never recomputed) -- the
    slide's worked example instead writes `u11 = 14`, a digit typo (an
    extra "1" prepended). The rest of that example's arithmetic
    (`l21 = 6/4 = 1.5`, `u22 = 3 - 1.5*3 = -1.5`) is internally
    consistent with `u11 = 4`, not `u11 = 14`, confirming this is a
    typo rather than a different (also valid) decomposition. Corrected,
    with the original slide's number called out explicitly, in
    `part1_statistics_foundations/ch00_matrix_algebra_review/ch00_text.tex`
    Section 6.1.
  - **Real math bug (derivative of a matrix inverse):** the slide gives
    the identity for `d(A^-1)/d(alpha)` without a leading minus sign,
    i.e. as `A^-1 (dA/d alpha) A^-1`. Differentiating both sides of
    `A A^-1 = I` with the product rule gives
    `(dA/d alpha) A^-1 + A d(A^-1)/d alpha = 0`, so
    `d(A^-1)/d alpha = -A^-1 (dA/d alpha) A^-1` -- the minus sign is
    required, not optional (dropping it flips the sign of every
    downstream computation that uses this identity, e.g. in
    gradient-based fitting of covariance matrices). Corrected, with the
    full product-rule derivation, in `ch00_text.tex` Section 7.

### Intro_Statistical_Learning (Part II)

- **Chapter 3 (Regularization), "How to solve ridge regression?" slide:** the extracted formula reads `LossR(β, λ) = Σ(yi − β0 − 6pβj Xij)² + λΣ 6pβj²` -- the `6p` is almost certainly a corrupted rendering of `Σ_{j=1}^{p}` (a summation glyph substitution), not an actual "6p" in the math. **Flagged for visual verification against the original PDF** -- if the slide itself renders this way (rather than it being a `pdftotext` artifact), it is a real typesetting bug in the LaTeX/Beamer source (likely a missing `\sum` macro).
- Same chapter: "Ordinary leas squares" -> "Ordinary least squares" (typo, "Two method for regularization" slide).
- Same chapter, Lasso slide: "Bad news: no closed form solution like ridge regression. Good news: no derivation." -- the second bullet doesn't make sense as stated; it most likely should say something like "Good news: solvable efficiently via convex optimization (e.g. coordinate descent)". Flagged as unclear/likely-incomplete original content, not just a typo.
- Reference list: Google Books URL contains a leftover escape artifact, `id=qcI%5C AAAAQBAJ` (should not contain `%5C`).

- **Chapter 9 (Activation and Loss Functions):**
  - **Real math bug:** the ELU derivative is given as
    ```
    ELU'(x) = 1        if x < 0
              α e^x    if x < 0
    ```
    both cases are labeled `x < 0`. The first case should be `x ≥ 0` (matching `ELU(x)`'s own case split). This is a genuine error, not just an extraction artifact -- fixed as a discussion point in `part2_intro_statistical_learning/ch08_nn_activation_and_loss_functions/README.md`.
  - The Mean Absolute Error and Mean Squared Error formulas are written with a plain `y` instead of `y_i` inside the sum (`MAE = (1/n) Σ |y − ŷ_i|`, `MSE = (1/n) Σ (y − ŷ_i)²`) -- missing subscript on the first term in both. MAPE, just below, has the subscript correct (`(y_i − ŷ_i)/y_i`), which makes the inconsistency clearer.
  - The "Mean Squared Logarithmic Error (MSLE)" slide defines its formula as `MSE = (1/n) Σ (log(y_i+1) − log(ŷ_i+1))²` -- the left-hand side is mislabeled `MSE` when it should be `MSLE` (copy-paste from the previous slide). This also explains why the table of contents lists "Mean Squared Error (MSE)" twice -- the second occurrence should read "Mean Squared Logarithmic Error (MSLE)".

- **Chapter 8, filename:** `Chapter_8__Clustrering.pdf` -- "Clustrering" -> "Clustering" (also see numbering drift, Section 1 above).

- **Chapter 11 (Transformers):** "it could be dominated by the the actual word itself" -- duplicated word.

### Advanced-course topic list (Intro_Statistical_Learning README, "Advanced Course" section)

These are typos in the README's topic list itself (no slides exist yet for
this part, so they were only ever prose, not rendered math):
- "epsilon Gridy" -> "epsilon-greedy" (Chapter 4, Multi-Armed Bandits).
- "UPC" -> "UCB" (upper confidence bound) (Chapter 4, Multi-Armed Bandits).
- "YOLO5" -> "YOLOv5", "POSE Detection: BLAZE POSE" -> "BlazePose" (Chapter 6).
- "Tacatron" -> "Tacotron" (Chapter 9, Speech Processing).

All four are corrected in `part3_advanced_statistical_learning/`'s
chapter READMEs.

## 3. Content gaps (topics announced but no slide deck exists)

These chapters are named in one of the two READMEs but have no
corresponding PDF anywhere in either source repository. They are
scaffolded as STUB chapters with this gap explicitly noted in their
`README.md`, and are called out again in `ROADMAP.md`:

- Part II: Chapter 4 (Recommendation Systems), Chapter 9 (CNN),
  Chapter 10 (RNN/LSTM), Chapter 11 (Language Models and Tokenization),
  Chapter 13 (Large Language Models). Also: Lasso regression is named in
  the Chapter 3 topic list but is only mentioned in passing in the actual
  slides (Ridge is fully derived; Lasso gets one slide with no derivation).
- Part III (Advanced Statistical Learning): the entire part has no slides
  yet -- the original README literally says "to be announced." All 12
  chapters are scaffolded from the existing topic list.

## 4. What this audit did *not* do

This was a manual read-through of extracted text, not a line-by-line diff
against the rendered PDF pages (no page images were rendered/inspected).
Three items above are explicitly flagged "verify against the rendered
PDF" because a plain-text extraction of Beamer slides can itself introduce
artifacts (dropped conditioning bars, substituted glyphs for `Σ`, `θ`
occasionally extracted as a similar-looking Latin letter). Genuine content
bugs (the ELU derivative, the MSLE mislabeling, the missing-subscript MAE/
MSE formulas, the numbering drift) are not in that category -- those are
present in the extracted text regardless of rendering, and are also
independently checkable against the definitions in `ch01_text.tex`/
`ch02_text.tex` (Part I) and the ISL chapter READMEs (Part II).
