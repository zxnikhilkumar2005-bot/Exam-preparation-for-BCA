# Unit 6: Tests of Significance (Hypothesis Testing)

**Block 2: Statistical Inference**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 6 - Tests of Significance (IGNOU BCS-040)

---

## 6.1 Introduction

**Hypothesis Testing**: A procedure to decide whether a claim about a population parameter is supported by sample data.

### Key Concepts (from Book)
| Term | Definition |
|------|------------|
| **Null Hypothesis (H₀)** | Hypothesis that is being tested; presumed true unless strong evidence against it |
| **Alternative Hypothesis (H₁)** | Statement that contradicts H₀ |
| **Simple Hypothesis** | H₀ is a singleton set (e.g., μ = 2) |
| **Composite Hypothesis** | H₀ is not a singleton set |
| **Test Statistic** | Value computed from sample to test H₀ |
| **Critical Region (Rejection Region)** | Values of test statistic that lead to rejection of H₀ |
| **Acceptance Region** | Values where we do not reject H₀ |
| **Significance Level (α)** | P(Type I error) = P(Reject H₀ \| H₀ true) |

### Hypothesis Formulation Examples (from Book)
1. **Conservative Manufacturer**: H₀: μ = 15 (old process), H₁: μ = 12 (new process) - continue old unless strong evidence for new
2. **Risk-taking Manufacturer**: H₀: μ = 12 (new process), H₁: μ = 15 (old process) - switch to new unless evidence against
3. **Aluminium Rods**: H₀: μ = 2 cm, H₁: μ ≠ 2 cm (two-sided)

---

## 6.2 Types of Errors

| Decision \ Reality | H₀ True | H₀ False |
|-------------------|---------|----------|
| **Do Not Reject H₀** | Correct (1-α) | **Type II Error (β)** |
| **Reject H₀** | **Type I Error (α)** | Correct (1-β) = **Power** |

### Type I Error (α)
- Rejecting H₀ when it is true
- "False Positive"
- Controlled by choosing α (typically 0.05, 0.01)

### Type II Error (β)
- Failing to reject H₀ when it is false
- "False Negative"
- Depends on true parameter value, sample size, α

### Power of Test
$$\text{Power} = 1 - \beta = P(\text{Reject } H_0 | H_0 \text{ false})$$

**Ways to Increase Power**:
- Increase sample size (n)
- Increase α
- Decrease variability (σ)
- Larger effect size (difference from H₀)

### Choosing α vs β (Book Example)
- If Type I error costs Rs.100, Type II costs Rs.10,000 → try to eliminate Type II
- **Medicine bottle example**: 
  - H₀: It's cough medicine, H₁: It's poison
  - Type I (drink poison): Death
  - Type II (don't drink medicine): Cough lasts longer
  - **Choose Type II error** as less costly

---

## 6.3 One-Tailed vs Two-Tailed Tests (from Book)

| Test | H₀ | H₁ | Critical Region | Example Wording |
|------|-----|-----|-----------------|-----------------|
| **Two-Tailed** | μ = μ₀ | μ ≠ μ₀ | Both tails (α/2 each) | "Different from", "Not equal to", "Changed" |
| **Left-Tailed** | μ = μ₀ | μ < μ₀ | Left tail (α) | "Less than", "Decreased", "Below" |
| **Right-Tailed** | μ = μ₀ | μ > μ₀ | Right tail (α) | "Greater than", "More than", "Exceeds" |

### Book Examples:
- **Light bulb**: H₀: μ = 1500, H₁: μ < 1500 (left-tailed - customers won't complain if longer)
- **Sales expenses**: H₀: μ = 100, H₁: μ > 100 (right-tailed - concerned about high expenses)
- **Rod diameter**: H₀: μ = 2, H₁: μ ≠ 2 (two-tailed - change in either direction is bad)

---

## 6.4 Steps in Hypothesis Testing (Book Procedure)

1. **Formulate the null and alternate hypothesis**
2. **Specify the significance level of the test** (fix α)
3. **Choose a test statistic**
4. **Find the critical region** (using confidence level from Unit 5)
5. **Collect the sample and calculate the numerical value of the test statistic**
6. **Conclusion**:
   - If test statistic falls in rejection region → Reject H₀, conclude H₁ true (Type I error only 100α% of time)
   - If test statistic does not fall in rejection region → Do not reject H₀ (reserve judgement; do NOT conclude H₀ true)

---

## 6.5 Tests About Population Mean (μ)

### Test 1: Z-Test (σ Known or n ≥ 30)
$$Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} \sim N(0,1)$$

**Use when**: σ known, OR n ≥ 30 (CLT), OR normal pop with σ known

**Book Example (Problem 1)**:
> Mean marks IGNOU = 54.5, σ = 8.0. Study centre n=100, x̄=55.9. Test if significantly (1) different from (2) better than rest at α=0.01.

**Solution from Book**:
- (1) Two-tailed: H₀: μ = 54.5, H₁: μ ≠ 54.5
- Z = (55.9 - 54.5) / (8/√100) = 1.4 / 0.8 = 1.75
- Critical Z_{0.005} = 2.576
- |Z| = 1.75 < 2.576 → Do not reject H₀
- (2) Right-tailed: H₁: μ > 54.5
- Critical Z_{0.01} = 2.326
- Z = 1.75 < 2.326 → Do not reject H₀

### Test 2: t-Test (σ Unknown, n < 30, Normal Population)
$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} \sim t_{n-1}$$

**Use when**: σ unknown, n < 30, population normal

**Book Problem 2 (Example)**:
> Sample of 10 sphere diameters: x̄ = 43.5mm, s² = 4mm². Test if μ = 43.0 at α = 0.05.

**Solution**:
- t = (43.5 - 43.0) / (2/√10) = 0.5 / 0.632 = 0.79
- df = 9, critical t_{0.025} = 2.262
- |t| < 2.262 → Do not reject H₀

---

## 6.6 Tests About Difference of Two Means

### Test 3: Two-Sample Z-Test (Independent, σ₁, σ₂ Known)
$$Z = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)_0}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$$

### Test 4: Two-Sample t-Test (Independent, Equal Variances, σ Unknown)
$$t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)_0}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t_{n_1+n_2-2}$$

**Pooled Variance**:
$$s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$$

**Assumptions**: Normal populations, independent samples, equal variances

**Book Example (Problem 3)**:
> Two machine types: Machine A (n₁=10, x̄₁=50, s₁=5), Machine B (n₂=12, x̄₂=55, s₂=6). 99% CI for difference (Unit 5) and test.

### Test 5: Paired t-Test (Dependent Samples)
$$t = \frac{\bar{d} - \mu_{d0}}{s_d/\sqrt{n}} \sim t_{n-1}$$

Where $d_i = x_i - y_i$ (before - after or matched pairs)

**Use when**: Before/after studies, matched pairs, same subjects under two conditions

**Book Example (Problem 2 - Pulse Rate)**:
> Pulse rate before/after drug for 8 patients. Test if drug reduces pulse rate at α=0.05.
> Before: 72, 75, 78, 80, 76, 74, 77, 79
> After:  68, 70, 74, 75, 72, 69, 71, 73

**Solution from Book (Dec 2021 - both 5-mark and 10-mark!)**:
- Differences: 4, 5, 4, 5, 4, 5, 6, 6
- d̄ = 4.875, s_d = 0.835
- t = 4.875 / (0.835/√8) = 16.53
- df = 7, critical t_{0.05} = 1.895 (right-tailed)
- Reject H₀ → Drug reduces pulse rate

---

## 6.7 Test About Population Variance (σ²)

### Test 6: Chi-Square Test for Single Variance
$$\chi^2 = \frac{(n-1)s^2}{\sigma_0^2} \sim \chi^2_{n-1}$$

**H₀**: σ² = σ₀²  
**H₁**: σ² ≠ σ₀² (two-tailed) or σ² > σ₀² / σ² < σ₀² (one-tailed)

**Book Example (Problem 4)**:
> Sample variance test for population variance.

---

## 6.8 Test About Equality of Two Variances

### Test 7: F-Test for Two Variances
$$F = \frac{s_1^2}{s_2^2} \sim F_{n_1-1, n_2-1} \quad \text{(under } H_0: \sigma_1^2 = \sigma_2^2\text{)}$$

**Always put larger variance in numerator**: $F = \frac{\max(s_1^2, s_2^2)}{\min(s_1^2, s_2^2)}$

**Critical region**: Right tail only (for two-tailed test, use α/2 in right tail)

---

## 6.9 Test About Population Proportion (p)

### Test 8: Z-Test for Single Proportion (Large Sample)
$$Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} \sim N(0,1)$$

**Conditions**: np₀ ≥ 5 and n(1-p₀) ≥ 5

### Test 9: Z-Test for Two Proportions
$$Z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})(\frac{1}{n_1} + \frac{1}{n_2})}}$$

Where pooled proportion: $\hat{p} = \frac{x_1 + x_2}{n_1 + n_2}$

---

## 6.10 Summary of Test Selection

| Situation | Test | Distribution | df |
|-----------|------|--------------|-----|
| 1 mean, σ known | Z-test | N(0,1) | - |
| 1 mean, σ unk, n≥30 | Z-test (with s) | N(0,1) | - |
| 1 mean, σ unk, n<30 | t-test | t | n-1 |
| 2 means indep, σ known | Z-test | N(0,1) | - |
| 2 means indep, σ unk, equal var | t-test (pooled) | t | n₁+n₂-2 |
| 2 means paired | Paired t-test | t | n-1 |
| 1 variance | χ²-test | χ² | n-1 |
| 2 variances | F-test | F | n₁-1, n₂-1 |
| 1 proportion (large n) | Z-test | N(0,1) | - |
| 2 proportions (large n) | Z-test | N(0,1) | - |

---

## 6.11 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - HIGH PRIORITY (6 appearances in 9 papers)

#### 1. One-Sample Z-Test / t-Test
> "CFL bulb claimed life 1500 hrs. Sample 100 bulbs: x̄=1480, σ=50. Test claim at α=0.01." (Jun 2021)

**Solution**:
- H₀: μ = 1500, H₁: μ ≠ 1500 (two-tailed)
- Z = (1480-1500)/(50/√100) = -20/5 = -4
- Critical: ±2.576 (α=0.01)
- |Z| = 4 > 2.576 → Reject H₀
- Conclusion: Claim not supported

#### 2. Paired t-Test ⭐⭐⭐⭐ (Dec 2021 - appeared as BOTH 5-mark and 10-mark!)
> "Pulse rate before/after drug for 8 patients. Test if drug reduces pulse rate at α=0.05."

**Data**: Before: 72, 75, 78, 80, 76, 74, 77, 79 | After: 68, 70, 74, 75, 72, 69, 71, 73

**Solution**:
- Differences: 4, 5, 4, 5, 4, 5, 6, 6
- d̄ = 4.875, s_d = 0.835
- t = 4.875/(0.835/√8) = 16.53
- Critical: t_{0.05, 7} = 1.895 (right-tailed)
- Reject H₀ → Drug reduces pulse rate

#### 3. Two-Sample t-Test (Equal Variances)
> "Two tyre brands: Brand A (n=10, x̄=25000, s=1500), Brand B (n=12, x̄=24000, s=1800). Test if A lasts longer at α=0.05." (Jun 2022)

**Solution**:
- H₀: μ₁ = μ₂, H₁: μ₁ > μ₂
- s_p² = (9×1500² + 11×1800²)/20 = 2,802,500
- s_p = 1674
- t = (25000-24000)/(1674×√(1/10+1/12)) = 1000/(1674×0.428) = 1.39
- Critical: t_{0.05, 20} = 1.725
- t < critical → Do not reject H₀

#### 4. F-Test for Variances
> "Two samples: s₁²=25, n₁=10; s₂²=16, n₂=12. Test equality of variances at α=0.05." (Dec 2025, Jun 2024)

**Solution**:
- H₀: σ₁² = σ₂², H₁: σ₁² ≠ σ₂²
- F = 25/16 = 1.5625
- Critical: F_{0.025, 9, 11} = 3.59 (two-tailed, use α/2)
- F < critical → Do not reject H₀

#### 5. Ad Campaign Effectiveness (Dec 2024)
> Test if ad campaign increased sales using paired data.

---

### 10-Mark Questions (Section B) - HIGH PRIORITY (6 appearances)

#### 1. Paired t-Test (Detailed) ⭐⭐⭐⭐
> "Blood pressure before and after treatment for 10 patients. Test if treatment effective. Also construct 95% CI for mean reduction." (Dec 2021 - pulse rate appeared as 10-mark!)

**Structure from Book**:
1. State H₀, H₁, α
2. Compute differences
3. Find d̄, s_d
4. Compute t-statistic
5. Critical value / p-value
6. Decision
7. Confidence interval
8. Conclusion in context

#### 2. Two-Sample t-Test with CI
> "Two tyre brands comparison. Test if means differ at α=0.05. Construct 95% CI for difference."

---

## 6.12 Important Formulas Summary

| Test | Statistic | Distribution | df |
|------|-----------|--------------|-----|
| **Z (1 mean, σ known)** | $\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}$ | N(0,1) | - |
| **t (1 mean, σ unk)** | $\frac{\bar{x}-\mu_0}{s/\sqrt{n}}$ | t | n-1 |
| **Z (2 means, σ known)** | $\frac{(\bar{x}_1-\bar{x}_2)-(\mu_1-\mu_2)_0}{\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}}$ | N(0,1) | - |
| **t (2 means, pooled)** | $\frac{(\bar{x}_1-\bar{x}_2)-(\mu_1-\mu_2)_0}{s_p\sqrt{1/n_1+1/n_2}}$ | t | n₁+n₂-2 |
| **Paired t** | $\frac{\bar{d}-\mu_{d0}}{s_d/\sqrt{n}}$ | t | n-1 |
| **χ² (1 variance)** | $\frac{(n-1)s^2}{\sigma_0^2}$ | χ² | n-1 |
| **F (2 variances)** | $\frac{s_1^2}{s_2^2}$ (larger on top) | F | n₁-1, n₂-1 |
| **Z (1 proportion)** | $\frac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}$ | N(0,1) | - |
| **Z (2 proportions)** | $\frac{\hat{p}_1-\hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})(1/n_1+1/n_2)}}$ | N(0,1) | - |

---

## 6.13 Critical Values (Memorize Common Ones)

| α | Z_{α/2} (two-tailed) | Z_α (one-tailed) |
|---|---------------------|------------------|
| 0.10 | 1.645 | 1.282 |
| 0.05 | 1.960 | 1.645 |
| 0.01 | 2.576 | 2.326 |

| α | t_{α/2, 9} | t_{α, 9} | t_{α/2, 19} | t_{α, 19} | t_{α/2, 29} | t_{α, 29} |
|---|-----------|---------|------------|----------|------------|----------|
| 0.10 | 1.833 | 1.383 | 1.729 | 1.328 | 1.699 | 1.311 |
| 0.05 | 2.262 | 1.833 | 2.093 | 1.729 | 2.045 | 1.699 |
| 0.01 | 3.250 | 2.821 | 2.861 | 2.539 | 2.756 | 2.462 |

---

## 6.14 Common Mistakes

| Mistake | Correction |
|---------|------------|
| Using Z when σ unknown and n < 30 | Use t-test |
| Not putting larger variance in numerator for F-test | Always: F = max(s₁², s₂²) / min(s₁², s₂²) |
| Wrong df for pooled t-test | df = n₁ + n₂ - 2 (not n₁-1 or n₂-1) |
| Confusing paired vs unpaired | Before/after = paired; different groups = unpaired |
| Two-tailed critical value for one-tailed test | Use α/2 for two-tailed, α for one-tailed |
| Not checking assumptions (normality, equal var) | State assumptions; use F-test for equal var if needed |
| p-value interpretation | p-value = P(data or more extreme \| H₀ true) |

---

## 6.15 Diagrams

### Two-Tailed Test (α=0.05)
```
Density
    │
    │    ┌─────┐
    │   /       \
    │  /         \
    │ /           \
    │/             \
    └─────────────────
   -1.96        1.96
   Reject      Reject
    H₀          H₀
```

### Right-Tailed Test (α=0.05)
```
Density
    │
    │    ┌─────┐
    │   /       \
    │  /         \
    │ /           \
    │/             \
    └─────────────────
              1.645
           Reject H₀
```

### Paired vs Unpaired Design
```
UNPAIRED (Independent Groups)
Group 1: ● ● ● ● ●     (n₁ subjects)
Group 2: ● ● ● ● ● ●   (n₂ different subjects)

PAIRED (Same Subjects / Matched)
Before:  ● ● ● ● ● ●
After:   ● ● ● ● ● ●
         ↓  ↓  ↓  ↓  ↓  ↓
Diff:    ● ● ● ● ● ●   (n pairs)
```

---

## 6.16 Worked Examples from Textbook (Must Practice)

### Example 1: IGNOU Marks (Book Problem 1)
> μ₀ = 54.5, σ = 8.0, n = 100, x̄ = 55.9
> (1) Two-tailed: Z = 1.75, crit = 2.576 → Do not reject
> (2) Right-tailed: Z = 1.75, crit = 2.326 → Do not reject

### Example 2: Sphere Diameter (Book Problem 2)
> n = 10, x̄ = 43.5, s² = 4, μ₀ = 43.0
> t = 0.79, crit = 2.262 → Do not reject

### Example 3: Pulse Rate Paired t-Test (Book Problem 2 / Dec 2021)
> n = 8, differences: 4, 5, 4, 5, 4, 5, 6, 6
> d̄ = 4.875, s_d = 0.835, t = 16.53, crit = 1.895 → Reject H₀

### Example 4: Fuse Manufacturer (Unit 4 Example 4)
> Claim: μ = 12.40, n = 20, x̄ = 10.63, s = 2.48
> t = -3.19, df = 19, crit = 2.861 → Reject claim (p < 0.005)

### Example 5: Two Machine Types (Book Problem 3)
> Machine A: n₁=10, x̄₁=50, s₁=5; Machine B: n₂=12, x̄₂=55, s₂=6
> Pooled t-test

---

## 6.17 Practice Problems (PYQ Style)

### Problem 1 (Jun 2021)
CFL bulb: claimed 1500 hrs. n=100, x̄=1480, σ=50. Test at α=0.01.

### Problem 2 (Dec 2021) - BOTH 5-mark and 10-mark!
Pulse rate before/after drug (paired t-test).

### Problem 3 (Jun 2022)
Tyre life claim. Two-sample t-test.

### Problem 4 (Dec 2024)
Ad campaign effectiveness. Paired or two-sample test.

### Problem 5 (Jun 2024)
Tyre claim test.

### Problem 6 (Jun 2025)
Various hypothesis testing scenarios.

---

## 6.18 Exam Tips

- ✅ **Identify test type** correctly (1-sample vs 2-sample, paired vs unpaired)
- ✅ **Check σ known/unknown** and sample size for Z vs t
- ✅ **State H₀ and H₁** clearly with parameter symbols (μ, p, σ²)
- ✅ **Choose correct tail** based on problem wording
- ✅ **Show all steps**: H₀, H₁, α, test stat, critical value, decision, conclusion
- ✅ **Paired t-test**: Very common in 5-mark and 10-mark questions (Dec 2021 had BOTH!)
- ✅ **F-test**: Put larger variance on top, right-tail only
- ✅ **Two-tailed vs one-tailed**: Critical value α/2 vs α
- ❌ Don't use Z when n<30 and σ unknown
- ❌ Don't confuse pooled vs unpooled t-test
- ❌ Don't forget to state conclusion in context of problem
- ❌ Don't conclude "H₀ is true" - only "do not reject H₀"

---

*End of Unit 6 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 6 "Tests of Significance" - All formulas, definitions, procedures, examples, and exercises verified against original textbook content.