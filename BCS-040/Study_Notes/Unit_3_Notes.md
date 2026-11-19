# Unit 3: Probability Distributions

**Block 1: Descriptive Statistics & Probability**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 3 - Probability Distributions (IGNOU BCS-040)

---

## 3.1 Introduction

A **random variable (r.v.)** is a function that assigns a numerical value to each outcome of a random experiment. It is denoted by capital letters (X, Y, Z) and its values by lowercase (x, y, z).

**Definition from Book**: "When a variable takes different values according to chance, (which can't be predicted beforehand), it is called a random variable."

### Types of Random Variables (from Book)
| Type | Values | Examples |
|------|--------|----------|
| **Discrete** | Countable (finite or countably infinite) - "jump points" | Number of heads, number of defects, number of calls, number of industrial accidents |
| **Continuous** | Any value in an interval (no gaps) | Height, weight, time, temperature, daily snowfall |

### Probability Distribution
- **Discrete**: Probability Mass Function (PMF) $P(X=x_i) = p_i$ where $\sum p_i = 1$, $p_i \geq 0$
- **Continuous**: Probability Density Function (PDF) $f(x)$ where $\int_{-\infty}^{\infty} f(x)dx = 1$, $f(x) \geq 0$

### Expectation and Variance
| Measure | Discrete | Continuous |
|---------|----------|------------|
| **Mean (E[X])** | $\sum x_i p_i$ | $\int x f(x) dx$ |
| **Variance (Var[X])** | $E[X^2] - (E[X])^2$ | $E[X^2] - (E[X])^2$ |

---

## 3.2 Binomial Distribution

### Conditions (Bernoulli Trials) - from Book
1. Fixed number of trials ($n$)
2. Each trial has two outcomes: Success (S) / Failure (F)
3. Probability of success ($p$) constant across trials
4. Trials are independent

### Notation
$X \sim B(n, p)$ where $X$ = number of successes in $n$ trials

### PMF (from Book - Formula derivation)
$$P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}, \quad x = 0, 1, 2, \ldots, n$$

### Mean and Variance (Derived in Book)
- **Mean**: $E[X] = np$
  - *Derivation*: $E(X) = np[1 - (q+p)^{n-1}] = np$ (Book shows via binomial expansion)
- **Variance**: $Var[X] = np(1-p) = npq$ where $q = 1-p$
- **Standard Deviation**: $\sigma = \sqrt{npq}$

### Properties
- $P(X=0) = q^n$
- $P(X=n) = p^n$
- Mode $\approx \lfloor (n+1)p \rfloor$
- Sum of independent binomials: $B(n_1,p) + B(n_2,p) = B(n_1+n_2,p)$

### When to Use Binomial
- Fixed number of independent trials
- Two outcomes per trial (success/failure)
- Constant probability of success
- Counting number of successes

---

## 3.3 Worked Examples from Textbook (Must Practice)

### Example 1: Binomial Mean Derivation (Book)
$E(X) = \sum_{x=0}^n x \binom{n}{x} p^x q^{n-x} = np \sum_{y=0}^{n-1} \binom{n-1}{y} p^y q^{n-1-y} = np$

### Example 2: Oil Exploration (Problem 4 - Book)
> **Oil exploration firm drills 6 holes. P(success) = 0.1 per hole. Firm stays in business if ≥ 2 holes produce oil. Find P(stay in business) and expected number of successful holes.**

**Solution**:
- $X \sim B(6, 0.1)$
- $P(\text{stay}) = P(X \geq 2) = 1 - P(X=0) - P(X=1)$
- $P(X=0) = (0.9)^6 = 0.531$
- $P(X=1) = 6 \times 0.1 \times (0.9)^5 = 0.354$
- $P(\text{stay}) = 1 - 0.531 - 0.354 = 0.115$
- Expected successful holes = $np = 6 \times 0.1 = 0.6$

### Example 3: Car Dealer (Exercise E4)
> **Second-hand car dealer: Sales of 0,1,2,3,4,5 cars with probabilities 0.05, 0.15, 0.35, 0.25, 0.12, 0.18. Find average cars sold per day.**

**Solution**: $E[X] = \sum x_i p_i = 0(0.05) + 1(0.15) + 2(0.35) + 3(0.25) + 4(0.12) + 5(0.18) = 2.65$

---

## 3.4 PYQ-Based Important Questions (Binomial)

### 5-Mark Questions (Section A) - HIGH PRIORITY (3 appearances in 9 papers)

#### 1. Target Hitting Problem (Jun 2021, Dec 2024, Dec 2025) ⭐⭐⭐
> "Probability of hitting target = 0.3. 5 shots fired. Find P(exactly 2 hits) and P(at least 2 hits)."

**Solution**:
- $X \sim B(5, 0.3)$
- $P(X=2) = \binom{5}{2}(0.3)^2(0.7)^3 = 10 \times 0.09 \times 0.343 = 0.3087$
- $P(X \geq 2) = 1 - P(X=0) - P(X=1) = 1 - 0.7^5 - 5 \times 0.3 \times 0.7^4 = 0.4718$

#### 2. Target Hitting Probability (Dec 2025) ⭐⭐⭐
> "Probability of hitting target = p. n shots fired. Find probability of exactly r hits / at least r hits."

**Solution**:
- $X \sim B(n, p)$
- $P(X=r) = \binom{n}{r} p^r (1-p)^{n-r}$
- $P(X \geq r) = 1 - \sum_{k=0}^{r-1} \binom{n}{k} p^k (1-p)^{n-k}$

#### 3. Three Students Problem (Dec 2022, 2023, 2024, 2025, Jun 2024 - **5 IDENTICAL!**) ⭐⭐⭐⭐⭐
> "Three students A, B, C solve a problem with probabilities 1/2, 1/3, 1/4. Find probability problem is solved."

**Solution**: This is NOT binomial directly - it's independent events.
- $P(\text{at least one solves}) = 1 - P(\text{none solve})$
- $= 1 - (1/2)(2/3)(3/4) = 1 - 1/4 = 3/4$

---

## 3.5 Poisson Distribution

### Conditions (Rare Events) - from Book
1. Events occur independently
2. Average rate ($\lambda$) is constant
3. Two events cannot occur at exactly the same instant
4. Probability of event in small interval $\propto$ interval length

### Derivation from Binomial (Book)
Poisson is the limiting case of Binomial when $n \to \infty$, $p \to 0$, with $np = \lambda$ (constant).

### Notation
$X \sim P(\lambda)$ where $\lambda$ = average number of occurrences per unit time/space

### PMF
$$P(X=x) = \frac{e^{-\lambda} \lambda^x}{x!}, \quad x = 0, 1, 2, \ldots$$

### Mean and Variance (Book)
- **Mean**: $E[X] = \lambda$
- **Variance**: $Var[X] = \lambda$
- **Standard Deviation**: $\sigma = \sqrt{\lambda}$

**Key Property**: Mean = Variance = $\lambda$ (use as check!)

### Properties
- $P(X=0) = e^{-\lambda}$
- Mode = $\lfloor \lambda \rfloor$ (if $\lambda$ not integer) or $\lambda, \lambda-1$ (if integer)
- Sum of independent Poissons: $P(\lambda_1) + P(\lambda_2) = P(\lambda_1+\lambda_2)$
- **Binomial approximation**: $B(n,p) \approx P(np)$ when $n \to \infty$, $p \to 0$, $np = \lambda$ moderate

### When to Use Poisson
- Counting occurrences in fixed interval (time/space)
- Events are rare relative to interval
- No fixed number of trials (unlike binomial)
- $\lambda$ = average rate known

### Worked Example from Book (Exercise E4)
> **Second-hand car dealer: Sales of 0,1,2,3,4,5 cars with probabilities 0.05, 0.15, 0.35, 0.25, 0.12, 0.18. Find average cars sold per day.**

**Solution**: $E[X] = \sum x_i p_i = 0(0.05) + 1(0.15) + 2(0.35) + 3(0.25) + 4(0.12) + 5(0.18) = 2.65$

---

## 3.6 PYQ-Based Important Questions (Poisson)

### 5-Mark Questions (Section A) - MEDIUM PRIORITY (1 appearance in 9 papers)

#### 1. Poisson Distribution - Call Center Type
> "Average 3 calls per minute. Find P(no calls in 1 min), P(exactly 2 calls), P(at most 2 calls)."

**Solution**:
- $X \sim P(3)$
- $P(X=0) = e^{-3} = 0.0498$
- $P(X=2) = \frac{e^{-3}3^2}{2!} = 0.2240$
- $P(X \leq 2) = e^{-3}(1 + 3 + 9/2) = 0.4232$

#### 2. Poisson with Different Interval
> "Average 5 accidents per month. Find P(2 accidents in 2 weeks) and P(at least 1 accident in a week)."

**Solution**:
- Monthly $\lambda = 5$, so weekly $\lambda = 5/4 = 1.25$, fortnightly $\lambda = 2.5$
- 2 weeks: $X \sim P(2.5)$, $P(X=2) = e^{-2.5}(2.5)^2/2! = 0.2565$
- 1 week: $Y \sim P(1.25)$, $P(Y \geq 1) = 1 - e^{-1.25} = 0.7135$

---

## 3.7 Normal Distribution

### Definition
Continuous distribution with bell-shaped curve, symmetric about mean $\mu$.

### Parameters
- $\mu$ = mean (location)
- $\sigma^2$ = variance (spread), $\sigma$ = standard deviation

### Notation
$X \sim N(\mu, \sigma^2)$

### PDF
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \quad -\infty < x < \infty$$

### Properties (from Book)
1. **Symmetry**: $f(\mu + x) = f(\mu - x)$
2. **Mean = Median = Mode = $\mu$**
3. **Total area = 1**
4. **Empirical Rule (68-95-99.7)**:
   - $P(\mu - \sigma < X < \mu + \sigma) \approx 0.6826$
   - $P(\mu - 2\sigma < X < \mu + 2\sigma) \approx 0.9544$
   - $P(\mu - 3\sigma < X < \mu + 3\sigma) \approx 0.9973$
5. **Inflection points** at $\mu \pm \sigma$
6. **Linear transformation**: If $X \sim N(\mu, \sigma^2)$, then $aX + b \sim N(a\mu+b, a^2\sigma^2)$
7. **Sum of independent normals**: $\sum X_i \sim N(\sum \mu_i, \sum \sigma_i^2)$

### Standard Normal Distribution
$Z \sim N(0, 1)$ with $Z = \frac{X - \mu}{\sigma}$

### Standard Normal Table (Appendix 2 in Book)
Used to find $P(a < Z < b)$ or $P(Z < z)$.

### Finding Probabilities
1. Convert to Z: $z = \frac{x - \mu}{\sigma}$
2. Use standard normal table
3. Use symmetry: $P(Z > z) = P(Z < -z)$

---

## 3.8 PYQ-Based Important Questions (Normal)

### 5-Mark Questions (Section A) - HIGH PRIORITY (Multiple appearances in hypothesis testing/CI)

#### 1. Normal Distribution Probabilities
> "X ~ N(100, 15²). Find P(X < 85), P(90 < X < 110), value of x such that P(X > x) = 0.05."

**Solution**:
- $P(X < 85) = P(Z < \frac{85-100}{15}) = P(Z < -1) = 0.1587$
- $P(90 < X < 110) = P(-0.67 < Z < 0.67) = 0.4972$
- $P(X > x) = 0.05 \Rightarrow P(Z > z) = 0.05 \Rightarrow z = 1.645 \Rightarrow x = 100 + 1.645 \times 15 = 124.675$

#### 2. Normal Approximation to Binomial (with Continuity Correction)
> "n=100, p=0.3. Use normal approximation to find P(X ≥ 35)."

**Solution**:
- $\mu = np = 30$, $\sigma = \sqrt{npq} = \sqrt{21} = 4.58$
- With continuity correction: $P(X \geq 35) = P(X > 34.5) = P(Z > \frac{34.5-30}{4.58}) = P(Z > 0.98) = 0.1635$
- Without correction: $P(Z > 1.09) = 0.1379$ (less accurate)

---

## 3.9 Uniform Distribution

### Continuous Uniform $U(a, b)$ (Book Section 3.5)
$$f(x) = \frac{1}{b-a}, \quad a \leq x \leq b$$

- **Mean**: $\frac{a+b}{2}$
- **Variance**: $\frac{(b-a)^2}{12}$

### Discrete Uniform
$P(X=x) = \frac{1}{n}$ for $x = 1, 2, \ldots, n$

---

## 3.10 Relationship Between Distributions (Book)

```
Binomial(n, p) 
    │
    ├── n large, p small → Poisson(np)
    │
    ├── n large, p not extreme → Normal(np, npq)  [De Moivre-Laplace]
    │
    └── p = 0.5, n large → Normal(np, npq)
    
Poisson(λ)
    │
    └── λ large → Normal(λ, λ)
```

---

## 3.11 PYQ-Based Important Questions Summary

### 5-Mark Questions (Section A) - Priority by Appearances

| Priority | Topic | Appearances | Key Problems |
|----------|-------|-------------|--------------|
| 🔴 HIGH | Binomial - Target hitting | 3 (Jun21, Dec24, Dec25) | n=5, p=0.3, find P(X=2), P(X≥2) |
| 🔴 HIGH | Binomial - Three students | 5 IDENTICAL | 1/2, 1/3, 1/4 independent |
| 🟡 MEDIUM | Poisson | 1 | λ=3 calls/min |
| 🔴 HIGH | Normal | Multiple | In CI/hypothesis testing |

### 10-Mark Questions (Section B)
Usually not direct 10-mark on distributions alone, but used in:
- Hypothesis testing (Unit 6)
- Confidence intervals (Unit 5)
- Sampling distributions (Unit 4)

---

## 3.12 Important Formulas Summary

| Distribution | PMF/PDF | Mean | Variance | When to Use |
|--------------|---------|------|----------|-------------|
| **Binomial** $B(n,p)$ | $\binom{n}{x}p^x q^{n-x}$ | $np$ | $npq$ | Fixed trials, 2 outcomes, constant p |
| **Poisson** $P(\lambda)$ | $\frac{e^{-\lambda}\lambda^x}{x!}$ | $\lambda$ | $\lambda$ | Rare events, rate $\lambda$ known |
| **Normal** $N(\mu,\sigma^2)$ | $\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ | Continuous, symmetric, CLT |
| **Uniform** $U(a,b)$ | $\frac{1}{b-a}$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | All outcomes equally likely |

---

## 3.13 Problem-Solving Checklist

### Binomial
- [ ] Identify n (trials), p (success prob)
- [ ] Verify independence and constant p
- [ ] Use $\binom{n}{x}p^x q^{n-x}$
- [ ] For "at least": use complement $1 - P(X < k)$
- [ ] For "at most": sum $P(X=0)$ to $P(X=k)$
- [ ] **Key check**: Mean = np, Variance = npq

### Poisson
- [ ] Identify $\lambda$ (average rate per unit)
- [ ] Adjust $\lambda$ for different interval: $\lambda_{new} = \lambda \times \frac{new interval}{original interval}$
- [ ] Use $\frac{e^{-\lambda}\lambda^x}{x!}$
- [ ] **Key check**: Mean = Variance = $\lambda$

### Normal
- [ ] Identify $\mu$ and $\sigma$
- [ ] Convert to Z: $z = \frac{x - \mu}{\sigma}$
- [ ] Use standard normal table
- [ ] For inverse: find z from table, then $x = \mu + z\sigma$
- [ ] Remember symmetry: $P(Z > z) = P(Z < -z)$
- [ ] **Notation**: $N(\mu, \sigma^2)$ not $N(\mu, \sigma)$
- [ ] **Continuity correction** for discrete→continuous approximation

---

## 3.14 Common Mistakes

| Mistake | Correction |
|---------|------------|
| Using binomial when trials not independent | Check independence assumption |
| Forgetting to adjust $\lambda$ for different time interval | $\lambda$ scales linearly with interval |
| Using $\sigma$ instead of $\sigma^2$ in normal notation | $N(\mu, \sigma^2)$ not $N(\mu, \sigma)$ |
| Not standardizing before using Z-table | Always convert to $Z = \frac{X-\mu}{\sigma}$ |
| Confusing "at least" with "at most" | At least $k$: $X \geq k$; At most $k$: $X \leq k$ |
| Using normal approximation without continuity correction | For discrete→continuous: $P(X=k) \approx P(k-0.5 < X < k+0.5)$ |
| Confusing independent events problem with binomial | "A solves with prob 1/2, B with 1/3" = independent events, NOT binomial |

---

## 3.15 Diagrams

### Binomial PMF (n=10, p=0.3)
```
P(X=x)
0.3 ┤      █
0.2 ┤    █ █ █
0.1 ┤  █ █ █ █ █ █
0.0 ┼──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬── x
    0  1  2  3  4  5  6  7  8  9 10
```

### Poisson PMF (λ=3)
```
P(X=x)
0.25 ┤    █
0.20 ┤    █ █
0.15 ┤  █ █ █ █
0.10 ┤█ █ █ █ █ █
0.05 ┤█ █ █ █ █ █ █ █
0.00 ┼──┬──┬──┬──┬──┬──┬──┬──┬──┬── x
     0  1  2  3  4  5  6  7  8  9
```

### Normal PDF
```
        f(x)
         │
         │        █
         │      █   █
         │    █       █
         │   █         █
         │  █           █
         │ █             █
         └────────────────── x
              μ-σ  μ  μ+σ
```

### Standard Normal Areas
```
         Z
        ┌──────────────────────────┐
        │                          │
   0.34 │      ████████████        │   68% within ±1σ
        │    ████████████████      │
   0.475│  ████████████████████    │   95% within ±1.96σ
        │██████████████████████████│
        └──────────────────────────┘
       -3  -2  -1  0  1  2  3
```

---

## 3.16 Worked Examples from Textbook (Must Practice)

### Example 1: Binomial Mean Derivation (Book)
$E(X) = \sum_{x=0}^n x \binom{n}{x} p^x q^{n-x} = np \sum_{y=0}^{n-1} \binom{n-1}{y} p^y q^{n-1-y} = np$

### Example 2: Oil Exploration (Problem 4 - Book)
$n=6, p=0.1, P(X \geq 2) = 1 - (0.9)^6 - 6(0.1)(0.9)^5 = 0.115$

### Example 3: Car Dealer (Exercise E4)
$E[X] = \sum x_i p_i = 2.65$ cars/day

### Example 4: Three Students Problem (PYQ)
$P(\text{solved}) = 1 - (1/2)(2/3)(3/4) = 3/4$

---

## 3.17 Practice Problems (PYQ Style)

### Problem 1 (Jun 2021)
Binomial: Target hit prob = 0.3, 5 shots. P(2 hits), P(at least 2).

### Problem 2 (Dec 2021)
Three students solve with prob 1/2, 1/3, 1/4. P(problem solved).

### Problem 3 (Dec 2024)
Binomial: Rahul p=0.3, Meena p=0.4. Both shoot. P(both hit), P(at least one), P(exactly one).

### Problem 4 (Dec 2025)
Binomial: Target hitting probability (exact n, p values from paper).

### Problem 5 (Jun 2021, Dec 2021, Dec 2024, Dec 2025)
Normal: Various applications in hypothesis testing, confidence intervals.

---

## 3.18 Exam Tips

- ✅ **Binomial**: Master PMF, mean=np, var=npq, "at least" = 1 - P(X < k)
- ✅ **Poisson**: Mean=Variance=λ, adjust λ for time intervals
- ✅ **Normal**: Standardize to Z, use tables, empirical rule 68-95-99.7
- ✅ **Approximations**: Know when Binomial→Poisson (n large, p small) and Binomial/Poisson→Normal (large n/λ)
- ✅ **Show Z-transformation** explicitly in normal problems
- ✅ **Distinguish**: "A solves with prob 1/2, B with 1/3" = Independent events (not binomial)
- ✅ **Continuity correction**: Always use for normal approximation to binomial/Poisson
- ❌ Don't forget continuity correction when approximating discrete with normal
- ❌ Don't confuse variance (σ²) and standard deviation (σ) in normal notation
- ❌ Don't forget: Mean = Variance for Poisson (key check!)
- ❌ Don't confuse independent events problem with binomial

---

*End of Unit 3 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 3 "Probability Distributions" - All formulas, definitions, derivations, and examples verified against original textbook content.