# UNIT 19: CREATING MASTERS IN TALLY

**Block 6: Computerised Accounting** | **PYQ Priority: 🟡 MEDIUM** (5/10 papers - Ledger, Group, Stock Masters appear in 50% of papers)

---

## 19.1 INTRODUCTION

**Masters** in Tally are the **building blocks** for recording transactions. They define the structure of accounts and inventory. Once created, they are used repeatedly in vouchers.

### **Types of Masters:**
1. **Accounts Masters** - Groups, Ledgers
2. **Inventory Masters** - Stock Items, Stock Groups, Stock Categories, Units of Measure, Godowns

---

## 19.2 GROUPS IN TALLY 🔴 HIGH PRIORITY

### **Definition:**
A **Group** is a collection of **ledgers of similar nature**. It determines how ledgers behave in reports (BS, P&L).

### **Primary Groups (15 Pre-defined):**

| Group | Under | Nature | Examples |
|-------|-------|--------|----------|
| **1. Capital Account** | Primary | Capital | Capital, Reserves |
| **2. Loans (Liability)** | Primary | Liability | Bank Loans, Unsecured Loans |
| **3. Current Liabilities** | Primary | Liability | Sundry Creditors, Expenses Payable |
| **4. Fixed Assets** | Primary | Asset | Land, Building, Machinery |
| **5. Investments** | Primary | Asset | Shares, Debentures, FD |
| **6. Current Assets** | Primary | Asset | Stock, Cash, Bank, Debtors |
| **7. Branch/Divisions** | Primary | Asset/Liability | Branch Accounts |
| **8. Sales Account** | Primary | Revenue | Sales, Export Sales |
| **9. Purchase Account** | Primary | Expense | Purchases, Import Purchases |
| **10. Direct Incomes** | Primary | Revenue | Freight Income, Commission |
| **11. Indirect Incomes** | Primary | Revenue | Interest, Rent, Discount Received |
| **12. Direct Expenses** | Primary | Expense | Wages, Carriage Inwards, Power |
| **13. Indirect Expenses** | Primary | Expense | Salaries, Rent, Office Expenses |
| **14. Suspense Account** | Primary | Asset/Liability | Suspense |
| **15. Misc. Expenses (ASSET)** | Primary | Asset | Preliminary Exp, Deferred Revenue |

### **Sub-Groups (User-created):**
Created under Primary Groups for further classification.
- Example: **Sundry Debtors** under Current Assets
- Example: **Bank Accounts** under Current Assets
- Example: **Taxes & Duties** under Current Liabilities

### **Group Behaviour (Critical for Reports):**

| Group | Appears In | Side |
|-------|------------|------|
| Capital, Loans, Current Liabilities | Balance Sheet | Liabilities |
| Fixed Assets, Investments, Current Assets, Branch/Divisions | Balance Sheet | Assets |
| Sales, Direct Incomes, Indirect Incomes | Profit & Loss | Credit (Income) |
| Purchase, Direct Expenses, Indirect Expenses | Profit & Loss | Debit (Expense) |

---

## 19.3 LEDGERS 🔴 HIGH PRIORITY

### **Definition:**
A **Ledger** is an **individual account head** for recording transactions. Each ledger belongs to a Group.

### **Ledger vs Group:**
| Aspect | **Group** | **Ledger** |
|--------|-----------|------------|
| **Definition** | Collection of similar ledgers | Individual account head |
| **Example** | Sundry Debtors | Ram's A/c, Shyam's A/c |
| **Transactions** | Not directly | Directly in vouchers |
| **Reports** | Grouped totals | Individual balances |

### **Pre-defined Ledgers (2):**
1. **Cash** - Under Cash-in-hand (Current Assets)
2. **Profit & Loss Account** - Under Primary (auto-updated)

### **Creating a Ledger:**
**Gateway → Accounts Info → Ledgers → Create**

**Fields:**
- **Name:** Ledger name (e.g., "Ram Traders")
- **Alias:** Short name (optional)
- **Under:** Select Group (e.g., Sundry Debtors)
- **Inventory Values Affected:** Yes/No (for stock items)
- **Opening Balance:** If any (Dr/Cr)
- **Mailing Details:** Address, Contact, GSTIN (for GST)

### **Common Ledgers with Groups:**

| Ledger Name | Under Group |
|-------------|-------------|
| Ram Traders | Sundry Debtors |
| Shyam Suppliers | Sundry Creditors |
| Sales | Sales Accounts |
| Purchases | Purchase Accounts |
| Wages | Direct Expenses |
| Salaries | Indirect Expenses |
| Rent | Indirect Expenses |
| Commission Received | Indirect Incomes |
| Interest Received | Indirect Incomes |
| Bank of India | Bank Accounts |
| Machinery | Fixed Assets |
| Stock | Stock-in-hand |

---

## 19.4 STOCK MASTERS (INVENTORY) 🔴 HIGH PRIORITY

### **Stock Item:**
**Individual product** you buy/sell/manufacture.
- **Example:** "Laptop HP 15s i5", "Cement UltraTech 50kg"
- **Fields:** Name, Alias, Under (Stock Group), Units, Rate (Standard Cost/Sale), Opening Stock, GST Details (HSN, Tax Rate)

### **Stock Group:**
**Collection of similar Stock Items.**
- **Example:** "Laptops" (contains HP 15s, Dell Inspiron, Lenovo ThinkPad)
- **Example:** "Cement" (contains UltraTech, ACC, Ambuja)
- **Hierarchy:** Primary → Sub-groups (e.g., Building Materials → Cement → UltraTech)

### **Stock Category:**
**Functional classification CROSS-CUTTING groups.**
- **Example:** "HP Brand" (contains HP Laptops, HP Printers, HP Toners)
- **Example:** "Imported Items" (across different groups)
- **Allows:** Reports by brand, origin, type across groups

### **Comparison:**

| Master | Purpose | Example |
|--------|---------|---------|
| **Stock Item** | Individual product | "Laptop HP 15s" |
| **Stock Group** | Similar products | "Laptops" |
| **Stock Category** | Cross-functional | "HP Brand" |

```
Stock Groups (Hierarchy)          Stock Categories (Parallel)
─────────────────────             ─────────────────────────
Electronics                       HP Brand
  └── Laptops                         ├── HP Laptops
      ├── HP 15s                         └── HP Printers
      ├── Dell Inspiron
  └── Printers                        Dell Brand
      ├── HP LaserJet
      └── Canon Pixma
```

---

## 19.5 UNITS OF MEASURE

### **Simple Units:**
Single unit (no conversion).
- **Examples:** Pcs, Nos, Kg, Mtr, Ltr, Box, Dozen

### **Compound Units:**
Two units with conversion factor.
- **Examples:** "Kg of 1000 Grams", "Box of 12 Pcs", "Dozen of 12 Pcs"
- **Format:** Main Unit / Sub Unit = Conversion Factor

### **Creating Units:**
**Gateway → Inventory Info → Units of Measure → Create**

---

## 19.6 GODOWNS (WAREHOUSES)

### **Definition:**
Physical locations where stock is stored.

### **Features:**
- **Multiple Godowns** supported
- **Hierarchical** (Main Godown → Sub-godowns)
- **Stock Transfer** between godowns via Stock Journal

### **Example:**
- **Main Warehouse** (Primary)
  - **Raw Material Section**
  - **Finished Goods Section**
- **Branch Godown - Delhi**
- **Branch Godown - Mumbai**

---

## 19.7 ALTERING, DELETING, DISPLAYING MASTERS

### **Alter Master:**
Gateway → Accounts/Inventory Info → Ledger/Group/Stock Item → Alter
- Modify any field except Name (Name change = Delete + Create)

### **Delete Master:**
Gateway → Accounts/Inventory Info → Ledger/Group/Stock Item → Delete
- **Only if NO transactions** exist
- **Shortcut:** Alt+D in Alter mode

### **Display Master:**
Gateway → Accounts/Inventory Info → Ledger/Group/Stock Item → Display
- View details without editing

---

## 19.8 IMPORTANT EXAM QUESTIONS (From PYQ Analysis)

### **2 Marks Questions:**
1. What is a Group in Tally?
2. What is a Ledger in Tally?
3. Difference between Group and Ledger.
4. What is a Stock Item?
5. What is a Stock Group?
6. What is a Stock Category?
7. Difference between Stock Group and Stock Category.
8. What are Units of Measure?
9. What is a Compound Unit?
10. What is a Godown?

### **5 Marks Questions:**
1. Explain the 15 Primary Groups in Tally.
2. Distinguish between Group and Ledger with examples.
3. Explain Stock Item, Stock Group, and Stock Category with examples.
4. Explain Simple and Compound Units of Measure.
5. How to create a Ledger in Tally?

### **10 Marks Questions:**
1. **Difference between stock item, stock group and stock category.** (Dec 2021, Dec 2024, Dec 2025, June 2025, June 2026 - 3+7+10 / 10+10 marks)
2. **Tally and its components.** (Dec 2022 - 10 marks)
3. **Creation of Masters - Ledger, Group, Stock.** (Dec 2024, June 2025, June 2026)

---

## 19.9 KEY POINTS FOR REVISION

- ✅ **15 Primary Groups** - Fixed in Tally, determine BS/P&L placement
- ✅ **Group** = Collection of ledgers | **Ledger** = Individual account
- ✅ **Ledger belongs to ONE Group** - Determines its behaviour
- ✅ **Stock Item** = Individual product
- ✅ **Stock Group** = Similar items (hierarchical)
- ✅ **Stock Category** = Cross-functional (parallel classification)
- ✅ **Units:** Simple (Pcs, Kg) | Compound (Box of 12 Pcs)
- ✅ **Godowns** = Physical storage locations
- ✅ **Pre-defined Ledgers:** Cash, Profit & Loss Account
- ✅ **Alter/Delete/Display** - Only delete if no transactions

---

## 19.10 MEMORY AIDS

### **15 Primary Groups: "CLIC FSD BIS PDI"**
- **C**apital Account
- **L**oans (Liability)
- **I**nvestments
- **C**urrent Liabilities
- **F**ixed Assets
- **S**uspense Account
- **D**irect Expenses
- **B**ranch/Divisions
- **I**ndirect Expenses
- **S**ales Account
- **P**urchase Account
- **D**irect Incomes
- **I**ndirect Incomes
- **C**urrent Assets
- **M**isc Expenses (Asset)

### **Stock Masters: "ITEM-GROUP-CATEGORY"**
- **Item** = Individual product
- **Group** = Similar products (tree)
- **Category** = Cross-functional (matrix)

---

## 19.11 QUICK REFERENCE - GROUP BEHAVIOUR

| Group | Financial Statement | Side | Normal Balance |
|-------|---------------------|------|----------------|
| Capital Account | Balance Sheet | Liabilities | Credit |
| Loans (Liability) | Balance Sheet | Liabilities | Credit |
| Current Liabilities | Balance Sheet | Liabilities | Credit |
| Fixed Assets | Balance Sheet | Assets | Debit |
| Investments | Balance Sheet | Assets | Debit |
| Current Assets | Balance Sheet | Assets | Debit |
| Branch/Divisions | Balance Sheet | Assets/Liab | Debit/Credit |
| Sales Account | Profit & Loss | Credit | Credit |
| Purchase Account | Profit & Loss | Debit | Debit |
| Direct Incomes | Profit & Loss | Credit | Credit |
| Indirect Incomes | Profit & Loss | Credit | Credit |
| Direct Expenses | Profit & Loss | Debit | Debit |
| Indirect Expenses | Profit & Loss | Debit | Debit |
| Suspense Account | Balance Sheet | Assets/Liab | Debit/Credit |
| Misc. Expenses (Asset) | Balance Sheet | Assets | Debit |

---

*End of Unit 19 Notes*