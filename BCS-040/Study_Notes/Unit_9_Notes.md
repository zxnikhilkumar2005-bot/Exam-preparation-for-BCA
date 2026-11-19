# Unit 9: Regression Analysis

**Block 3: Applied Statistical Methods**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 9 - Regression Analysis (IGNOU BCS-040)

---

## 9.1 Introduction

**Regression Analysis**: Statistical technique to model the relationship between a dependent variable (Y) and one or more independent variables (X).

### Simple Linear Regression
One independent variable X, one dependent variable Y.
Model: $Y = \alpha + \beta X + \epsilon$

Where:
- $\alpha$ = intercept
- $\beta$ = slope
- $\epsilon$ = random error ~ N(0, σ²)

### Terminology (from Book)
| Term | Symbol | Description |
|------|--------|-------------|
| **Dependent Variable** | Y | Response, predicted variable |
| **Independent Variable** | X | Regressor, predictor |
| **Parameters** | α, β | Population intercept and slope |
| **Estimates** | a, b | Sample intercept and slope |
| **Residual** | $e_i = y_i - \hat{y}_i$ | Error in prediction |

---

## 9.2 Scatter Diagram

**First step**: Plot (xᵢ, yᵢ) pairs to visually assess linear relationship.

### Patterns (from Book)
- **Positive linear**: Points trend upward (e.g., Setting Time vs SO₃)
- **Negative linear**: Points trend downward
- **No linear**: Random scatter
- **Curvilinear**: Curved pattern (not suitable for simple linear regression)

---

## 9.3 Least Squares Estimation

### Model
$\hat{y} = a + bx$ where $\hat{y}$ = predicted value

### Normal Equations (Book Method - Four Steps)
1. **Calculate Sₓₓ**: $S_{xx} = \sum x_i^2 - \frac{(\sum x_i)^2}{n} = \sum(x_i - \bar{x})^2$
2. **Calculate Sₓᵧ**: $S_{xy} = \sum x_i y_i - \frac{\sum x_i \sum y_i}{n} = \sum(x_i - \bar{x})(y_i - \bar{y})$
3. **Calculate Slope**: $b = \frac{S_{xy}}{S_{xx}}$
4. **Calculate Intercept**: $a = \bar{y} - b\bar{x}$

### Alternative Formulas (Equivalent)
**Slope**:
$$b = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2} = \frac{S_{xy}}{S_{xx}}$$

**Intercept**:
$$a = \bar{y} - b\bar{x} = \frac{\sum y}{n} - b\frac{\sum x}{n}$$

Where:
- $S_{xx} = \sum x^2 - \frac{(\sum x)^2}{n} = \sum(x - \bar{x})^2$
- $S_{xy} = \sum xy - \frac{\sum x \sum y}{n} = \sum(x - \bar{x})(y - \bar{y})$

---

## 9.4 Worked Examples from Textbook (Must Practice)

### Example 1: Cement Setting Time vs SO₃ (Main Example - Table 1)
**Data**: 25 cement samples, x = % SO₃, y = setting time (minutes)

**Sums from Book**:
- $\sum x = 39.04$
- $\sum y = 4217$
- $\sum x^2 = 64.446$
- $\sum y^2 = 726539$
- $\sum xy = ?$ (not directly given, but computed below)

**Means**:
- $\bar{x} = 39.04/25 = 1.5616$
- $\bar{y} = 4217/25 = 168.68$

**Corrected Sums of Squares (Book values)**:
- $S_{xx} = 3.4811$
- $S_{xy} = 191.2328$

**Regression Coefficients (Book)**:
- $b = S_{xy}/S_{xx} = 191.2328/3.4811 = 54.943$
- $a = \bar{y} - b\bar{x} = 168.68 - 54.943 \times 1.5616 = 82.88$

**Best Linear Prediction Formula**:
$$\hat{y} = 82.88 + 54.943x$$

**Comparison with Ad-hoc Lines (Book Exercise E1, E2, E3)**:
| Line | Formula | Residuals at x=0.96 |
|------|---------|---------------------|
| Ad-hoc 1 | y = 90 + 50x | e₁₂ = 0, e₁₉ = 2 |
| Ad-hoc 2 | y = 100 + 45x | Different residuals |
| **Least Squares** | **y = 82.88 + 54.943x** | **Best fit (smallest residuals)** |

---

### Example 2: Exercise E4 - Second SO₃ Data Set (Table 4)
**Data**: 15 observations (different sample)

**Sums from Book**:
- $\sum x = 22.59$
- $\sum x^2 = 36.7135$
- $\sum y = 2479$
- $\sum y^2 = 511637$ (approx)
- n = 15

**Result from Book**: $\hat{y} = 88.05 + 51.273x$

**Key Point**: Values of a and b depend on the sample of observations. Should use $\hat{a}$ and $\hat{b}$ to indicate estimates.

---

### Example 3: Hosiery Mill Cost vs Output (Problem 1 - Table 5)
**Data**: 9 months, x = output (tons), y = cost (thousands of $)

**Sums from Book**:
- $\sum x = 340$
- $\sum y = 303$
- $\sum xy = 319$
- n = 9

**Means**:
- $\bar{x} = 340/9 = 37.78$
- $\bar{y} = 303/9 = 33.67$

**Calculations (Book)**:
- $S_{xx} = \sum x^2 - (\sum x)^2/n$ (computed from data)
- $S_{xy} = \sum xy - (\sum x \sum y)/n = 319 - (340 \times 303)/9$
- $b = S_{xy}/S_{xx}$
- $a = \bar{y} - b\bar{x}$

**Prediction**: For x = 4 tons, $\hat{y} = a + b(4) = 4.274$ (thousands of $) = **$4,274**

---

### Example 4: Income vs Savings (Exercise E5)
**Data**: 9 families, x = income ($000s), y = savings ($000s)
| Income (x) | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Savings (y) | 0.0 | 0.1 | 0.2 | 0.2 | 0.5 | 0.5 | 0.6 | 0.7 | 0.8 |

**Book asks**: Work out the best linear regression formula.

---

## 9.5 PYQ-Specific Examples (Critical for Exam)

### Example 5: Speed vs Stopping Distance (MEMORIZE - Appeared 2 Times Identically!)
**PYQ Pattern**: This exact problem appeared in **Dec 2022** and **Jun 2024** identically.

**Typical Data Pattern** (from PYQs):
| Speed (X) | Stopping Distance (Y) |
|-----------|----------------------|
| 30 | 15 |
| 40 | 25 |
| 50 | 40 |
| 60 | 55 |
| 70 | 75 |

**Required Analysis** (10-mark question):
1. Scatter diagram
2. Regression equation Y on X
3. Correlation coefficient (r)
4. Coefficient of determination (R²)
5. Test significance of regression
6. Prediction for given speed
7. Confidence/prediction intervals

**Note**: Since this appeared identically twice, memorize the complete solution procedure.

---

### Example 5: BP vs Age (PYQ Dec 2021 - 10 Mark Question)
**Typical Data Pattern**: Blood Pressure (Y) vs Age (X)

**Required Analysis** (10-mark question):
1. Scatter diagram
2. Regression equation Y on X
3. Correlation coefficient (r) and R²
4. Test significance of regression
5. Prediction for given age
6. Confidence/prediction intervals
7. Residual analysis

---

### Example 6: IT Company Output vs Cost (PYQ Jun 2024 - 10 Mark Question)
**Typical Data Pattern**: Output (Y) vs Cost (X)

**Required Analysis** (10-mark question):
1. Scatter diagram
2. Regression equation Y on X
3. Correlation coefficient (r) and R²
4. Test significance of regression
5. Prediction for given cost/output
6. Confidence/prediction intervals

---

### Example 6: Cost vs Sales (PYQ Dec 2023 - 10 Mark Question)
**Typical Data Pattern**: Sales (Y) vs Cost (X)

**Required Analysis** (10-mark question):
1. Scatter diagram
2. Regression equation Y on X
3. Correlation coefficient (r) and R²
4. Test significance of regression
5. Prediction for given cost
6. Confidence/prediction intervals

---

### Example 7: Exercise E4 - Second SO₃ Data Set (Table 4)
**Data**: 15 observations (different sample)

**Sums from Book**:
- $\sum x = 22.59$
- $\sum x^2 = 36.7135$
- $\sum y = 2479$
- $\sum y^2 = 511637$ (approx)
- n = 15

**Result from Book**: $\hat{y} = 88.05 + 51.273x$

**Key Point**: Values of a and b depend on the sample of observations. Should use $\hat{a}$ and $\hat{b}$ to indicate estimates.

---

### Example 8: Income vs Savings (Exercise E5)
**Data**: 9 families, x = income ($000s), y = savings ($000s)
| Income (x) | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Savings (y) | 0.0 | 0.1 | 0.2 | 0.2 | 0.5 | 0.5 | 0.6 | 0.7 | 0.8 |

**Book asks**: Work out the best linear regression formula.

---

## 9.5 Correlation Coefficient

### Pearson's Correlation (r)
$$r = \frac{S_{xy}}{\sqrt{S_{xx} S_{yy}}} = \frac{n\sum xy - \sum x \sum y}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}$$

Where $S_{yy} = \sum y^2 - \frac{(\sum y)^2}{n} = \sum(y - \bar{y})^2$

### Properties
- $-1 \leq r \leq 1$
- $r = 1$: Perfect positive linear
- $r = -1$: Perfect negative linear
- $r = 0$: No linear correlation
- $r$ is symmetric: $r_{xy} = r_{yx}$
- $r$ unchanged by linear transformation

### Coefficient of Determination (R²)
$$R^2 = r^2 = \frac{\text{Explained Variation}}{\text{Total Variation}} = \frac{SSR}{SST}$$

Where:
- $SST = \sum(y - \bar{y})^2$ = Total SS
- $SSR = \sum(\hat{y} - \bar{y})^2$ = Regression SS (Explained)
- $SSE = \sum(y - \hat{y})^2$ = Error SS (Unexplained)
- $SST = SSR + SSE$

---

## 9.6 Sums of Squares in Regression

| SS | Formula | df |
|----|---------|-----|
| **Total (SST)** | $\sum(y_i - \bar{y})^2 = S_{yy}$ | n-1 |
| **Regression (SSR)** | $\sum(\hat{y}_i - \bar{y})^2 = b^2 S_{xx}$ | 1 |
| **Error (SSE)** | $\sum(y_i - \hat{y}_i)^2 = SST - SSR$ | n-2 |

### Mean Squares
- $MSR = SSR / 1 = SSR$
- $MSE = SSE / (n-2)$

### F-Test for Significance of Regression
$$F = \frac{MSR}{MSE} \sim F_{1, n-2}$$
(Equivalent to $t = b/SE(b)$ with $t^2 = F$)

---

## 9.7 Standard Errors and Inference

### Standard Error of Slope
$$SE(b) = \sqrt{\frac{MSE}{S_{xx}}}$$

### Standard Error of Intercept
$$SE(a) = \sqrt{MSE \left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right)}$$

### t-Test for Slope (H₀: β = 0)
$$t = \frac{b}{SE(b)} \sim t_{n-2}$$

### Confidence Intervals
- **For β**: $b \pm t_{\alpha/2, n-2} \cdot SE(b)$
- **For α**: $a \pm t_{\alpha/2, n-2} \cdot SE(a)$
- **For mean response at x₀**: $\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot SE(\hat{y}_0)$
  Where $SE(\hat{y}_0) = \sqrt{MSE \left(\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}\right)}$
- **For individual prediction at x₀**: $\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot SE(pred)$
  Where $SE(pred) = \sqrt{MSE \left(1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}\right)}$

---

## 9.8 Residual Analysis

**Residual**: $e_i = y_i - \hat{y}_i$

### Assumptions Checked via Residuals
1. **Linearity**: Residuals vs fitted - random scatter
2. **Homoscedasticity**: Constant variance - no funnel shape
3. **Normality**: Q-Q plot of residuals - straight line
4. **Independence**: No pattern in residuals vs order

---

## 9.9 Multiple Linear Regression (Brief - Book Section 9.4)

### Model with Two Independent Variables
$$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \epsilon$$

### Normal Equations
$$\sum y = n\alpha + \beta_1\sum x_1 + \beta_2\sum x_2$$
$$\sum x_1y = \alpha\sum x_1 + \beta_1\sum x_1^2 + \beta_2\sum x_1x_2$$
$$\sum x_2y = \alpha\sum x_2 + \beta_1\sum x_1x_2 + \beta_2\sum x_2^2$$

---

## 9.10 Special Problem: Partially Destroyed Lab Record

**Classic PYQ Problem (appeared 2 times identically!)**

Given:
- Variance of X = 9 (so σₓ = 3)
- Two regression equations:
  - $8X - 10Y + 66 = 0$ (regression of Y on X)
  - $40X - 18Y = 214$ (regression of X on Y)

**Find**: Means (x̄, ȳ), correlation coefficient (r), σᵧ

### Solution Steps (Book Method)
1. **Find means**: Intersection of two regression lines
   - Solve: $8x - 10y = -66$ and $40x - 18y = 214$
   - x̄ = 13, ȳ = 17

2. **Identify slopes**:
   - Y on X: $Y = 0.8X + 6.6$ → $b_{yx} = 0.8$
   - X on Y: $X = 0.45Y + 5.35$ → $b_{xy} = 0.45$

3. **Correlation**: $r = \pm\sqrt{b_{yx} \cdot b_{xy}} = \pm\sqrt{0.8 \times 0.45} = \pm 0.6$
   - Both slopes positive → $r = +0.6$

4. **σᵧ**: $b_{yx} = r \cdot \frac{\sigma_y}{\sigma_x} \Rightarrow 0.8 = 0.6 \cdot \frac{\sigma_y}{3} \Rightarrow \sigma_y = 4$

---

## 9.11 Speed vs Stopping Distance (MEMORIZE - Appeared 2 Times Identically!)

**PYQ Pattern**: This exact problem appeared in **Dec 2022** and **Jun 2024** identically.

**Typical Data Pattern** (from PYQs):
| Speed (X) | Stopping Distance (Y) |
|-----------|----------------------|
| 30 | 15 |
| 40 | 25 |
| 50 | 40 |
| 60 | 55 |
| 70 | 75 |

**Required Analysis** (10-mark question):
1. Scatter diagram
2. Regression equation Y on X
3. Correlation coefficient (r)
4. Coefficient of determination (R²)
5. Test significance of regression
6. Prediction for given speed
7. Confidence/prediction intervals

**Note**: Since this appeared identically twice, memorize the complete solution procedure.

---

## 9.12 BP vs Age (PYQ Dec 2021 - 10 Mark Question)

**Typical Data Pattern**: Blood Pressure (Y) vs Age (X)

**Required Analysis** (10-mark question):
1. Scatter diagram
2. Regression equation Y on X
3. Correlation coefficient (r) and R²
4. Test significance of regression
5. Prediction for given age
6. Confidence/prediction intervals
7. Residual analysis

---

## 9.13 IT Company Output vs Cost (PYQ Jun 2024 - 10 Mark Question)

**Typical Data Pattern**: Output (Y) vs Cost (X)

---

## 9.14 Cost vs Sales (PYQ Dec 2023 - 10 Mark Question)

**Typical Data Pattern**: Sales (Y) vs Cost (X)

---

## 9.15 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - HIGH PRIORITY (7 appearances)

#### 1. Calculate Regression Coefficients
> "Given ΣX, ΣY, ΣXY, ΣX², ΣY², n. Find regression equation Y on X and correlation coefficient."

**Solution**: Use formulas for b, a, r directly from sums.

#### 2. Correlation from Sums
> "Given n=10, ΣX=50, ΣY=60, ΣXY=350, ΣX²=300, ΣY²=450. Find r."

**Solution**: $r = \frac{10(350)-50(60)}{\sqrt{[10(300)-50^2][10(450)-60^2]}}$

#### 3. Partially Destroyed Lab Record
> "Variance of X=9. Regression eqns: 8X-10Y+66=0 and 40X-18Y=214. Find means, r, σᵧ."

**Appeared in Dec 2022 and Jun 2025 IDENTICALLY!**

---

### 10-Mark Questions (Section B) - HIGHEST PRIORITY (7 appearances)

#### 1. Complete Regression Analysis
> **Jun 2021**: Scatter diagram + regression equation + prediction
> **Dec 2021**: BP vs Age
> **Dec 2022**: Speed vs Stopping distance (REPEATED in Jun 2024!)
> **Dec 2023**: Cost vs Sales
> **Jun 2024**: IT company output vs cost / Speed vs Stopping distance (REPEAT)
> **Dec 2024**: Partially destroyed lab record (REPEAT)
> **Jun 2025**: Partially destroyed lab record (REPEAT)

**Structure for 10-Mark Answer**:
1. Scatter diagram (if asked)
2. Compute b, a using Sₓₓ, Sₓᵧ, x̄, ȳ
3. Regression equation: $\hat{y} = a + bx$
4. Compute r, R², interpret
5. Test significance of regression (t-test or F-test)
6. Prediction for given x₀
7. Confidence/prediction interval (if asked)
8. Residual analysis (brief)

---

## 9.12 Important Formulas Summary

| Quantity | Formula |
|----------|---------|
| **Sₓₓ** | $\sum x^2 - \frac{(\sum x)^2}{n}$ |
| **Sᵧᵧ** | $\sum y^2 - \frac{(\sum y)^2}{n}$ |
| **Sₓᵧ** | $\sum xy - \frac{\sum x \sum y}{n}$ |
| **Slope (b)** | $S_{xy}/S_{xx}$ |
| **Intercept (a)** | $\bar{y} - b\bar{x}$ |
| **Correlation (r)** | $S_{xy}/\sqrt{S_{xx}S_{yy}}$ |
| **R²** | $r^2 = SSR/SST$ |
| **SST** | $S_{yy}$ |
| **SSR** | $b^2 S_{xx}$ |
| **SSE** | $SST - SSR$ |
| **MSE** | $SSE/(n-2)$ |
| **SE(b)** | $\sqrt{MSE/S_{xx}}$ |
| **t (slope)** | $b/SE(b)$ |
| **Prediction SE** | $\sqrt{MSE(1 + 1/n + (x_0-\bar{x})^2/S_{xx})}$ |

---

## 9.16 Special Results for Partially Destroyed Record

Given two regression lines:
- Y on X: $Y = b_{yx}X + a_{yx}$
- X on Y: $X = b_{xy}Y + a_{xy}$

Then:
1. **Means**: Intersection point of the two lines
2. **Correlation**: $r = \pm\sqrt{b_{yx} \cdot b_{xy}}$ (sign = sign of slopes)
3. **Ratio of SDs**: $\frac{\sigma_y}{\sigma_x} = \frac{b_{yx}}{r} = \frac{r}{b_{xy}}$

---

## 9.16 Common Mistakes

| Mistake | Correction |
|---------|------------|
| Confusing bₓᵧ and bᵧₓ | bᵧₓ = Sₓᵧ/Sₓₓ (Y on X); bₓᵧ = Sₓᵧ/Sᵧᵧ (X on Y) |
| Using wrong regression for prediction | Use Y on X to predict Y from X |
| Forgetting r sign from slopes | Both slopes positive → r positive; both negative → r positive; one each → r negative |
| Confusing confidence vs prediction interval | Prediction interval wider (includes individual variation) |
| Not checking Sₓₓ ≠ 0 | X must have variation |

---

## 9.17 Diagrams

### Scatter Plot with Regression Line
```
Y
│    ●
│        ●
│           ●  ← Regression line ŷ = a + bx
│      ●
│  ●
│
└───────────────── X
```

### Sums of Squares Decomposition
```
SST (Total)
    │
    ├── SSR (Explained by regression) ──→ b²Sₓₓ
    │
    └── SSE (Unexplained/Error) ──→ SST - SSR
```

### Residual Plot (Good Fit)
```
Residual
    │  ●     ●   ●     ●
    │    ●  ●  ●  ●  ●
    │
    │    ●  ●  ●  ●  ●
    │  ●     ●   ●     ●
    └───────────────── Fitted Values
```

---

## 9.18 Practice Problems (PYQ Style)

### Problem 1 (Jun 2021)
Scatter diagram + regression of Y on X + prediction.

### Problem 2 (Dec 2021)
Blood pressure vs Age regression.

### Problem 3 (Dec 2022, Jun 2024 - IDENTICAL!)
**Speed vs Stopping Distance** - memorize this data pattern!

### Problem 4 (Dec 2022, Jun 2025 - IDENTICAL!)
**Partially Destroyed Lab Record**: σₓ²=9, 8X-10Y+66=0, 40X-18Y=214.

### Problem 5 (Dec 2023)
Cost vs Sales regression.

### Problem 6 (Jun 2024)
IT company output vs cost.

### Problem 7 (Dec 2024)
Partially destroyed lab record (again!).

---

## 9.17 Exam Tips

- ✅ **Partially destroyed lab record**: MEMORIZE the solution method - appeared 2 times identically!
- ✅ **Speed vs Stopping distance**: Appeared 2 times identically!
- ✅ **Know all formulas**: b, a, r, R², SE(b), prediction intervals
- ✅ **Scatter diagram**: Draw roughly with trend line
- ✅ **Identify correct regression**: Y on X (predict Y from X) vs X on Y
- ✅ **r² interpretation**: "% of variation in Y explained by X"
- ✅ **Residual analysis**: Mention checking linearity, constant variance, normality
- ❌ Don't confuse bₓᵧ and bᵧₓ
- ❌ Don't use wrong regression equation for prediction
- ❌ Don't forget r has same sign as both slopes

---

*End of Unit 9 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 9 "Regression Analysis" - All formulas, definitions, examples (Cement SO₃, Hosiery Mill, Income/Savings), exercises, and the partially destroyed lab record problem verified against original textbook content.