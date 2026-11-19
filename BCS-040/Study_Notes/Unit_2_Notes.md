# Unit 2: Probability Concepts

**Block 1: Descriptive Statistics & Probability**  
**Subject:** BCS-040 Statistical Techniques  
**Course:** BCA (IGNOU)  
**Textbook Reference:** Unit 2 - Probability Concepts (IGNOU BCS-040)

---

## 2.1 Introduction

Probability is the mathematical framework for quantifying uncertainty. While everyday language uses "probably" vaguely, probability theory provides precise rules for reasoning about uncertain events.

### Key Concepts (from Textbook)
| Term | Definition |
|------|------------|
| **Random Experiment** | Experiment whose outcome cannot be precisely predicted because totality of factors influencing outcome are not identifiable/controllable (e.g., tossing a coin, rolling a die) |
| **Trial** | A smaller sub-experiment within a random experiment |
| **Sample Space (S)** | Set of all possible sample points (outcomes) of an experiment |
| **Sample Point** | Each individual outcome of an experiment |
| **Event** | A specific collection/subset of sample points from S |
| **Simple Event** | Event consisting of a single sample point |
| **Compound Event** | Union of simple events (contains multiple sample points) |
| **Null Event (∅)** | Event with no sample points (impossible event) |

### Examples from Book
- **Coin toss (3 tosses)**: S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT} (8 points)
- **Two dice**: S = {(1,1), (1,2), ..., (6,6)} (36 points)
- **Marble draw without replacement**: Order matters, sample space size = 6 for 3 marbles drawing 2

---

## 2.2 Algebra of Events

Given events A and B in sample space S:

| Operation | Notation | Meaning | Occurs if |
|-----------|----------|---------|-----------|
| **Union** | $A \cup B$ | A or B (or both) occur | At least one of A, B occurs |
| **Intersection** | $A \cap B$ | Both A and B occur | Both A and B occur simultaneously |
| **Complement** | $A'$ or $A^C$ | A does not occur | A does not occur |
| **Difference** | $A - B$ | A occurs but B does not | A occurs, B does not |
| **Mutually Exclusive** | $A \cap B = \emptyset$ | Cannot occur together | Disjoint events |
| **Exhaustive** | $A \cup B = S$ | At least one must occur | Together cover sample space |

### Key Relationships (from Book)
- $E \cup E^C = S$ (event and its complement cover sample space)
- $E \cap E^C = \emptyset$ (mutually exclusive)
- $S^C = \emptyset$, $\emptyset^C = S$
- $P(E^C) = 1 - P(E)$

### De Morgan's Laws
- $(A \cup B)' = A' \cap B'$
- $(A \cap B)' = A' \cup B'$

### Venn Diagram Representation (Book Fig. 1)
- Rectangle = Sample space S
- Closed curves = Events
- Shaded regions = Intersections, unions

---

## 2.3 Probability of an Event

### Classical Definition (Equally Likely Outcomes)
If sample space has $N$ equally likely outcomes and event A has $n(A)$ favorable outcomes:
$$P(A) = \frac{n(A)}{N} = \frac{\text{Number of outcomes favoring A}}{\text{Total number of outcomes}}$$

**Book Formula (8)**: $P(E) = \frac{k}{m}$ where k = sample points in E, m = sample points in S

### Axiomatic Definition (Kolmogorov)
1. $0 \leq P(A) \leq 1$ for any event A
2. $P(S) = 1$
3. If $A_1, A_2, \ldots$ are mutually exclusive: $P(\bigcup A_i) = \sum P(A_i)$

### Propositions from Book (Important Properties)
| Proposition | Formula | Description |
|-------------|---------|-------------|
| **Proposition 1** | $P(A') = 1 - P(A)$ | Complement rule - useful when $P(A')$ easier to compute |
| **Proposition 2** | $P(\emptyset) = 0$ | Null event has zero probability |
| **Proposition 3** | $P(A) = \frac{k}{m}$ (equally likely) | Classical probability |
| **Proposition 4** | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Addition law for any two events |
| **Proposition 5** | $P(\cup E_i) = S_1 - S_2 + S_3 - \ldots + (-1)^{k-1}S_k$ | General addition for k events |
| **Proposition 6 (Boole's Inequality)** | $P(\cup E_i) \leq \sum P(E_i)$ | Upper bound for union probability |

### General Addition Law for k Events (Proposition 5)
For events $E_1, E_2, \ldots, E_k$:
$$P(\cup_{i=1}^k E_i) = S_1 - S_2 + S_3 - \ldots + (-1)^{k-1}S_k$$

Where:
- $S_1 = \sum P(E_i)$
- $S_2 = \sum_{i<j} P(E_i \cap E_j)$
- $S_3 = \sum_{i<j<l} P(E_i \cap E_j \cap E_l)$
- $S_k = P(E_1 \cap E_2 \cap \ldots \cap E_k)$

**For k = 3**:
$$P(A \cup B \cup C) = P(A)+P(B)+P(C) - P(A\cap B) - P(B\cap C) - P(C\cap A) + P(A\cap B\cap C)$$

**For k = 4**:
$$P(A\cup B\cup C\cup D) = S_1 - S_2 + S_3 - S_4$$

### Boole's Inequality (Proposition 6)
$$P(\cup_{i=1}^k E_i) \leq \sum_{i=1}^k P(E_i)$$
Useful for checking probability computations when exact formula is complex.

---

## 2.4 Conditional Probability and Multiplication Law

### Definition (Book Formula 15)
$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

**Interpretation**: Proportion of times A occurs out of repetitions where B takes place.

### Properties
- $0 \leq P(A|B) \leq 1$
- $P(S|B) = 1$
- If A and B mutually exclusive: $P(A|B) = 0$
- If $B \subseteq A$: $P(A|B) = 1$

### Multiplication Law (Book Formula 16)
$$P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$$

### For Three Events
$$P(A \cap B \cap C) = P(A) \cdot P(B|A) \cdot P(C|A \cap B)$$

---

## 2.5 Independent Events

### Definition (Book)
Two events A and B are **independent** iff:
$$P(A \cap B) = P(A) \cdot P(B)$$

Equivalently:
- $P(A|B) = P(A)$ (if $P(B) > 0$)
- $P(B|A) = P(B)$ (if $P(A) > 0$)

### With vs Without Replacement (Book Examples - Critical Concept!)
| Scenario | Example | Independence |
|----------|---------|--------------|
| **With Replacement** | Draw ball, replace, draw again | Events independent (e.g., 1st white, 2nd red) |
| **Without Replacement** | Draw ball, don't replace, draw again | Events dependent (probabilities change) |

**Book Example (Problem 1)**: 6 balls (4 white, 2 red)
- With replacement: $P(\text{1st white} \cap \text{2nd red}) = \frac{4}{6} \times \frac{2}{6} = \frac{2}{9} = P(\text{1st white}) \cdot P(\text{2nd red})$ ✓ Independent
- Without replacement: $P(\text{1st white} \cap \text{2nd red}) = \frac{4}{6} \times \frac{2}{5} = \frac{4}{15} \neq \frac{2}{9}$ ✗ Dependent

### Pairwise vs Mutual Independence
- **Pairwise Independent**: $P(A_i \cap A_j) = P(A_i)P(A_j)$ for all $i \neq j$
- **Mutually Independent**: Pairwise independent AND $P(A_1 \cap A_2 \cap \ldots \cap A_n) = \prod P(A_i)$

⚠️ **Pairwise independence does NOT imply mutual independence!**

---

## 2.6 Law of Total Probability

If $B_1, B_2, \ldots, B_n$ form a partition of S (mutually exclusive and exhaustive, i.e., $\cup B_i = S$, $B_i \cap B_j = \emptyset$ for $i \neq j$):
$$P(A) = \sum_{i=1}^{n} P(A|B_i) P(B_i)$$

**Book Application (Problem 4 - Blood Disease Test)**:
- $P(\text{Disease}) = 0.12$, $P(\text{No Disease}) = 0.88$
- $P(\text{Test +}|\text{Disease}) = 0.90$, $P(\text{Test +}|\text{No Disease}) = 0.05$
- $P(\text{Test +}) = (0.90)(0.12) + (0.05)(0.88) = 0.108 + 0.044 = 0.152$

---

## 2.7 Bayes' Theorem

**Reverses conditional probability**: From $P(A|B)$ to $P(B|A)$.

$$P(B_i|A) = \frac{P(A|B_i) P(B_i)}{\sum_{j=1}^{n} P(A|B_j) P(B_j)}$$

Where $B_1, B_2, \ldots, B_n$ partition the sample space.

### Components
| Component | Symbol | Description |
|-----------|--------|-------------|
| **Prior Probabilities** | $P(B_i)$ | Initial probabilities before observing A |
| **Likelihoods** | $P(A|B_i)$ | Probability of observing A given $B_i$ |
| **Posterior Probabilities** | $P(B_i|A)$ | Updated probabilities after observing A |

### Classic Examples from Book
1. **Problem 3 (3 Schools Admission)**: 
   - $P(A)=0.47, P(B)=0.29, P(C)=0.22$
   - $P(A\cap B)=0.08, P(A\cap C)=0.06, P(B\cap C)=0.07$
   - $P(A\cap B\cap C)=0.03$
   - $P(\text{at least one}) = 0.98 - 0.21 + 0.03 = 0.80$
   - $P(\text{none}) = 1 - 0.80 = 0.20$

2. **Problem 4 (Blood Disease Test)**:
   - $P(\text{Disease}|\text{Test +}) = \frac{(0.90)(0.12)}{0.152} = 0.7105$
   - $P(\text{Correct detection}) = 0.944$

---

## 2.8 PYQ-Based Important Questions

### 5-Mark Questions (Section A) - HIGH PRIORITY (6 appearances in 9 papers)

#### 1. Additive Law / "At Least One" Problems ⭐⭐⭐⭐⭐ (5+ appearances)
> "Probability that A solves a problem is 1/2, B is 1/3, C is 1/4. Find probability problem is solved."

**Solution**:
- $P(\text{at least one solves}) = 1 - P(\text{none solve})$
- $= 1 - (1/2)(2/3)(3/4) = 1 - 1/4 = 3/4$

> "Three students A, B, C solve a problem with probabilities 1/2, 1/3, 1/4." (Dec 2022, 2023, 2024, 2025, Jun 2024 - **5 IDENTICAL appearances!**)

#### 2. Conditional Probability / Bayes' Theorem ⭐⭐⭐⭐⭐
> "Radar traps at 4 locations with probabilities 0.4, 0.3, 0.2, 0.1. Person speeding has probabilities 0.2, 0.1, 0.5, 0.2 of passing through. Find probability of getting caught. If caught, probability it was at location 1?" (Dec 2023)

**Solution**:
- Total probability: $P(\text{caught}) = \sum P(\text{location}_i) \cdot P(\text{speeding}|\text{location}_i)$
- Bayes: $P(\text{loc}_1|\text{caught}) = \frac{P(\text{caught}|\text{loc}_1)P(\text{loc}_1)}{P(\text{caught})}$

#### 3. Binomial Distribution Applications ⭐⭐⭐
> "Probability of hitting target is 0.3. If 5 shots fired, find probability of (i) exactly 2 hits (ii) at least 2 hits" (Jun 2021, Dec 2024, Dec 2025)

**Solution**:
- $X \sim B(5, 0.3)$
- $P(X=2) = \binom{5}{2}(0.3)^2(0.7)^3$
- $P(X \geq 2) = 1 - P(X=0) - P(X=1)$

#### 4. Cancer/Smoker Type Problems (Bayes) ⭐⭐⭐⭐
> "Probability of cancer = 0.05. Smoker gets cancer with prob 0.1, non-smoker 0.01. 20% population smokes. Person has cancer - probability they smoke?" (Dec 2021)

**Bayes' Application**:
- $P(\text{Smoke}|\text{Cancer}) = \frac{P(\text{Cancer}|\text{Smoke})P(\text{Smoke})}{P(\text{Cancer})}$
- $P(\text{Cancer}) = (0.1)(0.2) + (0.01)(0.8) = 0.028$
- $P(\text{Smoke}|\text{Cancer}) = \frac{(0.1)(0.2)}{0.028} = 0.714$

#### 5. Independent Events (Rahul & Meena) ⭐⭐⭐⭐
> "Rahul hits target with prob 0.3, Meena with 0.4. Both shoot once. Find prob (i) both hit (ii) at least one hits (iii) exactly one hits" (Dec 2024)

**Solution**:
- (i) $P(\text{both}) = 0.3 \times 0.4 = 0.12$
- (ii) $P(\text{at least one}) = 1 - P(\text{neither}) = 1 - (0.7)(0.6) = 0.58$
- (iii) $P(\text{exactly one}) = (0.3)(0.6) + (0.7)(0.4) = 0.18 + 0.28 = 0.46$

#### 6. Without Replacement Problems ⭐⭐
> "Balls drawn from bag with 4 white, 6 black. Two drawn without replacement. Find prob both white / one each / both black" (Jun 2024)

**Solution**:
- $P(\text{both white}) = \frac{4}{10} \times \frac{3}{9} = \frac{2}{15}$
- $P(\text{one each}) = \frac{4}{10} \times \frac{6}{9} + \frac{6}{10} \times \frac{4}{9} = \frac{8}{15}$
- $P(\text{both black}) = \frac{6}{10} \times \frac{5}{9} = \frac{1}{3}$

---

### 10-Mark Questions (Section B)

#### 1. Bayes' Theorem - Complete Problem ⭐⭐⭐⭐
> "Radar traps at 4 locations L1, L2, L3, L4 operated 40%, 30%, 20%, 10% of time. Probabilities of speeding through: 0.2, 0.1, 0.5, 0.2. (a) Probability of getting caught? (b) If caught, probability at L1?" (Dec 2023)

**Complete Solution**:
1. **Define events**: $L_i$ = trap at location i operates, $S$ = speeding caught
2. **Given**: $P(L_1)=0.4, P(L_2)=0.3, P(L_3)=0.2, P(L_4)=0.1$; $P(S|L_1)=0.2, P(S|L_2)=0.1, P(S|L_3)=0.5, P(S|L_4)=0.2$
3. **Total Probability (a)**: $P(S) = \sum P(L_i)P(S|L_i) = 0.4(0.2)+0.3(0.1)+0.2(0.5)+0.1(0.2) = 0.08+0.03+0.10+0.02 = 0.23$
4. **Bayes (b)**: $P(L_1|S) = \frac{P(S|L_1)P(L_1)}{P(S)} = \frac{0.2 \times 0.4}{0.23} = \frac{0.08}{0.23} = 0.3478$
5. **Interpretation**: 23% chance of getting caught; if caught, 34.78% probability it was at location 1.

---

## 2.9 Important Formulas Summary

| Concept | Formula |
|---------|---------|
| **Classical Probability** | $P(A) = \frac{n(A)}{N}$ |
| **Complement Rule** | $P(A') = 1 - P(A)$ |
| **Addition Law (General)** | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| **Mutually Exclusive** | $P(A \cup B) = P(A) + P(B)$ |
| **Three Events** | $P(A\cup B\cup C) = \sum P - \sum P(\text{pairs}) + P(\text{triple})$ |
| **k Events (Prop 5)** | $S_1 - S_2 + S_3 - \ldots + (-1)^{k-1}S_k$ |
| **Boole's Inequality** | $P(\cup E_i) \leq \sum P(E_i)$ |
| **Conditional Probability** | $P(A|B) = \frac{P(A \cap B)}{P(B)}$ |
| **Multiplication Law** | $P(A \cap B) = P(A)P(B|A) = P(B)P(A|B)$ |
| **Independence** | $P(A \cap B) = P(A)P(B)$ |
| **Total Probability** | $P(A) = \sum P(A|B_i)P(B_i)$ |
| **Bayes' Theorem** | $P(B_i|A) = \frac{P(A|B_i)P(B_i)}{\sum P(A|B_j)P(B_j)}$ |

---

## 2.10 Problem-Solving Strategies

### For Additive Law Problems
1. Identify if events are mutually exclusive
2. If not, find $P(A \cap B)$ from given info
3. Apply $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
4. For "at least one": $P(\text{at least one}) = 1 - P(\text{none})$

### For Bayes' Theorem Problems
1. **Identify the partition**: $B_1, B_2, \ldots, B_n$ (causes/hypotheses)
2. **Identify the evidence**: A (observed event)
3. **List priors**: $P(B_i)$
4. **List likelihoods**: $P(A|B_i)$
5. **Compute denominator**: $P(A) = \sum P(A|B_i)P(B_i)$
6. **Apply Bayes**: $P(B_i|A) = \frac{P(A|B_i)P(B_i)}{P(A)}$

### For Binomial Problems
1. Verify: Fixed n trials, two outcomes, constant p, independent trials
2. Identify n, p, and x (number of successes)
3. Use $P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}$
4. For cumulative: Sum individual probabilities or use complement

### For With/Without Replacement
- **With replacement**: Independent draws, use multiplication rule directly
- **Without replacement**: Conditional probabilities change; use $P(A \cap B) = P(A)P(B|A)$

---

## 2.11 Common Mistakes to Avoid

| Mistake | Correction |
|---------|------------|
| Using $P(A \cup B) = P(A) + P(B)$ for non-mutually exclusive events | Always subtract $P(A \cap B)$ |
| Confusing $P(A|B)$ with $P(B|A)$ | Use Bayes to convert; they're different! |
| Assuming independence without justification | Check if $P(A \cap B) = P(A)P(B)$ holds |
| Forgetting partition must be exhaustive in Total Probability | Sum of $P(B_i)$ must = 1 |
| Using wrong denominator in Bayes | Denominator = $P(A) = \sum P(A|B_i)P(B_i)$, not just $P(A|B_i)$ |
| Forgetting order matters in without replacement | Sample space size = $N \times (N-1) \times \ldots$ |
| Not defining events clearly before solving | Always state: $A = \ldots$, $B = \ldots$ |
| Confusing mutually exclusive with independent | Mutually exclusive: $P(A \cap B) = 0$; Independent: $P(A \cap B) = P(A)P(B)$ |
| Forgetting "at least one" = 1 - P(none) | Use complement rule for "at least one" problems |

---

## 2.12 Diagrams

### Venn Diagram for Addition Law
```
        S
    ┌─────────┐
    │  ┌───┐  │
    │  │ A │  │
    │  └─┬─┘  │
    │    │    │
    │  ┌─┴─┐  │
    │  │ B │  │
    │  └───┘  │
    └─────────┘
A ∪ B = shaded area
A ∩ B = overlap
```

### Bayes' Theorem Flow
```
Prior: P(B₁)  P(B₂)  ...  P(Bₙ)
  │
  ▼ (Multiply by likelihoods)
Likelihood: P(A|B₁)  P(A|B₂)  ...  P(A|Bₙ)
  │
  ▼
Joint: P(A∩B₁)  P(A∩B₂)  ...  P(A∩Bₙ)
  │
  ▼ (Normalize by P(A))
Posterior: P(B₁|A)  P(B₂|A)  ...  P(Bₙ|A)
```

### With vs Without Replacement
```
WITH REPLACEMENT (Independent)
Draw 1: 6 choices → Replace → Draw 2: 6 choices
Sample space = 6 × 6 = 36

WITHOUT REPLACEMENT (Dependent)
Draw 1: 6 choices → No replace → Draw 2: 5 choices
Sample space = 6 × 5 = 30
```

---

## 2.13 Worked Examples from Textbook (Must Practice)

### Example 1: Classical Probability (Two Dice)
- Sample space: 36 outcomes
- P(sum ≥ 7) = 21/36 = 7/12
- P(both odd) = 9/36 = 1/4

### Example 2: Three Coin Tosses
- S = 8 outcomes
- P(at least 1 head) = 7/8
- P(odd number of heads) = 4/8 = 1/2

### Example 3: Marbles Without Replacement (Problem 1)
- 6 balls (4W, 2R), draw 2
- P(both white) = 12/30 = 2/5
- P(same colour) = 14/30 = 7/15
- P(at least one white) = 28/30 = 14/15

### Example 4: Three Schools Admission (Problem 3)
- P(A∪B∪C) = S₁ - S₂ + S₃ = 0.98 - 0.21 + 0.03 = 0.80
- P(none) = 0.20

### Example 5: Blood Disease Test (Problem 4)
- P(Disease|Test+) = 0.108/0.152 = 0.7105
- P(Correct detection) = 0.944

### Example 6: Coin Toss Independence (Example 18)
- P(H on 1st) = 0.5, P(H on 2nd) = 0.5
- P(H on both) = 0.25 = 0.5 × 0.5 ✓ Independent

---

## 2.14 Practice Problems (PYQ Style)

### Problem 1 (Dec 2022, 2023, 2024, 2025, Jun 2024 - 5 IDENTICAL!)
> Three students A, B, C solve a problem with probabilities 1/2, 1/3, 1/4. Find probability problem is solved.

### Problem 2 (Dec 2021)
> Probability of cancer = 0.05. Smoker: P(Cancer|Smoke) = 0.1. Non-smoker: P(Cancer|No Smoke) = 0.01. 20% smoke. Given cancer, find probability person smokes.

### Problem 3 (Dec 2024)
> Rahul hits target with prob 0.3, Meena with 0.4. Both shoot once. Find prob (i) both hit (ii) at least one hits (iii) exactly one hits.

### Problem 4 (Jun 2024)
> Balls drawn from bag with 4 white, 6 black. Two drawn without replacement. Find prob both white / one each / both black.

### Problem 5 (Dec 2023 - Bayes)
> Radar traps at 4 locations. Probabilities of operation: 0.4, 0.3, 0.2, 0.1. Probabilities of speeding through: 0.2, 0.1, 0.5, 0.2. Find prob caught; if caught, prob at location 1.

### Problem 6 (Book Exercise E9)
> How many times should unbiased coin be tossed so P(at least 1 head) ≥ 0.9?
> **Answer**: n = 4 (since 1 - (1/2)^4 = 15/16 = 0.9375 > 0.9)

### Problem 7 (Book Exercise E10 - Two Dice Conditional)
> Two fair dice rolled. P(sum=7 | sum odd) = 1/3
> P(sum=7 | sum > 6) = 2/7

---

## 2.15 Exam Tips

- ✅ **Additive Law**: Appeared 5+ times - MASTER IT (especially "at least one" = 1 - P(none))
- ✅ **Bayes' Theorem**: High priority, appears in 10-mark questions (Radar traps, Cancer/Smoker)
- ✅ **Conditional Probability**: Foundation for Bayes
- ✅ **Binomial Applications**: 5-mark calculation questions (target hitting, coin tosses)
- ✅ **With/Without Replacement**: Critical distinction for independence
- ✅ **Three Events Addition Law**: $P(A\cup B\cup C) = \sum P - \sum P(\text{pairs}) + P(\text{triple})$
- ✅ **Boole's Inequality**: $P(\cup E_i) \leq \sum P(E_i)$ - useful for bounds
- ✅ **Define events clearly** with notation before solving
- ✅ **Show all steps** - partial credit for correct method
- ❌ Don't assume independence unless stated or verified
- ❌ Don't forget $P(A \cap B)$ in addition law
- ❌ Don't confuse $P(A|B)$ with $P(B|A)$
- ❌ Don't forget partition must be exhaustive in Total Probability
- ❌ Don't confuse mutually exclusive with independent events

---

*End of Unit 2 Notes*

**Textbook Reference**: IGNOU BCS-040 Unit 2 "Probability Concepts" - All formulas, definitions, propositions, and examples verified against original textbook content.