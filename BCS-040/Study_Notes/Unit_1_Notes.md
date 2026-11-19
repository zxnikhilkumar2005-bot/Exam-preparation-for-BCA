# Unit 1: Descriptive Statistics

**Block 1: Descriptive Statistics & Probability**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 1 - Descriptive Statistics (IGNOU BCS-040)

---

## 1.1 Introduction

Statistics is the science of collection, organization, analysis, and interpretation of data. The word "statistics" is derived from the word "state" and originally referred to numerical data about the state (population, taxes, wealth, exports, imports, crop production, etc.).

### Two Senses of Statistics
- **Singular ("Statistics is")**: The science/methodology of statistics
- **Plural ("Statistics are")**: Numerical data/facts (batting averages, unemployment figures, number of deaths from malaria, etc.)

### Why Statistics?
1. Increasingly quantitative approach in sciences, business, and daily life
2. Volume of data has grown enormously
3. Need for professionals to collect, analyze, and interpret data

### Key Definitions (from Textbook)
| Term | Definition |
|------|------------|
| **Population** | Collection of all individuals/units under study (e.g., all adult males in India) |
| **Sample** | A subset of the population used to describe the population (e.g., 20 cancer patients chosen for drug test) |
| **Variable** | A characteristic that takes numerical values (e.g., height, weight, marks, age) |
| **Attribute** | A non-numerical characteristic (e.g., gender, quality: good/bad, yes/no) - can be coded as 1/0 |
| **Raw Data** | Unorganized, unanalyzed observations (observation before it is arranged and analyzed) |
| **Discrete Variable** | Takes isolated/countable values (e.g., number of students, number of defects, marks out of 10) |
| **Continuous Variable** | Takes any value within an interval (e.g., height, weight, time, temperature, bulb life) |
| **Grouped Data** | Data where observations are grouped into classes |
| **Ungrouped Data** | Raw data where each observation is listed individually |

### Continuous vs Discrete Variables - Important Distinction (from Book)
- **Discrete**: Result from counts; values jump (e.g., marks 0-10, number of calls). Even if recorded as whole numbers, they are discrete.
- **Continuous**: Theoretically can take any value in an interval; measuring instrument limitations impose artificial discreteness (e.g., bulb life recorded to 0.1 hour).

---

## 1.2 Collecting Data and Frequency Distribution

### Frequency Distribution
**Definition**: An organized display of data showing the frequency of each value against its value or against mutually exclusive classes.

**Frequency**: The number of times a value occurs in a data set.

**Relative Frequency**: Frequency as a fraction or percentage of the total number of observations.  
Formula: $rf_i = \frac{f_i}{\sum f_i}$ or $rf_i \times 100\%$

**Cumulative Frequency**:
- **Less than type**: Cumulative totals from top class downwards (e.g., "less than 6" = 53 students scored 5 or less)
- **More than type**: Cumulative totals from bottom class upwards (e.g., "more than 5" = 68 students scored 5 or more)

### Steps to Construct Frequency Distribution (Continuous Variable)
1. Find Range = Maximum - Minimum
2. Decide number of classes (typically 10-20 for >1000 observations; fewer for smaller datasets)
3. Determine class width = Range / Number of classes (prefer equal width)
4. Define class boundaries (non-overlapping, exhaustive, equal width preferred)
5. Tally observations into classes using tally marks (every 5th mark as slash)
6. Count frequencies

### Tally Mark Method (from Book - Table 4)
- Put a tally mark against a value as you read through the data
- Every 5th tally is a diagonal slash over the first four (easier counting)
- Count tallies to get frequency

### Important Terms for Grouped Data (Continuous Variables)

| Term | Definition | Example (from Book - Bulb Life) |
|------|------------|--------------------------------|
| **Class Limits** | Lower and upper values of a class as recorded (e.g., 510.6 - 590.5) | 510.6 (lower), 590.5 (upper) |
| **Class Boundaries** | True limits accounting for measurement precision (e.g., 510.55 - 590.55) | 510.55 (lower), 590.55 (upper) |
| **Class Interval/Width** | Difference between upper and lower boundaries | 590.55 - 510.55 = 80 |
| **Class Mark (Midpoint)** | (Lower boundary + Upper boundary) / 2 | (510.55 + 590.55)/2 = 550.55 |
| **Frequency Density** | Frequency per unit length of class interval = Frequency / Class Width | 1/80 = 0.0125 |

**Critical Rule from Book**: For continuous variables, classes are "exclusive of left boundaries but inclusive of right boundaries". The value x = 510.6 represents all bulbs with 510.55 < x ≤ 590.55.

### Guidelines for Choosing Classes (from Book)
1. Each class should correspond to an interval of values
2. Classes must be non-overlapping and exhaustive (each observation in exactly one class)
3. Number of classes not too small (otherwise distribution shape lost) nor too large
4. Classes preferably of equal width (for comparability of frequencies)
5. Rule of thumb: 10-20 classes when total frequency > 1000

---

## 1.3 Graphical Representation

### For Discrete Variables (each class = single value)
1. **Bar Diagram**: Rectangles with heights proportional to frequencies; x-axis = variable values, y-axis = frequencies
2. **Frequency Polygon**: Class frequencies plotted at class marks, successive points joined by straight lines; zero-frequency classes added at both ends to "tie down" graph to horizontal axis

### For Continuous Variables
1. **Histogram**: 
   - Plot class boundaries on x-axis
   - Erect rectangles over each class interval with height = relative frequency (or absolute frequency)
   - **Key**: Uses class BOUNDARIES (not limits) → rectangles touch, no gaps
   - Area of rectangles ∝ frequency of class
   - If class widths equal, heights ∝ frequencies
   
2. **Frequency Polygon**: 
   - Same construction as discrete but using class marks from continuous classes
   - Plotted at class marks, joined by straight lines
   
3. **Ogive (Cumulative Frequency Curve)**:
   - **Less than type**: Plot cumulative frequency (less than) vs upper class boundaries, join points
   - **More than type**: Plot cumulative frequency (more than) vs lower class boundaries, join points
   - Useful for finding how many observations above/below a given value
   
4. **Pie Chart**: 
   - Circle divided into sectors proportional to percentages
   - Central angle = Percentage × 3.6 (since 360° = 100%)
   - Best for showing percentage composition

### Comparison: Histogram vs Frequency Polygon (from Book)

| Feature | Histogram | Frequency Polygon |
|---------|-----------|-------------------|
| Shows separate classes clearly | ✓ | ✗ |
| Area proportional to frequency | ✓ | Approximate |
| Simplicity | Moderate | Simple |
| Pattern clarity | Good | Better outline |
| Smoothness with more classes | No | Yes (becomes curve-like) |

### Advantages of Histogram (Book)
- Rectangle clearly shows each separate class
- Area of each rectangle relative to all others shows proportion of total observations in that class

### Advantages of Frequency Polygon (Book)
- Simpler than histogram
- Sketches outline of data pattern more clearly
- Becomes increasingly smooth and curve-like as classes/observations increase

---

## 1.4 Summarisation of Data: Measures of Central Tendency

A representative value around which observations tend to cluster is a measure of central tendency (average). Three commonly used: Arithmetic Mean, Median, Mode.

### 1.4.1 Arithmetic Mean

**Definition**: Sum of all observations divided by number of observations.

#### Ungrouped Data (Population)
$$\mu = \frac{\sum_{i=1}^{N} x_i}{N}$$

#### Sample Mean
$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

#### Grouped Data - Discrete (each class = single value, e.g., marks 0-10)
$$\bar{x} = \frac{\sum f_i x_i}{\sum f_i}$$

#### Grouped Data - Continuous (using class marks)
$$\bar{x} = \frac{\sum f_i x_i}{\sum f_i}$$
where $x_i$ = class mark of $i^{th}$ class

**Note from Book**: For grouped continuous data, we assume all observations in a class are concentrated at the class mark. This gives an *estimate* of the mean (error averages out).

#### Weighted Mean
$$\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$$
- Used when measurements have different importance (e.g., firm profit rates weighted by firm assets)
- The grouped data mean is a special case of weighted mean (weights = frequencies)

#### Properties of Mean
1. Sum of deviations from mean = 0: $\sum (x_i - \bar{x}) = 0$
2. Mean of combined groups: $\bar{x}_{combined} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1 + n_2}$ (weighted mean of group means)
3. Affected by extreme values (sensitive to outliers)

#### Example from Book (Table 10 - 100 Students Marks)
| Score (x) | Freq (f) | xf |
|-----------|----------|-----|
| 0 | 1 | 0 |
| 1 | 2 | 2 |
| 2 | 4 | 8 |
| 3 | 9 | 27 |
| 4 | 15 | 60 |
| 5 | 21 | 105 |
| 6 | 20 | 120 |
| 7 | 15 | 105 |
| 8 | 9 | 72 |
| 9 | 4 | 36 |
| **Total** | **100** | **535** |

$\bar{x} = 535/100 = 5.35$

#### Example from Book (Table 11 - Bulb Life, Continuous)
Using class marks: $\bar{x} = 97775/100 = 977.75$ hours

---

### 1.4.2 Median

**Definition**: The middlemost observation (or mean of two middle observations) when data is ordered. Divides data into two equal halves.

#### Ungrouped Data
- $n$ odd: Median = $(\frac{n+1}{2})^{th}$ observation
- $n$ even: Median = Average of $(\frac{n}{2})^{th}$ and $(\frac{n}{2}+1)^{th}$ observations

**Example from Book**: Accidents on 5 days: 2,7,4,1,5 → Ordered: 1,2,4,5,7 → Median = 3rd = 4  
With 6th day (3 accidents): 1,2,3,4,5,7 → Median = (3+4)/2 = 3.5

#### Grouped Data (Formula from Book)
$$M = L + \frac{\frac{n}{2} - c}{f_m} \times l$$

Where:
- $L$ = Lower **boundary** of median class
- $n$ = Total frequency
- $c$ = Cumulative frequency (less than type) **before** median class
- $f_m$ = Frequency of median class
- $l$ = Class interval width

**Steps to Find Median Class (Book Method)**:
1. Compute $n/2$
2. Find cumulative frequencies (less than type)
3. Median class = first class where cumulative frequency ≥ $n/2$

**Example from Book (Table 9 - Bulb Life)**:
- $n=100$, $n/2=50$
- Cumulative freq for 5th class = 29, for 6th class = 55
- Median class = 6th class (910.55 - 990.55)
- $c=29$, $f_m=26$, $l=80$, $L=910.55$
- $M = 910.55 + \frac{50-29}{26} \times 80 = 975.17$

---

### 1.4.3 Mode

**Definition**: The most frequently occurring value in the data set.

#### Ungrouped Data
- Value with highest frequency
- May not exist (all distinct) or be multimodal (bimodal = 2 modes)

#### Grouped Data (from Book)
- **Discrete (single value per class)**: Value with highest frequency
- **Continuous (class intervals)**: Estimated by class mark of modal class (class with highest frequency)
  
**Formula for Continuous Data (Interpolation)**:
$$\text{Mode} = L + \frac{f_1 - f_0}{2f_1 - f_0 - f_2} \times l$$

Where:
- $L$ = Lower boundary of modal class
- $f_1$ = Frequency of modal class
- $f_0$ = Frequency of class preceding modal class
- $f_2$ = Frequency of class succeeding modal class
- $l$ = Class width

**Modal Class**: The class interval containing the largest number of measurements.

**Example from Book**: 
- Table 10 (discrete): Score 5 has highest freq (21) → Mode = 5
- Table 9 (continuous): Class 910.55-990.55 has highest freq (26) → Mode = class mark = 950.55

#### Empirical Relation (for Moderately Skewed Distributions)
$$\text{Mode} \approx 3 \times \text{Median} - 2 \times \text{Mean}$$
or
$$\text{Mean} - \text{Mode} \approx 3(\text{Mean} - \text{Median})$$

#### Uses of Mode (from Book)
- Can be used for quantitative AND qualitative data (e.g., "Sharp" impressions from printing press)
- Not affected by extreme values
- Can be used with open-ended classes
- **Limitations**: Often no mode (all distinct), or multiple modes; less used than mean/median

---

### Comparison: Mean vs Median vs Mode (from Book)

| Criterion | Mean | Median | Mode |
|-----------|------|--------|------|
| Uses all values | Yes | No | No |
| Affected by extremes | Highly | Slightly | Not |
| Open-ended classes | Cannot compute | Can compute | Can compute |
| Mathematical properties | Excellent (e.g., combined mean = weighted mean) | Limited (no formula for combined median) | Poor |
| Sampling stability | High (more reliable estimator) | Moderate | Low |
| **Best when...** | Symmetric data, further math needed | Skewed data, open-ended classes | Qualitative data, quick estimate |

---

## 1.5 Measures of Dispersion (Variability)

Measures how spread out the data is around the central value. Two types: distance measures and measures of average deviation.

### 1.5.1 Range
$$\text{Range} = \text{Maximum} - \text{Minimum}$$
- Quick but uses only two extreme values → unreliable for comparing distributions
- Example from Book: Supplier A range = 14, Supplier B range = 4 (A more variable)

### 1.5.2 Mean Deviation (About the Mean)
**Definition**: Mean of absolute deviations from mean.

**Ungrouped**:
$$MD(\bar{x}) = \frac{\sum |x_i - \bar{x}|}{n}$$

**Grouped (one value per class)**:
$$MD(\bar{x}) = \frac{\sum f_i |x_i - \bar{x}|}{\sum f_i}$$

### 1.5.3 Variance and Standard Deviation

**Definition**: Variance = average of squared deviations from mean; SD = √Variance.

#### Ungrouped Data (Population)
$$\sigma^2 = \frac{\sum (x_i - \mu)^2}{N} = \frac{\sum x_i^2}{N} - \mu^2$$
$$\sigma = \sqrt{\sigma^2}$$

#### Sample Variance (n-1 denominator for unbiasedness)
$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$$

#### Grouped Data (Discrete - one value per class)
$$\sigma^2 = \frac{\sum f_i (x_i - \bar{x})^2}{\sum f_i} = \frac{\sum f_i x_i^2}{\sum f_i} - \bar{x}^2$$

#### Grouped Data (Continuous - using class marks)
Same formula with $x_i$ = class mark (gives estimate).

#### Short-cut Method / Coding Method (from Book - for Large Numbers)
Let $y_i = \frac{x_i - a}{b}$ where $a$ = assumed mean (middle value), $b$ = class width
- Then $x_i = a + b y_i$
- $\bar{x} = a + b \bar{y}$
- $\sigma_x^2 = b^2 \sigma_y^2$
- Compute variance of $y$ (smaller numbers), multiply by $b^2$

**Example from Book (Table 14 - Bulb Life)**:
- $a = 950.55$, $b = 80$
- $\bar{y} = 0.34$, $\bar{x} = 950.55 + 80(0.34) = 977.75$
- $\sigma_y^2 = 3.39$, $\sigma_x^2 = 80^2 \times 3.39 = 21696$, $\sigma_x = 147.30$

#### Coefficient of Variation (CV)
$$CV = \frac{\sigma}{\bar{x}} \times 100\%$$
- Unit-free measure for comparing variability across different units/scales
- Example: Comparing income variability vs height variability

#### Variance of Combined Samples (from Book - Exercise E19)
For two samples of sizes $n$ and $m$ with means $\bar{x}, \bar{y}$ and variances $\sigma_x^2, \sigma_y^2$:
$$\sigma_{pooled}^2 = \frac{n\sigma_x^2 + m\sigma_y^2 + nm(\bar{x} - \bar{y})^2/(n+m)}{n+m}$$

---

## 1.6 Important Formulas Summary

| Measure | Ungrouped | Grouped (Discrete) | Grouped (Continuous) |
|---------|-----------|---------------------|----------------------|
| **Mean** | $\frac{\sum x}{n}$ | $\frac{\sum fx}{\sum f}$ | $\frac{\sum fx}{\sum f}$ (x = class mark) |
| **Median** | Middle value | - | $L + \frac{n/2 - c}{f_m} \times l$ |
| **Mode** | Most frequent | Most frequent | $L + \frac{f_1-f_0}{2f_1-f_0-f_2} \times l$ |
| **Variance** | $\frac{\sum x^2}{n} - \bar{x}^2$ | $\frac{\sum fx^2}{\sum f} - \bar{x}^2$ | Same (x = class mark) |
| **SD** | $\sqrt{\text{Variance}}$ | Same | Same |
| **CV** | $\frac{\sigma}{\bar{x}} \times 100$ | Same | Same |
| **Short-cut Var** | - | - | $\sigma_x^2 = b^2 \sigma_y^2$ |

---

## 1.7 Five-Number Summary (High Priority per PYQ)

The five-number summary gives a complete picture of distribution:
1. **Minimum** (Smallest value)
2. **First Quartile (Q1)** - 25th percentile
3. **Median (Q2)** - 50th percentile
4. **Third Quartile (Q3)** - 75th percentile
5. **Maximum** (Largest value)

**Interquartile Range (IQR)** = Q3 - Q1 (robust measure of spread)

**Box Plot**: Visual representation using five-number summary

---

## 1.8 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - HIGH PRIORITY (6 appearances in 9 papers)

**Q1. Frequency Distribution & Histogram**
> Construct a frequency distribution from raw data and draw a histogram.  
> **Key**: Bars must touch (class boundaries used), area ∝ frequency, label axes.

**Q2. Mean, SD, CV from Grouped Data** ⭐⭐⭐⭐⭐⭐
> Given frequency table, compute mean, standard deviation, coefficient of variation.  
> **Formulas**: $\bar{x} = \frac{\sum fx}{\sum f}$, $\sigma = \sqrt{\frac{\sum fx^2}{\sum f} - \bar{x}^2}$, $CV = \frac{\sigma}{\bar{x}} \times 100\%$

**Q3. Median from Grouped Data** ⭐⭐⭐⭐
> Identify median class correctly (where cumulative frequency ≥ n/2), apply formula:  
> $M = L + \frac{n/2 - c}{f_m} \times l$  
> **Watch**: Use class boundary for L, not class limit!

**Q4. Short Notes** (2-3 marks each)
> - Types of data (discrete/continuous, variable/attribute)
> - Graphical representation (histogram, frequency polygon, ogive, pie chart)
> - Measures of central tendency (mean, median, mode, comparison)

**Q5. Five-Number Summary / Quartiles**
> Compute min, Q1, median, Q3, max from grouped/ungrouped data.

---

### 10-Mark Questions (Section B)

**Q1. Complete Analysis (Rare but possible)**
> Given raw data: construct frequency distribution, compute mean, median, mode, SD, CV, draw histogram/frequency polygon, interpret results.

---

## 1.9 Key Points for Exam

- ✅ **Frequency distribution construction** (very common in 5-mark questions)
- ✅ **Mean, SD, CV from grouped data** (appeared 6 times in 9 papers)
- ✅ **Histogram drawing** (bars MUST touch for continuous data - use class boundaries!)
- ✅ **Median formula for grouped data** (identify median class correctly: cum freq ≥ n/2)
- ✅ **CV for comparing variability** across different units
- ✅ **Short-cut/coding method** for large numbers (assumed mean + class width)
- ✅ **Five-number summary** (min, Q1, median, Q3, max) - PYQ high priority
- ✅ **Class boundaries vs class limits** distinction (histograms use boundaries!)
- ✅ **Frequency density** = Frequency / Class width (for unequal class widths)
- ❌ Don't confuse class limits with class boundaries in histograms
- ❌ Don't forget to multiply by class width ($l$) in median formula
- ❌ Don't use class limits instead of boundaries for histogram x-axis
- ❌ Don't forget zero-frequency classes at ends for frequency polygon

---

## 1.10 Worked Examples from Textbook (Must Practice)

### Example 1: Mean from Discrete Frequency Distribution (Table 10)
Data: Marks of 100 students → $\bar{x} = 5.35$

### Example 2: Mean from Continuous Grouped Data (Table 11)
Data: Life of 100 bulbs → $\bar{x} = 977.75$ hours

### Example 3: Variance/SD from Discrete Distribution (Table 13)
Data: Same as Table 10 → $\sigma^2 = 3.5675$, $\sigma = 1.889$

### Example 4: Short-cut Method for Variance (Table 14)
Data: Bulb life with $a=950.55, b=80$ → $\sigma = 147.30$ hours

### Example 5: Median from Grouped Data (Table 9)
$M = 975.17$ hours

### Example 6: Combined Mean and SD (Exercise E19)
Formula for pooling two samples.

---

## 1.11 Diagrams

### Histogram Construction (Continuous - Class Boundaries)
```
Frequency
    │
    │    ┌─────────┐
    │    │         │ ┌─────────┐
    │    │         │ │         │ ┌─────────┐
    │    │         │ │         │ │         │
    └────┴─────────┴─┴─────────┴─┴─────────┴── Class Boundaries
         Class 1       Class 2        Class 3
(No gaps between rectangles - boundaries used)
```

### Frequency Polygon
```
Frequency
    │
    │        ●
    │       / \
    │      /   \      ●
    │     /     \    / \
    │  ● /       \  /   \  ●
    └───┴─────────┴─┴─────┴── Class Marks
(Points at class marks, joined by straight lines)
```

### Less Than Ogive
```
Cumulative Frequency
    │
    │                                  ●
    │                               ●
    │                            ●
    │                         ●
    │                      ●
    └────────────────────────────────── Upper Class Boundaries
```

### Pie Chart Construction
```
1. Convert frequencies to percentages: % = (f/Σf) × 100
2. Central angle = % × 3.6
3. Draw sectors with these angles
```

---

## 1.12 Practice Problems (PYQ Style)

### Problem 1 (Jun 2021 / Dec 2021 / Dec 2023 / Dec 2024 / Dec 2025)
> **Frequency Distribution & Histogram**: Given raw data of 50 observations, construct frequency distribution with appropriate class intervals and draw histogram.

### Problem 2 (Jun 2021 / Dec 2021 / Jun 2022 / Dec 2023 / Dec 2024 / Dec 2025)
> **Mean & SD from Grouped Data**: Given class intervals and frequencies, compute mean, standard deviation, and coefficient of variation.

### Problem 3
> **Median from Grouped Data**: Given grouped frequency distribution, find median using formula. Identify median class correctly.

### Problem 4
> **Five-Number Summary**: Compute min, Q1, median, Q3, max from given data.

---

*End of Unit 1 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 1 "Descriptive Statistics" - All formulas, definitions, and examples verified against original textbook content.