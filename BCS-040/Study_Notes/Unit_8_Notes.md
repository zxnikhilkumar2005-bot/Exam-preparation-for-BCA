# Unit 8: Analysis of Variance (One-Way Classification)

**Block 2: Statistical Inference**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 8 - Analysis of Variance: One-Way Classification (IGNOU BCS-040)

---

## 8.1 Introduction

**ANOVA (Analysis of Variance)**: Statistical method to compare means of **three or more** populations simultaneously.

### Why Not Multiple t-Tests?
- Comparing k groups with t-tests requires k(k-1)/2 pairwise tests
- Overall Type I error inflates: α_overall ≈ 1 - (1-α)^(k(k-1)/2)
- ANOVA tests all means simultaneously with single α

### Applications (from Book)
- Comparing crop yields from different fertilizers
- Comparing teaching methods of a foreign language
- Comparing drug effectiveness for blood pressure control
- Comparing production processes/machines
- Comparing gas cylinder weights from different agents

---

## 8.2 Basic Concepts: Sources of Variation

Total variation in data comes from two sources:
1. **Between-group variation (Treatment/SSB/SSA)**: Due to differences in group means
2. **Within-group variation (Error/SSW/SSE)**: Due to random variation within groups

### Key Identity
$$\text{Total SS} = \text{Between SS} + \text{Within SS}$$
$$SST = SSB + SSW$$

---

## 8.3 Model for One-Way Classification

### Mathematical Model (Book Equation 1)
$$y_{ij} = \mu + \tau_i + \epsilon_{ij}, \quad i = 1,2,\ldots,k; \quad j = 1,2,\ldots,n_i$$

Where:
- $y_{ij}$ = observation j in group i
- $\mu$ = overall mean (grand mean)
- $\tau_i$ = effect of treatment/group i
- $\epsilon_{ij}$ = random error ~ N(0, σ²), i.i.d.

**Alternative Parameterization (Book)**: Let $y_{ij} = \mu - \alpha_i + \epsilon_{ij}$ where $\alpha_i$ = amount of gas tapped by agent i, and $\tau_i = -\alpha_i$.

### Assumptions (from Book)
1. **Normality**: $\epsilon_{ij} \sim N(0, \sigma^2)$
2. **Homoscedasticity**: Equal variances across groups ($\sigma^2$ constant)
3. **Independence**: Observations independent
4. **Additivity**: Effects are additive

### Hypothesis
- **H₀**: $\tau_1 = \tau_2 = \ldots = \tau_k = 0$ (all group means equal)
- **H₁**: At least one $\tau_i \neq 0$ (at least one mean differs)
- Equivalent to: H₀: $\mu_1 = \mu_2 = \ldots = \mu_k$

---

## 8.4 Worked Example from Textbook: Gas Company Example (Main Example)

### Problem
Mrs. Devi suspected gas cylinders from ABC agency were underweight. Company checked 5 agents, took 7 cylinders from each (35 total). Test if mean gas weight differs among agents at α=0.05.

### Data (Table 1 - Book)
| Agent | 7 Cylinder Weights (kg) | Total (yᵢ.) | Average (ȳᵢ.) | Sample Variance |
|-------|------------------------|-------------|---------------|-----------------|
| 1 | 14.2, 14.1, 14.2, 14.1, 14.3, 14.2, 14.1 | 99.20 | 14.1714 | 0.0091 |
| 2 | 13.7, 13.8, 13.7, 13.6, 13.9, 13.8, 13.7 | 96.17 | 13.7386 | 0.02748 |
| 3 | 13.8, 13.9, 13.8, 13.9, 13.9, 13.8, 14.0 | 97.17 | 13.8814 | 0.02585 |
| 4 | 14.2, 14.1, 14.1, 14.2, 14.1, 14.2, 14.1 | 98.96 | 14.1371 | 0.10536 |
| 5 | 13.8, 13.7, 13.7, 13.8, 13.6, 13.7, 13.7 | 96.02 | 13.7171 | 0.08812 |

### Computations (Book)
- **Grand Total**: $y_{..} = 487.52$
- **Grand Mean**: $\bar{y}_{..} = 487.52/35 = 13.9291$
- **CF** = $(487.52)^2 / 35 = 6790.7357$
- **TSS** = $\sum\sum y_{ij}^2 - CF = 6793.5698 - 6790.7357 = 2.8341$
- **SSB** = $\sum y_{i.}^2/n_i - CF = (99.20^2+96.17^2+97.17^2+98.96^2+96.02^2)/7 - 6790.7357 = 1.2986$
- **SSW** = TSS - SSB = 2.8341 - 1.2986 = 1.5355

### ANOVA Table (Book Table 4)
| SV | DF | SS | MS | F-Ratio |
|----|----|-----|-----|---------|
| Agents (Treatments) | 4 | 1.2986 | 0.3246 | 6.34 |
| Error | 30 | 1.5355 | 0.0512 | |
| Total | 34 | 2.8341 | | |

**F_calc** = 0.3246 / 0.0512 = 6.34  
**df₁** = 4, **df₂** = 30  
**F_crit** (α=0.05, 4, 30) = 2.69

Since 6.34 > 2.69 → **Reject H₀**. Agents differ in average gas weight.

---

## 8.5 Sums of Squares

### Notation
- $k$ = number of groups (treatments)
- $n_i$ = sample size for group i
- $N = \sum n_i$ = total sample size
- $y_{i.} = \sum_{j=1}^{n_i} y_{ij}$ = group i total
- $\bar{y}_{i.} = y_{i.}/n_i$ = group i mean
- $y_{..} = \sum y_{i.}$ = grand total
- $\bar{y}_{..} = y_{..}/N$ = grand mean

### Formulas

#### General (Unbalanced) Case
| Sum of Squares | Formula | Computing Formula |
|----------------|---------|-------------------|
| **Total (SST)** | $\sum\sum (y_{ij} - \bar{y}_{..})^2$ | $\sum\sum y_{ij}^2 - CF$ |
| **Between (SSB)** | $\sum n_i(\bar{y}_{i.} - \bar{y}_{..})^2$ | $\sum \frac{y_{i.}^2}{n_i} - CF$ |
| **Within (SSW)** | $\sum\sum (y_{ij} - \bar{y}_{i.})^2$ | $SST - SSB$ |

Where **CF** (Correction Factor) = $\frac{y_{..}^2}{N}$

#### Balanced Case ($n_i = n$)
| Sum of Squares | Formula |
|----------------|---------|
| **SST** | $\sum\sum y_{ij}^2 - CF$ |
| **SSB** | $n\sum(\bar{y}_{i.} - \bar{y}_{..})^2$ or $\frac{1}{n}\sum y_{i.}^2 - CF$ |
| **SSW** | $SST - SSB$ |

### Degrees of Freedom
| Source | df |
|--------|-----|
| Between (Treatments) | $k - 1$ |
| Within (Error) | $N - k$ |
| Total | $N - 1$ |

### Mean Squares
| Source | MS = SS / df |
|--------|-------------|
| **MSB** (Between) | $SSB / (k-1)$ |
| **MSW** (Within) | $SSW / (N-k)$ |

---

## 8.6 F-Test Statistic

$$F = \frac{MSB}{MSW} \sim F_{k-1, N-k} \quad \text{(under H₀)}$$

### Decision Rule
- Reject H₀ if $F_{calc} > F_{\alpha, k-1, N-k}$
- Do not reject H₀ if $F_{calc} \leq F_{\alpha, k-1, N-k}$

---

## 8.7 ANOVA Table (Standard Format)

| Source of Variation | df | SS | MS | F |
|---------------------|----|-----|-----|---|
| **Between Groups** (Treatments) | $k-1$ | SSB | $MSB = \frac{SSB}{k-1}$ | $F = \frac{MSB}{MSW}$ |
| **Within Groups** (Error) | $N-k$ | SSW | $MSW = \frac{SSW}{N-k}$ | |
| **Total** | $N-1$ | SST | | |

---

## 8.8 Computational Shortcuts for Balanced Data (Book Remark)

**If data are balanced** (all $n_i$ equal):

**To get TSS**:
- Input all $y_{ij}$ and get their **population SD** (not sample SD)
- $TSS = N \times (SD)^2$
- *Example*: SD = 0.28426, $TSS = 35 \times (0.28426)^2 = 2.8281$

**To get SSB**:
- Compute SD of the **totals** ($y_{i.}$)
- $SSB = \frac{(SD_{totals})^2 \times k}{n}$  (Note: textbook has typo showing 7/5, correct is $k/n = 5/7$)
- *Book says*: "Compute SD of the totals (yᵢ.), square it and then multiply by k/n"
- For Gas Company: SD of totals = 1.3483, $SSB = (1.3483)^2 \times 5/7 = 1.2985$

**Then SSW = TSS - SSB**

⚠️ **These shortcuts apply ONLY for balanced data!**  
⚠️ **Textbook Error Alert**: Book shows "multiply by 7/5" but correct factor is $k/n = 5/7$ (k=5 agents, n=7 per agent). The book's numeric answer 1.2985 uses 5/7, but text says 7/5.

---

## 8.9 Pairwise Comparisons (Post-Hoc Tests)

After rejecting H₀, identify which means differ. Book uses **Least Significant Difference (LSD)** method.

### LSD Formula (Book Equation 8)
$$LSD = t_{\alpha/2, df_{error}} \cdot \sqrt{MSW \left(\frac{1}{n_i} + \frac{1}{n_j}\right)}$$

For balanced data ($n_i = n_j = n$):
$$LSD = t_{\alpha/2, df_{error}} \cdot \sqrt{\frac{2 \times MSW}{n}}$$

### Procedure (Book Gas Company Example)
1. Arrange group means in **descending order**
2. Compute differences between adjacent means
3. Compare each difference with LSD
4. If difference > LSD, means are significantly different

### Gas Company Example (Book)
**Means in descending order**:
- ȳ₁ = 14.1714
- ȳ₄ = 14.1371
- ȳ₃ = 13.8814
- ȳ₂ = 13.7386
- ȳ₅ = 13.7171

**Differences**:
- ȳ₁ - ȳ₄ = 0.0343
- ȳ₄ - ȳ₃ = 0.2557
- ȳ₃ - ȳ₂ = 0.1428
- ȳ₂ - ȳ₅ = 0.0215

**LSD** = $t_{0.025, 30} \times \sqrt{2 \times 0.0512 / 7} = 2.042 \times 0.1211 = 0.247$ (Book: LSD = 0.2366)

**Result**: Only ȳ₄ - ȳ₃ = 0.2557 > LSD → Significant difference between Agents 4 and 3

---

## 8.10 Unbalanced Design (nᵢ not equal)

### Formulas (Book Equations 5, 6, 7)
- $N = \sum n_i$
- $CF = y_{..}^2 / N$ (Correction Factor)
- $SST = \sum\sum y_{ij}^2 - CF$
- $SSB = \sum \frac{y_{i.}^2}{n_i} - CF$
- $SSW = SST - SSB$
- $df_{between} = k-1$, $df_{within} = N-k$

### Worked Example from Book: Brick Density (Example 2)
**Data**: 4 firing temperatures, unequal sample sizes (5, 4, 5, 4)
| Temp | 100°C | 125°C | 150°C | 175°C |
|------|-------|-------|-------|-------|
| nᵢ | 5 | 4 | 5 | 4 |
| Total (yᵢ.) | 108.7 | 86.0 | 108.6 | 86.8 |
| Mean (ȳᵢ.) | 21.74 | 21.50 | 21.72 | 21.70 |

**Computations**:
- $CF = (390.1)^2 / 18 = 8454.3338$
- $TSS = 8454.85 - 8454.3338 = 0.5161$
- $SSB = \frac{108.7^2}{5} + \frac{86.0^2}{4} + \frac{108.6^2}{5} + \frac{86.8^2}{4} - CF = 0.1562$
- $SSW = 0.5161 - 0.1562 = 0.3599$

**ANOVA Table (Book Table 8)**:
| SV | DF | SS | MS | F |
|----|----|-----|-----|---|
| Temperature | 3 | 0.1562 | 0.0520 | 2.02 |
| Error | 14 | 0.3599 | 0.0257 | |
| Total | 17 | 0.5161 | | |

$F_{crit}$ (3, 14, α=0.05) = 3.34. Since 2.02 < 3.34 → **Do not reject H₀**

**Pairwise t-test for τ₁ vs τ₂**:
$t = \frac{\bar{y}_1 - \bar{y}_2}{\sqrt{MSW(\frac{1}{n_1}+\frac{1}{n_2})}} = \frac{21.74-21.50}{\sqrt{0.0257(\frac{1}{5}+\frac{1}{4})}} = 2.231$

$t_{crit}$ (14 df, α=0.025) = 2.145 → **Significant difference between τ₁ and τ₂**

---

## 8.10 Random Effects Model (Book Section 8.7)

In the **fixed effects model**, treatments are specifically chosen (e.g., 4 specific drugs).

In the **random effects model**, treatments are a **random sample** from a larger population of treatments.

- Model: $y_{ij} = \mu + \alpha_i + \epsilon_{ij}$ where $\alpha_i \sim N(0, \sigma_\alpha^2)$
- H₀: $\sigma_\alpha^2 = 0$ (no treatment effect)
- Test statistic: $F = \frac{MSB}{MSW}$ (same as fixed effects)
- But interpretation differs: Inference about population of treatments, not just these specific ones
- Variance components: $\hat{\sigma}^2 = MSW$, $\hat{\sigma}_\alpha^2 = \frac{MSB - MSW}{n}$ (balanced)

---

## 8.11 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - HIGH PRIORITY

#### 1. ANOVA Table Construction
> "Construct model ANOVA table for one-way classification." (Dec 2025)

**Answer**: Draw the standard table with Sources: Treatments (k-1), Error (N-k), Total (N-1) with formulas for SS, MS, F.

#### 2. Complete ANOVA Calculation
> "Four catalysts tested in 3 plants. Data given. Test if catalysts differ at α=0.05." (Dec 2022)

**Structure**:
1. State H₀: μ₁=μ₂=μ₃=μ₄, H₁: At least one differs
2. Compute group totals, means, grand mean
3. Calculate SSB, SSW, SST
4. Fill ANOVA table
5. F = MSB/MSW
6. Compare with F_{0.05, 3, 8}
7. Conclusion

---

### 10-Mark Questions (Section B) - HIGHEST PRIORITY (8 appearances in 9 papers!)

#### 1. Complete One-Way ANOVA (Various Scenarios) ⭐⭐⭐⭐⭐⭐⭐⭐
> **Jun 2021**: Diet cholesterol (3 groups)
> **Dec 2021**: Production processes (4 groups)
> **Jun 2022**: Methods A,B,C (4 operators each)
> **Dec 2022**: Catalysts in 3 plants
> **Dec 2023**: Computer engineer 3 methods, 5 operators
> **Dec 2024**: ANOVA table from raw data
> **Dec 2025**: Model ANOVA table construction
> **Jun 2025**: Another scenario

**This is THE most repeated 10-mark question! Appeared in 8/9 papers.**

#### 2. Pairwise Comparisons (if H₀ rejected)
> "If significant, use LSD/Tukey to compare pairs."

---

## 8.12 Step-by-Step Procedure for 10-Mark Questions

```
STEP 1: State Hypotheses
  H₀: μ₁ = μ₂ = ... = μₖ
  H₁: At least one μᵢ differs
  α = 0.05 (or given)

STEP 2: Organize Data
  Group 1: y₁₁, y₁₂, ..., y₁ₙ₁  (n₁ obs)
  Group 2: y₂₁, y₂₂, ..., y₂ₙ₂
  ...
  Group k: yₖ₁, yₖ₂, ..., yₖₙₖ

STEP 3: Calculate Summaries
  For each group i: Total yᵢ., Mean ȳᵢ., nᵢ
  Grand Total y.., Grand Mean ȳ.., Total N

STEP 4: Compute Sums of Squares
  CF = (y..)²/N
  SST = ΣΣyᵢⱼ² - CF
  SSB = Σ(yᵢ.)²/nᵢ - CF
  SSW = SST - SSB

STEP 5: ANOVA Table
  | Source | df | SS | MS | F |
  |--------|----|-----|-----|---|
  | Between| k-1| SSB | SSB/(k-1) | MSB/MSW |
  | Within | N-k| SSW | SSW/(N-k) | |
  | Total  | N-1| SST | | |

STEP 6: F-Statistic
  F_calc = MSB/MSW

STEP 7: Critical Value
  F_crit = F_{α, k-1, N-k} from F-table

STEP 8: Decision
  If F_calc > F_crit → Reject H₀
  Else → Do not reject H₀

STEP 9: Conclusion
  "There is significant difference among group means"
  OR
  "No significant difference among group means"

STEP 10: Pairwise (if required)
  Use LSD or Tukey HSD
```

---

## 8.13 Important Formulas Summary

| Quantity | Balanced (nᵢ=n) | Unbalanced |
|----------|------------------|------------|
| **CF** | $y_{..}^2 / N$ | $y_{..}^2 / N$ |
| **SST** | $\sum\sum y_{ij}^2 - CF$ | $\sum\sum y_{ij}^2 - CF$ |
| **SSB** | $n\sum(\bar{y}_{i.}-\bar{y}_{..})^2$ | $\sum y_{i.}^2/n_i - CF$ |
| **SSW** | $SST - SSB$ | $SST - SSB$ |
| **df_B** | $k-1$ | $k-1$ |
| **df_W** | $N-k$ | $N-k$ |
| **MSB** | $SSB/(k-1)$ | $SSB/(k-1)$ |
| **MSW** | $SSW/(N-k)$ | $SSW/(N-k)$ |
| **F** | $MSB/MSW$ | $MSB/MSW$ |

---

## 8.14 Critical F-Values (Common)

| α | F_{0.05, 2, 12} | F_{0.05, 3, 16} | F_{0.05, 4, 15} | F_{0.05, 2, 20} |
|---|----------------|----------------|----------------|----------------|
| 0.05 | 3.89 | 3.24 | 3.06 | 3.49 |
| 0.01 | 6.93 | 5.29 | 4.89 | 5.85 |

| α | F_{0.05, 3, 8} | F_{0.05, 4, 10} | F_{0.05, 3, 12} | F_{0.05, 4, 30} (Gas Co.) |
|---|---------------|----------------|----------------|--------------------------|
| 0.05 | 4.07 | 3.48 | 3.49 | 2.69 |

---

## 8.15 Common Mistakes

| Mistake | Correction |
|---------|------------|
| Wrong df for SSB | df = k-1 (not k) |
| Wrong df for SSW | df = N-k (not N-1 or N-k-1) |
| Using SST instead of SSB in numerator | F = MSB/MSW (between/within) |
| Not checking assumptions | State: normality, equal variance, independence |
| Forgetting CF in calculations | Always compute CF = (grand total)²/N |
| Using wrong formula for unbalanced | Use yᵢ.²/nᵢ for SSB |
| Pairwise without rejecting H₀ | Only do pairwise if overall F-test significant |
| Using sample SD instead of population SD for shortcut | Shortcut uses population SD (divisor N) |
| **Textbook shortcut typo** | SSB shortcut uses k/n (not n/k) for balanced data |

---

## 8.16 Diagrams

### ANOVA Partitioning
```
Total Variation (SST)
    │
    ├── Between Groups (SSB) ──→ Explained by treatment differences
    │
    └── Within Groups (SSW) ──→ Random/error variation
```

### F-Distribution (Right-Tailed)
```
Density
    │
    │    ┌─────┐
    │   /       \
    │  /         \
    │ /           \
    │/             \
    └─────────────────
         F_crit
    Reject H₀ →
```

### ANOVA Table Template
```
┌──────────────────┬────┬──────┬──────┬──────┐
│ Source           │ df │  SS  │  MS  │  F   │
├──────────────────┼────┼──────┼──────┼──────┤
│ Treatments       │k-1 │ SSB  │ MSB  │ MSB/ │
│ (Between)        │    │      │      │ MSW  │
├──────────────────┼────┼──────┼──────┼──────┤
│ Error            │N-k │ SSW  │ MSW  │      │
│ (Within)         │    │      │      │      │
├──────────────────┼────┼──────┼──────┼──────┤
│ Total            │N-1 │ SST  │      │      │
└──────────────────┴────┴──────┴──────┴──────┘
```

---

## 8.17 Worked Examples from Textbook (Must Practice)

### Example 1: Gas Company (Main Example - 5 agents, 7 each)
- Data given in Table 1
- SSB = 1.2986, SSW = 1.5355, F = 6.34
- F_crit (4, 30) = 2.69 → Reject H₀
- Pairwise LSD = 0.2366
- Significant: Agent 4 vs Agent 3

### Example 2: Brick Density (Unbalanced - 4 temps, n=5,4,5,4)
- SSB = 0.1562, SSW = 0.3599, F = 2.02
- F_crit (3, 14) = 3.34 → Do not reject H₀
- But pairwise: τ₁ vs τ₂ significant (t = 2.231 > 2.145)

### Example 3: Drive Shaft Slot Lengths (Exercise E6)
- 8 stations, 10 each (balanced)
- Test if mean slot length = target 5.95
- Before/after adjustment comparison

### Example 4: Pairwise Comparisons (Exercise E8)
- Test if stations 1 and 6 differ
- Test if stations 4 and 6 differ
- Test if common mean of 4 and 7 equals target 5.95
- Test if station 3 < target 5.95

### Example 5: Target Testing (Exercise E9)
- Test if mean slot length = target 5.95 (all 8 stations)

---

## 8.18 Practice Problems (PYQ Style)

### Problem 1 (Jun 2021)
**Diet cholesterol**: 3 diet groups, test if mean cholesterol differs.

### Problem 2 (Dec 2021)
**Production processes**: 4 processes, test if output differs.

### Problem 3 (Jun 2022)
**Methods A,B,C**: 4 operators each, test if methods differ.

### Problem 4 (Dec 2022)
**Catalysts in 3 plants**: Test catalyst effects.

### Problem 5 (Dec 2023)
**Computer engineer**: 3 methods, 5 operators each.

### Problem 6 (Dec 2024)
**Complete ANOVA from raw data**.

### Problem 7 (Dec 2025)
**Model ANOVA table construction**.

### Problem 8 (Jun 2025)
**Another one-way ANOVA scenario**.

---

## 8.19 Exam Tips

- ✅ **THIS IS THE #1 MOST IMPORTANT TOPIC**: 8/9 papers, always 10 marks!
- ✅ **Memorize ANOVA table structure** with formulas
- ✅ **Practice computing SSB, SSW, SST** from raw data (Gas Company, Brick Density)
- ✅ **Know the F-test**: F = MSB/MSW, df₁=k-1, df₂=N-k
- ✅ **Right-tailed test only**: Reject if F_calc > F_crit
- ✅ **Check assumptions**: Normality, equal variance, independence
- ✅ **Pairwise comparisons**: LSD formula with t_{α/2, df_error} (only if H₀ rejected)
- ✅ **Balanced vs unbalanced formulas**: Know both
- ✅ **CF = (Σy)²/N** - always compute first!
- ✅ **Gas Company example**: Know the data pattern and LSD procedure
- ❌ Don't confuse SSB (between) and SSW (within) in F-ratio
- ❌ Don't forget Correction Factor CF = (Σy)²/N
- ❌ Don't do pairwise tests if overall F not significant
- ❌ Don't use sample SD for TSS shortcut - use population SD
- ⚠️ **Textbook typo**: SSB shortcut uses k/n (not n/k) for balanced data

---

*End of Unit 8 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 8 "Analysis of Variance: One-Way Classification" - All formulas, definitions, examples (Gas Company, Brick Density, Drive Shafts), exercises, and computational shortcuts verified against original textbook content.