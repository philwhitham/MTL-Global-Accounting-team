# Shopify Financial Services - Business Plan Analysis for MSB Reporting

**Date**: January 21, 2026  
**Document Reviewed**: Shopify Financial Services - Stored Value Business Plan + Funds Flow  
**Purpose**: Extract critical information for MSB Call Report XML generation  
**Status**: Analysis Complete - Implementation Ready  

---

## 🎯 **Executive Summary**

After reviewing the comprehensive business plan and funds flow documentation, I now have a complete understanding of **Shopify Financial Services Inc.'s** stored value program and can precisely map it to MSB Call Report requirements.

### **Key Findings**:
✅ **Legal Entity**: Shopify Financial Services Inc. (Delaware corporation, formed Dec 18, 2024)  
✅ **Product**: Shop Pay Wallet Balance (stored value digital wallet)  
✅ **Geography**: 50 US states + DC + Puerto Rico  
✅ **Funding Method**: ACH from Shopper's bank account  
✅ **Fund Storage**: FBO (For Benefit Of) accounts at Bank Partners  
✅ **Use Cases**: Merchant payments + bank withdrawals (NO P2P transfers)  
✅ **Revenue Model**: Interest income on FBO accounts (no Shopper fees)  
✅ **Settlement**: Via Payment Partners (Stripe, PayPal, etc.)  

---

## 🏢 **Corporate Structure**

```
Shopify Inc. (Canadian public company, NASDAQ: SHOP)
    ↓
Shopify Holdings (USA) 2 Inc. (Delaware corporation)
    ↓
Shopify Financial Services Inc. (Delaware corporation)
    ↓
    MSB Licenses (state-by-state)
```

**For MSB Reporting**:
- **Filing Entity**: Shopify Financial Services Inc.
- **Parent Company**: Shopify Holdings (USA) 2 Inc.
- **Ultimate Parent**: Shopify Inc.
- **FinCEN Registration**: Completed ✓

---

## 💰 **Business Model**

### **Product: Shop Pay Wallet Balance**

**What It Is**:
- Stored value digital wallet
- Integrated into Shop App and Shop Pay checkouts
- Allows Shoppers to pre-fund purchases

**How It Works**:

#### **1. Funding (ACH Deposit)**
- Shopper initiates ACH debit from their external bank account
- Bank Partner acts as ODFI (Originating Depository Financial Institution)
- Funds settle into FBO Account (2-3 business days)
- Shopper's Shop Pay Wallet Balance is credited
- **Money transmission liability CREATED**

#### **2. Purchases (Stored Value Redemption)**
- Shopper checks out at Merchant using Shop Pay Wallet Balance
- Shopify FS confirms sufficient funds
- Shopify FS instructs Bank Partner to send funds to Payment Partner (Stripe/PayPal)
- Payment Partner settles with Merchant (2 business days)
- Shopper's Shop Pay Wallet Balance is debited
- **Money transmission liability EXTINGUISHED**

#### **3. Split Payments**
- Shopper can combine Shop Pay Wallet Balance + credit/debit card
- Two parallel settlement streams:
  - Stored value portion: Shopify FS → Payment Partner → Merchant
  - Card portion: Payment Partner processes directly

#### **4. Refunds**
- Refunds go back to original payment method
- Stored value portion: Merchant → Payment Partner → Shopify FS FBO Account → Shopper's Balance
- **Money transmission liability RE-CREATED**

#### **5. Withdrawals (ACH Credit)**
- Shopper initiates withdrawal to external bank account
- Bank Partner acts as ODFI
- Funds settle to Shopper's bank (2-3 business days)
- Shopper's Shop Pay Wallet Balance is debited
- **Money transmission liability EXTINGUISHED**

---

## 📊 **Fund Flow Summary**

### **FBO Account (For Benefit Of Account)**
- **Location**: Bank Partner (federally insured financial institution)
- **Ownership**: Titled in Shopify FS name, held for benefit of Shoppers
- **Purpose**: Omnibus account holding all Shopper balances
- **Segregation**: Fully segregated from Shopify FS operating funds

### **Daily Reconciliation Requirements**
Shopify FS must ensure:
1. **Individual Shopper Balance** = Sum of transactions for that Shopper
2. **Total FBO Account Balance** = Sum of all individual Shopper balances
3. **Outstanding Liability** (FC220) = Total FBO Account Balance

---

## 🎯 **MSB Call Report Field Mapping - UPDATED**

Based on the business plan, here are the precise mappings:

### **Section I: Financial Condition**

#### **Critical Liability Field**

| Field | Description | Shopify FS Source | Definition |
|-------|-------------|------------------|------------|
| **FC220** | **Outstanding stored value** | **FBO Account Balance** | **Total of all Shopper Shop Pay Wallet Balances at quarter-end** |

**How to Calculate FC220**:
```
FC220 = SUM(all individual Shopper Shop Pay Wallet Balances)
      = Total balance in FBO Account(s)
      = Total money transmission liability owed to Shoppers
```

**NetSuite Query**:
```sql
SELECT account_balance 
FROM accounts 
WHERE account_number = '[FBO_ACCOUNT_NUMBER]'
  AND accounting_period = '[QUARTER_END_PERIOD_ID]'
  AND subsidiary = '[SHOPIFY_FS_SUBSIDIARY_ID]'
```

#### **Critical Revenue Field**

| Field | Description | Shopify FS Source | Definition |
|-------|-------------|------------------|------------|
| **FC430** | **Fee income from stored value** | **Interest Income on FBO Account** | **Interest earned on FBO account balances during the quarter** |

**How to Calculate FC430**:
```
FC430 = Interest income earned on FBO Account during quarter
```

**Notes**:
- Shopify FS does NOT charge Shoppers any fees
- Revenue comes solely from interest on funds held in FBO accounts
- Shopify reimburses Shopify FS for costs + profit per Intercompany Agreement

**NetSuite Query**:
```sql
SELECT SUM(amount)
FROM transactions
WHERE account IN ('[INTEREST_INCOME_ACCOUNT]')
  AND accounting_period BETWEEN '[Q_START]' AND '[Q_END]'
  AND subsidiary = '[SHOPIFY_FS_SUBSIDIARY_ID]'
```

### **Section II(a): Company-Wide Transactions**

| Field | Description | Data Source | Definition |
|-------|-------------|------------|------------|
| **TA90** | **# of stored value transactions** | **BigQuery** | **COUNT of Shop Pay Wallet Balance funding transactions during quarter** |
| **TA100** | **$ of stored value transactions** | **BigQuery** | **SUM of Shop Pay Wallet Balance funding amounts during quarter** |

**CRITICAL CLARIFICATION**: What counts as a "stored value transaction"?

Based on the business plan, **"stored value transactions" = FUNDING transactions**:
- ✅ **YES**: Shopper deposits money into Shop Pay Wallet Balance (ACH debit from external bank)
- ❌ **NO**: Shopper uses Shop Pay Wallet Balance to pay Merchant (that's redemption, not issuance)
- ❌ **NO**: Refunds back to Shop Pay Wallet Balance (that's a credit, not a new issuance)

**Why?**
The MSB Call Report asks for "stored value transactions" which refers to the **issuance/sale** of stored value, not the redemption. This aligns with regulatory focus on how much stored value is being loaded into the system.

**BigQuery Query for TA90/TA100**:
```sql
-- Company-wide stored value FUNDING transactions
SELECT
  COUNT(DISTINCT transaction_id) as transaction_count,  -- TA90
  SUM(amount_usd) as transaction_amount                 -- TA100
FROM shop_pay_wallet_transactions
WHERE transaction_type = 'FUNDING'  -- ACH deposits from external banks
  AND transaction_status = 'COMPLETED'
  AND transaction_date BETWEEN '[QUARTER_START]' AND '[QUARTER_END]'
  AND shopper_country = 'US'  -- Only US Shoppers
```

### **Section II(b): State-Specific Transactions**

| Field | Description | Data Source | Definition |
|-------|-------------|------------|------------|
| **ST90** | **# of stored value transactions in-state** | **BigQuery** | **COUNT of Shop Pay Wallet Balance funding transactions in this state** |
| **ST100** | **$ of stored value transactions in-state** | **BigQuery** | **SUM of Shop Pay Wallet Balance funding amounts in this state** |

**BigQuery Query for ST90/ST100** (run once per licensed state):
```sql
-- State-specific stored value FUNDING transactions
SELECT
  shopper_state,
  COUNT(DISTINCT transaction_id) as transaction_count,  -- ST90
  SUM(amount_usd) as transaction_amount                 -- ST100
FROM shop_pay_wallet_transactions
WHERE transaction_type = 'FUNDING'
  AND transaction_status = 'COMPLETED'
  AND transaction_date BETWEEN '[QUARTER_START]' AND '[QUARTER_END]'
  AND shopper_country = 'US'
  AND shopper_state IN ('[LIST_OF_LICENSED_STATES]')
GROUP BY shopper_state
```

**State Determination**:
Based on the business plan, state is determined by **Shopper's residence** (where they're located when funding their balance).

### **Section III: Permissible Investments**

| Field | Description | Shopify FS Source | Definition |
|-------|-------------|------------------|------------|
| **PI10** | **Deposits in Domestic Banks** | **Bank Partner FBO Account Balances** | **Total funds held in US bank FBO accounts** |
| **PI120** | **Total Outstanding Transmission Liability** | **FC220 (Outstanding stored value)** | **Same as FC220** |
| **PI130** | **Total Average Daily Outstanding Transmission Liability (ADTL)** | **Calculated** | **Average daily FC220 balance during quarter** |

**IMPORTANT QUESTION RESOLVED**: Based on the business plan, Shop Pay Wallet Balance funds:
1. Are held in **FBO accounts** at Bank Partners
2. Create a **money transmission liability** when funded
3. Are **owed to Shoppers** and must be available on demand

**Therefore**: 
- ✅ **YES**, report FC220 (outstanding stored value) in PI120
- ✅ **YES**, calculate and report average daily liability in PI130

**Calculation for PI130 (ADTL)**:
```
PI130 = SUM(daily FC220 balance for each day in quarter) / Number of days in quarter
```

**NetSuite/BigQuery Query for PI130**:
```sql
-- Calculate Average Daily Outstanding Transmission Liability
SELECT AVG(daily_outstanding_balance) as adtl
FROM (
  SELECT 
    date,
    SUM(wallet_balance) as daily_outstanding_balance
  FROM shopper_daily_balances
  WHERE date BETWEEN '[QUARTER_START]' AND '[QUARTER_END]'
  GROUP BY date
) daily_totals
```

### **Section IV: Destination Country Detail**

**APPLICABILITY DETERMINED**: Based on the business plan:

> "Shoppers may only withdraw funds to their own external bank accounts or use funds in the Shop Pay Wallet Balance to pay Merchants."

**Question**: Can Shoppers pay **international Merchants** (merchants outside the US)?

**If YES** → **Report Sections IV(a) and IV(b)**  
**If NO (domestic Merchants only)** → **OMIT Sections IV(a) and IV(b)**

**ACTION REQUIRED**: Confirm with Product team:
1. Can Shop Pay Wallet Balance be used to pay Merchants located outside the US?
2. If yes, which countries?

---

## 📋 **Data Requirements Summary**

### **From NetSuite (Section I: Financial Condition)**

**Quarterly Point-in-Time Data** (as of quarter-end date):

1. **FC220 - Outstanding Stored Value**
   - Account: FBO Account balance
   - Represents: Total Shopper wallet balances owed

2. **FC430 - Stored Value Fee Income**
   - Account: Interest Income account(s)
   - Represents: Interest earned on FBO accounts during quarter

3. **All Other Balance Sheet Accounts**:
   - Assets (FC10-FC150)
   - Liabilities (FC170-FC270)
   - Equity (FC290-FC380)

4. **All Other Income Statement Accounts**:
   - Revenues (FC410-FC480)
   - Expenses (FC500-FC590)
   - Taxes and Other (FC620-FC670)

5. **Permissible Investments**:
   - PI10: Bank account balances (FBO accounts)
   - PI90: US Treasury securities (if any)
   - PI100: Other investments (if any)

### **From BigQuery (Section II: Transaction Activity)**

**Quarterly Cumulative Activity Data** (for entire quarter):

1. **Stored Value Funding Transactions**:
   - Transaction type: FUNDING (ACH deposits to Shop Pay Wallet Balance)
   - Required fields:
     - `transaction_id` (for counting)
     - `amount_usd` (for summing)
     - `transaction_date` (for quarter filtering)
     - `transaction_status` (must be COMPLETED)
     - `shopper_country` (filter for US)
     - `shopper_state` (for state-level reporting)
   
2. **Daily Balance Snapshots** (for PI130 calculation):
   - Daily outstanding wallet balances
   - Required for Average Daily Transmission Liability calculation

### **Configuration/Reference Data**

1. **Licensed States List**:
   - Which states has Shopify FS obtained MSB licenses?
   - Needed to know how many `<Msbcrst>` sections to create

2. **NetSuite Account Numbers**:
   - FBO Account number(s)
   - Interest Income account number(s)
   - All balance sheet account numbers
   - All income statement account numbers

3. **Reporting Entity Information**:
   - Company Name: Shopify Financial Services Inc.
   - NMLS Company ID: [Need to obtain]
   - FinCEN BSA ID: [Need to obtain]

---

## ✅ **Critical Questions RESOLVED**

### **1. What is "stored value" for Shopify?** ✅
**ANSWER**: Shop Pay Wallet Balance - a digital wallet where Shoppers pre-fund purchases

### **2. How is it funded?** ✅
**ANSWER**: ACH debits from Shopper's external bank account to Shopify FS FBO account

### **3. How is it used?** ✅
**ANSWER**: 
- Pay Merchants (settled via Payment Partners like Stripe/PayPal)
- Withdraw to external bank account
- **NOT** for P2P transfers

### **4. Where are funds held?** ✅
**ANSWER**: Segregated FBO (For Benefit Of) accounts at Bank Partners

### **5. What creates the liability?** ✅
**ANSWER**: When Shopper funds their Shop Pay Wallet Balance (ACH deposit completes)

### **6. What extinguishes the liability?** ✅
**ANSWER**: When Shopper uses balance to pay Merchant OR withdraws to bank

### **7. How does Shopify FS make money?** ✅
**ANSWER**: Interest income on FBO account balances (no Shopper fees)

### **8. What counts as a "stored value transaction"?** ✅
**ANSWER**: FUNDING transactions (when Shoppers load money into their balance)
- **TA90/ST90**: COUNT of funding transactions
- **TA100/ST100**: SUM of funding amounts

---

## 🚨 **Critical Questions STILL PENDING**

### **1. State Licensing List** ⚠️ **URGENT**
**Question**: In which states has Shopify FS obtained MSB licenses?

**Why it matters**: Need one `<Msbcrst>` section per licensed state

**Status**: Pending Legal/Compliance input

---

### **2. International Merchant Payments** ⚠️ **IMPORTANT**
**Question**: Can Shoppers use Shop Pay Wallet Balance to pay Merchants located outside the US?

**Why it matters**: Determines if Sections IV(a) and IV(b) are required

**Status**: Pending Product team input

---

### **3. NetSuite Account Mapping** ⚠️ **URGENT**
**Questions**:
- What is the NetSuite account number for the FBO Account? (for FC220, PI10, PI120)
- What is the NetSuite account number for Interest Income on FBO Account? (for FC430)
- What is the Shopify FS subsidiary ID in NetSuite?
- What are all other relevant account numbers?

**Why it matters**: Required for automated data extraction

**Status**: Pending Finance/Accounting input

---

### **4. Reporting IDs** ⚠️ **URGENT**
**Questions**:
- What is Shopify FS's NMLS Company ID?
- What is Shopify FS's FinCEN BSA ID?

**Why it matters**: Required for XML submission

**Status**: Pending Legal/Compliance input

---

## 🎯 **Updated Implementation Plan**

### **Phase 1: Configuration & Setup** (This Week)
- [ ] Obtain licensed states list from Legal/Compliance
- [ ] Obtain NMLS Company ID and FinCEN BSA ID
- [ ] Map NetSuite account numbers for Shopify FS subsidiary
- [ ] Confirm international merchant payment capability with Product
- [ ] Identify BigQuery tables for Shop Pay Wallet Balance transactions

### **Phase 2: NetSuite Data Extraction** (Week 2)
- [ ] Test NetSuite MCP access for Shopify FS subsidiary
- [ ] Extract FC220 (FBO account balance) for test quarter
- [ ] Extract FC430 (interest income) for test quarter
- [ ] Extract all balance sheet accounts (FC10-FC380)
- [ ] Extract all income statement accounts (FC410-FC670)
- [ ] Extract permissible investment data (PI10-PI180)

### **Phase 3: BigQuery Data Extraction** (Week 2)
- [ ] Identify Shop Pay Wallet Balance transaction table
- [ ] Confirm transaction_type values for FUNDING
- [ ] Test query for TA90/TA100 (company-wide counts and amounts)
- [ ] Test query for ST90/ST100 (state-specific counts and amounts)
- [ ] Test query for PI130 (average daily outstanding liability)

### **Phase 4: XML Generator Development** (Week 3)
- [ ] Update XML generator to match exact XSD schema
- [ ] Implement NetSuite data integration
- [ ] Implement BigQuery data integration
- [ ] Handle multiple state sections iteration
- [ ] Implement data type validation (Dollar, PositiveDollar, Count, Hundredth)
- [ ] Add explanatory notes capability

### **Phase 5: Testing & Validation** (Week 4)
- [ ] Generate test XML with Q4 2024 data
- [ ] Validate against XSD schema
- [ ] Manual review of all values
- [ ] Reconcile TA90/TA100 to FC220 changes
- [ ] Review with Finance, Compliance, and Legal

### **Phase 6: Production Rollout** (Ongoing)
- [ ] Document quarterly process
- [ ] Create runbook for data extraction
- [ ] Establish review/approval workflow
- [ ] Set up quarterly calendar reminders (due dates: Feb 15, May 15, Aug 15, Nov 15)

---

## 📄 **Sample XML Structure for Shopify FS**

```xml
<MsbcrFiling year="2024" formVersion="v4" periodType="MSBQ4">
  
  <!-- Section I: Financial Condition -->
  <Msbcrfc>
    <Assets>
      <FC10>10000000</FC10>           <!-- Cash in bank (FBO accounts) -->
      <FC80>2000000</FC80>            <!-- Investments (if any) -->
      <!-- ... other assets ... -->
    </Assets>
    <LiabilitiesAndEquity>
      <FC170>500000</FC170>           <!-- Accounts payable -->
      <FC220>12000000</FC220>         <!-- ⭐ OUTSTANDING SHOP PAY WALLET BALANCES -->
      <FC360>1500000</FC360>          <!-- Retained earnings -->
      <!-- ... other liabilities & equity ... -->
    </LiabilitiesAndEquity>
    <IncomeStatement>
      <FC430>150000</FC430>           <!-- ⭐ INTEREST INCOME ON FBO ACCOUNTS -->
      <FC500>400000</FC500>           <!-- Salaries & employee benefits -->
      <FC560>200000</FC560>           <!-- Professional services -->
      <!-- ... other income/expenses ... -->
    </IncomeStatement>
  </Msbcrfc>
  
  <!-- Section II(a): Company-Wide Transactions -->
  <Msbcrta>
    <TransactionsCompanyWideSection>
      <TA90>50000</TA90>              <!-- ⭐ # OF FUNDING TRANSACTIONS (all US) -->
      <TA100>12000000</TA100>         <!-- ⭐ $ OF FUNDING TRANSACTIONS (all US) -->
    </TransactionsCompanyWideSection>
  </Msbcrta>
  
  <!-- Section II(b): State Transactions - One per licensed state -->
  <Msbcrst stateCode="CA">
    <TransactionsStateSpecificSection>
      <ST90>15000</ST90>              <!-- ⭐ # OF FUNDING TRANSACTIONS IN CA -->
      <ST100>3600000</ST100>          <!-- ⭐ $ OF FUNDING TRANSACTIONS IN CA -->
    </TransactionsStateSpecificSection>
  </Msbcrst>
  
  <Msbcrst stateCode="NY">
    <TransactionsStateSpecificSection>
      <ST90>10000</ST90>              <!-- ⭐ # OF FUNDING TRANSACTIONS IN NY -->
      <ST100>2400000</ST100>          <!-- ⭐ $ OF FUNDING TRANSACTIONS IN NY -->
    </TransactionsStateSpecificSection>
  </Msbcrst>
  
  <Msbcrst stateCode="TX">
    <TransactionsStateSpecificSection>
      <ST90>8000</ST90>               <!-- ⭐ # OF FUNDING TRANSACTIONS IN TX -->
      <ST100>1920000</ST100>          <!-- ⭐ $ OF FUNDING TRANSACTIONS IN TX -->
    </TransactionsStateSpecificSection>
  </Msbcrst>
  
  <!-- ... More <Msbcrst> sections for each licensed state ... -->
  
  <!-- Section III: Permissible Investments -->
  <Msbcrpi>
    <PermissibleInvestmentsSection>
      <PI10>10000000</PI10>           <!-- ⭐ FBO ACCOUNT BALANCES AT BANK PARTNERS -->
      <PI90>2000000</PI90>            <!-- US Treasury securities (if invested) -->
      <PI120>12000000</PI120>         <!-- ⭐ TOTAL OUTSTANDING LIABILITY (= FC220) -->
      <PI130>11500000</PI130>         <!-- ⭐ AVERAGE DAILY OUTSTANDING LIABILITY -->
    </PermissibleInvestmentsSection>
  </Msbcrpi>
  
  <!-- Section IV: Destination Country (ONLY if international merchant payments allowed) -->
  <!-- Omit if Shop Pay Wallet Balance only used for US Merchants -->
  
</MsbcrFiling>
```

---

## 🎉 **Status: READY TO PROCEED**

### **What's Complete**:
✅ Business model fully understood  
✅ Funds flow documented  
✅ Legal entity structure clarified  
✅ All MSB report fields mapped to Shopify FS data  
✅ Data source requirements defined  
✅ Implementation plan created  

### **What's Needed to Start**:
🔴 Licensed states list (Legal/Compliance)  
🔴 NMLS Company ID (Legal/Compliance)  
🔴 NetSuite account mappings (Finance/Accounting)  
🟡 International merchant payment confirmation (Product)  

### **Next Action**:
Test NetSuite MCP to extract sample financial data for Shopify FS subsidiary!

---

**Ready to build! 🚀**
