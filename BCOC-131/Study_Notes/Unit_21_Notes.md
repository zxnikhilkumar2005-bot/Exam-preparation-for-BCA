# UNIT 21: PREPARATION OF REPORTS IN TALLY

**Block 6: Computerised Accounting** | **PYQ Priority: 🟡 MEDIUM** (4/10 papers - Reports appear in 40% of papers)

---

## 21.1 INTRODUCTION

One of the **biggest advantages** of computerised accounting is **instant report generation**. Tally automatically prepares all standard financial reports from voucher entries without any additional work.

---

## 21.2 KEY REPORTS IN TALLY 🔴 HIGH PRIORITY

### **1. BALANCE SHEET**

**Purpose:** Shows **Financial Position** (Assets, Liabilities, Capital) on a specific date.

**Features:**
- **Vertical Format** (Schedule VI compliant) / **Horizontal Format**
- **Group-wise** / **Ledger-wise** detail
- **As on Date** - Any date (default: current date)
- **With/Without** Opening/Closing Stock
- **Comparison** - Current vs Previous Year

**Path:** Gateway → **Balance Sheet** (F12 for options)

---

### **2. PROFIT & LOSS ACCOUNT**

**Purpose:** Shows **Operating Result** (Net Profit/Loss) for a period.

**Features:**
- **Vertical Format** / **Horizontal Format**
- **Group-wise** / **Ledger-wise** detail
- **Period:** Any date range (default: financial year)
- **Comparison** - Current vs Previous Period
- **Gross Profit, Net Profit** automatically calculated

**Path:** Gateway → **Profit & Loss A/c** (F12 for options)

---

### **3. STOCK SUMMARY**

**Purpose:** Shows **Inventory Position** (Quantity, Rate, Value).

**Features:**
- **Stock Item-wise** / **Stock Group-wise** / **Stock Category-wise**
- **Godown-wise** detail
- **Batch-wise** (for pharma/FMCG)
- **Valuation Method:** FIFO, LIFO, Weighted Average, Standard Cost
- **Ageing Analysis** - Slow/Non-moving stock
- **Reorder Level** status

**Path:** Gateway → **Stock Summary** (F12 for options)

---

### **4. DAY BOOK**

**Purpose:** Shows **All Vouchers** date-wise (Complete transaction log).

**Features:**
- **All voucher types** or **specific type** (Sales, Purchase, etc.)
- **Date range** filter
- **Party-wise** / **Amount-wise** filters
- **Drill-down** to voucher from Day Book
- **Export** to Excel/PDF

**Path:** Gateway → **Display → Day Book** (F12 for options)

---

### **5. TRIAL BALANCE**

**Purpose:** Checks **Arithmetical Accuracy** (Debits = Credits).

**Features:**
- **Grouped** (by Group) / **Detailed** (All Ledgers)
- **Opening/Closing** balances
- **Net Balances** only
- **As on Date** / **Period** balances
- **With/Without** Zero-balance ledgers

**Path:** Gateway → **Trial Balance** (F12 for options)

---

### **6. CASH/BANK BOOK**

**Purpose:** Shows **Cash Flow** (Receipts & Payments).

**Features:**
- **Cash Book** / **Bank Book** / **Both**
- **Daily** / **Monthly** summary
- **Receipt/Payment** side totals
- **Opening/Closing** balance
- **Bank Reconciliation** integration

**Path:** Gateway → **Display → Account Books → Cash/Bank Book**

---

### **7. RATIO ANALYSIS**

**Purpose:** **Financial Health** analysis.

**Key Ratios:**
| Category | Ratios |
|----------|--------|
| **Liquidity** | Current Ratio, Quick Ratio, Cash Ratio |
| **Profitability** | Gross Profit %, Net Profit %, ROCE, ROE |
| **Solvency** | Debt-Equity, Interest Coverage, Debt Service |
| **Efficiency** | Stock Turnover, Debtor Turnover, Creditor Turnover |
| **Leverage** | Capital Gearing, Proprietary Ratio |

**Path:** Gateway → **Ratio Analysis** (F12 for options)

---

### **8. GST RETURNS (GSTR-1, GSTR-3B) 🔴 HIGH PRIORITY**

**Purpose:** **GST Compliance** - Auto-filled from vouchers.

**GSTR-1 (Monthly/Quarterly Outward Supplies):**
- B2B Invoices (Inter/Intra-state)
- B2C Large Invoices
- Credit/Debit Notes
- Export Invoices
- HSN Summary
- Document Summary

**GSTR-3B (Monthly Summary Return):**
- Outward Supplies Summary
- Inward Supplies (Reverse Charge)
- ITC Claimed
- Tax Liability & Payment

**Features:**
- **Auto-populated** from Sales/Purchase vouchers
- **Error detection** (Missing GSTIN, HSN, etc.)
- **JSON Export** for portal upload
- **Reconciliation** with books

**Path:** Gateway → **Display → GST Reports → GSTR-1 / GSTR-3B**

---

### **9. PAYROLL REPORTS**

**Purpose:** **Salary Processing** & Compliance.

**Reports:**
- **Pay Slips** (Employee-wise)
- **Payroll Register** (Month-wise)
- **PF/ESI Challans** (Auto-filled)
- **Form 16 / 16A** (TDS Certificates)
- **Salary Register** (Component-wise)
- **Attendance Register**

**Path:** Gateway → **Display → Payroll Reports**

---

### **10. EXCEPTION REPORTS**

**Purpose:** **Identify Issues** - Negative Cash, Negative Stock, etc.

**Common Exception Reports:**
- **Negative Cash/Bank** - Overdrawn accounts
- **Negative Stock** - Oversold items
- **Outstanding Receivables/Payables** - Ageing
- **Budget Variance** - Actual vs Budget
- **Cost Centre Variance**

**Path:** Gateway → **Display → Exception Reports**

---

## 21.3 REPORT CUSTOMISATION (F12 CONFIGURATION)

### **Common Options (F12 in any Report):**

| Option | Description |
|--------|-------------|
| **Format** | Vertical / Horizontal / Detailed / Condensed |
| **Period** | Specific Date / Date Range / Financial Year |
| **Method of Stock Valuation** | FIFO / LIFO / Weighted Avg / Standard Cost |
| **Show** | Opening/Closing Stock / Zero-balance / Net Balances |
| **Group By** | Primary Group / Ledger / Cost Centre / Godown |
| **Sorting** | Alphabetical / Amount / Date |
| **Percentage** | Show % of Total / % of Previous Period |
| **Export** | ASCII / Excel / HTML / PDF / XML |

---

## 21.4 DRILL-DOWN FACILITY

### **Concept:**
Click **Enter** on any figure in a report to **drill down** to:
1. **Group Total** → Ledger Balances
2. **Ledger Balance** → Voucher Register (All entries)
3. **Voucher Register** → Individual Voucher
4. **Voucher** → Modify/View entry

### **Navigation:**
- **Enter** = Drill down
- **Esc** = Go back one level
- **Alt+F1** = Back to Gateway

---

## 21.5 EXPORTING REPORTS

### **Export Formats:**
| Format | Use Case |
|--------|----------|
| **Excel** | Further analysis, pivot tables |
| **PDF** | Sharing, printing, audit trail |
| **HTML** | Web publishing |
| **XML** | Data interchange, GST portal |
| **ASCII** | Legacy system import |

### **Export Path:**
Any Report → **Alt+E** (Export) → Select Format → File Name → **Accept**

---

## 21.6 IMPORTANT EXAM QUESTIONS (From PYQ Analysis)

### **2 Marks Questions:**
1. What is Balance Sheet in Tally?
2. What is Profit & Loss Account in Tally?
3. What is Stock Summary?
4. What is Day Book?
5. What is Trial Balance in Tally?
6. What is Ratio Analysis?
7. What is GSTR-1?
8. What is GSTR-3B?
9. What is Drill-down facility?
10. Name four reports in Tally.

### **5 Marks Questions:**
1. Explain the features of Balance Sheet in Tally.
2. Explain the Stock Summary report.
3. What is Day Book? How is it useful?
4. Explain Ratio Analysis in Tally.
5. How are GST Returns generated in Tally?
6. Explain the Drill-down facility in Tally.

### **10 Marks Questions:**
1. **Preparation of Reports using Tally ERP.** (Dec 2022, Dec 2023, June 2024, June 2025 - 10+10 / 2×10 marks)
2. **Reports in Tally - Balance Sheet, P&L, Stock Summary, Day Book.** (Multiple years)

---

## 21.7 KEY POINTS FOR REVISION

- ✅ **Auto-generated Reports** - No manual preparation needed
- ✅ **10 Key Reports:** Balance Sheet, P&L, Stock Summary, Day Book, Trial Balance, Cash/Bank Book, Ratio Analysis, GSTR-1, GSTR-3B, Payroll Reports
- ✅ **Customisation (F12):** Format, Period, Valuation, Grouping, Sorting
- ✅ **Drill-down:** Enter on any figure → Voucher level detail
- ✅ **GSTR-1/GSTR-3B** - Auto-filled, JSON export for portal
- ✅ **Export Formats:** Excel, PDF, XML, HTML, ASCII
- ✅ **Vertical/Horizontal** formats for BS & P&L
- ✅ **Stock Valuation Methods:** FIFO, LIFO, Weighted Avg, Standard Cost

---

## 21.8 MEMORY AIDS

### **Key Reports: "BS PL SS DB TB CB RA GST PR"**
- **B**alance **S**heet
- **P**rofit & **L**oss
- **S**tock **S**ummary
- **D**ay **B**ook
- **T**rial **B**alance
- **C**ash/**B**ank Book
- **R**atio **A**nalysis
- **GST** Returns (GSTR-1, GSTR-3B)
- **P**ay**R**oll Reports

### **Drill-down: "ENTER-ESC-ENTER"**
- **Enter** = Go deeper
- **Esc** = Go back
- **Enter** = Open voucher

---

## 21.9 QUICK REFERENCE - REPORT PATHS

| Report | Gateway Path |
|--------|--------------|
| Balance Sheet | Balance Sheet (Direct) |
| Profit & Loss | Profit & Loss A/c (Direct) |
| Stock Summary | Stock Summary (Direct) |
| Day Book | Display → Day Book |
| Trial Balance | Trial Balance (Direct) |
| Cash/Bank Book | Display → Account Books → Cash/Bank Book |
| Ratio Analysis | Ratio Analysis (Direct) |
| GSTR-1 | Display → GST Reports → GSTR-1 |
| GSTR-3B | Display → GST Reports → GSTR-3B |
| Payroll Reports | Display → Payroll Reports |
| Exception Reports | Display → Exception Reports |

---

*End of Unit 21 Notes*