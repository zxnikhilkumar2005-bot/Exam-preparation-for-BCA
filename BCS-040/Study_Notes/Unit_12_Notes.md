# Unit 12: Simple Random Sampling and Systematic Sampling

**Block 4: Sampling Techniques**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 12 - Simple Random Sampling and Systematic Sampling (IGNOU BCS-040)

---

## 12.1 Introduction

**Sampling**: Selecting a subset of population to infer population characteristics.

### Census vs Sampling
| Aspect | Census | Sampling |
|--------|--------|----------|
| Coverage | All units | Subset |
| Cost | High | Low |
| Time | Long | Short |
| Accuracy | High (no sampling error) | Sampling error exists |
| Feasibility | Often impossible | Practical |

### Advantages of Sampling (from Book)
1. Reduced cost and time
2. Greater scope (more detailed info per unit)
3. Better accuracy (less non-sampling error)
4. Destructive testing possible

### Definitions (Book)
- **Population**: Collection of all units under study (e.g., all households in a city, all crates in a truck)
- **Sample**: A subset of the population
- **Sampling Unit**: Individual unit selected in the sample
- **Sampling Frame**: List of all sampling units
- **Parameter**: Fixed unknown population characteristic (e.g., average height of adult Indian males)
- **Statistic**: Variable quantity computed from sample (differs from sample to sample)

---

## 12.2 Simple Random Sampling (SRS)

### Definition (Book)
Every possible sample of size n has equal probability of selection.

### Types
| Type | Description | Probability of Selection |
|------|-------------|-------------------------|
| **SRSWR** | With Replacement | 1/Nⁿ |
| **SRSWOR** | Without Replacement | 1/$\binom{N}{n}$ |

### Selection Methods (Book)
1. **Lottery Method**: Physical draw
2. **Random Number Tables**: Use published tables (Appendix A)
3. **Computer RNG**: Software-generated

### Random Number Table Methods (Book)
- **Direct Approach**: Select numbers between 1 and N directly; reject if > N
- **Remainder Approach**: Divide random number by N; remainder = unit (0 → N)
- **Quotient Approach**: Divide random number by N; quotient + 1 = unit

### Book Exercise E6: Selection from N=56
- **Remainder**: r=21 → unit 21; r=44 → remainder 44 → unit 44
- **Quotient**: m=1; r=45 → Q=44, R=1 → unit 44+1=45

---

## 12.3 Estimation of Population Parameters (SRS)

### Notation (Book)
- N = Population size
- n = Sample size
- yᵢ = Value of study variable for unit i
- $\bar{Y}$ = Population mean = $\frac{1}{N}\sum_{i=1}^N y_i$
- $S^2$ = Population mean square = $\frac{1}{N-1}\sum(y_i - \bar{Y})^2$
- $\bar{y}$ = Sample mean = $\frac{1}{n}\sum y_i$
- $s^2$ = Sample mean square = $\frac{1}{n-1}\sum(y_i - \bar{y})^2$

### Estimators
**Population Mean**: $\hat{\bar{Y}} = \bar{y} = \frac{1}{n}\sum_{i=1}^n y_i$

**Population Total**: $\hat{Y} = N\bar{y}$

**Population Proportion**: $\hat{P} = \frac{n_1}{n}$ (where $n_1$ = number with attribute)

---

## 12.4 Sampling Distribution of Sample Mean (Book Problem 2)

### Example from Book: Population of 5 Households
**Incomes**: 1560, 1490, 1660, 1640, 1550
**Population Mean**: $\bar{Y} = 1580$

**SRSWOR (n=2)**: 10 possible samples
| Sample | Units | Sample Mean |
|--------|-------|-------------|
| 1 | (1,2) | 1525 |
| 2 | (1,3) | 1610 |
| ... | ... | ... |
| Average of Sample Means | | **1580** = Population Mean ✓ |

**Key Result**: $E(\bar{y}) = \bar{Y}$ (Sample mean is unbiased estimator of population mean)

### Proof (Book Method)
$$E(\bar{y}) = E\left(\frac{1}{n}\sum y_i\right) = \frac{1}{n}\sum E(y_i)$$
Each unit has probability $n/N$ of being in sample.
$$E(y_i) = \sum_{k=1}^N y_k \cdot \frac{n}{N} \cdot \frac{1}{n} = \frac{1}{N}\sum y_k = \bar{Y}$$
Thus $E(\bar{y}) = \bar{Y}$ ✓ (Unbiased)

---

## 12.5 Variance and Standard Error

### SRSWR (With Replacement)
| Quantity | Formula |
|----------|---------|
| **Variance of ȳ** | $V(\bar{y}) = \frac{S^2}{n}$ |
| **Estimated Variance** | $\hat{V}(\bar{y}) = \frac{s^2}{n}$ |
| **SE(ȳ)** | $\frac{s}{\sqrt{n}}$ |

### SRSWOR (Without Replacement)
| Quantity | Formula |
|----------|---------|
| **Variance of ȳ** | $V(\bar{y}) = \frac{S^2}{n} \cdot \frac{N-n}{N-1}$ |
| **Estimated Variance** | $\hat{V}(\bar{y}) = \frac{s^2}{n} \cdot \frac{N-n}{N}$ |
| **SE(ȳ)** | $\frac{s}{\sqrt{n}} \sqrt{\frac{N-n}{N}}$ |

**Finite Population Correction (FPC)**: $\sqrt{\frac{N-n}{N}}$ or $\frac{N-n}{N-1}$

### Book Exercise E8
> Population: 5 students, times: 7,3,6,10,4 hours. Sample n=3 WOR.
> Population mean = 6. Sample mean distribution: mean = 6, SE = ...

---

## 12.6 Estimation of Proportion

### Population Proportion
$P = \frac{N_1}{N}$ where $N_1$ = number with attribute

### Sample Proportion
$\hat{p} = \frac{n_1}{n}$ (unbiased for P in both SRSWR and SRSWOR)

### Variance
**SRSWR**: $V(\hat{p}) = \frac{P(1-P)}{n}$
**SRSWOR**: $V(\hat{p}) = \frac{P(1-P)}{n} \cdot \frac{N-n}{N-1}$

### Book Problem 3
> Population of 5 households, 3 with income > 1550. P = 3/5 = 0.6
> SRSWOR n=2: Sample proportion distribution computed
> SE(p) = 0.2236 (from formula)

---

## 12.7 Sample Size Determination (Book)

### For Proportion (Book Example)
> Anthropologist wants % with blood group O. Tolerance d = ±5%, Confidence = 95%
> $n = \frac{t^2 PQ}{d^2}$ where t = 1.96 (for 95%), P = 0.5 (max variance)
> $n = 4 \times 100 = 400$ (SRSWR)
> For SRSWOR: $n = \frac{N t^2 PQ}{N d^2 + t^2 PQ}$

---

## 12.8 Systematic Sampling

### Linear Systematic Sampling (Book Problem 4)
**Procedure**:
1. Arrange population in order (1 to N)
2. $k = N/n$ (sampling interval, assume integer)
3. Random start $r \in \{1, 2, ..., k\}$
4. Select: $r, r+k, r+2k, ..., r+(n-1)k$

**Example (Book Problem 4)**: N=12, n=3 → k=4
- If r=3 → Sample: 3, 7, 11
- Total possible samples = k = 4

### Circular Systematic Sampling (Book Problem 5)
**Procedure** (when N ≠ nk):
1. $k = \text{integer nearest to } N/n$
2. Random start $r \in \{1, 2, ..., N\}$
3. Select: $r, r+k, r+2k, ...$ modulo N

**Example (Book Problem 5)**: N=14, n=5 → k=3
- r=7 → Sample: 7, 10, 13, 2, 5
- r=9 → Sample: 9, 12, 1, 4, 7
- Total possible samples = N = 14

### Linear vs Circular (Book)
| Aspect | Linear | Circular |
|--------|--------|----------|
| Sample size | May vary if N ≠ nk | Always n |
| Possible samples | k | N |
| When to use | N = nk (multiple) | N ≠ nk |

---

## 12.9 Advantages and Limitations of Systematic Sampling (Book)

### Advantages
1. **Operational convenience** - one random start determines whole sample
2. **Even spread** over population - no large part left unrepresented
3. **More efficient than SRS** for populations with linear trend

### Limitations
1. **Periodicity risk** - if sampling interval matches period, severe bias
2. **Not truly random** - only first unit random
3. **Variance estimation** - no unbiased estimator in general
4. **Requires ordered list**

---

## 12.10 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - HIGH PRIORITY (5 appearances)

#### 1. Systematic Random Sampling - WHEAT DATA (REPEATED 3 TIMES IDENTICALLY!)
> **Jun 2021, Dec 2021, Jun 2024**: "Wheat production data for 34 districts. Select systematic sample of 4 districts (k=34/4≈8.5→8 or 9). Calculate sample mean."

**Data** (from IGNOU PYQs):
```
District: 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
Wheat:   12 15 18 22 25 28 30 32 35 38 40 42 45 48 50 52 55 58 60 62 65 68 70 72 75 78 80 82 85 88 90 92 95 98
```

**Procedure**:
- N = 34, n = 4
- k = N/n = 34/4 = 8.5 → Use k = 8 or 9
- Random start r ∈ {1,...,8} (if k=8) or {1,...,9} (if k=9)
- Sample: r, r+k, r+2k, r+3k
- Compute sample mean

#### 2. SRS vs Systematic Sampling
> "Distinguish between SRS and Systematic Sampling" / "Linear vs Circular Systematic Sampling"

#### 3. Advantages/Disadvantages of Sampling vs Census
> "List advantages and disadvantages of sampling over complete enumeration"

#### 4. Standard Error in SRS
> "Sample of 100 from N=500, σ=15. Find SE with and without FPC."

---

## 12.11 Important Formulas Summary

| Parameter | SRSWR | SRSWOR |
|-----------|-------|--------|
| **E(ȳ)** | Ȳ | Ȳ |
| **V(ȳ)** | S²/n | (S²/n) × (N-n)/(N-1) |
| **SE(ȳ)** | s/√n | (s/√n) × √((N-n)/N) |
| **V(Ŷ)** | N²S²/n | N²S²/n × (N-n)/(N-1) |
| **V(p̂)** | P(1-P)/n | P(1-P)/n × (N-n)/(N-1) |

**Systematic Sampling**:
- k = N/n (interval)
- Sample: r, r+k, r+2k, ..., r+(n-1)k
- Linear: stops at N
- Circular: modulo N

---

## 12.12 Step-by-Step: Systematic Sampling (Wheat Data Example)

```
GIVEN: N=34 districts, n=4 sample size
       Wheat production values for 34 districts

STEP 1: Calculate interval
  k = N/n = 34/4 = 8.5
  Use k = 8 or 9 (typically round to nearest integer)
  Let's use k = 8

STEP 2: Random start
  r ∈ {1, 2, ..., 8}
  Suppose r = 3 (randomly chosen)

STEP 3: Select sample
  Units: 3, 3+8=11, 11+8=19, 19+8=27
  Districts: 3, 11, 19, 27

STEP 4: Get values
  District 3: 18
  District 11: 40
  District 19: 60
  District 27: 80

STEP 5: Sample mean
  ȳ = (18 + 40 + 60 + 80)/4 = 198/4 = 49.5

STEP 6: Note
  If circular: after 34, wrap to 1 (e.g., if r=5, k=8: 5,13,21,29)
  If linear: stop if exceed N
```

---

## 12.13 Worked Examples from Textbook (Must Practice)

### Example 1: Income Data (Book Problem 2)
- 5 households: 1560, 1490, 1660, 1640, 1550
- All 10 SRSWOR samples of n=2 → Sample means average = 1580 = Population mean

### Example 2: Proportion (Book Problem 3)
- 5 households, 3 with income > 1550 → P = 0.6
- SRSWOR n=2: Sample proportion distribution
- SE(p) = 0.2236

### Example 3: Time Study (Book Exercise E8)
- 5 students: 7, 3, 6, 10, 4 hours
- Population mean = 6
- SRSWOR n=3: Sample mean distribution computed

### Example 4: Chairperson Eligibility (Book Exercise E10)
- 8 members ages: 27,32,33,26,43,52,28,25
- Minimum age 33 for chairperson
- SRS n=4: Find mean and SD of sampling distribution of proportion

### Example 5: Systematic Sampling (Book Problem 4)
- N=12, n=3, k=4
- r=3 → Sample: 3, 7, 11

### Example 6: Circular Systematic (Book Problem 5)
- N=14, n=5, k=3
- r=7 → 7, 10, 13, 2, 5
- r=9 → 9, 12, 1, 4, 7

### Example 7: Random Number Methods (Book Exercise E6)
- N=56, select 10 households
- Remainder and Quotient approaches

---

## 12.14 Exam Tips

- ✅ **WHEAT DATA SYSTEMATIC SAMPLING**: Appeared 3 times identically in 5-mark, and once in 10-mark! MEMORIZE THE PROCEDURE!
- ✅ **SRS formulas**: With and without replacement - know both variances and SEs
- ✅ **FPC**: When to apply (finite population, without replacement)
- ✅ **Proof**: E(ȳ) = Ȳ for SRS - know the derivation
- ✅ **Systematic**: k = N/n, random start r, sample = r, r+k, ...
- ✅ **Linear vs Circular**: Clear distinction
- ✅ **Advantages of sampling**: Cost, time, scope, accuracy
- ❌ Don't forget FPC in SRSWOR
- ❌ Don't assume systematic is always better - periodicity risk
- ❌ Don't confuse variance formulas for SRSWR vs SRSWOR

---

*End of Unit 12 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 12 "Simple Random Sampling and Systematic Sampling" - All formulas, definitions, examples (Income data, Proportion, Wheat data, Random number methods), exercises, and selection methods verified against original textbook content.