# Unit 10: Forecasting and Time Series Analysis

**Block 3: Applied Statistical Methods**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 10 - Forecasting and Time Series Analysis (IGNOU BCS-040)

---

## 10.1 Introduction

**Time Series**: Data collected on a variable over time at regular intervals (daily, monthly, quarterly, yearly).

**Forecasting**: Predicting future values based on historical time series patterns.

### Components of Time Series (from Book)
| Component | Symbol | Description | Period |
|-----------|--------|-------------|--------|
| **Trend (Secular)** | Tₜ | Long-term movement (up/down) | ≥ 15 years |
| **Seasonal** | Sₜ | Regular pattern within year | ≤ 1 year |
| **Cyclical** | Cₜ | Business cycles (boom/recession) | > 1 year (2-10 years) |
| **Irregular/Random** | Iₜ | Unpredictable fluctuations (i.i.d. normal, mean 0) | Any |

---

## 10.2 Time Series Models

### 1. Additive Model
$$Y_t = T_t + S_t + C_t + I_t$$

**Use when**: Seasonal variation is constant over time (amplitude doesn't change with trend).

### 2. Multiplicative Model
$$Y_t = T_t \times S_t \times C_t \times I_t$$

**Use when**: Seasonal variation increases with trend (amplitude proportional to level).

### Relationship
- If $S_t$ constant amplitude → Additive
- If $S_t$ proportional to $T_t$ → Multiplicative
- Can transform multiplicative to additive via log: $\log Y_t = \log T_t + \log S_t + \log C_t + \log I_t$

---

## 10.3 Trend Analysis Methods

### Method 1: Method of Least Squares (Linear Trend)

**Model**: $T_t = a + bt$ where t = time coded as 1, 2, 3, ... or centered

**Normal Equations**:
$$\sum Y = na + b\sum t$$
$$\sum tY = a\sum t + b\sum t^2$$

**With coding** (origin at middle):
- Odd n: t = ..., -2, -1, 0, 1, 2, ... → $\sum t = 0$
- Even n: t = ..., -5, -3, -1, 1, 3, 5, ... → $\sum t = 0$

Then: $a = \frac{\sum Y}{n}$, $b = \frac{\sum tY}{\sum t^2}$

**Trend Equation**: $\hat{Y}_t = a + bt$

### Worked Example from Book: Bread Sales (Linear Trend)
**Data**: 35 days of bread sales (Table 10)
- $\sum t = 18$
- $\sum Y = ?$ (computed from data)
- $S_{xx} = 3570$
- $S_{tY} = 1732$
- $b = S_{tY}/S_{xx} = 0.485$
- $a = \bar{Y} - b\bar{t} = 48.06$

**Trend Equation**: $T_t = 48.06 + 0.485t$

$R^2 = 0.49$ (reasonably reliable but could be better)

### Non-Linear Trends (Book Examples)
1. **Quadratic**: $T_t = a_0 + a_1t + a_2t^2$ (Rice yield data - $R^2 = 0.94$)
2. **Exponential**: $T_t = ab^t$ → Linearize: $\log T_t = \log a + t \log b$ (Population data - $R^2 = 0.96$)

---

## 10.4 Method of Moving Averages

### Purpose
Smooth out seasonal/irregular variations to reveal trend. Eliminates seasonal variations by taking average over period equal to season length.

### Moving Average of Length m
$$MA_t = \frac{Y_{t-k} + Y_{t-k+1} + \ldots + Y_t + \ldots + Y_{t+k}}{m}$$

Where $m = 2k+1$ (odd) for centered MA.

### For Even m: Double Moving Average (Centered)
1. Compute MA of length m
2. Compute MA of length 2 on the first MAs

### Length Selection (Book Guidelines)
- **Quarterly data**: m = 4 (or double MA with m=4 then m=2)
- **Monthly data**: m = 12
- **Short-term/Weekly**: m = 3, 5, 7

### Worked Example from Book: Bread Sales (Table 14)
**Data**: 35 days of bread sales

| Length | Method | Notes |
|--------|--------|-------|
| m=7 (odd) | Average of 7 consecutive days, centered at day 4, 5, ... | Best - eliminates weekly seasonality |
| m=5 (odd) | Similar | Good |
| m=4 (even) | Double MA: 4-day MA → 2-day MA of those | Centers at half-days |

**Key Book Observations (Fig. 10, 11)**:
- Fluctuations smallest when MA length = seasonal period (7 for weekly data)
- Moving averages are serially correlated - may show spurious cycles
- Peaks/troughs in MA may occur at different times than original series
- Cannot compute MA for earliest/latest years
- MA not useful for forecasting (needs future observations)
- Effective when trend is approximately linear

---

## 10.5 Exponential Smoothing

### Simple Exponential Smoothing (SES) - No trend, no seasonality
$$\hat{Y}_{t+1} = \alpha Y_t + (1-\alpha)\hat{Y}_t = \hat{Y}_t + \alpha(Y_t - \hat{Y}_t)$$

Where:
- $\alpha$ = smoothing constant (0 < α < 1)
- $\hat{Y}_1 = Y_1$ (initial forecast)

**Properties**:
- Large α (0.7-0.9): Fast response, more weight to recent
- Small α (0.1-0.3): Slow response, more smoothing
- Optimal α minimizes MSE

### Holt's Double Exponential Smoothing (Trend)
**Level**: $L_t = \alpha Y_t + (1-\alpha)(L_{t-1} + T_{t-1})$
**Trend**: $T_t = \beta(L_t - L_{t-1}) + (1-\beta)T_{t-1}$
**Forecast**: $\hat{Y}_{t+h} = L_t + h T_t$

### Holt-Winters (Trend + Seasonality)
Additive or multiplicative seasonal versions.

---

## 10.6 Seasonal Indices

### Ratio-to-Moving-Average Method (Multiplicative)
1. Compute centered moving averages (length = season length)
2. Ratios: $R_t = Y_t / MA_t \times 100$
3. Average ratios for each season
4. Adjust to sum to 400 (quarterly) or 1200 (monthly)

### Seasonal Adjustment (Deseasonalizing)
- **Additive**: $D_t = Y_t - S_t$
- **Multiplicative**: $D_t = Y_t / S_t$

---

## 10.7 Forecasting Procedure

### Steps
1. **Decompose**: Separate T, S, C, I
2. **Forecast Trend**: Extend trend line
3. **Forecast Seasonal**: Repeat seasonal indices
4. **Combine**: Additive → $Forecast = \hat{T} + \hat{S}$; Multiplicative → $Forecast = \hat{T} \times \hat{S}$
5. **Adjust for Cyclical** (if identifiable)

### Forecast Accuracy Measures
| Measure | Formula |
|---------|---------|
| **MAD** (Mean Absolute Deviation) | $\frac{1}{n}\sum |Y_t - \hat{Y}_t|$ |
| **MSE** (Mean Squared Error) | $\frac{1}{n}\sum (Y_t - \hat{Y}_t)^2$ |
| **MAPE** (Mean Absolute % Error) | $\frac{100}{n}\sum |\frac{Y_t - \hat{Y}_t}{Y_t}|$ |

---

## 10.8 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - HIGH PRIORITY (6 appearances)

#### 1. Moving Average (Length 3) - REPEATED 4 TIMES!
> "Compute 3-yearly moving averages for sales/water/milk/wheat data. Plot original and trend."

**Data Pattern** (appeared Jun 2021, Dec 2021, Dec 2024, Jun 2024):
- Year/Quarter and values given
- Compute MA₃ = (Yₜ₋₁ + Yₜ + Yₜ₊₁)/3
- Plot both series

**Jun 2021**: Sales data
**Dec 2021**: Water consumption
**Dec 2024**: Milk sales
**Jun 2024**: Wheat production

#### 2. Exponential Smoothing
> "Given α=0.3, compute exponential smoothing forecasts."

**Jun 2021, Jun 2024**: Short note / calculation

#### 3. Time Series Components
> "Describe four components of time series" / "Additive vs Multiplicative model"

#### 4. Least Squares Trend
> "Fit linear trend by least squares. Forecast next 2 years."

### 10-Mark Questions (Section B) - HIGH PRIORITY (4 appearances)

#### 1. Complete Time Series Analysis
> **Jun 2022**: Describe time series components / forecasting models
> **Jun 2024**: Forecasting concept & categories
> **Dec 2024**: Define time series & discuss categories
> **Jun 2025**: Similar

**Structure**:
1. Define time series
2. Four components with examples
3. Additive vs Multiplicative models
4. Methods: Least squares, Moving averages, Exponential smoothing
5. Forecasting steps
6. Accuracy measures

---

## 10.9 Important Formulas Summary

| Method | Formula |
|--------|---------|
| **Linear Trend (coded)** | $a = \frac{\sum Y}{n}$, $b = \frac{\sum tY}{\sum t^2}$ |
| **Linear Trend (uncoded)** | $b = \frac{n\sum tY - \sum t\sum Y}{n\sum t^2 - (\sum t)^2}$, $a = \bar{Y} - b\bar{t}$ |
| **Moving Average (odd m)** | $MA_t = \frac{1}{m}\sum_{i=-k}^{k} Y_{t+i}$ |
| **Moving Average (even m=4)** | Double MA: 4-quarter MA → 2-quarter MA of those |
| **Exponential Smoothing** | $\hat{Y}_{t+1} = \alpha Y_t + (1-\alpha)\hat{Y}_t$ |
| **Seasonal Index (Multiplicative)** | $SI = \frac{\text{Average Ratio}}{100} \times \text{Adjustment}$ |
| **Additive Forecast** | $\hat{Y} = \hat{T} + \hat{S}$ |
| **Multiplicative Forecast** | $\hat{Y} = \hat{T} \times \hat{S}$ |
| **MAD** | $\frac{1}{n}\sum |Y - \hat{Y}|$ |
| **MAPE** | $\frac{100}{n}\sum |\frac{Y - \hat{Y}}{Y}|$ |

---

## 10.10 Step-by-Step: Moving Average Length 3

```
Data: t=1,2,3,4,5,6,7
Y:    10,12,14,16,18,20,22

MA₃ at t=2: (10+12+14)/3 = 12
MA₃ at t=3: (12+14+16)/3 = 14
MA₃ at t=4: (14+16+18)/3 = 16
MA₃ at t=5: (16+18+20)/3 = 18
MA₃ at t=6: (18+20+22)/3 = 20

No MA for t=1 and t=7 (endpoints)
```

---

## 10.11 Worked Examples from Textbook (Must Practice)

### Example 1: Bread Shop Forecasting (Book Example 1, 2, 3)
- **Data**: 3 weeks of daily bread demand
- **Naive forecast**: 50 loaves/day → Profit = Rs. 1832
- **Day-wise average forecast**: Profit = Rs. 2015 (superior!)
- **Additive model decomposition** (5 weeks data):
  - Trend: Tₜ = 50 + 3.2×(week-1) [weekly increase avg = 3.2]
  - Seasonal: Sₜ averaged over 5 weeks (e.g., Sunday = -2, Tuesday = -7, Thursday = +7)
  - Forecast week 6: T₃₆ + S₃₆ = 66 + (-2) = 64

### Example 2: Bread Sales Linear Trend (Sec 10.5.1)
**Data**: 35 days (Table 10)
- $\sum t = 18$, $S_{xx} = 3570$, $S_{tY} = 1732$
- $b = 0.485$, $a = 48.06$
- $T_t = 48.06 + 0.485t$, $R^2 = 0.49$

### Example 3: Moving Averages for Bread Sales (Sec 10.5.2)
**Data**: 35 days (Table 14)
- MA length 7 (seasonal period): Best smoothing, eliminates weekly seasonality
- MA length 4 (even): Double MA centered at half-days
- MA length 5: Good smoothing

**Book Exercise E17**: Compute first 3 MA of length 3
**Book Exercise E18**: Compute 2nd and last MA of length 6

### Example 4: Rice Yield Quadratic Trend (Example 5)
**Data**: 1955-1995 (41 years)
- $T_t = 2660 - 67.1t + 0.716t^2$
- $R^2 = 0.94$, standard error = 126.8

### Example 5: Population Exponential Trend (Example 6)
**Data**: 1901-1991 censuses
- $T_t = 1493 \times (1.1462)^t$ (t=1 for 1901)
- $R^2 = 0.96$

### Example 6: Coconut Sales Multiplicative Model (Example 4)
**Data**: Seasonal sales 1994-1998
- Seasonal range increasing with trend → Use multiplicative model
- $Y_t = T_t \times S_t \times I_t$

---

## 10.12 Common Mistakes

| Mistake | Correction |
|---------|------------|
| Computing MA at endpoints | MA starts at t=2 for length 3, ends at t=n-1 |
| Not centering even-length MA | Use double MA for quarterly (m=4) |
| Using additive when multiplicative needed | Check if seasonal amplitude changes with trend |
| Forgetting to adjust seasonal indices | Must sum to 400 (quarterly) or 1200 (monthly) |
| Confusing forecast types | Point forecast vs interval forecast |

---

## 10.13 Diagrams

### Time Series Decomposition (Multiplicative)
```
Y = T × S × C × I

Original:    ●●●●●●●●●●●●●●●●
Trend:       ─────────────────
Seasonal:    ~~~~~~~~~~~~~~~~~
Irregular:   · · · · · · · · · · · ·
```

### Moving Average Smoothing
```
Y
│  ●  ●  ●  ●  ●  ●  (Original)
│   \  \  \  \  \  
│    ●●●●●●●        (MA - smoother)
│
└────────────────── t
```

### Additive vs Multiplicative Seasonal
```
ADDITIVE (constant amplitude)
Y
│  ~~~~~~~
│ ~~~~~~~
│~~~~~~~
└───────── t

MULTIPLICATIVE (growing amplitude)
Y
│    ~~~~~~
│  ~~~~~~~
│~~~~~~~
└───────── t
```

---

## 10.14 Practice Problems (PYQ Style)

### Problem 1 (Jun 2021)
Sales data: Compute 3-yearly moving average, plot.

### Problem 2 (Dec 2021)
Water consumption: 3-yearly moving average.

### Problem 3 (Dec 2022, Jun 2024)
Describe time series components / forecasting concept.

### Problem 4 (Dec 2024)
Milk sales: 3-yearly moving average / define time series.

### Problem 5 (Jun 2024)
Wheat production: 3-yearly moving average / exponential smoothing.

### Problem 6 (Jun 2025)
Time series components and categories.

---

## 10.15 Exam Tips

- ✅ **Moving Average Length 3**: Appeared 4 times! Master the calculation.
- ✅ **Know all 4 components** with examples (Trend, Seasonal, Cyclical, Irregular)
- ✅ **Additive vs Multiplicative**: Clear distinction with diagrams
- ✅ **Exponential smoothing formula**: $\hat{Y}_{t+1} = \alpha Y_t + (1-\alpha)\hat{Y}_t$
- ✅ **Least squares trend**: Know coding method (t centered at 0)
- ✅ **Seasonal indices**: Ratio-to-MA method for multiplicative
- ✅ **Forecast accuracy**: MAD, MSE, MAPE formulas
- ❌ Don't compute MA at endpoints
- ❌ Don't forget double MA for even periods (quarterly)
- ❌ Don't confuse components (cyclical > 1 year, seasonal ≤ 1 year)

---

*End of Unit 10 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 10 "Forecasting and Time Series Analysis" - All formulas, definitions, examples (Bread shop, Rice yield, Population, Coconut sales), exercises, and methods verified against original textbook content.