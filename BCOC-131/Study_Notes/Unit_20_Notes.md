# UNIT 20: VOUCHER ENTRIES AND INVOICING

**Block 6: Computerised Accounting** | **PYQ Priority: 🟡 MEDIUM** (5/10 papers - Voucher types, creation, post-dated appear in 50% of papers)

---

## 20.1 INTRODUCTION

**Vouchers** in Tally are the **primary documents** for recording transactions. Every accounting entry is made through a voucher. Tally provides different voucher types for different transaction categories.

---

## 20.2 VOUCHER TYPES IN TALLY 🔴 HIGH PRIORITY

### **Accounting Vouchers (F4-F9, Ctrl+F8/F9):**

| Voucher Type | Shortcut | Purpose | Dr./Cr. Rules |
|--------------|----------|---------|---------------|
| **Contra** | **F4** | Cash ↔ Bank, Bank ↔ Bank | Cash/Bank Dr, Cash/Bank Cr |
| **Payment** | **F5** | Cash/Bank Payments | Expense/Asset/Creditor Dr, Cash/Bank Cr |
| **Receipt** | **F6** | Cash/Bank Receipts | Cash/Bank Dr, Income/Asset/Debtor Cr |
| **Journal** | **F7** | Non-cash adjustments | Any Dr, Any Cr |
| **Sales** | **F8** | Credit Sales | Debtor Dr, Sales Cr |
| **Purchase** | **F9** | Credit Purchases | Purchase Dr, Creditor Cr |
| **Debit Note** | **Ctrl+F9** | Purchase Returns | Creditor Dr, Purchase Returns Cr |
| **Credit Note** | **Ctrl+F8** | Sales Returns | Sales Returns Cr, Debtor Cr |
| **Memo** | **Ctrl+F10** | Non-accounting entries | No ledger impact |
| **Optional** | **Ctrl+F7** | Post-dated / Reversing | Temporary, becomes regular on date |

### **Inventory Vouchers (Alt+F4-F9):**
- **Alt+F4** - Receipt Note (Goods received)
- **Alt+F5** - Delivery Note (Goods delivered)
- **Alt+F6** - Rejection In (Purchase Returns)
- **Alt+F7** - Stock Journal (Inter-godown, Manufacturing)
- **Alt+F8** - Physical Stock (Stock taking)
- **Alt+F9** - Sales Order / Purchase Order

### **Payroll Voucher:**
- **Ctrl+F4** - Payroll (Salary, Wages, PF, ESI)

---

## 20.3 DETAILED VOUCHER USAGE

### **1. Contra Voucher (F4) - Cash/Bank Transfers**
| Transaction | Dr. | Cr. |
|-------------|-----|-----|
| Cash deposited in Bank | Bank | Cash |
| Cash withdrawn from Bank | Cash | Bank |
| Cheque deposited | Bank | Cash |
| Bank to Bank transfer | Bank A | Bank B |

### **2. Payment Voucher (F5) - All Payments**
| Transaction | Dr. | Cr. |
|-------------|-----|-----|
| Expenses paid (Rent, Salary) | Expense | Cash/Bank |
| Creditor paid | Creditor | Cash/Bank |
| Asset purchased | Asset | Cash/Bank |
| Loan repaid | Loan | Cash/Bank |
| Advance to supplier | Advance | Cash/Bank |

### **3. Receipt Voucher (F6) - All Receipts**
| Transaction | Dr. | Cr. |
|-------------|-----|-----|
| Cash sales | Cash | Sales |
| Debtor collection | Cash/Bank | Debtor |
| Income received (Commission) | Cash/Bank | Income |
| Loan received | Cash/Bank | Loan |
| Capital introduced | Cash/Bank | Capital |

### **4. Journal Voucher (F7) - Adjustments (Non-cash)**
| Transaction | Dr. | Cr. |
|-------------|-----|-----|
| Depreciation | Depreciation | Asset/Provision |
| Outstanding Expenses | Expense | Outstanding Exp |
| Prepaid Expenses | Prepaid Exp | Expense |
| Accrued Income | Accrued Income | Income |
| Bad Debts | Bad Debts | Debtor |
| Provision for Bad Debts | P&L | Provision |
| Rectification Entries | Various | Various |
| Interest on Capital | Interest on Capital | Capital |

### **5. Sales Voucher (F8) - Credit Sales**
- **Dr.** Debtor / **Cr.** Sales
- Auto-updates Stock (if inventory integrated)
- **Invoice Mode** available (Alt+I) for printing invoice

### **6. Purchase Voucher (F9) - Credit Purchases**
- **Dr.** Purchase / **Cr.** Creditor
- Auto-updates Stock (if inventory integrated)

### **7. Debit Note (Ctrl+F9) - Purchase Returns**
- **Dr.** Creditor / **Cr.** Purchase Returns
- Used when returning goods to supplier

### **8. Credit Note (Ctrl+F8) - Sales Returns**
- **Dr.** Sales Returns / **Cr.** Debtor
- Used when customer returns goods

### **9. Memo Voucher (Ctrl+F10) - Non-accounting**
- **No ledger impact** - for reference only
- Examples: Proforma entries, reminders, internal notes

### **10. Optional Voucher (Ctrl+F7) - Post-dated/Reversing**
- **Not posted to ledgers** until made "Regular"
- **Post-dated Vouchers:** Dated future, become regular on that date
- **Reversing Vouchers:** Auto-reverse on specified date
- Used for: PDCs, recurring entries (rent, EMI), accruals

---

## 20.4 CREATING VOUCHERS IN TALLY

### **Standard Voucher Entry Screen:**
```
Voucher Type: Payment (F5)
Date: 15-01-2024
Particulars:
  Dr. Rent A/c                    10,000
  Cr. Cash A/c                    10,000
Narration: Rent paid for Jan 2024
```

### **Steps:**
1. Select Voucher Type (F4-F9, Ctrl+F8/F9)
2. Enter Date (F2 to change)
3. **Dr. Side:** Select Ledger, Enter Amount
4. **Cr. Side:** Select Ledger, Enter Amount
5. Enter Narration
6. **Accept** (Enter) → Saved

### **Invoice Mode (Sales/Purchase):**
- Press **Alt+I** in Sales/Purchase voucher
- Shows **Invoice format** with quantity, rate, amount
- Auto-calculates GST if configured
- Print directly from voucher

---

## 20.5 POST-DATED VOUCHERS 🔴 HIGH PRIORITY

### **Concept:**
Vouchers dated **future** but entered **now**. Remain as **Optional** until due date.

### **Process:**
1. Create voucher with **future date**
2. Mark as **Optional** (Ctrl+F7) or use **Optional Voucher Type**
3. On due date: **Make Regular** (Alt+R or click "Make Regular")
4. Then posts to ledgers

### **Uses:**
- **Post-dated Cheques (PDCs)** received/issued
- **Recurring entries:** Rent, EMI, Salary, Interest
- **Accruals:** Provision entries at year-end

### **Example:**
PDC received dated 15-Feb-2024, entered on 1-Jan-2024:
```
1-Jan: Receipt Voucher (Optional) - Date 15-Feb
       Dr. Bank (PDC) / Cr. Debtor
15-Feb: Make Regular → Posts to ledgers
```

---

## 20.6 ALTERING AND DELETING VOUCHERS

### **Alter Voucher:**
1. Display voucher (Day Book → Select → Enter)
2. Press **Enter** to edit
3. Modify fields
4. **Accept** (Enter)

### **Delete Voucher:**
1. Display voucher
2. Press **Alt+D** (Delete)
3. Confirm

### **Restrictions:**
- **Cannot delete** if:
  - Part of reconciled bank statement
  - Linked to inventory (stock affected)
  - In a locked period (TallyVault/Security)
- **Alter** preferred over Delete

---

## 20.7 INVOICING IN TALLY

### **Sales Invoice (F8 + Alt+I):**
- **Party Details:** Name, Address, GSTIN, State
- **Item Details:** Stock Item, Quantity, Rate, Discount
- **Tax Details:** GST (CGST/SGST/IGST), HSN Code
- **Additional Charges:** Freight, Insurance, Packing
- **Totals:** Taxable Value, Tax Amount, Invoice Total

### **Purchase Invoice (F9 + Alt+I):**
- Similar to Sales but for purchases
- Auto-updates Stock and Creditor

### **GST Invoice Requirements:**
- Supplier/Recipient GSTIN
- HSN/SAC Code
- Taxable Value, Rate, Amount (CGST/SGST/IGST)
- Place of Supply
- Invoice Number & Date

---

## 20.8 COMMON VOUCHER ENTRY SCENARIOS

| Scenario | Voucher Type | Dr. | Cr. |
|----------|--------------|-----|-----|
| Cash Sales | Receipt (F6) | Cash | Sales |
| Credit Sales | Sales (F8) | Debtor | Sales |
| Cash Purchase | Payment (F5) | Purchase | Cash |
| Credit Purchase | Purchase (F9) | Purchase | Creditor |
| Cash Deposited | Contra (F4) | Bank | Cash |
| Cash Withdrawn | Contra (F4) | Cash | Bank |
| Expense Paid | Payment (F5) | Expense | Cash/Bank |
| Income Received | Receipt (F6) | Cash/Bank | Income |
| Depreciation | Journal (F7) | Depreciation | Asset/Provision |
| Outstanding Salary | Journal (F7) | Salary | O/s Salary |
| Bad Debts | Journal (F7) | Bad Debts | Debtor |
| Purchase Return | Debit Note (Ctrl+F9) | Creditor | Purchase Return |
| Sales Return | Credit Note (Ctrl+F8) | Sales Return | Debtor |

---

## 20.9 IMPORTANT EXAM QUESTIONS (From PYQ Analysis)

### **2 Marks Questions:**
1. What is a Voucher in Tally?
2. Name the Accounting Voucher types in Tally.
3. What is Contra Voucher? When is it used?
4. What is Payment Voucher?
5. What is Receipt Voucher?
6. What is Journal Voucher? When is it used?
7. What is Debit Note? When is it used?
8. What is Credit Note? When is it used?
9. What is a Memo Voucher?
10. What is an Optional Voucher?
11. What is a Post-dated Voucher?

### **5 Marks Questions:**
1. Explain the different types of Vouchers in Tally.
2. Distinguish between Debit Note and Credit Note.
3. Explain the use of Journal Voucher with examples.
4. What are Post-dated Vouchers? How are they used?
5. Explain the Invoice Mode in Tally.

### **10 Marks Questions:**
1. **What are the different types of Vouchers? Explain the use of Post-dated Vouchers.** (Dec 2022, Dec 2023, June 2024, June 2025, June 2026 - 5+5 / 10+10 marks)
2. **Vouchers - Types, Creation, Post-dated.** (Multiple years)

---

## 20.10 KEY POINTS FOR REVISION

- ✅ **10 Accounting Voucher Types:** Contra(F4), Payment(F5), Receipt(F6), Journal(F7), Sales(F8), Purchase(F9), Debit Note(Ctrl+F9), Credit Note(Ctrl+F8), Memo(Ctrl+F10), Optional(Ctrl+F7)
- ✅ **Contra** = Cash↔Bank | **Payment** = All payments | **Receipt** = All receipts
- ✅ **Journal** = Non-cash adjustments (Depreciation, Outstanding, Rectification)
- ✅ **Sales(F8)/Purchase(F9)** = Credit transactions only
- ✅ **Debit Note** = Purchase Returns | **Credit Note** = Sales Returns
- ✅ **Memo** = No ledger impact | **Optional** = Post-dated/Reversing
- ✅ **Post-dated Vouchers** = Optional until due date, then "Make Regular"
- ✅ **Invoice Mode** = Alt+I in Sales/Purchase for printed invoices with GST
- ✅ **Alter** = Edit voucher | **Delete** = Alt+D (if allowed)

---

## 20.11 MEMORY AIDS

### **Voucher Shortcuts: "CPRJ SP DCMO"**
- **C**ontra - **F4**
- **P**ayment - **F5**
- **R**eceipt - **F6**
- **J**ournal - **F7**
- **S**ales - **F8**
- **P**urchase - **F9**
- **D**ebit Note - **Ctrl+F9**
- **C**redit Note - **Ctrl+F8**
- **M**emo - **Ctrl+F10**
- **O**ptional - **Ctrl+F7**

### **When to Use: "C-P-R-J-S-P"**
- **C**ash/Bank transfer → **Contra**
- **P**ayments → **Payment**
- **R**eceipts → **Receipt**
- **J**ournal entries → **Journal**
- **S**ales (Credit) → **Sales**
- **P**urchases (Credit) → **Purchase**

---

## 20.12 QUICK REFERENCE - VOUCHER SUMMARY TABLE

| Voucher | Shortcut | Dr. Side | Cr. Side | Common Use |
|---------|----------|----------|----------|------------|
| Contra | F4 | Cash/Bank | Cash/Bank | Deposit/Withdrawal |
| Payment | F5 | Expense/Asset/Creditor | Cash/Bank | All Payments |
| Receipt | F6 | Cash/Bank | Income/Asset/Debtor | All Receipts |
| Journal | F7 | Any | Any | Adjustments |
| Sales | F8 | Debtor | Sales | Credit Sales |
| Purchase | F9 | Purchase | Creditor | Credit Purchases |
| Debit Note | Ctrl+F9 | Creditor | Purchase Return | Purchase Returns |
| Credit Note | Ctrl+F8 | Sales Return | Debtor | Sales Returns |
| Memo | Ctrl+F10 | None | None | Reference Only |
| Optional | Ctrl+F7 | Any | Any | Post-dated |

---

*End of Unit 20 Notes*