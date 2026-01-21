# Shopify Financial Services Inc. - Reference Data

**Last Updated**: January 21, 2026  
**Purpose**: Critical reference information for MSB Call Report generation  

---

## 🏢 **Legal Entity Information**

| Field | Value |
|-------|-------|
| **Legal Name** | Shopify Financial Services Inc. |
| **State of Incorporation** | Delaware |
| **Formation Date** | December 18, 2024 |
| **NMLS ID** | **2689562** |
| **FinCEN Registration** | ✓ Completed (BSA ID: TBD) |
| **NetSuite Subsidiary ID** | 87 |

---

## 🏦 **Corporate Structure**

```
Shopify Inc. (Canada)
  └── Shopify Holdings (USA) 2 Inc. (Delaware)
      └── Shopify Financial Services Inc. (Delaware)
          └── NMLS ID: 2689562
```

---

## 💼 **Business Activity**

| Field | Value |
|-------|-------|
| **Product** | Shop Pay Wallet Balance |
| **MSB Activity Type** | Stored Value / Prepaid Access |
| **Launch Status** | Pre-Operational (licenses being obtained) |
| **Target Geography** | 50 US States + DC + Puerto Rico |

---

## 📋 **Licensed States**

**Status**: 🔴 **PENDING** - Information needed from Legal/Compliance

| State | License Status | License Number | Notes |
|-------|---------------|----------------|-------|
| TBD | | | |

**ACTION REQUIRED**: Obtain list of states where MSB licenses have been obtained or applied for.

---

## 🏦 **NetSuite Account Mappings**

**Status**: 🔴 **PENDING** - Information needed from Finance/Accounting

### **Known Bank Accounts**
| Account # | Account Name | Purpose |
|-----------|-------------|---------|
| 11623 | CITI Shopify Financial Services CLE USD (0935) | Bank Account |
| 11624 | CITI Shopify Financial Services OPS USD (0839) | Bank Account |

### **Required Account Mappings for MSB Reporting**

#### **Section I: Financial Condition - Assets**
| XML Field | Description | NetSuite Account # | Status |
|-----------|-------------|-------------------|--------|
| FC10 | Cash on Hand and in Bank | TBD | 🔴 Needed |
| FC20 | Due from agents | TBD (if applicable) | 🟡 Optional |
| FC40 | Accounts receivable | TBD (if applicable) | 🟡 Optional |
| FC60 | Inter-company receivables | TBD (if applicable) | 🟡 Optional |
| FC80 | Investments | TBD (if applicable) | 🟡 Optional |
| FC120 | PP&E (net) | TBD (if applicable) | 🟡 Optional |
| FC140 | Goodwill and intangibles | TBD (if applicable) | 🟡 Optional |
| FC150 | Other assets | TBD (if applicable) | 🟡 Optional |

#### **Section I: Financial Condition - Liabilities**
| XML Field | Description | NetSuite Account # | Status |
|-----------|-------------|-------------------|--------|
| FC170 | Accounts payable | TBD | 🟡 Optional |
| FC180 | Inter-company payables | TBD (if applicable) | 🟡 Optional |
| **FC220** | **Outstanding stored value** | **TBD - FBO Account** | **🔴 CRITICAL** |
| FC240 | Other current liabilities | TBD (if applicable) | 🟡 Optional |
| FC260 | Long term debt | TBD (if applicable) | 🟡 Optional |

#### **Section I: Financial Condition - Equity**
| XML Field | Description | NetSuite Account # | Status |
|-----------|-------------|-------------------|--------|
| FC310 | Common stock | TBD | 🔴 Needed |
| FC340 | Paid-in capital | TBD | 🔴 Needed |
| FC360 | Retained earnings | TBD | 🟡 Optional |

#### **Section I: Financial Condition - Revenue**
| XML Field | Description | NetSuite Account # | Status |
|-----------|-------------|-------------------|--------|
| **FC430** | **Stored value fee income** | **TBD - Interest Income** | **🔴 CRITICAL** |
| FC460 | Interest and dividends | TBD (if applicable) | 🟡 Optional |
| FC480 | Other income | TBD (if applicable) | 🟡 Optional |

#### **Section I: Financial Condition - Expenses**
| XML Field | Description | NetSuite Account # | Status |
|-----------|-------------|-------------------|--------|
| FC500 | Salaries and benefits | TBD | 🟡 Optional |
| FC520 | Rent | TBD (if applicable) | 🟡 Optional |
| FC530 | Interest expense | TBD (if applicable) | 🟡 Optional |
| FC540 | Depreciation | TBD (if applicable) | 🟡 Optional |
| FC560 | Professional services | TBD | 🟡 Optional |
| FC580 | Insurance | TBD (if applicable) | 🟡 Optional |
| FC590 | Other expenses | TBD (if applicable) | 🟡 Optional |
| FC620 | Income tax | TBD (if applicable) | 🟡 Optional |

#### **Section III: Permissible Investments**
| XML Field | Description | NetSuite Account # | Status |
|-----------|-------------|-------------------|--------|
| PI10 | Deposits in domestic banks | TBD (same as FC10?) | 🔴 Needed |
| PI90 | US Treasury securities | TBD (if applicable) | 🟡 Optional |

---

## 📅 **Accounting Periods (NetSuite)**

| Period Name | Period ID | Start Date | End Date | Type |
|-------------|-----------|------------|----------|------|
| Q1 2025 | 344 | 2025-01-01 | 2025-03-31 | Quarter |
| FY 2025 | 343 | 2025-01-01 | 2025-12-31 | Year |
| Jan 2025 | 345 | 2025-01-01 | 2025-01-31 | Month |
| Dec 2024 | 342 | 2024-12-01 | 2024-12-31 | Month |
| Q4 2024 | 339 | 2024-10-01 | 2024-12-31 | Quarter |

---

## 💾 **BigQuery Data Sources**

**Status**: 🟡 **NOT URGENT** (no transactions yet, but will be needed when operations launch)

### **Shop Pay Wallet Balance Transactions**
| Field | BigQuery Table/Column | Status |
|-------|----------------------|--------|
| Transaction ID | TBD | 🟡 Pending |
| Transaction Type | TBD (FUNDING vs REDEMPTION) | 🟡 Pending |
| Transaction Amount | TBD | 🟡 Pending |
| Transaction Date | TBD | 🟡 Pending |
| Shopper State | TBD | 🟡 Pending |
| Shopper Country | TBD | 🟡 Pending |

**ACTION REQUIRED**: Identify BigQuery tables/columns when Shop Pay Wallet Balance launches

---

## 📊 **MSB Reporting Schedule**

| Quarter | Period End | Due Date | First Report? |
|---------|-----------|----------|---------------|
| **Q1 2025** | March 31, 2025 | **May 15, 2025** | ✓ YES (Pre-operational) |
| Q2 2025 | June 30, 2025 | August 15, 2025 | (May have transactions) |
| Q3 2025 | September 30, 2025 | November 17, 2025 | |
| Q4 2025 | December 31, 2025 | February 16, 2026 | (Annual report with Section IV) |

---

## ✅ **Information Status**

| Item | Status | Source | Date Received |
|------|--------|--------|---------------|
| Legal Name | ✅ Complete | Business Plan | Jan 21, 2026 |
| Formation Date | ✅ Complete | Business Plan | Jan 21, 2026 |
| **NMLS ID** | **✅ Complete** | **Phil** | **Jan 21, 2026** |
| FinCEN BSA ID | 🔴 Pending | Legal/Compliance | - |
| NetSuite Subsidiary ID | ✅ Complete | NetSuite MCP | Jan 21, 2026 |
| Licensed States List | 🔴 Pending | Legal/Compliance | - |
| NetSuite Account Mappings | 🔴 Pending | Finance/Accounting | - |
| BigQuery Table Info | 🟡 Not Urgent | Data Engineering | - |

---

## 🚨 **Critical Next Steps**

1. **Get Licensed States List** from Legal/Compliance
2. **Map NetSuite Accounts** with Finance/Accounting (focus on cash, equity, FBO account when operational)
3. Get FinCEN BSA ID from Legal/Compliance (if different from NMLS ID)

---

## 📞 **Contact Information**

| Team | Contact Person | Purpose |
|------|---------------|---------|
| Legal/Compliance | TBD | Licensed states, regulatory IDs |
| Finance/Accounting | TBD | NetSuite account mappings |
| Product | TBD | Launch timeline, feature scope |
| Data Engineering | TBD | BigQuery tables (when operational) |

---

**Document Owner**: Phil Whitham  
**Last Review**: January 21, 2026  
**Next Review**: When licensed states list received
