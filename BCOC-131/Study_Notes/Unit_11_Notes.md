# UNIT 11: HIRE PURCHASE ACCOUNTS-I

**Block 4: Hire Purchase and Inland Branches** | **PYQ Priority: 🔴 HIGH** (9/10 papers - Hire Purchase appears in 90% of papers)

---

## 11.1 INTRODUCTION

**Hire Purchase System** is a method of selling goods where:
- Buyer takes **possession** immediately
- Payment made in **instalments** over time
- **Ownership** transfers only after **last instalment** paid
- Each instalment treated as **hire charge** until full payment
- If buyer defaults, seller can **repossess** goods without refund

---

## 11.2 NATURE OF HIRE PURCHASE AGREEMENT

### **Key Features:**
1. **Possession** delivered to hire purchaser
2. **Payment in instalments** (includes interest)
3. **Each instalment = hire charge** (until full payment)
4. **Ownership** passes on last instalment
5. **Right to terminate** - Hirer can return goods anytime
6. **Default consequences** - Seller repossesses, no refund of past payments

### **Hire Purchase Price = Cash Price + Interest + Other Charges**

---

## 11.3 LEGAL POSITION (HIRE PURCHASE ACT, 1972)

### **Definition (Section 2(c)):**
Agreement where goods let on hire with option to purchase, where:
1. Possession delivered on condition of periodical payments
2. Property passes on last payment
3. Hirer can terminate anytime before property passes

### **Characteristics (Section 4):**
- Must be in writing, signed by all parties
- Must state: HP Price, Cash Price, Commencement date, Number/amount/dates of instalments, Description of goods

### **Rights of Hirer:**
1. Owner cannot terminate without notice (1 week for weekly, 2 weeks otherwise)
2. Court permission needed for repossession if:
   - HP Price < ₹15,000 and ½ paid, OR
   - HP Price ≥ ₹15,000 and ¾ paid
   - Motor vehicles: special rules apply
3. Right to statement of account on payment of ₹1

---

## 11.4 ASCERTAINING INTEREST AND CASH PRICE

### **Key Terms:**
| Term | Meaning |
|------|---------|
| **Cash Price** | Price if paid in full upfront |
| **Hire Purchase Price** | Total of all instalments + Down payment |
| **Total Interest** | HP Price - Cash Price |
| **Down Payment** | Initial payment on signing |

### **Interest Calculation Methods:**

#### **Method 1: When Cash Price and Rate Given**
```
Interest for Period = Opening Balance × Rate × Period
Closing Balance = Opening Balance + Interest - Instalment
```

#### **Method 2: When Cash Price Not Given (Sum of Digits / Ratio Method)**
```
Total Interest = HP Price - Cash Price
Interest allocated in ratio of outstanding balances
Ratio = Sum of digits of outstanding months
```

#### **Method 3: Flat Rate (Simple Interest on Original Amount)**
```
Interest = Cash Price × Rate × Total Period
```
(Not commonly used in HP accounting)

---

## 11.5 ACCOUNTING IN BOOKS OF HIRE PURCHASER

### **Two Methods:**

### **Method A: Asset Recorded at Full Cash Price (Standard Method)**

**Journal Entries:**

| Transaction | Journal Entry |
|-------------|---------------|
| **1. On Purchase (Asset at Cash Price)** | Asset A/c Dr. (Cash Price)<br>To Vendor A/c (Cash Price) |
| **2. Down Payment** | Vendor A/c Dr. (Down Payment)<br>To Bank A/c (Down Payment) |
| **3. Interest Due (Each Period)** | Interest A/c Dr. (Interest)<br>To Vendor A/c (Interest) |
| **4. Instalment Paid** | Vendor A/c Dr. (Instalment)<br>To Bank A/c (Instalment) |
| **5. Depreciation (Year-end)** | Depreciation A/c Dr.<br>To Asset A/c |
| **6. Transfer to P&L** | P&L A/c Dr. (Depreciation + Interest)<br>To Depreciation A/c<br>To Interest A/c |

### **Ledger Accounts:**

#### **Asset Account (at Cash Price):**
```
DR.                              ASSET ACCOUNT                              CR.
Date       Particulars           Amount          Date       Particulars           Amount
Year 1                                                     Year 1
Apr 1      To Vendor A/c        (Cash Price)     Mar 31   By Depreciation A/c     (Dep)
           To Bank (additions)                   Mar 31   By Balance c/d          (WDV)
                                                        ----                  ----
                                                        Total                 Total
Year 2                                                     Year 2
Apr 1      To Balance b/d       (WDV)            Mar 31   By Depreciation A/c     (Dep)
                                                        Mar 31   By Balance c/d          (WDV)
```

#### **Vendor Account:**
```
DR.                              VENDOR ACCOUNT                              CR.
Date       Particulars           Amount          Date       Particulars           Amount
Year 1                                                     Year 1
Apr 1      To Bank (Down Pmt)    (Down Pmt)       Apr 1      By Asset A/c           (Cash Price)
Mar 31     To Bank (Instalment)  (Instalment)     Mar 31     By Interest A/c        (Interest)
Mar 31     To Balance c/d        (Bal)                                                        ----
                                                        ----                  ----
                                                        Total                 Total
Year 2                                                     Year 2
Apr 1      To Balance b/d        (Bal)            Apr 1      By Interest A/c        (Interest)
Mar 31     To Bank (Instalment)  (Instalment)     Mar 31     By Balance c/d         (Bal)
Mar 31     To Balance c/d        (Bal)                                                        ----
                                                        ----                  ----
                                                        Total                 Total
```

---

### **Method B: Asset Recorded at Cash Price Actually Paid**

- Asset debited only with amount **actually paid** (Down payment + Instalments paid)
- No Interest Account - Interest forms part of asset cost
- **Not recommended** - Doesn't show true asset value or interest expense separately

---

## 11.6 ACCOUNTING IN BOOKS OF VENDOR

### **Journal Entries:**

| Transaction | Journal Entry |
|-------------|---------------|
| **1. On Sale (HP Price)** | Hire Purchaser A/c Dr. (HP Price)<br>To HP Sales A/c (Cash Price)<br>To Interest Suspense A/c (Total Interest) |
| **2. Down Payment Received** | Bank A/c Dr. (Down Payment)<br>To Hire Purchaser A/c (Down Payment) |
| **3. Interest Due (Each Period)** | Interest Suspense A/c Dr. (Interest Due)<br>To Interest A/c (Interest Income) |
| **4. Instalment Received** | Bank A/c Dr. (Instalment)<br>To Hire Purchaser A/c (Instalment) |
| **5. Transfer Sales to P&L** | HP Sales A/c Dr.<br>To Trading/P&L A/c |

### **Ledger Accounts:**

#### **Hire Purchaser Account (Vendor's Books):**
```
DR.                              HIRE PURCHASER ACCOUNT                              CR.
Date       Particulars           Amount          Date       Particulars           Amount
Year 1                                                     Year 1
Apr 1      To HP Sales A/c       (Cash Price)     Apr 1      By Bank (Down Pmt)     (Down Pmt)
           To Interest Suspense  (Total Int)      Mar 31     By Balance c/d         (Bal)
Mar 31     By Interest Suspense  (Int Due)                                                     ----
                                                        ----                  ----
                                                        Total                 Total
Year 2                                                     Year 2
Apr 1      To Balance b/d        (Bal)            Apr 1      By Bank (Instalment)   (Instalment)
Mar 31     By Interest Suspense  (Int Due)        Mar 31     By Balance c/d         (Bal)
                                                        ----                  ----
                                                        Total                 Total
```

#### **Interest Suspense Account:**
```
DR.                              INTEREST SUSPENSE ACCOUNT                              CR.
Date       Particulars           Amount          Date       Particulars           Amount
Year 1                                                     Year 1
Mar 31     To Interest A/c       (Int Due)        Apr 1      By Hire Purchaser A/c   (Total Int)
                                                        Mar 31     By Balance c/d         (Bal)
                                                        ----                  ----
                                                        Total                 Total
Year 2                                                     Year 2
Mar 31     To Interest A/c       (Int Due)        Apr 1      By Balance b/d         (Bal)
                                                        Mar 31     By Balance c/d         (Bal)
                                                        ----                  ----
                                                        Total                 Total
```

---

## 11.7 INTEREST CALCULATION - DETAILED EXAMPLE

### **Problem:**
Machine Cash Price ₹1,00,000. Down payment ₹20,000. Balance in 4 yearly instalments of ₹25,000 each. Interest 10% p.a.

### **Calculation:**

| Year | Opening Balance | Interest (10%) | Instalment | Principal Repaid | Closing Balance |
|------|-----------------|----------------|------------|------------------|-----------------|
| 1 | 80,000 (1,00,000-20,000) | 8,000 | 25,000 | 17,000 | 63,000 |
| 2 | 63,000 | 6,300 | 25,000 | 18,700 | 44,300 |
| 3 | 44,300 | 4,430 | 25,000 | 20,570 | 23,730 |
| 4 | 23,730 | 2,373* | 25,000 | 22,627* | 1,103* |

*Adjustment in last year to balance

---

## 11.8 IMPORTANT EXAM QUESTIONS (From PYQ Analysis)

### **2 Marks Questions:**
1. Define Hire Purchase Agreement.
2. What is Cash Price?
3. What is Hire Purchase Price?
4. Difference between Hire Purchase and Instalment System.
5. What is Down Payment?
6. Rights of Hirer under HP Act.
7. What is Interest Suspense Account?

### **5 Marks Questions:**
1. Explain the nature of Hire Purchase Agreement.
2. Distinguish between Hire Purchase System and Instalment Payment System.
3. Explain the legal position of Hire Purchase Agreement.
4. How is interest calculated in Hire Purchase?
5. State the constituents of a Hire Purchase Agreement.

### **10 Marks Questions:**
1. **Hire Purchase - Accounting in Books of Hire Purchaser and Vendor.** (Dec 2021, Dec 2022, Dec 2023, Dec 2024, Dec 2025, June 2022, June 2024, June 2025, June 2026 - 9/10 years)
2. **Define Hire Purchase System. Mention the important constituents of a Hire Purchase Agreement.** (Dec 2024 - 3+7 marks)
3. **Explain the accounting treatment of important items in the books of Hire Purchaser.** (Dec 2025, June 2026 - 5+15 marks)

### **15+5 / 20 Marks Practical (Standard Format):**
- Cash Price, Down Payment, Instalments, Interest Rate given
- Prepare: Asset A/c, Vendor A/c in Purchaser's books
- Prepare: Hire Purchaser A/c, Interest Suspense A/c in Vendor's books
- Sometimes: Depreciation also required
- 3-4 years data

---

## 11.9 KEY POINTS FOR REVISION

- ✅ **Hire Purchase** = Possession now, Ownership later, Instalments include interest
- ✅ **Cash Price** = Upfront price | **HP Price** = Total instalments + Down payment
- ✅ **Interest** = HP Price - Cash Price (allocated over periods on reducing balance)
- ✅ **Purchaser's Books:** Asset at Cash Price, Vendor A/c, Interest A/c, Depreciation
- ✅ **Vendor's Books:** Hire Purchaser A/c (HP Price), HP Sales (Cash Price), Interest Suspense (Total Interest)
- ✅ **Interest Suspense** = Unearned interest, transferred to Interest Income periodically
- ✅ **Default/Repossession** = Covered in Unit 12
- ✅ **Instalment System** = Ownership passes immediately, no repossession right

---

## 11.10 MEMORY AIDS

### **Purchaser's Entries: "AVID"**
- **A**sset Dr (Cash Price) / To Vendor
- **V**endor Dr (Down Pmt) / To Bank
- **I**nterest Dr / To Vendor
- **V**endor Dr (Instalment) / To Bank
- **D**epreciation Dr / To Asset

### **Vendor's Entries: "HIS BI"**
- **H**ire Purchaser Dr (HP Price) / To HP Sales + Interest Suspense
- **I**nterest Suspense Dr / To Interest Income
- **S**uspense = Unearned Interest
- **B**ank Dr (Down/Instalment) / To Hire Purchaser
- **I**ncome = Interest transferred from Suspense

---

## 11.11 QUICK REFERENCE - LEDGER ACCOUNT FORMATS

### **Asset Account (Purchaser):**
```
Dr. Side: To Vendor (Cash Price), To Bank (Additions), To Balance b/d
Cr. Side: By Depreciation, By Disposal (if sold), By Balance c/d
```

### **Vendor Account (Purchaser):**
```
Dr. Side: To Bank (Down Pmt), To Bank (Instalments), To Balance c/d
Cr. Side: By Asset (Cash Price), By Interest, By Balance b/d
```

### **Hire Purchaser Account (Vendor):**
```
Dr. Side: To HP Sales (Cash Price), To Interest Suspense (Total Int), To Balance b/d
Cr. Side: By Bank (Down Pmt), By Interest Suspense (Int Due), By Bank (Instalments), By Balance c/d
```

### **Interest Suspense Account (Vendor):**
```
Dr. Side: To Interest Income (Periodic)
Cr. Side: By Hire Purchaser (Total Int), By Balance b/d/c/d
```

---

*End of Unit 11 Notes*