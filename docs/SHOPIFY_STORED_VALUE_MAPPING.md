# Shopify Shop Dollars - MSB Call Report Field Mapping

**Date**: January 21, 2026  
**Product**: Shop Dollars (Stored Value/Prepaid Access)  
**Purpose**: Complete field mapping for MSB Call Report XML generation  
**Status**: Ready for Implementation  

---

## 📝 **Executive Summary**

Shopify's Shop Dollars program is classified as **Stored Value / Prepaid Access** under MSB regulations:
- Users **purchase** Shop dollars
- Funds are **stored** in Shop dollars accounts  
- Shop dollars are **redeemed** on future purchases

This document maps every MSB Call Report field required for reporting Shop Dollars activity.

---

## 🎯 **Required XML Fields for Shopify**

### **Section I: Financial Condition (`<Msbcrfc>`)**

These fields come from **NetSuite** and represent the balance sheet and income statement at quarter-end.

#### **A. Assets Section**

| Field Code | Field Description | Shopify Data Source | Notes |
|------------|------------------|-------------------|-------|
| **FC10** | Cash on Hand and in Bank | NetSuite: Cash accounts | Bank balances |
| **FC20** | Due from agents (net of allowance) | NetSuite: Receivables | If applicable |
| **FC30** | Amount of allowance for doubtful accounts | NetSuite: Allowance | If applicable |
| **FC40** | Accounts receivable (net) | NetSuite: AR | General receivables |
| **FC50** | Amount of allowance for doubtful accounts | NetSuite: Allowance | For AR |
| **FC60** | Inter-company receivables | NetSuite: IC Receivables | Between Shopify entities |
| **FC70** | Notes/other receivables | NetSuite: Other Receivables | Miscellaneous |
| **FC80** | Investments (including government securities) | NetSuite: Investment accounts | Where Shop $ funds invested |
| **FC90** | Virtual currency (in U.S. dollars) | N/A | Not applicable - no crypto |
| **FC100** | Other current assets | NetSuite: Other Current Assets | Miscellaneous |
| FC100NOTE | Explanatory Note | Manual | If needed |
| **FC120** | Premises, furniture, fixtures and equipment (net) | NetSuite: PP&E | Fixed assets |
| **FC130** | Investments in subsidiaries not consolidated | NetSuite: Investment in Subs | If applicable |
| **FC140** | Goodwill and other intangibles | NetSuite: Intangibles | Goodwill |
| **FC150** | Other assets | NetSuite: Other Assets | Long-term assets |
| FC150NOTE | Explanatory Note | Manual | If needed |

#### **B. Liabilities and Equity Section**

| Field Code | Field Description | Shopify Data Source | Notes |
|------------|------------------|-------------------|-------|
| **FC170** | Accounts payable | NetSuite: AP | Trade payables |
| **FC180** | Inter-company payables | NetSuite: IC Payables | Between Shopify entities |
| **FC190** | Notes/other payables | NetSuite: Other Payables | Other obligations |
| **FC200** | Outstanding money received for transmission liability | N/A | Not applicable - not doing money transmission |
| **FC210** | Outstanding payment instruments | N/A | Not applicable - not issuing money orders |
| **🔴 FC220** | **Outstanding stored value** | **NetSuite: Shop Dollars Liability** | **⭐ CRITICAL - Total Shop $ balance owed to customers** |
| **FC230** | Outstanding virtual currency liability | N/A | Not applicable - no crypto |
| **FC240** | Other current liabilities | NetSuite: Other Current Liab | Accrued expenses, etc. |
| FC240NOTE | Explanatory Note | Manual | If needed |
| **FC260** | Long term notes payable | NetSuite: LT Debt | Long-term debt |
| **FC270** | Other Liabilities | NetSuite: Other Liab | Other long-term |
| FC270NOTE | Explanatory Note | Manual | If needed |
| **FC290** | Preferred stock | NetSuite: Preferred Stock | If applicable |
| **FC300** | Number of preferred shares outstanding | NetSuite: Share count | Actual number |
| **FC310** | Common stock | NetSuite: Common Stock | Par value |
| **FC320** | Number of common shares authorized | NetSuite: Share count | Actual number |
| **FC330** | Number of common shares outstanding | NetSuite: Share count | Actual number |
| **FC340** | Paid-in-capital in excess of par | NetSuite: APIC | Additional paid-in capital |
| **FC360** | Retained earnings | NetSuite: Retained Earnings | Cumulative earnings |
| **FC370** | Other comprehensive income | NetSuite: OCI | Unrealized gains/losses |
| **FC380** | Shareholder distribution | NetSuite: Distributions | Dividends paid |

#### **C. Income Statement Section**

| Field Code | Field Description | Shopify Data Source | Notes |
|------------|------------------|-------------------|-------|
| **FC410** | Fee income from money received for transmission | N/A | Not applicable |
| **FC420** | Fee income from sale issuance of payments instruments | N/A | Not applicable |
| **🔴 FC430** | **Fee income from sale issuance of stored value** | **NetSuite: Shop Dollars Revenue** | **⭐ CRITICAL - Revenue/fees from Shop $** |
| **FC440** | Fee income from check cashing services | N/A | Not applicable |
| **FC450** | Fee income from currency exchange services | N/A | Not applicable |
| **FC460** | Interest and dividends | NetSuite: Interest Income | Investment income |
| **FC470** | Foreign exchange gains or losses | NetSuite: FX Gain/Loss | Currency fluctuations |
| **FC480** | Other income | NetSuite: Other Income | Miscellaneous |
| FC480NOTE | Explanatory Note | Manual | If needed |
| **FC500** | Salaries and employee benefits | NetSuite: Payroll | Personnel costs |
| **FC510** | Agent fees | NetSuite: Agent Fees | If using agents |
| **FC520** | Rent | NetSuite: Rent Expense | Facility costs |
| **FC530** | Interest expense | NetSuite: Interest Expense | Debt interest |
| **FC540** | Depreciation and amortization | NetSuite: D&A | Asset depreciation |
| **FC550** | Communication expense | NetSuite: Communications | Phone, internet |
| **FC560** | Professional services expense | NetSuite: Prof Services | Legal, audit, consulting |
| **FC570** | Marketing and promotion | NetSuite: Marketing | Advertising |
| **FC580** | Insurance expense | NetSuite: Insurance | Coverage costs |
| **FC590** | Other expenses | NetSuite: Other Expenses | Miscellaneous |
| FC590NOTE | Explanatory Note | Manual | If needed |
| **FC620** | Income tax | NetSuite: Tax Expense | Income taxes |
| **FC640** | Discontinued operations, Net of tax effect | NetSuite: Discontinued Ops | If applicable |
| **FC650** | Other comprehensive income/currency translation | NetSuite: Translation Adj | Currency translation |
| **FC670** | Extraordinary items, net of tax effect | NetSuite: Extraordinary | If applicable |

---

### **Section II(a): Company-Wide Transactions (`<Msbcrta>`)**

These fields come from **Shopify Data Warehouse** and represent transaction activity for the **entire quarter**.

#### **Stored Value Transactions (Shop Dollars)**

| Field Code | Field Description | Shopify Data Source | Notes |
|------------|------------------|-------------------|-------|
| **🔴 TA90** | **Total # of stored value transactions** | **BigQuery: COUNT of Shop $ purchases** | **⭐ CRITICAL - Number of times users bought Shop $** |
| **🔴 TA100** | **Total $ amount of stored value transactions** | **BigQuery: SUM of Shop $ purchases** | **⭐ CRITICAL - Total $ amount of Shop $ sold** |

#### **Fields NOT Applicable to Shopify**

| Field Code | Field Description | Applicable? |
|------------|------------------|-------------|
| TA10-TA60 | Money Transmission | ❌ No - Not doing money transmission |
| TA70-TA80 | Payment Instruments (money orders, etc.) | ❌ No - Not issuing payment instruments |
| TA110-TA140 | Check Cashing | ❌ No - Not cashing checks |
| TA150-TA170 | FIAT Currency Exchange | ❌ No - Not exchanging currency |
| TA180-TA350 | Virtual Currency | ❌ No - Not dealing with crypto |

---

### **Section II(b): State-Specific Transactions (`<Msbcrst>`)**

These fields come from **Shopify Data Warehouse** with **state-level filtering** and represent transaction activity for the **entire quarter** in **each licensed state**.

#### **Stored Value Transactions by State**

**IMPORTANT**: Create **one `<Msbcrst>` section per state** where Shopify holds an MSB license.

| Field Code | Field Description | Shopify Data Source | Notes |
|------------|------------------|-------------------|-------|
| **stateCode** | Two-letter state code (attribute) | Manual/Config | e.g., "CA", "NY", "TX" |
| **🔴 ST90** | **# of stored value transactions in-state** | **BigQuery: COUNT filtered by user state** | **⭐ CRITICAL - Number of Shop $ purchases in this state** |
| **🔴 ST100** | **$ amount of stored value transactions in-state** | **BigQuery: SUM filtered by user state** | **⭐ CRITICAL - Total $ Shop $ sold in this state** |

#### **Fields NOT Applicable to Shopify**

| Field Code | Field Description | Applicable? |
|------------|------------------|-------------|
| ST10-ST60 | Money Transmission | ❌ No |
| ST70-ST80 | Payment Instruments | ❌ No |
| ST110-ST140 | Check Cashing | ❌ No |
| ST150-ST170 | Currency Exchange | ❌ No |
| ST180-ST350 | Virtual Currency | ❌ No |
| ST360-ST361 | Additional state fields | ❌ No |

---

### **Section III: Permissible Investments (`<Msbcrpi>`)**

These fields come from **NetSuite** and represent where the Shop Dollars funds are invested/held.

| Field Code | Field Description | Shopify Data Source | Notes |
|------------|------------------|-------------------|-------|
| **🔴 PI10** | **Deposits in Domestic Banks** | **NetSuite: US Bank Accounts** | **⭐ PRIMARY - Where Shop $ funds held** |
| **PI20** | Deposits in All Foreign Banks | NetSuite: Foreign Banks | If funds held overseas |
| **PI21** | Deposits in Stipulated Foreign Banks | NetSuite: Specific Foreign Banks | Subset of PI20 |
| **PI30** | Cash on Hand and in Transit | NetSuite: Cash in Transit | Funds in transit |
| **PI31** | Debit card and Credit card-Funded Transmissions | N/A | Not applicable |
| **PI32** | Money market mutual funds rated AAA | NetSuite: Money Market Funds | If invested in MMFs |
| **PI50** | Irrevocable Letter of Credit | NetSuite: LOC | If have LOC for surety |
| **PI60** | Due from agents (net of allowance) | NetSuite: Agent Receivables | If using agents |
| **PI61** | Due from authorized delegates (< 7 days old) | NetSuite: Delegate Receivables | If using delegates |
| **PI62** | Due from delegates > 10% of outstanding liability | NetSuite: Delegate Receivables | Specific calculation |
| **PI70** | Investments rated A or equivalent and above | NetSuite: Investment Grade Securities | High-quality investments |
| **PI71** | Short-term investments | NetSuite: Short-term Securities | < 1 year maturity |
| **PI72** | Commercial paper | NetSuite: Commercial Paper | If invested in CP |
| **PI73** | U.S. tri-party repurchase agreements | NetSuite: Repo Agreements | If using repos |
| **PI74** | Money market mutual funds rated AAA to A- | NetSuite: MMFs | Mid-grade MMFs |
| **PI75** | Mutual funds | NetSuite: Mutual Fund Investments | General mutual funds |
| **PI76** | Bills, notes, bonds, or debentures | NetSuite: Fixed Income | Debt securities |
| **PI80** | Investments rated BBB or lower | NetSuite: Lower-Grade Securities | Lower quality (risky) |
| **PI90** | U.S. Treasury and Agency Securities | NetSuite: Treasuries | Government securities |
| **PI100** | Other Investments | NetSuite: Other Investments | Miscellaneous |
| PI100NOTE | Explanatory Note | Manual | Describe other investments |
| **PI110** | Amount pledged or restricted | NetSuite: Restricted Cash | Pledged/restricted funds |
| **🔴 PI120** | **Total Outstanding Transmission Liability** | **N/A or Zero** | **May not apply - confirm with counsel** |
| **🔴 PI130** | **Total Average Daily Outstanding Transmission Liability** | **N/A or Zero** | **May not apply - confirm with counsel** |
| **PI140-PI180** | Virtual Currency fields | N/A | Not applicable - no crypto |

**⚠️ IMPORTANT QUESTION**: Does "stored value" fall under "transmission liability" for PI120/PI130?  
**ACTION REQUIRED**: Confirm with legal/compliance whether Shop Dollars should be reported in PI120/PI130.

---

### **Section IV(a): Destination Country Detail - Company (`<Msbcrtda>`)**

**APPLICABILITY**: Only required if Shop Dollars can be used for **cross-border/international transactions**.

**QUESTION**: Can Shop Dollars be used to pay international merchants?
- If **YES**: Report each destination country
- If **NO**: **Omit this entire section**

If applicable:

| Field Code | Field Description | Shopify Data Source | Notes |
|------------|------------------|-------------------|-------|
| **TDA** | Country code (ISO) | BigQuery: Merchant country | e.g., "CA", "GB", "DE" |
| **TDA_1** | $ amount of transactions to this country | BigQuery: SUM(amount) by country | Shop $ spent in this country |
| **TDA_2** | # of transactions to this country | BigQuery: COUNT by country | Number of redemptions |

**ACTION REQUIRED**: Confirm with product team if Shop Dollars can be used internationally.

---

### **Section IV(b): Destination Country Detail - State (`<Msbcrtdb>`)**

**APPLICABILITY**: Same as Section IV(a) but broken down by **customer's state**.

Create **one `<Msbcrtdb>` section per licensed state** if international transactions occur.

| Field Code | Field Description | Shopify Data Source | Notes |
|------------|------------------|-------------------|-------|
| **stateCode** | Two-letter state code (attribute) | Manual/Config | Customer's state |
| **TDB** | Country code (ISO) | BigQuery: Merchant country | Destination country |
| **TDB_1** | $ amount to this country from this state | BigQuery: SUM(amount) by state + country | Filtered by customer state |
| **TDB_2** | # of transactions to this country from state | BigQuery: COUNT by state + country | Filtered by customer state |

**ACTION REQUIRED**: Confirm if this section is needed based on Section IV(a) applicability.

---

## 🗂️ **Data Source Summary**

### **1. NetSuite (Financial Condition & Permissible Investments)**

**Sections**: I (FC fields) and III (PI fields)

**Data Type**: **Point-in-time balances** at quarter-end

**Extraction Method**: NetSuite MCP (now configured!)

**Key Accounts to Query**:
- **FC220**: Shop Dollars Liability account (outstanding balance owed to customers)
- **FC430**: Shop Dollars Revenue account (fee income for quarter)
- **PI10**: Bank account balances where Shop Dollars funds held
- All other balance sheet accounts (FC10-FC380)
- All other income statement accounts (FC410-FC670)
- All investment accounts (PI fields)

### **2. BigQuery/Data Warehouse (Transaction Activity)**

**Sections**: II(a) (TA fields) and II(b) (ST fields)

**Data Type**: **Activity data** for the entire quarter (cumulative)

**Extraction Method**: SuiteQL or custom BigQuery queries

**Key Metrics to Calculate**:
- **TA90**: `COUNT(DISTINCT transaction_id) WHERE transaction_type = 'shop_dollars_purchase'`
- **TA100**: `SUM(amount) WHERE transaction_type = 'shop_dollars_purchase'`
- **ST90**: `COUNT(DISTINCT transaction_id) WHERE transaction_type = 'shop_dollars_purchase' AND user_state = '{STATE}'`
- **ST100**: `SUM(amount) WHERE transaction_type = 'shop_dollars_purchase' AND user_state = '{STATE}'`

**Required Transaction Data**:
- Transaction ID
- Transaction type (purchase of Shop dollars)
- Transaction amount (in USD)
- Transaction date (to filter by quarter)
- User state (for state-level reporting)
- Merchant country (if international redemptions tracked for Section IV)

---

## 📊 **Sample Data Structure Needed**

### **From NetSuite (for FC220 and FC430)**

```json
{
  "quarter_end_date": "2024-12-31",
  "outstanding_stored_value_liability": 5000000,  // FC220
  "stored_value_fee_income": 50000,              // FC430
  "cash_in_bank": 10000000,                      // FC10
  "investments": 3000000,                        // FC80
  // ... other balance sheet items
}
```

### **From BigQuery (for TA90, TA100, ST90, ST100)**

```sql
-- Company-wide (TA fields)
SELECT
  COUNT(*) as transaction_count,           -- TA90
  SUM(amount_usd) as transaction_amount    -- TA100
FROM shop_dollars_transactions
WHERE transaction_type = 'purchase'
  AND transaction_date BETWEEN '2024-10-01' AND '2024-12-31'

-- State-specific (ST fields) - run once per licensed state
SELECT
  user_state,
  COUNT(*) as transaction_count,           -- ST90
  SUM(amount_usd) as transaction_amount    -- ST100
FROM shop_dollars_transactions
WHERE transaction_type = 'purchase'
  AND transaction_date BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY user_state
```

---

## ✅ **Implementation Checklist**

### **Phase 1: Data Mapping** (Current)
- [x] Identify all required XML fields
- [x] Map fields to Shopify data sources
- [x] Understand stored value field definitions
- [ ] Confirm state licensing list
- [ ] Confirm international transaction applicability

### **Phase 2: NetSuite Integration**
- [ ] Identify NetSuite account numbers for:
  - [ ] FC220 - Shop Dollars Liability
  - [ ] FC430 - Shop Dollars Revenue
  - [ ] PI10 - Bank accounts holding Shop Dollars funds
  - [ ] All other FC fields (assets, liabilities, equity, income, expenses)
  - [ ] All other PI fields (investments)
- [ ] Test NetSuite MCP queries for quarter-end balances
- [ ] Create NetSuite extraction script

### **Phase 3: BigQuery Integration**
- [ ] Identify Shop Dollars transaction table(s)
- [ ] Confirm transaction_type values for purchases
- [ ] Confirm user_state field availability
- [ ] Create BigQuery queries for TA90, TA100, ST90, ST100
- [ ] Test queries for Q4 2024 data

### **Phase 4: XML Generator Updates**
- [ ] Update generator to match exact XSD schema
- [ ] Implement NetSuite data extraction
- [ ] Implement BigQuery data extraction
- [ ] Handle multiple state sections (`<Msbcrst>`)
- [ ] Implement data validation (Dollar, PositiveDollar, Count types)
- [ ] Add explanatory notes capability
- [ ] Test with sample data

### **Phase 5: Validation & Testing**
- [ ] Generate sample XML with test data
- [ ] Validate against XSD schema
- [ ] Review with compliance/legal team
- [ ] Test submission to NMLS (if test environment available)

### **Phase 6: Production**
- [ ] Generate Q1 2025 report (due May 15, 2025)
- [ ] Review and approve before submission
- [ ] Submit to NMLS
- [ ] Archive report and supporting documentation

---

## 🚨 **Critical Questions to Resolve**

### **1. State Licensing** ⚠️ URGENT
**Question**: In which states does Shopify hold MSB licenses for stored value?

**Why it matters**: We need one `<Msbcrst>` section per licensed state.

**Action**: Get list from Legal/Compliance

### **2. International Transactions** ⚠️ IMPORTANT
**Question**: Can Shop Dollars be used for international purchases (cross-border)?

**Why it matters**: Determines if we need Sections IV(a) and IV(b).

**Action**: Confirm with Product team

### **3. Permissible Investments Classification** ⚠️ IMPORTANT
**Question**: Are "stored value" funds subject to the same permissible investment requirements as "money transmission"?

**Specifically**: Should we report FC220 (outstanding stored value) in PI120/PI130 (transmission liability)?

**Why it matters**: Impacts Section III reporting and regulatory compliance.

**Action**: Confirm with Legal/Compliance

### **4. NetSuite Account Mapping** ⚠️ URGENT
**Question**: What are the specific NetSuite account numbers for:
- Shop Dollars Liability (FC220)
- Shop Dollars Revenue (FC430)
- Bank accounts holding Shop Dollars funds (PI10)

**Why it matters**: Required for automated data extraction.

**Action**: Work with Finance/Accounting team to identify accounts

---

## 🎯 **Next Steps**

### **Immediate (This Week)**
1. ✅ Complete field mapping - **DONE!**
2. ⏳ Get answers to critical questions above
3. ⏳ Identify NetSuite account numbers
4. ⏳ Test NetSuite MCP for balance extraction

### **Short Term (Next 2 Weeks)**
1. Build NetSuite extraction queries
2. Build BigQuery transaction queries
3. Update XML generator with correct schema
4. Test with sample data

### **Medium Term (Next Month)**
1. Full end-to-end test with Q4 2024 data
2. Review with compliance/legal
3. Document process for quarterly reporting
4. Prepare for Q1 2025 reporting (due May 15)

---

## 📄 **XML Structure for Shopify**

### **Minimal Required Structure**

```xml
<MsbcrFiling year="2024" formVersion="v4" periodType="MSBQ4">
  
  <!-- Section I: Financial Condition -->
  <Msbcrfc>
    <Assets>
      <FC10>1000000</FC10>         <!-- Cash in bank -->
      <FC80>500000</FC80>          <!-- Investments -->
      <!-- ... other asset fields ... -->
    </Assets>
    <LiabilitiesAndEquity>
      <FC170>100000</FC170>        <!-- Accounts payable -->
      <FC220>5000000</FC220>       <!-- ⭐ SHOP DOLLARS LIABILITY -->
      <!-- ... other liability fields ... -->
      <FC360>2000000</FC360>       <!-- Retained earnings -->
    </LiabilitiesAndEquity>
    <IncomeStatement>
      <FC430>50000</FC430>         <!-- ⭐ SHOP DOLLARS REVENUE -->
      <FC500>200000</FC500>        <!-- Salaries -->
      <!-- ... other income/expense fields ... -->
    </IncomeStatement>
  </Msbcrfc>
  
  <!-- Section II(a): Company-Wide Transactions -->
  <Msbcrta>
    <TransactionsCompanyWideSection>
      <TA90>10000</TA90>           <!-- ⭐ # OF SHOP $ PURCHASES -->
      <TA100>5000000</TA100>       <!-- ⭐ $ OF SHOP $ PURCHASES -->
    </TransactionsCompanyWideSection>
  </Msbcrta>
  
  <!-- Section II(b): State Transactions - Repeat per licensed state -->
  <Msbcrst stateCode="CA">
    <TransactionsStateSpecificSection>
      <ST90>3000</ST90>            <!-- ⭐ # OF SHOP $ PURCHASES IN CA -->
      <ST100>1500000</ST100>       <!-- ⭐ $ OF SHOP $ PURCHASES IN CA -->
    </TransactionsStateSpecificSection>
  </Msbcrst>
  
  <Msbcrst stateCode="NY">
    <TransactionsStateSpecificSection>
      <ST90>2000</ST90>            <!-- ⭐ # OF SHOP $ PURCHASES IN NY -->
      <ST100>1000000</ST100>       <!-- ⭐ $ OF SHOP $ PURCHASES IN NY -->
    </TransactionsStateSpecificSection>
  </Msbcrst>
  
  <!-- ... More <Msbcrst> sections for each licensed state ... -->
  
  <!-- Section III: Permissible Investments -->
  <Msbcrpi>
    <PermissibleInvestmentsSection>
      <PI10>8000000</PI10>         <!-- ⭐ BANK DEPOSITS HOLDING SHOP $ FUNDS -->
      <PI90>2000000</PI90>         <!-- US Treasury securities -->
      <!-- ... other investment fields ... -->
    </PermissibleInvestmentsSection>
  </Msbcrpi>
  
  <!-- Section IV: Destination Country (only if international transactions) -->
  <!-- Omit if Shop Dollars only used domestically -->
  
</MsbcrFiling>
```

---

**Status**: ✅ **READY FOR IMPLEMENTATION** - All field mappings complete, awaiting critical business input!
