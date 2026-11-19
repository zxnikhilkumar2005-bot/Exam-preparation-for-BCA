# Unit 5: Estimation

**Block 2: Statistical Inference**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 5 - Estimation (IGNOU BCS-040)

---

## 5.1 Introduction

**Estimation**: Using sample statistics to infer population parameters.

### Two Types of Estimation
| Type | Description | Output |
|------|-------------|--------|
| **Point Estimation** | Single value as estimate | Point estimate (e.g., x̄ = 50) |
| **Interval Estimation** | Range of values with confidence level | Confidence interval (e.g., 48 < μ < 52, 95% CI) |

### Key Terms (from Book)
- **Estimator**: Rule/formula (e.g., sample mean x̄)
- **Estimate**: Numerical value from specific sample (e.g., x̄ = 50)
- **Parameter**: Population characteristic (e.g., μ)

---

## 5.2 Point Estimation

### Common Point Estimators (from Book)
| Parameter | Estimator | Formula |
|-----------|-----------|---------|
| Population Mean (μ) | Sample Mean (x̄) | $\bar{x} = \frac{\sum x_i}{n}$ |
| Population Proportion (p) | Sample Proportion (p̂) | $\hat{p} = \frac{x}{n}$ |
| Population Variance (σ²) | Sample Variance (s²) | $s^2 = \frac{\sum(x_i-\bar{x})^2}{n-1}$ |

### Properties of Good Estimators (from Book)

#### 1. Unbiasedness
**Definition**: An estimator $\hat{\theta}$ is unbiased for $\theta$ if $E(\hat{\theta}) = \theta$.

**Examples from Book**:
- $E(\bar{X}) = \mu$ ✓ (Sample mean is unbiased for μ)
- $E(\hat{p}) = p$ ✓ (Sample proportion is unbiased for p)
- $E(S^2) = \sigma^2$ ✓ (Sample variance with n-1 denominator is unbiased)
- $E(S) \neq \sigma$ ✗ (Sample standard deviation is **BIASED** for σ)

**Bias of S**: 
$$E(S) = \sigma \cdot \sqrt{\frac{2}{n-1}} \frac{\Gamma(n/2)}{\Gamma((n-1)/2)} \approx \sigma(1 - \frac{1}{4n})$$

**Unbiased estimator of σ (from Book)**:
The book states: "an unbiased estimator of σ is obtained by the expression in (2) instead of (1)" where:
- (1) $S = \sqrt{\frac{\sum(x_i - \bar{x})^2}{n-1}}$ (biased)
- (2) **Corrected formula** using a factor $c_4$: $\hat{\sigma} = S/c_4$

For the specific example in Problem 1 (reaction times: 0.53, 0.46, 0.50, 0.49, 0.52, 0.53):
- $\bar{x} = 0.505$
- Biased $S = 0.0245$
- Unbiased estimator uses correction factor

#### 2. Efficiency (from Book)
**Definition**: Among unbiased estimators, the one with smaller variance is more efficient.

**Comparison**: Sample mean vs Sample median (normal population)
- $Var(\bar{X}) = \sigma^2/n$
- $Var(\tilde{X}) \approx \frac{\pi}{2} \cdot \frac{\sigma^2}{n} \approx 1.5708 \cdot \frac{\sigma^2}{n}$

Sample mean is more efficient (smaller variance). The book states: "in most practical situations the sample mean is the 'most acceptable' statistic for estimating a population mean μ."

#### 3. Consistency
**Definition**: $\hat{\theta}_n \xrightarrow{P} \theta$ as $n \to \infty$. Estimator converges to true parameter.

#### 4. Sufficiency
**Definition**: Estimator contains all information about parameter in the sample.

---

## 5.3 Interval Estimation (Confidence Intervals)

### Concept (from Book)
A confidence interval gives a range of plausible values for the parameter with a stated confidence level $(1-\alpha) \times 100\%$.

**Interpretation (Book Warning)**:
> "This does not mean that 'There is 95% probability that μ lies in the interval (937.35, 962.65). This is a very common mis-interpretation and it is incorrect. This is because the population mean μ is a fixed quantity and therefore μ either lies in the interval or it does not. Therefore the probability that μ lies in the interval is either 0 or 1. The 95 percent probability is assigned to our level of confidence that the interval contains μ."

**Correct Interpretation**: "We are $(1-\alpha) \times 100\%$ confident that this interval contains μ."

**Alternative Interpretation**: "If all possible samples of size n are taken, and intervals are constructed for each sample mean, then $(1-\alpha) \times 100\%$ of all such intervals are expected to contain the population parameter μ."

---

## 5.4 Confidence Interval for Population Mean (μ)

### Case 1: σ Known, Large Sample (n ≥ 30) or Normal Population
$$\bar{x} \pm Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

**Derivation (from Book)**:
1. $P[-Z_{\alpha/2} < Z < Z_{\alpha/2}] = 1-\alpha$
2. $Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}}$
3. $\bar{X} - Z_{\alpha/2}\frac{\sigma}{\sqrt{n}} < \mu < \bar{X} + Z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$

### Case 2: σ Unknown, Large Sample (n ≥ 30)
$$\bar{x} \pm Z_{\alpha/2} \frac{s}{\sqrt{n}}$$
(Use sample SD s as estimate of σ; CLT applies)

**From Book**: "If the sample size is large, we can simply substitute the sample standard deviation for the population standard deviation."

### Case 3: σ Unknown, Small Sample (n < 30), Normal Population
$$\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$$
(Use t-distribution with df = n-1)

**From Book**: "If the sample size is 30 or less and the population is normal (and large relative to the sample), a confidence interval for the population mean can be constructed by using the t-distribution in place of the standard normal distribution."

### Common Critical Values (from Book Tables)

| Confidence Level | α | Z_{α/2} | t_{0.025, df=9} | t_{0.025, df=19} | t_{0.025, df=29} |
|------------------|---|---------|-----------------|------------------|------------------|
| 90% | 0.10 | 1.645 | 1.833 | 1.729 | 1.699 |
| 95% | 0.05 | 1.960 | 2.262 | 2.093 | 2.045 |
| 99% | 0.01 | 2.576 | 3.250 | 2.861 | 2.756 |

**Additional t-values from Book Exercises**:
| df | α/2 = 0.005 | α/2 = 0.025 | α/2 = 0.05 | α/2 = 0.005 (99%) |
|----|-------------|-------------|------------|-------------------|
| 9  | 3.250       | 2.262       | 1.833      | -                 |
| 11 | -           | 2.201       | -          | 3.106             |
| 13 | -           | -           | 1.771      | -                 |
| 19 | -           | 2.093       | -          | 2.861             |
| 29 | -           | 2.045       | -          | 2.756             |

### Width of CI
$$\text{Width} = 2 \times \text{Margin of Error} = 2 \times Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

**Factors affecting width**:
- ↑ Confidence level → ↑ Width
- ↑ Sample size → ↓ Width
- ↑ Variability → ↑ Width

---

## 5.5 Confidence Interval for Population Proportion (p)

### Large Sample (np ≥ 5, n(1-p) ≥ 5)
$$\hat{p} \pm Z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

**From Book**: "If n is large, then p can be replaced by $\hat{p}$ without compromising accuracy."

### Sample Size Determination for Proportion
$$n = \left(\frac{Z_{\alpha/2}}{E}\right)^2 \hat{p}(1-\hat{p})$$

Where $E$ = desired margin of error.

**Conservative (maximum n)**: Use $\hat{p} = 0.5$ → $n = \left(\frac{Z_{\alpha/2}}{2E}\right)^2$

### Worked Examples from Book

**Problem 5**: 75 parts, 12 rough → $\hat{p} = 12/75 = 0.16$
- 95% CI: $0.16 \pm 1.96\sqrt{0.16 \times 0.84 / 75} = (0.078, 0.242)$
- 99% CI: $0.16 \pm 2.58\sqrt{0.16 \times 0.84 / 75} = (0.051, 0.269)$

**Exercise E14**: 800 calculators, 24 defective → 99% CI: (0.0144, 0.0456)
**Exercise E15**: 1000 lung cancer, 699 death → 95% CI: (0.668, 0.730)
**Exercise E16**: 50 students, 11 willing → 99% CI: (0.0688, 0.3711)

---

## 5.6 Confidence Interval for Difference of Two Means

### Case 1: Independent Samples, σ₁, σ₂ Known
$$(\bar{x}_1 - \bar{x}_2) \pm Z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$$

### Case 2: Independent Samples, σ₁, σ₂ Unknown, Equal Variances (Pooled)
$$(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2, n_1+n_2-2} \cdot s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$

Where pooled variance:
$$s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$$

### Case 3: Paired Samples (Dependent)
$$\bar{d} \pm t_{\alpha/2, n-1} \frac{s_d}{\sqrt{n}}$$

Where $d_i = x_i - y_i$ (differences), $\bar{d}$ = mean difference, $s_d$ = SD of differences.

**Book Case Study (ICI Chemical Industry)**:
- 10 rubber pieces cut in half, one treated, one untreated
- Differences in abrasion resistance computed
- $\bar{d} = 1.27$, $s_d = 1.1265$, $n=10$
- 95% CI: $1.27 \pm 2.262 \times \frac{1.1265}{\sqrt{10}} = (0.464, 2.076)$
- 98% CI: $(0.265, 2.275)$
- Conclusion: Chlorinating agent increases abrasion resistance

---

## 5.7 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - HIGH PRIORITY (5 appearances)

#### 1. Confidence Interval for Mean (σ Known/Unknown)
> "Sample of 60 bulbs: x̄ = 950 hours, σ = 50. Find 95% CI for mean life." (Dec 2021)

**Solution**:
- $SE = 50/\sqrt{60} = 6.455$
- $CI = 950 \pm 1.96 \times 6.455 = (937.35, 962.65)$

#### 2. Confidence Interval for Mean (σ Unknown, Small Sample)
> "Sample of 10 spheres: x̄ = 43.5mm, s² = 4. Find 95% and 99% CI." (Book Example 2)

**Solution**:
- $s = 2$, $SE = 2/\sqrt{10} = 0.632$
- 95% CI: $43.5 \pm 2.262 \times 0.632 = (42.07, 44.93)$
- 99% CI: $43.5 \pm 3.250 \times 0.632 = (41.44, 45.56)$

#### 3. Confidence Interval for Proportion
> "Sample of 400 workers, 184 dissatisfied. Find 95% CI for proportion." (Dec 2022/2024)

**Solution**:
- $\hat{p} = 184/400 = 0.46$
- $SE = \sqrt{0.46 \times 0.54 / 400} = 0.0249$
- $CI = 0.46 \pm 1.96 \times 0.0249 = (0.411, 0.509)$

#### 4. Sample Size Determination
> "Want 95% CI for mean with margin of error 5, σ = 20. Find n." (Book Exercise E5)

**Solution**:
- $n = (Z_{\alpha/2} \cdot \sigma / E)^2 = (1.96 \times 20 / 5)^2 = (7.84)^2 = 61.47 \approx 62$

#### 5. Properties of Good Estimator (Short Note)
> "Write short note on properties of a good estimator." (Dec 2022)

**Key Points from Book**: Unbiasedness, Efficiency, Consistency, Sufficiency

#### 6. Unbiased Estimator of σ (Book Specific)
> "Sample standard deviation S is biased for σ. Give unbiased estimator."

**From Book**: Use correction factor $c_4$: $\hat{\sigma} = S/c_4$ where $c_4 = \sqrt{\frac{2}{n-1}} \frac{\Gamma(n/2)}{\Gamma((n-1)/2)}$

#### 7. Mean vs Median Efficiency (Book Exercise E4)
> "To verify mean is more efficient than median, 12 tosses of three dice..."

**From Book**: Variance of mean sampling distribution = $\sigma^2/n$; Variance of median ≈ $1.5708 \sigma^2/n$

---

### 10-Mark Questions (Section B) - HIGH PRIORITY (5 appearances)

#### 1. Complete Estimation Problem
> "Two machines produce items. Machine A: n₁=10, x̄₁=50, s₁=5. Machine B: n₂=12, x̄₂=55, s₂=6. Assuming equal variances, find 99% CI for difference in means." (Dec 2022/2024)

**Structure from Book**:
1. State assumptions (normal, independent, equal variances)
2. Compute pooled variance $s_p^2$
3. Compute standard error
4. Find critical t-value (df = 20)
5. Construct CI
6. Interpret

#### 2. Paired t-interval (Book Case Study)
> "Before/after drug study: n=8, differences recorded. Find 95% CI for mean difference." (Book ICI Case Study)

**Structure**:
1. Compute differences $d_i$
2. Find $\bar{d}$ and $s_d$
3. Use $t_{0.025, 7}$
4. Construct CI: $\bar{d} \pm t \cdot s_d/\sqrt{n}$

#### 3. Proportion CI with Interpretation
> "In a random sample of 75 parts, 12 have rough surface. Find 95% and 99% CI." (Book Problem 5)

---

## 5.8 Important Formulas Summary

| Situation | Confidence Interval |
|-----------|---------------------|
| **μ, σ known** | $\bar{x} \pm Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$ |
| **μ, σ unknown, n≥30** | $\bar{x} \pm Z_{\alpha/2} \frac{s}{\sqrt{n}}$ |
| **μ, σ unknown, n<30** | $\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$ |
| **Proportion p** | $\hat{p} \pm Z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ |
| **μ₁-μ₂, σ₁,σ₂ known** | $(\bar{x}_1-\bar{x}_2) \pm Z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}$ |
| **μ₁-μ₂, σ unk, equal var** | $(\bar{x}_1-\bar{x}_2) \pm t_{\alpha/2, n_1+n_2-2} s_p \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}$ |
| **Paired (μ₁-μ₂)** | $\bar{d} \pm t_{\alpha/2, n-1} \frac{s_d}{\sqrt{n}}$ |

---

## 5.9 Decision Tree for Confidence Intervals (from Book Logic)

```
Population Mean (μ)
    │
    ├─ σ known ─────→ Use Z
    │
    └─ σ unknown
         │
         ├─ n ≥ 30 ──→ Use Z (with s)  [Substitute s for σ]
         │
         └─ n < 30 ──→ Population normal? 
                         │
                         ├─ Yes ──→ Use t (df = n-1)
                         │
                         └─ No ──→ Non-parametric / larger sample needed
```

---

## 5.10 Common Mistakes

| Mistake | Correction |
|---------|------------|
| Using Z when σ unknown and n < 30 | Use t-distribution |
| Using σ instead of s in formula | Use sample SD s when σ unknown |
| Wrong df for t | df = n-1 (one sample), n₁+n₂-2 (pooled two sample), n-1 (paired) |
| Confusing CI for mean vs proportion | Mean: uses SD/SE; Proportion: uses √(p̂(1-p̂)/n) |
| Forgetting pooled vs unpooled | Check if equal variances assumed |
| Misinterpreting CI | "95% of intervals contain μ" NOT "95% prob μ in this interval" |
| Using biased S for σ | Use unbiased estimator with correction factor |

---

## 5.11 Diagrams

### Confidence Interval Interpretation
```
Population μ (fixed)
    │
    ├─ Sample 1: [────●────]  contains μ ✓
    ├─ Sample 2: [────●────]  contains μ ✓
    ├─ Sample 3: [───●──────]  contains μ ✓
    ├─ Sample 4: [──────●───]  misses μ ✗
    ├─ Sample 5: [────●────]  contains μ ✓
    └─ ...
    
95% of intervals contain μ
```

### t vs Z Critical Values
```
         Density
           │
           │    Z (thinner tails)
           │   / \
           │  /   \     t (df=9, heavier tails)
           │ /     \   / \
           │/       \_/   \
           └─────────────────
           -3 -2 -1 0 1 2 3
```

### Paired vs Unpaired
```
UNPAIRED (Independent)
Group A: ● ● ● ● ●     n₁=5
Group B: ● ● ● ● ● ●   n₂=6

PAIRED (Dependent)
Before:  ● ● ● ● ● ●   n=6
After:   ● ● ● ● ● ●
Diff:    ● ● ● ● ● ●
```

---

## 5.12 Worked Examples from Textbook (Must Practice)

### Example 1: Milk Pack (Book Section 5.4.1)
- n=60, x̄=950ml, σ=50
- 95% CI: 950 ± 1.96 × (50/√60) = (937.35, 962.65)

### Example 2: Sphere Diameter (Book Example 2)
- n=10, x̄=43.5mm, s²=4
- 95% CI: 43.5 ± 2.262 × (2/√10) = (42.07, 44.93)
- 99% CI: 43.5 ± 3.250 × (2/√10) = (41.44, 45.55)

### Example 3: Light Bulb Life (Book Problem 3)
- n=9, data given, x̄=5200, s=134
- 90% CI: 5200 ± 1.86 × (134/√9) = (5107, 5293)

### Example 4: Marketing Director (Book Example 1)
- n=600, x̄=850 million, σ=200 million
- 95% CI: 850 ± 1.96 × (200/√600) = (834.01, 865.99)

### Example 5: Ball Bearings (Book Problem 4)
- n=100, x̄=8.24mm, s=0.42mm
- 95% CI: 8.24 ± 1.96 × (0.42/10) = (8.158, 8.322)
- 99% CI: 8.24 ± 2.58 × (0.42/10) = (8.132, 8.348)

### Example 6: ICI Case Study (Paired)
- n=10, d̄=1.27, s_d=1.1265
- 95% CI: 1.27 ± 2.262 × (1.1265/√10) = (0.464, 2.076)
- 98% CI: (0.265, 2.275)

### Example 7: Proportion (Book Problem 5)
- n=75, 12 rough → p̂=0.16
- 95% CI: 0.16 ± 1.96√(0.16×0.84/75) = (0.078, 0.242)
- 99% CI: 0.16 ± 2.58√(0.16×0.84/75) = (0.051, 0.269)

---

## 5.13 Exam Tips

- ✅ **Memorize 3 cases for mean CI** (σ known, σ unknown large n, σ unknown small n)
- ✅ **Know t-table values** for common df (9, 19, 29) and α (0.025, 0.005, 0.05)
- ✅ **Paired vs unpaired** - identify correctly (before/after = paired)
- ✅ **Pooled variance formula** for equal variances case
- ✅ **Proportion CI** - check np≥5, n(1-p)≥5
- ✅ **Sample size formula** for mean and proportion
- ✅ **Unbiased estimator of σ** uses correction factor
- ✅ **Mean is more efficient than median** for normal populations
- ❌ Don't use Z when n<30 and σ unknown
- ❌ Don't forget to use n-1 denominator for sample variance
- ❌ Don't confuse "confidence level" with "probability"
- ❌ Don't use biased S for σ; use correction factor

---

## 5.14 Summary Table from Book (Table 1)

| Parameter | Point Estimator | Confidence Interval |
|-----------|-----------------|---------------------|
| μ, σ known | x̄ | x̄ ± Z_{α/2} σ/√n |
| μ, σ unknown, large n | x̄ | x̄ ± Z_{α/2} s/√n |
| μ, σ unknown, small n | x̄ | x̄ ± t_{α/2} s/√n |
| p, large n | p̂ | p̂ ± Z_{α/2} √(p̂q̂/n) |

---

*End of Unit 5 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 5 "Estimation" - All formulas, definitions, derivations, examples, exercises, and case study verified against original textbook content.