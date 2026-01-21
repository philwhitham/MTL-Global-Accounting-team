# MSB Call Report XML Project - Status Summary

**Date**: January 21, 2026  
**Project**: Shopify Financial Services Inc. MSB Call Report Automation  
**Status**: ✅ **Analysis Complete - Ready for Implementation**  

---

## 📋 **What I've Completed Today**

### ✅ **1. XML Schema Analysis**
- Reviewed complete XSD schema (`ExternalMsbcrBatchFileSchemaV4.txt`)
- Analyzed sample XML (`EXTERNAL_MSBCR_2024_Q4.xml`)
- Extracted all field definitions from Excel (`MSBCR Data Specification v4.xlsx`)
- **Created**: `docs/XML_SCHEMA_ANALYSIS.md` (comprehensive schema documentation)

### ✅ **2. Field Mapping**
- Mapped every XML field code (FC10, TA10, etc.) to its description
- Identified which fields apply to Shopify's stored value business
- Determined data types and validation rules
- **Created**: `docs/SHOPIFY_STORED_VALUE_MAPPING.md` (complete field mappings)

### ✅ **3. Business Plan Analysis**
- Reviewed Shopify Financial Services business plan in detail
- Analyzed funds flow for all transaction types:
  - ACH Funding
  - Merchant Payments
  - Split Payments
  - Refunds
  - Withdrawals
- **Created**: `docs/BUSINESS_PLAN_ANALYSIS.md` (business model + MSB mappings)

### ✅ **4. NetSuite MCP Testing**
- Successfully connected to NetSuite MCP
- Found Shopify Financial Services Inc. subsidiary (ID: 87)
- Identified bank accounts:
  - `11623`: CITI Shopify Financial Services CLE USD
  - `11624`: CITI Shopify Financial Services OPS USD
- Mapped accounting period structure (Q4 2024 = Period ID 339)
- **Status**: NetSuite MCP operational and ready for data extraction

---

## 🎯 **Key Findings**

### **Entity Information**
- **Legal Name**: Shopify Financial Services Inc.
- **Formation**: Delaware corporation, December 18, 2024
- **Parent**: Shopify Holdings (USA) 2 Inc.
- **NetSuite Subsidiary ID**: 87
- **FinCEN Registration**: ✓ Completed

###  **Product: Shop Pay Wallet Balance**
- **Classification**: Stored Value / Prepaid Access
- **Funding**: ACH from Shopper's external bank account
- **Storage**: FBO (For Benefit Of) accounts at Bank Partners
- **Uses**: Pay Merchants, Withdraw to bank (NO P2P transfers)
- **Revenue Model**: Interest income on FBO balances (no Shopper fees)

### **Critical MSB Report Fields for Shopify FS**

| Section | Field | Description | Data Source |
|---------|-------|-------------|-------------|
| **I. Financial Condition** | FC220 | Outstanding stored value liability | NetSuite: FBO Account balance |
| **I. Financial Condition** | FC430 | Stored value fee income | NetSuite: Interest income |
| **II(a). Company Transactions** | TA90 | # of stored value funding transactions | BigQuery: COUNT of deposits |
| **II(a). Company Transactions** | TA100 | $ of stored value funding transactions | BigQuery: SUM of deposits |
| **II(b). State Transactions** | ST90 | # of funding transactions per state | BigQuery: COUNT by state |
| **II(b). State Transactions** | ST100 | $ of funding transactions per state | BigQuery: SUM by state |
| **III. Permissible Investments** | PI10 | Deposits in domestic banks | NetSuite: FBO account balances |
| **III. Permissible Investments** | PI120 | Total outstanding liability | NetSuite: Same as FC220 |
| **III. Permissible Investments** | PI130 | Average daily outstanding liability | Calculated: Avg daily FC220 |

---

## 📁 **Documentation Created**

1. **`docs/XML_SCHEMA_ANALYSIS.md`**
   - Complete XML structure breakdown
   - All data type definitions
   - Validation rules
   - 6 main sections explained

2. **`docs/SHOPIFY_STORED_VALUE_MAPPING.md`**
   - Field-by-field mapping for Shopify FS
   - Data source identification
   - Sample queries for NetSuite and BigQuery
   - Implementation checklist

3. **`docs/BUSINESS_PLAN_ANALYSIS.md`**
   - Business model analysis
   - Funds flow documentation
   - MSB reporting implications
   - Critical questions identified

4. **`docs/scoping-document.md`**
   - Project scope and requirements
   - Reporting frequency
   - Submission details

5. **`docs/msb_specifications.txt`**
   - Extracted PDF specifications
   - Complete regulatory requirements

---

## 🚨 **Critical Information STILL NEEDED**

### **1. State Licensing List** ⚠️ **URGENT**
**Question**: In which states has Shopify FS obtained MSB licenses?

**Why it matters**: Need one `<Msbcrst>` XML section per licensed state

**Who to ask**: Legal/Compliance team

**Impact**: Cannot generate complete XML without this

---

### **2. NMLS Company ID** ⚠️ **URGENT**
**Question**: What is Shopify FS's NMLS Company ID?

**Why it matters**: Required XML attribute for submission

**Who to ask**: Legal/Compliance team

**Impact**: Cannot submit XML without this

---

### **3. NetSuite Account Mappings** ⚠️ **URGENT**
**Questions**:
- What is the NetSuite account number for the FBO Account liability?
- What is the account number for interest income on FBO account?
- Which accounts map to which FC fields (FC10-FC670)?

**Why it matters**: Required for automated data extraction

**Who to ask**: Finance/Accounting team

**Impact**: Cannot extract financial data without account mappings

---

### **4. International Merchant Payments** 🟡 **IMPORTANT**
**Question**: Can Shoppers use Shop Pay Wallet Balance to pay international Merchants (outside US)?

**Why it matters**: Determines if Sections IV(a) and IV(b) (Destination Country Detail) are required

**Who to ask**: Product team

**Impact**: May need additional country-level reporting

---

### **5. BigQuery Table Identification** 🟡 **IMPORTANT**
**Questions**:
- Which BigQuery table contains Shop Pay Wallet Balance transactions?
- What are the field names for transaction_type, amount, date, user_state?
- How are "funding" transactions identified vs. "redemption" transactions?

**Why it matters**: Required for transaction activity reporting (TA/ST fields)

**Who to ask**: Data Engineering team

**Impact**: Cannot calculate TA90/TA100/ST90/ST100 without this

---

## 🎯 **Next Steps**

### **Immediate Actions (This Week)**
1. **Gather Critical Information**:
   - [ ] Get licensed states list from Legal/Compliance
   - [ ] Get NMLS Company ID from Legal/Compliance
   - [ ] Map NetSuite accounts with Finance/Accounting
   - [ ] Confirm international payment capability with Product
   - [ ] Identify BigQuery tables with Data Engineering

2. **Update XML Generator**:
   - [ ] Rewrite generator to match exact XSD schema
   - [ ] Implement proper data type validation
   - [ ] Add state iteration logic
   - [ ] Add explanatory notes capability

### **Short Term (Next 2 Weeks)**
3. **Build Data Extraction**:
   - [ ] Create NetSuite extraction queries for FC fields
   - [ ] Create BigQuery extraction queries for TA/ST fields
   - [ ] Test with sample data
   - [ ] Validate against XSD schema

4. **Testing & Validation**:
   - [ ] Generate test XML
   - [ ] Review with Finance, Compliance, Legal
   - [ ] Prepare for Q1 2025 reporting

### **Medium Term (Next Month)**
5. **Production Readiness**:
   - [ ] Document quarterly process
   - [ ] Create runbook
   - [ ] Establish review/approval workflow
   - [ ] Set up quarterly reminders

---

## 📊 **MSB Reporting Calendar**

| Quarter | Period End | Due Date | Days to File |
|---------|-----------|----------|--------------|
| **Q1 2025** | March 31, 2025 | **May 15, 2025** | 45 days |
| Q2 2025 | June 30, 2025 | August 15, 2025 | 46 days |
| Q3 2025 | September 30, 2025 | November 17, 2025 | 48 days |
| Q4 2025 | December 31, 2025 | February 16, 2026 | 47 days |

**NOTE**: Sections IV(a) and IV(b) (Destination Country Detail) are **Q4 only** (annual data)

---

## 🏗️ **Technical Architecture**

```
Data Sources:
├── NetSuite (Section I: Financial Condition)
│   ├── Balance Sheet (FC10-FC380)
│   ├── Income Statement (FC410-FC670)
│   └── Permissible Investments (PI10-PI180)
│
├── BigQuery (Section II: Transaction Activity)
│   ├── Company-Wide (TA90, TA100)
│   └── State-Specific (ST90, ST100 x N states)
│
└── Configuration
    ├── Licensed States List
    ├── NMLS Company ID
    └── Account Mappings

          ↓

XML Generator (Python)
├── NetSuite MCP Integration
├── BigQuery Query Engine
├── XSD Schema Validator
└── State Iteration Logic

          ↓

MSB Call Report XML
└── Submit to NMLS Portal
```

---

## 💡 **Implementation Approach**

### **Recommended: Phased Rollout**

**Phase 1: Financial Condition Only** (Weeks 1-2)
- Extract Section I (FC fields) from NetSuite
- Generate partial XML with financial data
- Validate structure
- **Outcome**: Prove NetSuite integration works

**Phase 2: Transaction Activity** (Weeks 3-4)
- Add Sections II(a) and II(b) (TA/ST fields) from BigQuery
- Implement state iteration
- Test with real transaction data
- **Outcome**: Complete quarterly reporting (excluding Section III/IV)

**Phase 3: Permissible Investments** (Week 5)
- Add Section III (PI fields)
- Calculate ADTL (PI130)
- **Outcome**: Full quarterly report ready

**Phase 4: Destination Country (If Needed)** (Week 6)
- Add Sections IV(a) and IV(b) if international transactions exist
- **Outcome**: Q4 annual report ready

---

## ✅ **What's Working**

✅ NetSuite MCP configured and operational  
✅ Shopify FS subsidiary identified in NetSuite  
✅ All XML field meanings documented  
✅ Business model fully understood  
✅ Data source requirements defined  
✅ Implementation plan created  

---

## ❌ **What's Blocking**

🔴 Licensed states list (URGENT - needed for XML generation)  
🔴 NMLS Company ID (URGENT - needed for XML submission)  
🔴 NetSuite account mappings (URGENT - needed for data extraction)  
🟡 BigQuery table identification (IMPORTANT - needed for transaction data)  
🟡 International payment confirmation (IMPORTANT - determines Section IV need)  

---

## 📝 **Questions for Follow-Up Discussion**

1. **Legal/Compliance**:
   - Which states has Shopify FS obtained MSB licenses?
   - What is the NMLS Company ID?
   - What is the FinCEN BSA ID?

2. **Finance/Accounting**:
   - What is the NetSuite account number for FBO account liability?
   - What account captures interest income on FBO account?
   - Can you provide a complete chart of accounts for Shopify FS?

3. **Product**:
   - Can Shop Pay Wallet Balance be used to pay international Merchants?
   - If yes, which countries?

4. **Data Engineering**:
   - Which BigQuery table(s) contain Shop Pay Wallet Balance transactions?
   - How do we identify "funding" vs. "redemption" transactions?
   - Is user_state captured in the transaction data?

5. **All Teams**:
   - Who should review/approve the XML before submission?
   - What is the escalation path if we encounter data issues?
   - Should we set up a quarterly review meeting?

---

## 🚀 **Ready to Build!**

**All analysis complete. Waiting on critical business inputs to proceed with implementation.**

**Estimated Time to First XML Generation**: 2-3 weeks after receiving:
- Licensed states list
- NMLS Company ID  
- NetSuite account mappings
- BigQuery table identification

---

**Contact**: Phil Whitham  
**Project Location**: `/Users/philwhitham/MTL-Global-Accounting-team`  
**GitHub**: https://github.com/philwhitham/MTL-Global-Accounting-team  
