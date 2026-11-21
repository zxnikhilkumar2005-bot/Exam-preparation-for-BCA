# UNIT 18: COMPUTERISED ACCOUNTING AND CREATION OF COMPANY

**Block 6: Computerised Accounting** | **PYQ Priority: 🟡 MEDIUM** (9/10 papers - Computerised Accounting appears in 90% of papers)

---

## 18.1 INTRODUCTION

**Computerised Accounting System (CAS)** uses **computer software** to record, process, and report financial transactions. It replaces manual book-keeping with automated processes.

---

## 18.2 MANUAL vs COMPUTERISED ACCOUNTING

| Basis | **Manual Accounting** | **Computerised Accounting** |
|-------|----------------------|----------------------------|
| **Recording** | Hand-written in journals/ledgers | Data entry in software |
| **Speed** | Slow | Very fast |
| **Accuracy** | Prone to human errors | High accuracy (validations) |
| **Reports** | Manual preparation | Auto-generated (BS, P&L, TB, etc.) |
| **Storage** | Physical files | Digital (database, cloud) |
| **Backup** | Difficult | Easy (auto-backup) |
| **Security** | Physical locks | Passwords, encryption, access control |
| **Cost** | Low initial, high recurring | High initial, lower recurring |
| **Staff Skill** | Basic accounting | Accounting + Software knowledge |
| **Query/Analysis** | Manual, time-consuming | Instant (drill-down, filters) |

---

## 18.3 ADVANTAGES OF COMPUTERISED ACCOUNTING 🔴 HIGH PRIORITY

| # | Advantage | Description |
|---|-----------|-------------|
| 1 | **Speed & Accuracy** | Fast processing, mathematical accuracy guaranteed |
| 2 | **Automatic Reports** | BS, P&L, Trial Balance, Stock Summary generated instantly |
| 3 | **Data Security & Backup** | Password protection, encryption, auto-backup, disaster recovery |
| 4 | **Less Paperwork** | Digital records, paperless office |
| 5 | **Easy Data Retrieval** | Search, filter, sort instantly |
| 6 | **Multi-user Access** | Simultaneous access with user rights |
| 7 | **GST/TDS Compliance** | Auto-calculation, return filing (GSTR-1, GSTR-3B) |
| 8 | **Ratio Analysis & Forecasting** | Built-in analytical tools |
| 9 | **Integration** | With inventory, payroll, CRM, banking |
| 10 | **Audit Trail** | Complete log of all entries/changes |

---

## 18.4 DISADVANTAGES OF COMPUTERISED ACCOUNTING 🔴 HIGH PRIORITY

| # | Disadvantage | Description |
|---|--------------|-------------|
| 1 | **High Initial Cost** | Software, hardware, training, implementation |
| 2 | **Requires Trained Staff** | Accounting + Software skills needed |
| 3 | **System Failure Risk** | Hardware crash, software bugs, power failure |
| 4 | **Virus/Hacking Threat** | Cybersecurity risks, data theft |
| 5 | **Dependence on Electricity** | Cannot work without power/UPS |
| 6 | **Software Upgradation Cost** | Annual maintenance (AMC), version upgrades |
| 7 | **Data Corruption Risk** | File corruption, database issues |
| 8 | **Lack of Judgement** | Software processes, doesn't think (needs human oversight) |

---

## 18.5 CONSIDERATIONS FOR CHOOSING ACCOUNTING SOFTWARE

| Factor | What to Evaluate |
|--------|------------------|
| **1. Business Size & Complexity** | Small/medium/large, transaction volume |
| **2. Features Required** | Inventory, Payroll, GST, Multi-currency, Project costing |
| **3. User-friendliness** | Easy to learn, intuitive interface |
| **4. Vendor Support & Training** | Helpdesk, training, documentation |
| **5. Scalability** | Grows with business |
| **6. Cost** | License fee + AMC + Implementation + Training |
| **7. Integration** | With other systems (banking, CRM, e-commerce) |
| **8. Statutory Compliance** | GST, TDS, Companies Act, Ind AS |
| **9. Data Export/Import** | Compatibility with other software |
| **10. Cloud vs On-premise** | Accessibility, backup, cost model |

---

## 18.6 ACCOUNTING SOFTWARE IN INDIA

| Software | Features |
|----------|----------|
| **Tally ERP 9 / TallyPrime** | Most popular, GST compliant, inventory, payroll |
| **Marg ERP** | Strong in pharma, distribution, GST |
| **Busy Accounting** | SME focused, GST, inventory |
| **ProfitBooks** | Cloud-based, simple |
| **Zoho Books** | Cloud, integration with Zoho suite |
| **QuickBooks** | Global, cloud, Indian GST version |
| **SAP Business One** | Enterprise, ERP |
| **Oracle NetSuite** | Cloud ERP for large enterprises |

---

## 18.7 INTRODUCTION TO TALLY ERP 9

### **About Tally:**
- **Most widely used** accounting software in India
- **ERP** = Enterprise Resource Planning
- **Versions:** Tally ERP 9, TallyPrime (latest)
- **Features:** Accounting, Inventory, Payroll, GST, TDS, Banking

### **How to Start Tally:**
1. Double-click Tally icon
2. Gateway of Tally screen appears
3. Select Company or Create Company

### **Components of Tally Gateway:**
```
Gateway of Tally
├── Masters
│   ├── Accounts Info (Ledgers, Groups)
│   └── Inventory Info (Stock Items, Groups, Categories, Units, Godowns)
├── Transactions
│   ├── Accounting Vouchers (F4-F9, Ctrl+F8/F9)
│   ├── Inventory Vouchers (Alt+F4-F9)
│   └── Payroll Vouchers (Ctrl+F4)
├── Reports
│   ├── Balance Sheet
│   ├── Profit & Loss
│   ├── Stock Summary
│   ├── Trial Balance
│   ├── Day Book
│   ├── Ratio Analysis
│   └── GST Reports (GSTR-1, GSTR-3B)
├── Display
│   ├── Account Books
│   ├── Statements of Inventory
│   └── Exception Reports
└── Configuration (F12)
    ├── Accounting
    ├── Inventory
    └── Printing
```

---

## 18.8 CREATION OF A COMPANY 🔴 HIGH PRIORITY

### **Steps to Create Company:**

1. **Gateway of Tally** → **Create Company** (Alt+F3 → Create Company)
2. **Fill Company Details:**
   - **Name:** Company name
   - **Mailing Address:** Address for correspondence
   - **State:** For GST state code
   - **Pin Code**
   - **Telephone/Email**
   - **Currency Symbol:** ₹ (default)
   - **Maintain:** Accounts Only / Accounts with Inventory
   - **Financial Year From:** 1-Apr-20XX
   - **Books Beginning From:** 1-Apr-20XX
   - **TallyVault Password:** (Optional - encrypts data)
   - **Use Security Control:** Yes/No (User roles)
   - **Base Currency Information:** Symbol, Formal Name, Decimal Places

3. **Accept** (Enter) → Company created

### **Company Operations:**

| Operation | Path |
|-----------|------|
| **Select Company** | Gateway → Select Company (F1) |
| **Shut Company** | Gateway → Shut Company (Alt+F1) |
| **Alter Company** | Gateway → Alter (Alt+F3 → Alter) |
| **Delete Company** | Gateway → Delete Company (Alt+F3 → Delete) - **Irreversible!** |
| **Shut Tally** | Gateway → Quit (Ctrl+Q) |

### **Security Features:**
- **TallyVault:** Encrypts data (password required to open)
- **Security Control:** User roles (Admin, Data Entry, Auditor) with permissions

---

## 18.9 FEATURES AND CONFIGURATIONS (F11, F12)

### **F11 - Features (Company-level):**

| Feature Category | Key Options |
|------------------|-------------|
| **Accounting Features** | Integrate Accounts/Inventory, Cost Centres, Budgets, Interest Calculation, Multi-currency |
| **Inventory Features** | Stock Categories, Multiple Godowns, Batch-wise, Expiry Dates, Order Processing, Invoicing |
| **Statutory & Taxation** | GST (Enable, Set rates), TDS, TCS, Payroll Statutory |

### **F12 - Configuration (System-level):**
- **General:** Number format, Date format, Language
- **Accounts:** Master creation, Voucher entry, Printing
- **Inventory:** Stock summary, Ageing, Movement analysis
- **Printing:** Report printing options

---

## 18.10 KEYBOARD CONVENTIONS (TALLY SHORTCUTS)

| Key | Function |
|-----|----------|
| **F1** | Select Company / Help |
| **F2** | Change Date |
| **F3** | Company Menu |
| **F4** | Contra Voucher |
| **F5** | Payment Voucher |
| **F6** | Receipt Voucher |
| **F7** | Journal Voucher |
| **F8** | Sales Voucher |
| **F9** | Purchase Voucher |
| **Ctrl+F4** | Payroll Voucher |
| **Ctrl+F7** | Optional Voucher |
| **Ctrl+F8** | Credit Note |
| **Ctrl+F9** | Debit Note |
| **Ctrl+F10** | Memo Voucher |
| **Alt+F1** | Shut Company |
| **Alt+F3** | Company Menu (Create/Alter/Delete) |
| **Alt+F4** | Receipt Note (Inventory) |
| **Alt+F5** | Order Voucher |
| **Alt+F7** | Stock Journal |
| **Alt+F9** | Delivery Note |
| **Alt+F10** | Physical Stock Voucher |
| **Ctrl+Q** | Quit Tally |
| **Enter** | Accept/Save |
| **Esc** | Cancel/Go Back |

---

## 18.11 IMPORTANT EXAM QUESTIONS (From PYQ Analysis)

### **2 Marks Questions:**
1. What is Computerised Accounting System?
2. Name two advantages of Computerised Accounting.
3. Name two disadvantages of Computerised Accounting.
4. What is Tally ERP 9?
5. What is TallyVault?
6. What is Security Control in Tally?
7. Name four accounting software in India.
8. What is the shortcut for Contra Voucher in Tally?

### **5 Marks Questions:**
1. Distinguish between Manual and Computerised Accounting.
2. Explain the advantages of Computerised Accounting.
3. Explain the disadvantages of Computerised Accounting.
4. State the considerations for choosing Accounting Software.
5. Explain the procedure for Creating a Company in Tally.
6. Explain the Features (F11) in Tally.

### **10 Marks Questions:**
1. **What is meant by Computerised Accounting? Explain its merits and demerits. State the considerations to be kept in mind while choosing an Accounting Software.** (Dec 2021, Dec 2022, Dec 2023, June 2023, Dec 2024, June 2024, Dec 2025, June 2025, June 2026 - 2+6+6+6 / 10+10 marks)
2. **Difference between Manual and Computerised Accounting Systems.** (June 2025, June 2026 - 10 marks)
3. **Computerised Accounting system and Manual Accounting Systems.** (June 2025 - 10 marks)

---

## 18.12 KEY POINTS FOR REVISION

- ✅ **Computerised Accounting** = Software-based accounting (Tally, Marg, Busy, etc.)
- ✅ **Advantages (8):** Speed, Auto-reports, Security, Less paper, Retrieval, Multi-user, GST, Analysis
- ✅ **Disadvantages (8):** High cost, Trained staff, System failure, Virus, Electricity, Upgrade cost, Corruption, No judgement
- ✅ **Considerations (8):** Size, Features, User-friendly, Support, Scalability, Cost, Integration, Compliance
- ✅ **Tally ERP 9** = Most popular Indian accounting software
- ✅ **Company Creation:** Alt+F3 → Create → Fill details → Accept
- ✅ **Company Operations:** Select (F1), Shut (Alt+F1), Alter (Alt+F3), Delete (Alt+F3)
- ✅ **Features (F11):** Accounting, Inventory, Statutory
- ✅ **Configuration (F12):** System settings
- ✅ **Key Shortcuts:** F4-F9 (Vouchers), Ctrl+F8/F9 (Credit/Debit Note), Alt+F1 (Shut)

---

## 18.13 MEMORY AIDS

### **Advantages: "SAD BE MARG"**
- **S**peed & Accuracy
- **A**uto Reports
- **D**ata Security
- **B**ackup Easy
- **E**asy Retrieval
- **M**ulti-user
- **A**nalysis (Ratio)
- **G**ST Compliance

### **Disadvantages: "HIGH COST VD"**
- **H**igh Initial Cost
- **I**ntensive Training
- **G** - System Failure
- **H**acking/Virus
- **C**ost of Upgrades
- **O** - Electricity Dependent
- **S** - Data Corruption
- **T** - No Judgement
- **V** - Vendor Lock-in
- **D** - Data Loss Risk

---

*End of Unit 18 Notes*