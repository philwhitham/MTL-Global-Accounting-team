# Q4 2025 MSB Call Report - Pre-Submission Validation

**Validation Date**: January 21, 2026  
**Validator**: Phil Whitham  
**Report**: Shopify Financial Services Inc. Q4 2025  
**NMLS ID**: 2689562  

---

## ✅ **SECTION 1: Data Validation**

### ✅ **1.1 Balance Sheet Balances**
**Status**: PASS ✅

**Check**: Assets = Liabilities + Equity

**Calculation**:
- **Assets**: $2,000,000
- **Liabilities**: $32,588
- **Equity**: $1,967,412
- **Total L+E**: $32,588 + $1,967,412 = $2,000,000

**Result**: ✅ Balance sheet balances correctly

---

### ✅ **1.2 Data Extraction Method**
**Status**: PASS ✅

**Check**: All amounts extracted from NetSuite using accounting periods (not dates)

**Method Used**:
- Balance Sheet: Used `accountingPeriod <= 359` (cumulative through Dec 31, 2025)
- Income Statement: Used `accountingPeriod IN (357, 358, 359)` (Q4 months only)
- Subsidiary Filter: `subsidiary = 87` (Shopify Financial Services Inc.)
- Accounting Book: `accountingBook = 1` (Primary)

**Periods Used**:
- Period 357: October 2025
- Period 358: November 2025
- Period 359: December 2025 (Q4 end)

**Result**: ✅ Correct methodology confirmed by user

---

### ✅ **1.3 Income Statement vs Balance Sheet Reconciliation**
**Status**: PASS ✅

**Check**: Income statement expenses match balance sheet net income

**Calculation**:
- **Total Q4 Expenses**: $30,588 (Rent: $7,128 + Insurance: $23,460)
- **Total Q4 Revenue**: $0
- **Q4 Net Loss**: ($30,588)
- **Cumulative Net Loss (FC360)**: ($32,588)

**Reconciliation**:
- Cumulative Loss: ($32,588)
- Q4 Loss: ($30,588)
- Prior Period Activity: $32,588 - $30,588 = $2,000

**Result**: ✅ Reconciles correctly (includes $2,000 prior period expenses)

---

### ✅ **1.4 Dollar Amount Format**
**Status**: PASS ✅

**Check**: All dollar amounts are whole numbers (no decimals)

**Sample Verification**:
```xml
<FC10>2000000</FC10>      ✅ No decimals
<FC180>9128</FC180>        ✅ No decimals
<FC240>23460</FC240>       ✅ No decimals
<FC310>10</FC310>          ✅ No decimals
<FC340>1999990</FC340>     ✅ No decimals
<FC360>-32588</FC360>      ✅ No decimals (negative allowed)
<FC520>7128</FC520>        ✅ No decimals
<FC580>23460</FC580>       ✅ No decimals
<PI10>2000000</PI10>       ✅ No decimals
```

**Result**: ✅ All dollar amounts are whole numbers

---

### ✅ **1.5 State Code Format**
**Status**: PASS ✅

**Check**: All state codes use proper 2-letter abbreviations

**State Codes Used**:
```xml
<Msbcrst stateCode="PA">   ✅ Pennsylvania (correct)
<Msbcrst stateCode="AZ">   ✅ Arizona (correct)
<Msbcrst stateCode="AL">   ✅ Alabama (correct)
```

**Result**: ✅ All state codes are valid 2-letter abbreviations

---

## ✅ **SECTION 2: Required Information**

### ✅ **2.1 NMLS ID**
**Status**: PASS ✅

**Requirement**: NMLS ID must be included

**Where to Find**: This is included in the NMLS portal submission form, not in the XML file itself. The XML file does not have an NMLS ID field.

**Confirmed NMLS ID**: 2689562

**Result**: ✅ NMLS ID documented and ready for portal entry

---

### ✅ **2.2 Form Version**
**Status**: PASS ✅

**Requirement**: Form version must be v4

**XML Attribute**:
```xml
<MsbcrFiling year="2025" formVersion="v4" periodType="MSBQ4">
```

**Result**: ✅ Form version is "v4" (correct)

---

### ✅ **2.3 Period Type**
**Status**: PASS ✅

**Requirement**: Period type must be MSBQ4 for Q4 2025

**XML Attribute**:
```xml
<MsbcrFiling year="2025" formVersion="v4" periodType="MSBQ4">
```

**Result**: ✅ Period type is "MSBQ4" (correct)

---

### ✅ **2.4 Year**
**Status**: PASS ✅

**Requirement**: Year must be 2025

**XML Attribute**:
```xml
<MsbcrFiling year="2025" formVersion="v4" periodType="MSBQ4">
```

**Result**: ✅ Year is "2025" (correct)

---

### ✅ **2.5 Licensed States Included**
**Status**: PASS ✅

**Requirement**: All states licensed during Q4 2025 must be included

**Licensed States in Q4 2025**:
1. **Pennsylvania** - License #117728, Effective Nov 7, 2025 (54 days in Q4)
2. **Arizona** - License #MT-2012267, Effective Dec 4, 2025 (27 days in Q4)
3. **Alabama** - License #1008, Effective Dec 12, 2025 (19 days in Q4)

**States in XML**:
```xml
<Msbcrst stateCode="PA">   ✅ Pennsylvania included
<Msbcrst stateCode="AZ">   ✅ Arizona included
<Msbcrst stateCode="AL">   ✅ Alabama included
```

**States NOT Included (Correct)**:
- Michigan (Effective Jan 1, 2026 - not in Q4 2025) ✅
- Oregon (Effective Jan 8, 2026 - not in Q4 2025) ✅

**Result**: ✅ All required states included, future states correctly excluded

---

## ✅ **SECTION 3: XML Structure**

### ✅ **3.1 Section I: Financial Condition (Msbcrfc)**
**Status**: PASS ✅

**Required Elements**:
- [x] `<Assets>` section with balance sheet assets
- [x] `<LiabilitiesAndEquity>` section with liabilities and equity
- [x] `<IncomeStatement>` section with P&L data
- [x] `<ExplanatoryNotesSection>` with FCNOTE_1

**Key Fields Populated**:
```xml
Assets:
- FC10 (Cash): $2,000,000 ✅
  
Liabilities:
- FC180 (IC Payables): $9,128 ✅
- FC240 (Other Liabilities): $23,460 ✅
- FC220 (Stored Value Liability): $0 ✅ (pre-operational)

Equity:
- FC310 (Common Stock): $10 ✅
- FC340 (APIC): $1,999,990 ✅
- FC360 (Retained Earnings): -$32,588 ✅

Income Statement:
- FC430 (Stored Value Fees): $0 ✅ (pre-operational)
- FC520 (Rent): $7,128 ✅
- FC580 (Insurance): $23,460 ✅
```

**Result**: ✅ Section I complete and accurate

---

### ✅ **3.2 Section II(a): Company-Wide Transactions (Msbcrta)**
**Status**: PASS ✅

**Required Elements**:
- [x] `<TransactionsCompanyWideSection>` with company-wide transaction data
- [x] `<ExplanatoryNotesSection>` with TANOTE_1

**Key Fields Populated**:
```xml
- TA90 (# Stored Value Transactions): 0 ✅ (pre-operational)
- TA100 ($ Stored Value Transactions): $0 ✅ (pre-operational)
```

**Explanatory Note**: Included - explains pre-operational status

**Result**: ✅ Section II(a) complete with appropriate zeros and explanatory note

---

### ✅ **3.3 Section II(b): State Transactions (Msbcrst)**
**Status**: PASS ✅

**Required Elements**: One `<Msbcrst>` section for each licensed state

**Pennsylvania (PA)**:
```xml
<Msbcrst stateCode="PA">
  <TransactionsStateSpecificSection>
    <ST90>0</ST90>  ✅ # of transactions
    <ST100>0</ST100> ✅ $ of transactions
  </TransactionsStateSpecificSection>
  <ExplanatoryNotesSection>
    <STNOTE_1>Pennsylvania license effective November 7, 2025...</STNOTE_1> ✅
  </ExplanatoryNotesSection>
</Msbcrst>
```

**Arizona (AZ)**:
```xml
<Msbcrst stateCode="AZ">
  <TransactionsStateSpecificSection>
    <ST90>0</ST90>  ✅
    <ST100>0</ST100> ✅
  </TransactionsStateSpecificSection>
  <ExplanatoryNotesSection>
    <STNOTE_1>Arizona license effective December 4, 2025...</STNOTE_1> ✅
  </ExplanatoryNotesSection>
</Msbcrst>
```

**Alabama (AL)**:
```xml
<Msbcrst stateCode="AL">
  <TransactionsStateSpecificSection>
    <ST90>0</ST90>  ✅
    <ST100>0</ST100> ✅
  </TransactionsStateSpecificSection>
  <ExplanatoryNotesSection>
    <STNOTE_1>Alabama license effective December 12, 2025...</STNOTE_1> ✅
  </ExplanatoryNotesSection>
</Msbcrst>
```

**Result**: ✅ Section II(b) complete with 3 state sections (PA, AZ, AL)

---

### ✅ **3.4 Section III: Permissible Investments (Msbcrpi)**
**Status**: PASS ✅

**Required Elements**:
- [x] `<PermissibleInvestmentsSection>` with investment data
- [x] `<ExplanatoryNotesSection>` with PINOTE_1

**Key Fields Populated**:
```xml
- PI10 (Bank Deposits): $2,000,000 ✅ (CITI Bank)
- PI120 (Outstanding Stored Value): $0 ✅ (pre-operational)
- PI130 (Avg Daily Trans Liability): $0 ✅ (pre-operational)
```

**Explanatory Note**: Included - explains funds held at CITI Bank

**Result**: ✅ Section III complete and accurate

---

### ✅ **3.5 Section IV(a): Destination Country - Company (Msbcrtda)**
**Status**: PASS ✅

**Required Elements** (Q4 only):
- [x] `<ListSectionOfCompanyTransactionsItem>` with destination country data
- [x] `<ExplanatoryNotesSection>` with TDANOTE_1

**Structure**:
```xml
<Msbcrtda>
  <ListSectionOfCompanyTransactionsItem>
    <DetailItemList>
    </DetailItemList>  ✅ Empty (no international transactions)
  </ListSectionOfCompanyTransactionsItem>
  <ExplanatoryNotesSection>
    <TDANOTE_1>No international transactions during Q4 2025...</TDANOTE_1> ✅
  </ExplanatoryNotesSection>
</Msbcrtda>
```

**Result**: ✅ Section IV(a) included with empty list and explanatory note (correct for pre-operational)

---

### ✅ **3.6 Explanatory Notes**
**Status**: PASS ✅

**Required**: Explanatory notes should provide context for zeros and pre-operational status

**Notes Included**:
1. **FCNOTE_1** (Financial Condition): ✅
   - Explains formation date, licenses obtained, pre-operational status
   - Clear and comprehensive

2. **TANOTE_1** (Company Transactions): ✅
   - Explains zero transactions due to pre-operational status
   - References pending product launch

3. **STNOTE_1** (Pennsylvania): ✅
   - License effective date
   - Zero transactions explained

4. **STNOTE_1** (Arizona): ✅
   - License effective date
   - Zero transactions explained

5. **STNOTE_1** (Alabama): ✅
   - License effective date
   - Zero transactions explained

6. **PINOTE_1** (Permissible Investments): ✅
   - Explains CITI Bank account
   - Zero stored value liability explained

7. **TDANOTE_1** (Destination Country): ✅
   - Explains no international transactions
   - Pre-operational status noted

**Result**: ✅ All sections have appropriate explanatory notes

---

## ✅ **SECTION 4: Technical Validation**

### ✅ **4.1 XML Schema Validation**
**Status**: PASS ✅

**Test Performed**: Validated XML against official XSD schema
**Tool Used**: `lxml` XML validator
**Schema File**: `Data Specification File - ExternalMsbcrBatchFileSchemaV4.txt`

**Validation Result**:
```
✅ ✅ ✅ VALIDATION SUCCESSFUL! ✅ ✅ ✅
🎉 The XML file is valid and conforms to the XSD schema.
```

**Result**: ✅ XML is valid and conforms to official NMLS XSD schema

---

### ✅ **4.2 XML Well-Formedness**
**Status**: PASS ✅

**Checks**:
- [x] Valid XML declaration
- [x] Proper nesting of elements
- [x] All opening tags have closing tags
- [x] Attribute values properly quoted
- [x] No special characters that need escaping

**Result**: ✅ XML is well-formed

---

### ✅ **4.3 File Encoding**
**Status**: PASS ✅

**Check**: File must be UTF-8 encoded

**XML Declaration**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
```

**Result**: ✅ File is UTF-8 encoded

---

## ⏳ **SECTION 5: Review & Approval** (Pending)

### ⏳ **5.1 Finance Team Review**
**Status**: PENDING ⏳

**Required Actions**:
- [ ] Finance team to verify all NetSuite amounts
- [ ] Confirm balance sheet balances
- [ ] Confirm P&L amounts
- [ ] Approve for submission

**Assigned To**: Finance/Accounting Team  
**Due Date**: February 7, 2026  
**Status**: Not yet started

---

### ⏳ **5.2 Legal/Compliance Team Review**
**Status**: PENDING ⏳

**Required Actions**:
- [ ] Verify all licensed states are included correctly
- [ ] Review explanatory notes for accuracy
- [ ] Confirm regulatory compliance
- [ ] Approve for submission

**Assigned To**: Legal/Compliance Team  
**Due Date**: February 7, 2026  
**Status**: Not yet started

---

### ⏳ **5.3 Final Approval**
**Status**: PENDING ⏳

**Required Actions**:
- [ ] Obtain final sign-off from all stakeholders
- [ ] Confirm no changes needed
- [ ] Authorize submission to NMLS

**Assigned To**: Phil Whitham (coordinator)  
**Due Date**: February 14, 2026  
**Status**: Waiting for team reviews

---

## 📊 **VALIDATION SUMMARY**

| Category | Items | Passed | Failed | Pending |
|----------|-------|--------|--------|---------|
| **Data Validation** | 5 | 5 ✅ | 0 | 0 |
| **Required Information** | 5 | 5 ✅ | 0 | 0 |
| **XML Structure** | 6 | 6 ✅ | 0 | 0 |
| **Technical Validation** | 3 | 3 ✅ | 0 | 0 |
| **Review & Approval** | 3 | 0 | 0 | 3 ⏳ |
| **TOTAL** | **22** | **19 ✅** | **0** | **3 ⏳** |

---

## 🎯 **READINESS ASSESSMENT**

### ✅ **Technical Readiness: 100%**
- All automated validation checks passed
- XML structure is complete and valid
- Data integrity confirmed
- Schema validation successful

### ⏳ **Stakeholder Readiness: 0%**
- Finance review pending
- Legal/Compliance review pending
- Final approval pending

### 🟢 **Overall Status: READY FOR REVIEW**

The XML file is technically complete and valid. All automated checks have passed. The report is ready for internal stakeholder review and approval.

---

## 📅 **NEXT STEPS & TIMELINE**

### **Week of January 27, 2026**
- [ ] Schedule review meetings with Finance and Legal teams
- [ ] Distribute report summary and XML file
- [ ] Prepare answers to anticipated questions

### **By February 7, 2026** (Target)
- [ ] Complete Finance team review
- [ ] Complete Legal/Compliance team review
- [ ] Address any feedback or corrections

### **By February 14, 2026** (Final Deadline)
- [ ] Obtain final approval from all stakeholders
- [ ] Make any final corrections if needed
- [ ] Prepare for NMLS portal submission

### **February 15, 2026** (Due Date)
- [ ] Submit to NMLS portal
- [ ] Retain copy for records
- [ ] Document submission confirmation

---

## 🚨 **RISK ASSESSMENT**

### **LOW RISK ITEMS** 🟢
- ✅ Technical validation (complete)
- ✅ Data accuracy (user-confirmed)
- ✅ XML structure (validated against schema)
- ✅ Timeline (25 days ahead of deadline)

### **MEDIUM RISK ITEMS** 🟡
- ⏳ Stakeholder review timing (need to schedule soon)
- ⏳ First-time submission (learning curve for portal)

### **NO HIGH RISK ITEMS** ✅

---

## 📝 **VALIDATION NOTES**

### **Strengths**
1. ✅ Pre-operational status makes validation straightforward
2. ✅ All zeros are legitimate and well-documented
3. ✅ Explanatory notes provide excellent context
4. ✅ Financial data confirmed accurate by user
5. ✅ Well ahead of deadline (25 days)

### **Considerations**
1. ℹ️ First MSB Call Report for Shopify FS (no prior submissions to reference)
2. ℹ️ Pre-operational status is unusual but legitimate
3. ℹ️ Explanatory notes are critical for NMLS acceptance

### **Recommendations**
1. 📋 Schedule stakeholder reviews immediately (don't wait)
2. 📋 Prepare FAQ document for reviewers
3. 📋 Create NMLS portal submission guide
4. 📋 Document lessons learned for Q1 2026 report

---

## ✅ **CERTIFICATION**

I certify that:
- ✅ All automated validation checks have been performed
- ✅ All technical requirements have been met
- ✅ The XML file validates successfully against the official XSD schema
- ✅ Financial data has been confirmed accurate
- ✅ The report is ready for stakeholder review

**Validated By**: Phil Whitham  
**Date**: January 21, 2026  
**Next Review**: February 7, 2026  

---

**Status**: ✅ **TECHNICAL VALIDATION COMPLETE - READY FOR STAKEHOLDER REVIEW**
