# Unit 13: Stratified Sampling

**Block 4: Sampling Techniques**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 13 - Stratified Sampling (IGNOU BCS-040)

---

## 13.1 Introduction

**Stratification**: Dividing population into homogeneous subgroups (strata) based on auxiliary variable.

**Stratified Random Sampling**: SRS within each stratum independently.

### Why Stratify? (from Book)
1. **Increased precision** (reduced variance)
2. **Administrative convenience**
3. **Separate estimates** for each stratum
4. **Different sampling designs** per stratum possible

### Case Study: A&B Transport Company (Book Example)
- 23,000 waybills over 6 months
- Strata by freight charge ranges: 0-200, 201-400, 401-700, 701-1400, >1401
- More variable strata → larger sample allocation
- Used serial number sampling for selection

---

## 13.2 Notation (Book Table 3)

| Symbol | Meaning |
|--------|---------|
| L | Number of strata |
| Nₕ | Population size of stratum h |
| nₕ | Sample size from stratum h |
| N = ΣNₕ | Total population size |
| n = Σnₕ | Total sample size |
| Wₕ = Nₕ/N | Stratum weight |
| ȳₕ | Sample mean in stratum h |
| Sₕ² | Population variance in stratum h |
| sₕ² | Sample variance in stratum h |
| fₕ = nₕ/Nₕ | Sampling fraction in stratum h |

---

## 13.3 Estimation of Population Parameters

### Population Mean
$$\bar{y}_{st} = \sum_{h=1}^L W_h \bar{y}_h = \frac{1}{N}\sum_{h=1}^L N_h \bar{y}_h$$

### Population Total
$$\hat{Y}_{st} = N \bar{y}_{st} = \sum_{h=1}^L N_h \bar{y}_h$$

### Population Proportion
$$\hat{P}_{st} = \sum_{h=1}^L W_h \hat{p}_h = \frac{1}{N}\sum_{h=1}^L N_h \hat{p}_h$$

Where $\hat{p}_h$ = sample proportion in stratum h.

---

## 13.4 Variance of Estimators (SRSWOR within Strata)

### Variance of Mean
$$V(\bar{y}_{st}) = \sum_{h=1}^L W_h^2 \frac{S_h^2}{n_h} \left(1 - \frac{n_h}{N_h}\right)$$

### Estimated Variance
$$\hat{V}(\bar{y}_{st}) = \sum_{h=1}^L W_h^2 \frac{s_h^2}{n_h} \left(1 - \frac{n_h}{N_h}\right)$$

### Variance of Total
$$V(\hat{Y}_{st}) = N^2 V(\bar{y}_{st}) = \sum_{h=1}^L N_h^2 \frac{S_h^2}{n_h} \left(1 - \frac{n_h}{N_h}\right)$$

---

## 13.5 Worked Example from Textbook: Apple Orchards (Problem 1)

### Data
| Stratum | A | B | C | D |
|---------|---|---|---|---|
| Villages (Nₕ) | 275 | 146 | 93 | 62 |
| Sample (nₕ) | 15 | 10 | 12 | 11 |
| Orchard counts | 2,5,1,9,6,7,0,4,7,0,5,0,0,3,0 | 21,11,7,5,6,19,5,24,30,24 | 3,10,4,11,38,11,4,46,4,18,1,19 | 30,42,20,38,29,22,31,28,66,41,15 |

### Solution (Book)
**Step 1: Compute stratum means and variances**
| Stratum | Nₕ | nₕ | Wₕ | ȳₕ | sₕ² |
|---------|----|----|-----|-----|-----|
| A | 275 | 15 | 0.477 | 3.533 | 9.552 |
| B | 146 | 10 | 0.253 | 14.2 | 88.4 |
| C | 93 | 12 | 0.161 | 19.5 | 349.2 |
| D | 62 | 11 | 0.108 | 34.0 | 247.5 |

**Step 2: Estimate Population Mean**
$$\bar{y}_{st} = \sum W_h \bar{y}_h = 0.477(3.533) + 0.253(14.2) + 0.161(19.5) + 0.108(34.0) = 11.23$$

**Step 3: Estimate Population Total**
$$\hat{Y}_{st} = N \bar{y}_{st} = 576 \times 11.23 = 6468.48$$

**Step 4: Estimated Variance**
$$\hat{V}(\bar{y}_{st}) = \sum W_h^2 \frac{s_h^2}{n_h}(1-f_h) = 1.2277$$
$$\hat{V}(\hat{Y}_{st}) = 576^2 \times 1.2277 = 407321.39$$

---

## 13.6 Allocation of Sample Size

### 1. Equal Allocation
$$n_h = \frac{n}{L} \quad \text{for all } h$$

**Use when**: Strata sizes similar, no variability info, equal cost

**Variance**: $V_{equal} = \frac{1}{n}\sum W_h S_h^2 - \frac{1}{N}\sum W_h S_h^2$

---

### 2. Proportional Allocation (Bowley, 1926)
$$n_h = n \frac{N_h}{N} = n W_h$$

**Properties**:
- $f_h = n_h/N_h = n/N$ = constant (same sampling fraction)
- Self-weighting: $\bar{y}_{st} = \frac{1}{n}\sum n_h \bar{y}_h = \bar{y}$ (overall sample mean)
- **Variance**: $V_{prop} = \frac{1}{n}\sum W_h S_h^2 - \frac{1}{N}\sum W_h S_h^2$

**Advantage**: Simple, no need for Sₕ estimates
**Disadvantage**: Ignores stratum variability

---

### 3. Neyman / Optimum Allocation (Neyman, 1934)
**Minimizes variance for fixed n** (assuming equal cost per unit)

$$n_h = n \frac{N_h S_h}{\sum_{j=1}^L N_j S_j} = n \frac{W_h S_h}{\sum W_j S_j}$$

**Properties**:
- Larger strata → larger allocation
- More variable strata → larger allocation
- **Optimum Variance**: $V_{opt} = \frac{1}{n}\left(\sum W_h S_h\right)^2 - \frac{1}{N}\sum W_h S_h^2$

---

### 4. Cost-Optimal Allocation
**Minimizes cost for fixed variance** (or variance for fixed cost)

Cost function: $C = C_0 + \sum C_h n_h$

$$n_h = \frac{(C - C_0) W_h S_h / \sqrt{C_h}}{\sum W_j S_j / \sqrt{C_j}}$$

Where $C_h$ = cost per unit in stratum h, $C_0$ = fixed overhead cost.

---

## 13.7 Worked Example from Textbook: Three Towns (Problem 2)

### Data
| Town | Nₕ | Sₕ |
|------|-----|-----|
| 1 | 50,000 | 30 |
| 2 | 30,000 | 15 |
| 3 | 40,000 | 20 |
| **Total n** | **500** |

### Solution (Book)

**Proportional Allocation**:
- $n_1 = 500 \times 50000/120000 = 208$
- $n_2 = 500 \times 30000/120000 = 125$
- $n_3 = 500 \times 40000/120000 = 167$

**Neyman (Optimum) Allocation**:
- $N_1 S_1 = 50000 \times 30 = 1,500,000$
- $N_2 S_2 = 30000 \times 15 = 450,000$
- $N_3 S_3 = 40000 \times 20 = 800,000$
- Sum = 2,750,000
- $n_1 = 500 \times 1,500,000/2,750,000 = 273$
- $n_2 = 500 \times 450,000/2,750,000 = 82$
- $n_3 = 500 \times 800,000/2,750,000 = 145$

---

## 13.8 Comparison of Allocations

| Allocation | Formula | Best When |
|------------|---------|-----------|
| **Equal** | $n_h = n/L$ | Strata similar size & variability |
| **Proportional** | $n_h = n W_h$ | No variability info, simple |
| **Neyman (Optimum)** | $n_h \propto N_h S_h$ | Variability differs, equal cost |
| **Cost-Optimal** | $n_h \propto N_h S_h/\sqrt{C_h}$ | Costs differ across strata |

### Efficiency Gains
$$V_{ran} \geq V_{prop} \geq V_{opt}$$

**Relative Efficiency**:
$$\frac{V_{prop}}{V_{opt}} = \frac{\sum W_h S_h^2}{(\sum W_h S_h)^2} \geq 1$$

**Equality holds only if** all $S_h$ equal (no gain from optimum allocation).

---

## 13.9 Construction of Strata (Dalenius-Hodges Rule)

### Principles (Book)
1. Strata non-overlapping, exhaustive
2. Within-stratum homogeneity
3. Between-stratum heterogeneity
4. Administrative feasibility

### Dalenius-Hodges Rule (for continuous variable)
1. Obtain frequency table with K classes for stratification variable x
2. Compute square roots of frequencies: $f_i = \sqrt{f_i}$
3. Compute cumulative square roots: $d_i = \sum_{j=1}^i \sqrt{f_j}$
4. Let T = cumulative total for K-th class
5. For L strata, boundaries at: $x_i$ corresponding to $i \cdot T/L$ in cumulative column
6. Use linear interpolation on class intervals

### Worked Example from Book: Milk Yield (Problem 3)
- 127 cows, 3 strata, 25 cows total
- Optimum allocation
- First lactation length as stratification variable

**Solution (Book)**:
| Length Class | Freq | √freq | Cumulative |
|--------------|------|-------|------------|
| 30-100 | 1 | 1.00 | 1.00 |
| 100-150 | 5 | 2.24 | 3.24 |
| 150-200 | 12 | 3.46 | 6.70 |
| 200-250 | 28 | 5.29 | 11.99 |
| 250-300 | 31 | 5.57 | 17.56 |
| 300-350 | 25 | 5.00 | 22.56 |
| 350-400 | 12 | 3.46 | 26.02 |
| 400-450 | 8 | 2.83 | 28.85 |
| 450-500 | 5 | 2.24 | 31.09 |
| 500-550 | 3 | 1.73 | 32.82 |
| 550-600 | 2 | 1.41 | 34.23 |
| 600-650 | 1 | 1.00 | 35.23 |

T = 35.23, L = 3 → Boundaries at T/3 = 11.74 and 2T/3 = 23.48

**Linear Interpolation**:
- $x_1$ at 11.74: in interval 200-250 (cum: 11.99 to 17.56)
  - $x_1 = 200 + \frac{11.74 - 11.99}{17.56 - 11.99} \times 50 = 216.67$
- $x_2$ at 23.48: in interval 300-350 (cum: 22.56 to 26.02)
  - $x_2 = 300 + \frac{23.48 - 22.56}{26.02 - 22.56} \times 50 = 313.21$

**Strata**:
1. [30, 216.67]
2. [216.67, 313.21]
3. [313.21, 510]

---

## 13.10 Post-Stratification

### When to Use
Stratification after sample selection (when stratum membership unknown beforehand).

### Estimation
Same formulas, but $W_h$ estimated from sample: $\hat{W}_h = n_h/n$

**Caution**: Introduces additional variability; use only when necessary.

---

## 13.11 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - MEDIUM PRIORITY (3-4 appearances)

#### 1. Stratified Allocation Calculations
> "Population with 3 strata: N₁=1000, N₂=2000, N₃=3000; S₁=10, S₂=15, S₃=20. Total n=120. Find proportional and Neyman allocations."

**Solution**:
- Proportional: n₁ = 120×1000/6000 = 20, n₂ = 40, n₃ = 60
- Neyman: n₁ ∝ 1000×10=10000, n₂ ∝ 2000×15=30000, n₃ ∝ 3000×20=60000
  - Sum = 100000
  - n₁ = 120×10000/100000 = 12, n₂ = 36, n₃ = 72

#### 2. Estimation of Population Mean/Total
> "Stratified sample data given. Estimate population mean and its variance."

#### 3. Relative Efficiency
> "Compare efficiency of Neyman vs Proportional allocation."

### 10-Mark Questions (Section B) - MEDIUM PRIORITY (3 appearances)

#### 1. Complete Stratified Sampling Problem
> **Jun 2021**: Stratified sampling with proportional and Neyman allocation
> **Dec 2023**: Stratified sampling estimation
> **Jun 2025**: Stratified/Neyman allocation

**Structure**:
1. Define strata and notation
2. Show allocation calculations (Proportional & Neyman)
3. Estimate population mean/total
4. Compute variance of estimator
5. Compare allocations (relative efficiency)
6. Conclusion

---

## 13.12 Important Formulas Summary

| Quantity | Formula |
|----------|---------|
| **Stratum Weight** | $W_h = N_h/N$ |
| **Mean (Estimator)** | $\bar{y}_{st} = \sum W_h \bar{y}_h$ |
| **Total (Estimator)** | $\hat{Y}_{st} = N \bar{y}_{st}$ |
| **Variance (Mean)** | $V(\bar{y}_{st}) = \sum W_h^2 \frac{S_h^2}{n_h}(1-f_h)$ |
| **Est. Variance** | $\hat{V}(\bar{y}_{st}) = \sum W_h^2 \frac{s_h^2}{n_h}(1-f_h)$ |
| **Proportional nₕ** | $n_h = n W_h$ |
| **Neyman nₕ** | $n_h = n \frac{N_h S_h}{\sum N_j S_j}$ |
| **Cost-Optimal nₕ** | $n_h \propto \frac{N_h S_h}{\sqrt{C_h}}$ |
| **V_prop** | $\frac{1}{n}\sum W_h S_h^2 - \frac{1}{N}\sum W_h S_h^2$ |
| **V_opt** | $\frac{1}{n}(\sum W_h S_h)^2 - \frac{1}{N}\sum W_h S_h^2$ |

---

## 13.13 Step-by-Step: Allocation Calculations

```
GIVEN: 3 Strata
  N₁ = 1000, S₁ = 10
  N₂ = 2000, S₂ = 15
  N₃ = 3000, S₃ = 20
  Total n = 120

STEP 1: Proportional Allocation
  N = 1000+2000+3000 = 6000
  W₁ = 1000/6000 = 1/6, W₂ = 1/3, W₃ = 1/2
  n₁ = 120 × 1/6 = 20
  n₂ = 120 × 1/3 = 40
  n₃ = 120 × 1/2 = 60

STEP 2: Neyman Allocation
  N₁S₁ = 1000×10 = 10,000
  N₂S₂ = 2000×15 = 30,000
  N₃S₃ = 3000×20 = 60,000
  Sum = 100,000
  n₁ = 120 × 10000/100000 = 12
  n₂ = 120 × 30000/100000 = 36
  n₃ = 120 × 60000/100000 = 72

STEP 3: Compare
  Neyman allocates MORE to stratum 3 (largest & most variable)
  Neyman allocates LESS to stratum 1 (smallest & least variable)
```

---

## 13.14 Common Mistakes

| Mistake | Correction |
|---------|------------|
| Using S instead of S² in Neyman | Neyman uses NₕSₕ (standard deviation), not variance |
| Forgetting (1-fₕ) in variance | Include FPC if nₕ/Nₕ not negligible |
| Confusing Proportional and Neyman | Proportional: nₕ ∝ Nₕ; Neyman: nₕ ∝ NₕSₕ |
| Not checking Σnₕ = n | Always verify total sample size matches |
| Using estimated Sₕ for allocation | If Sₕ unknown, use Proportional or pilot study |

---

## 13.15 Diagrams

### Strata Formation
```
Population
┌─────────────────────────────────┐
│  Stratum 1 (Low)   N₁, S₁       │
├─────────────────────────────────┤
│  Stratum 2 (Medium) N₂, S₂       │
├─────────────────────────────────┤
│  Stratum 3 (High)  N₃, S₃        │
└─────────────────────────────────┘
  SRS in each stratum independently
```

### Allocation Comparison
```
Stratum Size:     Small      Medium      Large
Variability:      Low        Medium      High

Proportional:     ████       ████████    ████████████
Neyman:           ██         ████████    ████████████████
Optimal:          ██         ██████████  ██████████████████
```

---

## 13.16 Practice Problems (PYQ Style)

### Problem 1 (Jun 2021)
Stratified sampling: proportional and Neyman allocation for given strata sizes and SDs.

### Problem 2 (Dec 2023)
Stratified sample data - estimate mean and variance.

### Problem 3 (Jun 2025)
Neyman allocation calculation.

### Problem 4 (Various)
A&B transport company example from textbook - strata by freight charges.

---

## 13.17 Exam Tips

- ✅ **Neyman allocation formula**: nₕ = n × (NₕSₕ)/ΣNⱼSⱼ - MEMORIZE!
- ✅ **Proportional vs Neyman**: Know the difference and when each is used
- ✅ **Variance formulas**: With FPC (1 - nₕ/Nₕ)
- ✅ **Relative efficiency**: Neyman always ≤ Proportional
- ✅ **Cost-optimal**: When costs differ across strata
- ✅ **A&B company example**: Understand strata formation by freight charges
- ❌ Don't use variance instead of SD in Neyman allocation
- ❌ Don't forget the FPC term in variance
- ❌ Don't confuse Wₕ (Nₕ/N) with nₕ/n

---

*End of Unit 13 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 13 "Stratified Sampling" - All formulas, definitions, examples (A&B Transport, Apple Orchards, Three Towns, Milk Yield), allocation methods, and Dalenius-Hodges rule verified against original textbook content.