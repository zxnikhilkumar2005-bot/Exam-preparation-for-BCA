# Unit 4: Sampling Distributions

**Block 1: Descriptive Statistics & Probability**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 4 - Sampling Distributions (IGNOU BCS-040)

---

## 4.1 Introduction

**Statistical Inference**: Using sample data to make conclusions about population parameters.

### Key Concepts (from Book)
| Term | Definition |
|------|------------|
| **Parameter** | Numerical characteristic of population (μ, σ, p) |
| **Statistic** | Numerical characteristic of sample (x̄, s, p̂) |
| **Sampling Distribution** | A list of all possible values for a sample statistic and the probability associated with each value |
| **Standard Error (SE)** | Standard deviation of the sampling distribution (measures sampling error) |
| **Sampling Error** | Difference between population parameter and sample statistic used to estimate it |

### Why Sampling Distributions Matter
- Sample statistics vary from sample to sample (sampling variability)
- Need to understand this variation to make valid inferences
- Foundation for confidence intervals and hypothesis testing

---

## 4.2 Sampling Distribution of Sample Mean

### Construction of Sampling Distribution (Book Method)
1. List all possible samples of size n from population of size N
2. Number of possible samples = $\binom{N}{n}$ (without replacement) or $N^n$ (with replacement)
3. Calculate sample mean for each sample
4. Each sample is equally likely: probability = $1/k$ where k = number of samples
5. Tabulate sample means with their probabilities → **Sampling Distribution of Mean**

### Key Results from Book (Theorem 1)
> **If a random sample of size n is taken from a population having mean μ and variance σ², then X̄ = the sample mean is a random variable whose distribution has mean μ.**
> - **Infinite population / SRSWR**: Variance = $\sigma^2/n$
> - **Finite population / SRSWOR**: Variance = $\frac{\sigma^2}{n} \cdot \frac{N-n}{N-1}$

### Grand Mean = Population Mean (Book Example)
**Example from Book**: 4 families with incomes 100, 200, 300, 400 (thousand Rs.)
- Population mean μ = 250
- All possible samples of size 2 (without replacement): 6 samples
- Sample means: 150, 200, 250, 250, 300, 350
- **Grand mean (mean of sample means)** = 250 = Population mean!

**Example 2 (Problem 1)**: Student scores 70, 75, 65, 80, 95 on 5 tests
- Population mean μ = 77
- All samples of size 3: 10 samples
- Mean of sample means = 77 = Population mean!

> **Key Result**: $E(\bar{X}) = \mu$ (Sample mean is an unbiased estimator of population mean)

### Proof: $E(\bar{X}) = \mu$
$$E(\bar{X}) = E\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{1}{n}\sum_{i=1}^n E(X_i) = \frac{1}{n} \cdot n\mu = \mu$$

---

## 4.3 Standard Error of the Mean

### Definition (Book)
> The standard error is the standard deviation of the sample means around the population mean and is denoted by SE(X̄).

### Formulas

#### SRS With Replacement (SRSWR) / Infinite Population
$$SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}$$

#### SRS Without Replacement (SRSWOR) / Finite Population
$$SE(\bar{X}) = \frac{\sigma}{\sqrt{n}} \sqrt{\frac{N-n}{N-1}}$$

Where $\sqrt{\frac{N-n}{N-1}}$ is the **Finite Population Correction (FPC) factor**.

### When to Ignore FPC (Book Rule of Thumb)
> When $\frac{n}{N} < 0.1$, the correction factor can be ignored.
> Use SRSWR formula when N is large relative to n.

### Worked Examples from Book

#### Example: Birth Rates (Problem 3)
- N = 100 cities, σ = 12 births per 100,000
- **n = 8**: n/N = 0.08 < 0.1 → Use SRSWR: $SE = 12/\sqrt{8} = 4.24$
- **n = 15**: n/N = 0.15 > 0.1 → Use SRSWOR: $SE = \frac{12}{\sqrt{15}} \sqrt{\frac{100-15}{100-1}} = 2.87$
- **Observation**: Larger sample → smaller standard error → less sampling error

#### Exercise E6
> From population of 200, sample n=50 selected. σ = 22. Find SE.
> $SE = \frac{22}{\sqrt{50}} \sqrt{\frac{200-50}{200-1}} = 2.61$

---

## 4.4 Central Limit Theorem (CLT)

### Statement (Book Theorem 2)
> Let $X_1, X_2, \ldots, X_n$ be n independent and identically distributed random variables having mean μ and variance σ². Let $\bar{X} = \frac{1}{n}\sum X_i$. Then $\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}$ has approximately the standard normal distribution N(0, 1).

### Implications
- For large sample size (n ≥ 30), sampling distribution of $\bar{X}$ is approximately normal regardless of population distribution
- If population is normal, $\bar{X}$ is exactly normal for any n
- Basis for Z-tests and confidence intervals
- Book Appendix 1 shows: even for non-normal populations (uniform, skewed), sampling distribution becomes normal as n increases

### Standardized Form
$$Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1) \text{ approximately for large } n$$

---

## 4.5 Sampling Distribution of Sample Proportion

### Population Proportion
$p$ = proportion of population with attribute = $\frac{k}{N}$ where k = number with attribute

### Sample Proportion
$\hat{p} = \frac{s}{n}$ where s = number with attribute in sample

### Properties (from Book)
- **Mean of sampling distribution of p** = Population proportion p
- **Standard Error of p**:
  - **Finite population (SRSWOR)**: $SE(\hat{p}) = \sqrt{\frac{p(1-p)}{n}} \sqrt{\frac{N-n}{N-1}}$
  - **Infinite population (SRSWR)**: $SE(\hat{p}) = \sqrt{\frac{p(1-p)}{n}}$

### Worked Example from Book (Example 3)
> Milk packets: 50 packets in 5 cartons. Proportion defective (qty < 495ml) = 20/50 = 0.4
> Sample 2 cartons (20 packets): all possible samples and their defective proportions calculated
> **Mean of sample proportions** = 0.4 = Population proportion!

### Exercise E7
> (a) 250 bulbs/day, sample 50: 4 defective → $SE = \sqrt{\frac{0.08 \times 0.92}{50}} \sqrt{\frac{250-50}{250-1}} = 0.037$
> (b) Continuous process, sample 60: 7 defective → $p = 7/60 = 0.1167$, $SE = \sqrt{\frac{0.1167 \times 0.8833}{60}} = 0.041$

---

## 4.6 t-Distribution (Student's t)

### When to Use (Book)
- Population normal
- Sample size small (n < 30)
- Population variance σ² **unknown**
- Use sample standard deviation s

### Definition (Book)
> Suppose we take a sample from a population having normal distribution N(μ, σ²), where μ and σ² are unknown. If X₁, X₂, ..., Xₙ are n observations in the sample, then $\frac{\bar{X} - \mu}{S/\sqrt{n}}$ has t-distribution with parameter ν = n - 1, where s is the sample standard deviation.

### Formula
$$t = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t_{n-1}$$

Where $S^2 = \frac{1}{n-1}\sum (X_i - \bar{X})^2$

### Properties (from Book)
- Symmetric, bell-shaped like normal
- Heavier tails than normal (more spread)
- Degrees of freedom (df) = n - 1
- As df → ∞, t → N(0,1)
- Mean = 0 (for df > 1)
- Variance = df/(df-2) for df > 2
- For df ≥ 30, t-values ≈ standard normal Z-values

### t-Table (Book Appendix Table 2)
- Left column: degrees of freedom (v)
- Column headings: areas α in right-hand tail
- Entries: values of $t_\alpha$
- **Symmetry**: $t_{1-\alpha} = -t_\alpha$ (left-tail values)

### Worked Examples from Book

#### Example 3: t-Table Usage (df = 9)
| Condition | α | t-value |
|-----------|---|---------|
| Right tail = 0.05 | 0.05 | 1.833 |
| Total two-tail = 0.05 | 0.025 each | 2.262 |
| Total unshaded = 0.99 | 0.005 each | 3.250 |
| Left tail = 0.01 | 0.01 | 2.821 |

#### Example 4: Fuse Manufacturer Claim (Problem 4)
> Claim: μ = 12.40 minutes. Sample n=20, x̄=10.63, s=2.48. Test claim.
> $t = \frac{10.63 - 12.40}{2.48/\sqrt{20}} = -3.19$
> df = 19, $t_{0.005} = 2.861$
> Since -3.19 < -2.861, α < 0.005 (very small)
> **Conclusion**: Data refute manufacturer's claim

#### Exercise E9
> Process mean = 0.5 cm. Sample n=10, x̄=0.5060, s=0.0040. Assume normal.
> $t = \frac{0.5060 - 0.5}{0.0040/\sqrt{10}} = 4.74$
> df = 9, $t_{0.005} = 3.250$
> Since 4.74 > 3.250, process is out of control

#### Exercise E10
> t-values for right-tail α = 0.05:
> (a) df=16: 1.746
> (b) df=27: 1.703
> (c) df=200: ≈ 1.645 (Z-value)

---

## 4.7 Chi-Square Distribution ($\chi^2$)

### Definition (Book)
> A random variable Y has $\chi^2$ (chi-square) distribution with ν degrees of freedom if its density function is:
> $$f(y) = \frac{1}{2^{\nu/2}\Gamma(\nu/2)} y^{\nu/2-1} e^{-y/2}, \quad y > 0$$

### Distribution of Sample Variance (Key Result)
> If $X_1, \ldots, X_n$ i.i.d. $N(\mu, \sigma^2)$, then $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$

### Properties (from Book)
- Skewed right (positive skew)
- df = n - 1 (for sample variance)
- Mean = df, Variance = 2df
- As df → ∞, approaches normal
- Additive: $\chi^2_{df_1} + \chi^2_{df_2} = \chi^2_{df_1+df_2}$

### Applications
- Testing hypothesis about population variance
- Goodness-of-fit tests (Unit 7)
- Test of independence (Unit 7)

---

## 4.8 F-Distribution

### Definition (Book)
> If $U \sim \chi^2_{df_1}$, $V \sim \chi^2_{df_2}$ independent, then $F = \frac{U/df_1}{V/df_2} \sim F_{df_1, df_2}$

### Distribution of Variance Ratio
> If $S_1^2$, $S_2^2$ are sample variances from independent normal populations:
> $$\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim F_{n_1-1, n_2-1}$$
> Under $H_0: \sigma_1^2 = \sigma_2^2$: $\frac{S_1^2}{S_2^2} \sim F_{n_1-1, n_2-1}$

### Properties
- Positive skew
- Two parameters: df₁ (numerator), df₂ (denominator)
- Reciprocal property: $F_{df_1, df_2} = 1/F_{df_2, df_1}$
- Mean = df₂/(df₂-2) for df₂ > 2

### Applications
- Testing equality of two variances (Unit 6)
- ANOVA (Unit 8)

---

## 4.9 Summary of Sampling Distributions

| Situation | Statistic | Distribution | Parameters |
|-----------|-----------|--------------|------------|
| σ known, pop normal or n≥30 | $\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}$ | Z ~ N(0,1) | - |
| σ unknown, pop normal, n<30 | $\frac{\bar{X}-\mu}{S/\sqrt{n}}$ | t | df = n-1 |
| σ² unknown, pop normal | $\frac{(n-1)S^2}{\sigma^2}$ | $\chi^2$ | df = n-1 |
| Two normal pops, compare variances | $\frac{S_1^2}{S_2^2}$ | F | df₁=n₁-1, df₂=n₂-1 |
| Large n, proportion | $\frac{\hat{p}-p}{\sqrt{p(1-p)/n}}$ | Z ~ N(0,1) | - |

---

## 4.10 Standard Error Formulas (Quick Reference)

| Parameter | SRSWR / Infinite | SRSWOR / Finite |
|-----------|------------------|-----------------|
| **Mean (σ known)** | $\frac{\sigma}{\sqrt{n}}$ | $\frac{\sigma}{\sqrt{n}}\sqrt{\frac{N-n}{N-1}}$ |
| **Mean (σ unknown)** | $\frac{s}{\sqrt{n}}$ | $\frac{s}{\sqrt{n}}\sqrt{\frac{N-n}{N-1}}$ |
| **Proportion** | $\sqrt{\frac{p(1-p)}{n}}$ | $\sqrt{\frac{p(1-p)}{n}}\sqrt{\frac{N-n}{N-1}}$ |
| **Total** | $N\frac{\sigma}{\sqrt{n}}$ | $N\frac{\sigma}{\sqrt{n}}\sqrt{\frac{N-n}{N-1}}$ |

---

## 4.11 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - HIGH PRIORITY (6 appearances in 9 papers)

#### 1. Standard Error Calculation ⭐⭐⭐⭐
> "Sample of 100 from population with σ=15. Find SE of mean. If population size N=500, find SE with FPC."

**Solution**:
- SRSWR: $SE = 15/\sqrt{100} = 1.5$
- SRSWOR: $SE = 1.5 \times \sqrt{(500-100)/(500-1)} = 1.5 \times 0.895 = 1.34$

#### 2. Sampling Distribution of Mean ⭐⭐⭐
> "Population mean=50, σ=10. Sample n=25. Find P(48 < x̄ < 52)."

**Solution**:
- $SE = 10/\sqrt{25} = 2$
- $Z_1 = (48-50)/2 = -1$, $Z_2 = (52-50)/2 = 1$
- $P(-1 < Z < 1) = 0.6826$

#### 3. Confidence Limits / Standard Error ⭐⭐⭐
> "Sample mean=550, σ=40, n=16. Find 95% confidence interval."

**Solution**:
- $SE = 40/\sqrt{16} = 10$
- $CI = 550 \pm 1.96 \times 10 = (530.4, 569.6)$

#### 4. Difference Between Sampling Methods ⭐⭐
> "Distinguish between SRS and Systematic Sampling" or "Linear vs Circular Systematic Sampling"

**Key Points from Book**:
- **SRS**: Each sample equally likely, independent selection
- **Systematic**: Fixed interval k=N/n, random start
- **Linear**: Stop at end of list
- **Circular**: Wrap around modulo N

---

## 4.12 Problem-Solving Checklist

### Standard Error Problems
- [ ] Identify: σ known/unknown, SRSWR/SRSWOR, finite/infinite population
- [ ] Apply correct SE formula
- [ ] Use FPC when sampling without replacement from finite population
- [ ] Check if n/N > 0.05 (FPC matters) or n/N < 0.1 (FPC can be ignored)

### Sampling Distribution Problems
- [ ] Identify parameter (μ, p, σ²)
- [ ] Determine sample size n
- [ ] Check normality: pop normal or n ≥ 30 (CLT)
- [ ] Choose correct distribution (Z, t, χ², F)
- [ ] Compute test statistic/standard error
- [ ] Use appropriate table

### t, χ², F Distribution Problems
- [ ] Identify degrees of freedom correctly
- [ ] t: df = n-1
- [ ] χ²: df = n-1 (for variance)
- [ ] F: df₁ = n₁-1, df₂ = n₂-1
- [ ] Use correct table (one-tailed vs two-tailed)
- [ ] For t: if df ≥ 30, use Z-values

---

## 4.13 Common Mistakes

| Mistake | Correction |
|---------|------------|
| Using Z when σ unknown and n < 30 | Use t-distribution |
| Forgetting FPC in SRSWOR | Multiply by √((N-n)/(N-1)) |
| Using σ instead of s in t-statistic | t uses sample SD s |
| Wrong df for χ²/F | χ²: n-1; F: n₁-1, n₂-1 |
| Confusing one-tailed and two-tailed critical values | Check α vs α/2 |
| Not checking CLT conditions | n ≥ 30 or pop normal |
| Not knowing t ≈ Z for df ≥ 30 | Bottom row of t-table = Z-values |

---

## 4.14 Diagrams

### Sampling Distribution of x̄
```
        f(x̄)
         │
         │        █
         │      █   █
μ-2σ/√n  │    █       █  μ  μ+2σ/√n
μ-σ/√n   │   █         █
         │  █           █
         └────────────────── x̄
                SE = σ/√n
```

### t vs Normal Distribution
```
Density
    │
    │    Normal (thinner tails)
    │   / \
    │  /   \     t (heavier tails)
    │ /     \   / \
    │/       \_/   \
    └─────────────────
```

### χ² Distribution (df=1, 5, 10)
```
Density
    │  df=1 (J-shaped)
    │  █
    │  █
    │  █
    │   █ df=5
    │    █  █
    │     ██  █ df=10
    └─────────────────
```

### F Distribution
```
Density
    │
    │     █
    │    █ █
    │   █   █
    │  █     █
    └─────────────────
```

---

## 4.15 Key Proofs to Know

### 1. $E(\bar{X}) = \mu$ (Unbiasedness of sample mean)
$$E(\bar{X}) = E\left(\frac{1}{n}\sum X_i\right) = \frac{1}{n}\sum E(X_i) = \frac{1}{n} \cdot n\mu = \mu$$

### 2. $Var(\bar{X}) = \sigma^2/n$ (SRSWR)
$$Var(\bar{X}) = Var\left(\frac{1}{n}\sum X_i\right) = \frac{1}{n^2}\sum Var(X_i) = \frac{1}{n^2} \cdot n\sigma^2 = \frac{\sigma^2}{n}$$

### 3. SST = SSB + SSW (ANOVA Identity) - *Unit 8*

---

## 4.16 Worked Examples from Textbook (Must Practice)

### Example 1: Income Problem (Book Section 4.3)
- 4 families: incomes 100, 200, 300, 400
- μ = 250
- All samples n=2: 6 samples, means: 150, 200, 250, 250, 300, 350
- Grand mean = 250 = μ

### Example 2: Student Test Scores (Book Problem 1)
- 5 tests: 70, 75, 65, 80, 95
- μ = 77
- All samples n=3: 10 samples
- Mean of sample means = 77 = μ

### Example 3: Birth Rates (Book Problem 3)
- N=100, σ=12
- n=8: SE = 4.24; n=15: SE = 2.87
- Larger sample → smaller SE

### Example 4: Milk Packets Proportion (Book Example 3)
- 50 packets, 20 defective → p = 0.4
- Sample 2 cartons (20 packets)
- Mean of sample proportions = 0.4 = p

### Example 5: Fuse Manufacturer (Book Problem 4)
- Claim: μ = 12.40, n=20, x̄=10.63, s=2.48
- t = -3.19, df=19, t_{0.005} = 2.861
- Reject claim (p < 0.005)

---

## 4.17 Exam Tips

- ✅ **Standard Error formulas** - memorize all 4 cases (σ known/unknown × SRSWR/SRSWOR)
- ✅ **FPC** - know when to apply (finite population, without replacement, n/N ≥ 0.05)
- ✅ **FPC ignore rule** - n/N < 0.1 can ignore FPC
- ✅ **CLT** - n ≥ 30 → normal approximation
- ✅ **t, χ², F distributions** - know df and when each is used
- ✅ **Sampling distribution of mean = population mean** proof
- ✅ **Difference between SRS and Systematic** - common short question
- ✅ **t-table**: bottom row = Z-values for df ≥ 30
- ✅ **Mean of sample proportions = population proportion** proof
- ❌ Don't use Z when σ unknown and n < 30
- ❌ Don't forget FPC in SRSWOR
- ❌ Don't confuse df for t (n-1) vs χ² (n-1) vs F (n₁-1, n₂-1)

---

*End of Unit 4 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 4 "Sampling Distributions" - All formulas, definitions, theorems, examples, and exercises verified against original textbook content.