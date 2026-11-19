# Unit 11: Statistical Quality Control (SQC)

**Block 3: Applied Statistical Methods**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 11 - Statistical Quality Control (IGNOU BCS-040)

---

## 11.1 Introduction

**Quality**: Fitness for use / conformance to specifications.

**Statistical Quality Control (SQC)**: Application of statistical methods to monitor and control quality.

### Two Main Categories (from Book)
1. **Statistical Process Control (SPC)**: Control charts for monitoring process
2. **Acceptance Sampling**: Inspecting samples to accept/reject lots

### Quality Characteristics (from Book)
- **Variables**: Measurable characteristics (length, weight, diameter, time)
- **Attributes**: Non-measurable characteristics (defective/non-defective, pass/fail)

---

## 11.2 Concept of Variation

### Chance Causes (Common Causes) - from Book
- Inherent, random variation
- Many small, uncontrollable factors
- Process is **stable** / **in control**
- Cannot be eliminated economically

### Assignable Causes (Special Causes) - from Book
- Identifiable, specific factors
- Machine malfunction, operator error, material defect
- Process is **unstable** / **out of control**
- Can and should be eliminated

### Control Chart Purpose (Book)
- Distinguish chance vs assignable causes
- Signal when assignable causes present
- Maintain process stability

---

## 11.3 Control Charts for Variables (X-bar and R Charts)

### When to Use
Quality characteristic is **measurable** (length, weight, diameter, time, etc.)

### Rational Subgroups (Book Definition)
- Subgroup = sample collected at same time under similar conditions
- Within-subgroup variation = chance causes only
- Between-subgroup variation = chance + assignable causes
- Typical subgroup size: n = 4, 5, or 6

### X-bar Chart (Controls Process Mean)
**Control Limits**:
- $CL = \bar{\bar{X}}$ (grand mean)
- $UCL = \bar{\bar{X}} + A_2 \bar{R}$
- $LCL = \bar{\bar{X}} - A_2 \bar{R}$

Where $\bar{R}$ = average range, $A_2$ = constant from table

### R Chart (Controls Process Variability)
**Control Limits**:
- $CL = \bar{R}$
- $UCL = D_4 \bar{R}$
- $LCL = D_3 \bar{R}$

Where $D_3$, $D_4$ = constants from table

### Control Chart Constants (Book Table 2)

| n | A₂ | D₃ | D₄ | d₂ |
|---|-----|-----|-----|-----|
| 2 | 1.880 | 0 | 3.267 | 1.128 |
| 3 | 1.023 | 0 | 2.574 | 1.693 |
| 4 | 0.729 | 0 | 2.282 | 2.059 |
| 5 | 0.577 | 0 | 2.114 | 2.326 |
| 6 | 0.483 | 0 | 2.004 | 2.534 |
| 7 | 0.419 | 0.076 | 1.924 | 2.704 |
| 8 | 0.373 | 0.136 | 1.864 | 2.847 |
| 9 | 0.337 | 0.184 | 1.816 | 2.970 |
| 10 | 0.308 | 0.223 | 1.777 | 3.078 |

### Estimation of Process Parameters
- **Process Mean**: $\hat{\mu} = \bar{\bar{X}}$
- **Process SD**: $\hat{\sigma} = \bar{R} / d_2$

---

## 11.4 Worked Example from Textbook: Refill Length (Main Example)

### Problem 1
**Data**: 20 subgroups of size 5 (Table 1 - refill lengths)
- Subgroup averages and ranges given
- Specifications: 10 ± 0.2 cm (LSL=9.80, USL=10.20)

### Solution from Book
**Step 1: Compute Grand Statistics**
- $\bar{\bar{X}} = \frac{10.116 + 10.094 + ... + 10.066}{20} = 10.09$
- $\bar{R} = \frac{0.07 + 0.07 + ... + 0.15}{20} = 0.175$

**Step 2: Get Constants for n=5**
- $A_2 = 0.577$, $D_3 = 0$, $D_4 = 2.11$, $d_2 = 2.326$

**Step 3: X-bar Chart Limits**
- $CL = 10.09$
- $UCL = 10.09 + 0.577 \times 0.175 = 10.19$
- $LCL = 10.09 - 0.577 \times 0.175 = 9.99$

**Step 4: R Chart Limits**
- $CL = 0.175$
- $UCL = 2.11 \times 0.175 = 0.369$
- $LCL = 0 \times 0.175 = 0$

**Step 5: Process Parameters**
- $\hat{\mu} = 10.09$
- $\hat{\sigma} = 0.175 / 2.326 = 0.0752$

### Book Exercise E2: Cricket Ball Weight
- 25 samples, n=4
- $\sum \bar{X} = 7575$ grams, $\sum R = 154$ grams
- $\bar{\bar{X}} = 303$, $\bar{R} = 6.16$
- Constants for n=4: $A_2=0.729$, $D_3=0$, $D_4=2.282$, $d_2=2.059$
- X-chart: CL=303, UCL=307.49, LCL=298.51
- R-chart: CL=6.16, UCL=14.05, LCL=0

---

## 11.5 Process Capability Analysis

### Capability Indices (from Book)
**Cp (Process Capability)**:
$$C_p = \frac{USL - LSL}{6\sigma} = \frac{\text{Specification Width}}{6\sigma}$$

**Cpk (Process Capability Index)**:
$$C_{pk} = \min\left(\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma}\right)$$

### Interpretation (Book)
| Cp / Cpk | Interpretation |
|----------|----------------|
| < 1.00 | Not capable |
| 1.00 - 1.33 | Marginally capable |
| 1.33 - 1.67 | Capable |
| > 1.67 | Highly capable |

**Note**: $C_{pk} \leq C_p$. If process centered, $C_{pk} = C_p$.

---

## 11.6 Control Charts for Attributes

### When to Use
Quality characteristic is **countable** (defectives, defects, nonconformities)

### p-Chart (Fraction Defective)
- **Statistic**: $\bar{p} = \frac{\text{Total defectives}}{\text{Total inspected}}$
- **Control Limits**:
  - $CL = \bar{p}$
  - $UCL = \bar{p} + 3\sqrt{\frac{\bar{p}(1-\bar{p})}{n}}$
  - $LCL = \bar{p} - 3\sqrt{\frac{\bar{p}(1-\bar{p})}{n}}$ (set to 0 if negative)
- **Use when**: Sample size constant or variable (different limits per sample)

### np-Chart (Number Defective)
- **Use when**: Constant sample size n
- **Control Limits**:
  - $CL = n\bar{p}$
  - $UCL = n\bar{p} + 3\sqrt{n\bar{p}(1-\bar{p})}$
  - $LCL = n\bar{p} - 3\sqrt{n\bar{p}(1-\bar{p})}$

### c-Chart (Defects per Unit)
- **Statistic**: $\bar{c} = \frac{\text{Total defects}}{\text{Number of units}}$
- **Control Limits**:
  - $CL = \bar{c}$
  - $UCL = \bar{c} + 3\sqrt{\bar{c}}$
  - $LCL = \bar{c} - 3\sqrt{\bar{c}}$ (set to 0 if negative)
- **Use when**: Area of opportunity constant

### u-Chart (Defects per Unit, Variable Area)
- **Control Limits** (per unit):
  - $UCL = \bar{u} + 3\sqrt{\frac{\bar{u}}{n}}$
  - $LCL = \bar{u} - 3\sqrt{\frac{\bar{u}}{n}}$

---

## 11.7 Acceptance Sampling

### Purpose
Decide whether to accept or reject a lot based on sample inspection.

### Single Sampling Plan (Book Definition)
**Parameters**:
- $N$ = Lot size
- $n$ = Sample size
- $c$ = Acceptance number (max defectives to accept)

**Procedure**:
1. Randomly select n items from lot
2. Count defectives $d$
3. If $d \leq c$ → Accept lot
4. If $d > c$ → Reject lot

### Risks (from Book)
| | Good Lot (p ≤ AQL) | Bad Lot (p ≥ LTPD) |
|---|-------------------|-------------------|
| **Accept** | Correct (1 - α) | **Consumer's Risk (β)** |
| **Reject** | **Producer's Risk (α)** | Correct (1 - β) |

- **AQL** (Acceptable Quality Level): Max % defective considered acceptable
- **LTPD** (Lot Tolerance Percent Defective): % defective considered unacceptable
- **α** (Producer's Risk): P(Reject \| Good lot) - typically 0.05
- **β** (Consumer's Risk): P(Accept \| Bad lot) - typically 0.10

### Operating Characteristic (OC) Curve
Plot of $P_a(p)$ = Probability of acceptance vs lot fraction defective $p$.

For single sampling (binomial):
$$P_a(p) = \sum_{d=0}^{c} \binom{n}{d} p^d (1-p)^{n-d}$$

For large n, small p: Poisson approximation with $np$.

---

## 11.8 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - MEDIUM PRIORITY (3 appearances)

#### 1. X-bar and R Chart Limits
> "Given subgroup data (n=5), compute control limits for X-bar and R charts. Constants A₂, D₃, D₄ given."

**Solution**:
1. Compute $\bar{X}_i$ and $R_i$ for each subgroup
2. $\bar{\bar{X}} = \frac{\sum \bar{X}_i}{k}$, $\bar{R} = \frac{\sum R_i}{k}$
3. X-chart: $CL = \bar{\bar{X}}$, $UCL/LCL = \bar{\bar{X}} \pm A_2\bar{R}$
4. R-chart: $CL = \bar{R}$, $UCL = D_4\bar{R}$, $LCL = D_3\bar{R}$

#### 2. Control Chart Interpretation / Short Notes
> "Short note on X-chart / control charts for variables" (Dec 2024)

#### 3. Process Capability
> "Given USL, LSL, process mean and SD, compute Cp and Cpk."

---

## 11.9 Important Formulas Summary

| Chart | Center Line | UCL | LCL |
|-------|-------------|-----|-----|
| **X-bar** | $\bar{\bar{X}}$ | $\bar{\bar{X}} + A_2\bar{R}$ | $\bar{\bar{X}} - A_2\bar{R}$ |
| **R** | $\bar{R}$ | $D_4\bar{R}$ | $D_3\bar{R}$ |
| **p** | $\bar{p}$ | $\bar{p} + 3\sqrt{\frac{\bar{p}(1-\bar{p})}{n}}$ | $\bar{p} - 3\sqrt{\frac{\bar{p}(1-\bar{p})}{n}}$ |
| **np** | $n\bar{p}$ | $n\bar{p} + 3\sqrt{n\bar{p}(1-\bar{p})}$ | $n\bar{p} - 3\sqrt{n\bar{p}(1-\bar{p})}$ |
| **c** | $\bar{c}$ | $\bar{c} + 3\sqrt{\bar{c}}$ | $\bar{c} - 3\sqrt{\bar{c}}$ |
| **u** | $\bar{u}$ | $\bar{u} + 3\sqrt{\frac{\bar{u}}{n}}$ | $\bar{u} - 3\sqrt{\frac{\bar{u}}{n}}$ |

**Process Capability**:
- $C_p = \frac{USL - LSL}{6\sigma}$
- $C_{pk} = \min\left(\frac{USL-\mu}{3\sigma}, \frac{\mu-LSL}{3\sigma}\right)$
- $\hat{\sigma} = \bar{R}/d_2$

---

## 11.10 Step-by-Step: X-bar and R Chart Construction (Book Method)

```
STEP 1: Collect Data
  k subgroups, each of size n (typically 4-6)
  Example: 20 subgroups of 5 refills each

STEP 2: Compute Subgroup Statistics
  For each subgroup i:
    X̄ᵢ = mean of n observations
    Rᵢ = max - min of n observations

STEP 3: Compute Grand Statistics
  X̄̄ = ΣX̄ᵢ / k
  R̄ = ΣRᵢ / k

STEP 4: Get Constants (from table for given n)
  A₂, D₃, D₄, d₂

STEP 5: Calculate Control Limits
  X-chart:
    CL = X̄̄
    UCL = X̄̄ + A₂ × R̄
    LCL = X̄̄ - A₂ × R̄
  R-chart:
    CL = R̄
    UCL = D₄ × R̄
    LCL = D₃ × R̄

STEP 6: Plot Charts
  X-axis: Subgroup number (1 to k)
  Y-axis: X̄ᵢ values (X-chart) or Rᵢ values (R-chart)
  Draw CL, UCL, LCL lines
  Plot points and connect

STEP 7: Interpret
  All points within limits + no patterns → In control
  Points outside limits or patterns → Out of control (assignable cause)

STEP 8: Estimate Process Parameters
  μ̂ = X̄̄
  σ̂ = R̄ / d₂
  Cp = (USL - LSL) / (6σ̂)
  Cpk = min((USL - μ̂)/(3σ̂), (μ̂ - LSL)/(3σ̂))
```

---

## 11.11 Common Mistakes

| Mistake | Correction |
|---------|------------|
| Using wrong constants for n | Check n (subgroup size) in table |
| Plotting R-chart before X-chart | Plot R-chart FIRST - if R out of control, X-chart limits invalid |
| Not checking R-chart first | Variability must be in control before mean |
| Using σ instead of R̄/d₂ | For X-bar/R charts, use R̄/d₂ |
| Confusing p-chart and np-chart | p-chart: fraction defective; np-chart: number defective (constant n) |
| Forgetting LCL = 0 for attribute charts | LCL cannot be negative for p, np, c, u |

---

## 11.12 Diagrams

### X-bar and R Charts
```
X̄-CHART                    R-CHART
     │                         │
UCL──┤───●───●                UCL──┤●───●
     │     ●                   │    ●
CL──┤───────────●              CL──┤──────●
     │●                          │
LCL──┤────●                       LCL──┤
     │                            │
     └─────────────────           └─────────────────
       Subgroup #                   Subgroup #
```

### Process Capability
```
SPECIFICATIONS:    LSL                    USL
                    │                     │
PROCESS:         ┌───────┐
                  ▼       ▼
               μ̂ ± 3σ̂

Cp = (USL-LSL)/6σ̂
Cpk = min distance to spec / 3σ̂
```

---

## 11.13 Practice Problems (PYQ Style)

### Problem 1 (Dec 2023)
Given refill length data (20 subgroups, n=5). Compute X-bar and R chart limits.

### Problem 2 (Dec 2024)
Short note on X-chart / control charts.

### Problem 3 (Jun 2025)
Control chart limits computation / interpretation.

### Problem 4 (Various)
Cricket ball weight: 25 samples of size 4. ΣX̄ = 7575g, ΣR = 154g. Find limits.

---

## 11.14 Exam Tips

- ✅ **X-bar and R chart formulas**: Memorize with constants A₂, D₃, D₄
- ✅ **R-chart FIRST**: Always check variability before mean
- ✅ **Constants table**: Know how to use for n=4,5,6
- ✅ **Process capability**: Cp and Cpk formulas
- ✅ **Attribute charts**: p, np, c, u - know when to use each
- ✅ **Acceptance sampling**: Single sampling plan, AQL, LTPD, α, β
- ❌ Don't use X-chart limits if R-chart out of control
- ❌ Don't forget LCL = 0 for attribute charts (no negative limits)
- ❌ Don't confuse subgroup size (n) with number of subgroups (k)

---

*End of Unit 11 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 11 "Statistical Quality Control" - All formulas, definitions, examples (Refill length, Cricket ball weight), control chart constants, and acceptance sampling verified against original textbook content.