# Unit 14: Cluster and Multistage Sampling

**Block 4: Sampling Techniques**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 14 - Cluster Sampling and Multistage Sampling (IGNOU BCS-040)

---

## 14.1 Introduction

**Cluster Sampling**: Population divided into clusters (groups), random sample of clusters selected, all units in selected clusters surveyed.

**Multistage Sampling**: Extension of cluster sampling - sample clusters, then sample within clusters (2+ stages).

### When to Use (from Book)
- No complete sampling frame of individual units
- Population geographically dispersed
- Cost of listing all units prohibitive
- Natural clusters exist (villages, schools, households)
- Travel cost reduction important

### Cluster vs Stratified (Book Comparison)
| Aspect | Stratified Sampling | Cluster Sampling |
|--------|---------------------|------------------|
| **Homogeneity** | Within strata | Within clusters |
| **Heterogeneity** | Between strata | Between clusters |
| **Efficiency** | Usually > SRS | Usually < SRS |
| **Purpose** | Precision | Cost reduction |
| **Sampling** | From EVERY stratum | Only SELECTED clusters |

**Key Book Insight**: "While stratification may reduce sampling error, clustering tends to decrease costs and increase sampling error for the same size of sample."

---

## 14.2 Cluster Sampling (Single-Stage)

### Design
1. Divide population into N clusters
2. Select n clusters by SRSWOR
3. Survey ALL units in selected clusters

### Notation (Book Table 1)
| Symbol | Meaning |
|--------|---------|
| N | Number of clusters in population |
| n | Number of clusters in sample |
| Mᵢ | Number of units in cluster i |
| M = ΣMᵢ | Total population size |
| ȳᵢ | Mean of cluster i |
| Yᵢ = Mᵢȳᵢ | Total of cluster i |

---

## 14.3 Estimation (Unequal Cluster Sizes)

### Population Mean (Ratio Estimator)
$$\bar{y}_{cl} = \frac{\sum Y_i}{\sum M_i} = \frac{\text{Sample total}}{\text{Sample size}}$$

### Population Total
$$\hat{Y}_{cl} = M \bar{y}_{cl}$$

### Variance
$$V(\bar{y}_{cl}) = \frac{N-n}{Nn} \cdot \frac{1}{n-1} \sum_{i=1}^n (Y_i - M_i \bar{y}_{cl})^2 \cdot \frac{1}{\bar{M}^2}$$

### Estimated Variance
$$\hat{V}(\bar{y}_{cl}) = \frac{N-n}{Nn} \cdot \frac{1}{n-1} \sum_{i=1}^n (Y_i - M_i \bar{y}_{cl})^2 \cdot \frac{1}{\bar{M}^2}$$

---

## 14.4 Estimation (Equal Cluster Sizes: Mᵢ = M₀)

### Population Mean
$$\bar{y}_{cl} = \frac{1}{n}\sum_{i=1}^n \bar{y}_i = \frac{1}{nM_0}\sum_{i=1}^n Y_i$$

### Variance
$$V(\bar{y}_{cl}) = \frac{S_b^2}{n}\left(1 - \frac{n}{N}\right)$$

Where $S_b^2 = \frac{1}{N-1}\sum_{i=1}^N (\bar{Y}_i - \bar{Y})^2$ = between-cluster variance

### Estimated Variance
$$\hat{V}(\bar{y}_{cl}) = \frac{S_b^2}{n}\left(1 - \frac{n}{N}\right)$$

Where $S_b^2 = \frac{1}{n-1}\sum_{i=1}^n (\bar{y}_i - \bar{y}_{cl})^2$

---

## 14.5 Worked Examples from Textbook

### Example 1: Guava Trees (Problem 1)
**Data**: 5 clusters of 4 trees each from 20 trees
| Cluster | Yields (kg) | Yᵢ |
|---------|-------------|-----|
| 1 | 5, 4, 1, 15 | 25 |
| 2 | 6, 8, 4, 5 | 23 |
| 3 | 20, 18, 22, 16 | 76 |
| 4 | 10, 12, 11, 11 | 44 |
| 5 | 8, 10, 12, 8 | 38 |

**Results**: Yc = 41.2, M = 20, ȳ = 41.2

---

### Example 2: Apple Yield (Problem 2 - Unequal Clusters)
**Data**: 3 clusters from 15, average M = 10
| Cluster | Mᵢ | Yᵢ |
|---------|-----|-----|
| 1 | 12 | 181.03 |
| 2 | 10 | 205.61 |
| 3 | 6 | 105.57 |

**Results**: 
- $\bar{y}_c = 16.407$ kg
- $\hat{V}(\bar{y}_c) = 79.0$
- SE = 8.89 kg

---

### Example 3: Apple Yield (Problem 3 - Equal Clusters)
**Data**: 10 clusters of 3 trees each from 300 trees
**Result**: $\bar{y}_c = 24.94$ kg, SE = 4.299 kg

---

## 14.6 Efficiency of Cluster Sampling vs SRS

### Design Effect (deff)
$$\text{deff} = \frac{V(\bar{y}_{cl})}{V(\bar{y}_{srs})}$$

### Intra-Class Correlation (ρ)
$$\rho = \frac{\text{Between-cluster variance}}{\text{Total variance}} = \frac{S_b^2}{S_b^2 + S_w^2}$$

### Relationship (Equal Clusters)
$$\text{deff} = 1 + (M_0 - 1)\rho$$

- **ρ > 0**: Clusters heterogeneous internally → deff > 1 → Cluster LESS efficient
- **ρ < 0**: Clusters homogeneous internally → deff < 1 → Cluster MORE efficient
- **ρ = 0**: Same efficiency as SRS

**Typically**: ρ > 0 (units in same cluster similar) → Cluster sampling less efficient than SRS.

**Why still use?**: Cost savings often outweigh efficiency loss.

---

## 14.7 Worked Example from Textbook: Telephone Calls (Problem 4)

### Data
- N = 25 centres, n = 5 centres, M = 4 phones each
- Cluster means: 31.00, 33.75, 28.25, 32.50, 30.25

### Results
- $\bar{y}_c = 31.15$ calls/phone
- $V(\bar{y}_c) = 2.0081$
- RE = 1.05 (Cluster sampling MORE efficient than SRS!)

---

## 14.8 Two-Stage Sampling

### Design
1. **First Stage**: Select n clusters (PSUs - Primary Sampling Units) by SRSWOR
2. **Second Stage**: From each selected cluster, select m units (SSUs - Secondary Sampling Units) by SRSWOR

### Notation (Book Table 3)
- N = number of PSUs in population
- n = number of PSUs in sample
- M = number of SSUs in each PSU (equal size)
- m = number of SSUs selected from each PSU
- Yᵢⱼ = value for j-th SSU in i-th PSU

---

## 14.9 Estimation in Two-Stage Sampling

### Population Mean
$$\bar{y}_{2s} = \frac{1}{n}\sum_{i=1}^n \bar{y}_i$$

### Variance
$$V(\bar{y}_{2s}) = \frac{S_b^2}{n}\left(1 - \frac{n}{N}\right) + \frac{S_w^2}{nm}\left(1 - \frac{m}{M}\right)$$

Where:
- $S_b^2$ = between-PSU variance
- $S_w^2$ = within-PSU variance

### Estimated Variance
$$\hat{V}(\bar{y}_{2s}) = \frac{1-f_1}{n} s_b^2 + \frac{f_1(1-f_2)}{nm} s_w^2$$

Where $f_1 = n/N$, $f_2 = m/M$

---

## 14.10 Worked Example from Textbook: Telephone Calls (Problem 5)

### Data
- N = 25 centres, n = 5, M = 4, m = 2
- Cluster means: 31.00, 33.75, 28.25, 32.50, 30.25

### Results
- $\bar{y}_{2s} = 31.15$ calls/phone
- $\hat{V}(\bar{y}_{2s}) = 2.0081$ (same as cluster sampling here because m=2)

---

## 14.11 Multistage Sampling (3+ Stages)

### General Principle
Extend two-stage logic: sample PSUs → SSUs → TSUs (Third Stage Units) → ...

### Example: National Survey
1. **Stage 1**: Sample districts (PSUs)
2. **Stage 2**: Sample villages/blocks within districts (SSUs)
3. **Stage 3**: Sample households within villages (TSUs)
4. **Stage 4**: Sample individuals within households (USUs)

### Variance Decomposition
Total variance = Σ (Stage k contribution)

Each stage adds a variance component depending on between-unit variability at that level.

---

## 14.12 Probability Proportional to Size (PPS) Sampling

### When to Use
Clusters have very different sizes, want to give larger clusters higher selection probability.

### Methods
1. **PPS with Replacement (PPSWR)**:
   - $P(\text{select cluster } i) = M_i / M$
   - Hansen-Hurwitz estimator

2. **PPS without Replacement (PPSWOR)**:
   - More complex (e.g., Lahiri's method, Brewer's method)
   - Horvitz-Thompson estimator

---

## 14.13 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - LOW PRIORITY (1 appearance)

#### 1. Cluster Sampling (Short Note)
> **Jun 2021**: "Write short note on cluster sampling."

**Key Points**:
- Definition and procedure
- Equal vs unequal cluster sizes
- Estimation of mean/total
- Efficiency comparison with SRS (deff, ρ)
- Advantages: cost, frame availability
- Disadvantages: less efficient if ρ > 0

#### 2. Two-Stage Sampling (Conceptual)
> "Explain two-stage sampling with example."

---

## 14.14 Important Formulas Summary

| Design | Mean Estimator | Variance (Approx) |
|--------|----------------|-------------------|
| **Cluster (equal M)** | $\frac{1}{n}\sum \bar{y}_i$ | $\frac{S_b^2}{n}(1-\frac{n}{N})$ |
| **Cluster (unequal M)** | $\frac{\sum Y_i}{\sum M_i}$ | $\frac{1}{n\bar{M}^2}(1-\frac{n}{N})\frac{1}{N-1}\sum(Y_i-\bar{M}\bar{Y}_i)^2$ |
| **Two-Stage (equal)** | $\frac{1}{n}\sum \bar{y}_i$ | $\frac{S_b^2}{n}(1-f_1) + \frac{S_w^2}{nm}(1-f_2)$ |
| **deff** | $1 + (M_0-1)\rho$ | |
| **ρ** | $\frac{S_b^2}{S_b^2+S_w^2}$ | |

---

## 14.15 Step-by-Step: Cluster Sampling Efficiency

```
GIVEN: N=100 clusters, M₀=20 units each
       S_b² = 25, S_w² = 75
       SRS sample size n = 200 units

STEP 1: Intra-class correlation
  ρ = S_b² / (S_b² + S_w²) = 25 / (25+75) = 0.25

STEP 2: Design effect
  deff = 1 + (M₀-1)ρ = 1 + 19×0.25 = 1 + 4.75 = 5.75

STEP 3: Interpretation
  Cluster sampling variance is 5.75× SRS variance
  Need 5.75× larger sample for same precision
  OR: SRS with n=200 equivalent to cluster with n=1150

STEP 4: When still worthwhile?
  If cluster sampling cost per unit is < 1/5.75 of SRS cost
```

---

## 14.16 Common Mistakes

| Mistake | Correction |
|---------|------------|
| Assuming cluster sampling always more efficient | Usually LESS efficient (ρ > 0) |
| Forgetting deff = 1 + (M₀-1)ρ | Key formula for efficiency comparison |
| Using SRS variance formula for cluster data | Must use between-cluster variance |
| Confusing one-stage and two-stage | One-stage: all units in selected clusters; Two-stage: subsample within clusters |
| Ignoring cost considerations | Cluster sampling used for COST reasons, not precision |

---

## 14.17 Diagrams

### Cluster Sampling Design
```
Population (N=10 clusters)
┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐
│●●│ │○○│ │●○│ │○○│ │●●│ │○○│ │●○│ │○○│ │●●│ │○○│  ← All units surveyed in selected clusters
└──┘ └──┘ └──┘ └──┘ └──┘ └──┘ └──┘ └──┘ └──┘ └──┘
   ↑                              ↑
Selected clusters (n=3)           Not selected
```

### Two-Stage Sampling
```
Stage 1: Select clusters (PSUs)
┌──┐    ┌──┐    ┌──┐    ┌──┐    ┌──┐
│▓▓│    │░░│    │▓▓│    │░░│    │▓▓│  ← 3 clusters selected
└──┘    └──┘    └──┘    └──┘    └──┘

Stage 2: Sample within clusters (SSUs)
Cluster 1:     ● ○ ● ○ ●       (sample m from M)
Cluster 3:     ○ ● ○ ○ ●
Cluster 5:     ● ● ○ ○ ○
```

### Intra-Class Correlation
```
ρ HIGH (≈1):     Clusters very different internally, similar within
  Cluster 1: AAAAAAAAA
  Cluster 2: BBBBBBBBB
  Cluster 3: CCCCCCCCC

ρ LOW (≈0):      Clusters similar internally
  Cluster 1: ABCDABCD
  Cluster 2: BCDABCDA
  Cluster 3: CDABCDAB

ρ NEGATIVE:      Clusters more diverse than population (rare)
```

---

## 14.18 Practice Problems (PYQ Style)

### Problem 1 (Jun 2021)
Short note on cluster sampling - definition, procedure, efficiency.

### Problem 2 (Textbook Examples)
- Cluster sampling with equal/unequal sizes
- Two-stage sampling variance calculation

---

## 14.19 Exam Tips

- ✅ **Short note on cluster sampling**: Low priority but easy marks
- ✅ **Know deff formula**: deff = 1 + (M₀-1)ρ
- ✅ **Understand ρ**: Between-cluster vs within-cluster variance
- ✅ **Two-stage vs one-stage**: Subsampling within clusters
- ✅ **When to use**: No frame, geographical dispersion, cost
- ❌ Don't assume cluster sampling is more precise
- ❌ Don't confuse with stratified sampling (stratified = sample FROM each group; cluster = sample OF groups)
- ❌ Don't forget cost-efficiency tradeoff

---

## 14.20 Comparison: Stratified vs Cluster Sampling

| Aspect | Stratified Sampling | Cluster Sampling |
|--------|---------------------|------------------|
| **Division** | All strata sampled | Sample of clusters |
| **Homogeneity** | Within strata | Within clusters |
| **Heterogeneity** | Between strata | Between clusters |
| **Efficiency** | Usually > SRS | Usually < SRS |
| **Purpose** | Precision | Cost reduction |
| **Sampling** | From EVERY stratum | Only SELECTED clusters |

---

*End of Unit 14 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 14 "Cluster Sampling and Multistage Sampling" - All formulas, definitions, examples (Guava trees, Apple yield, Telephone calls, Two-stage), and exercises verified against original textbook content.