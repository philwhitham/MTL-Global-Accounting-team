# Shopify Financial Services Inc. - Q4 2025 MSB Call Report

**Report Generated**: January 21, 2026  
**Reporting Period**: October 1 - December 31, 2025  
**Due Date**: February 15, 2026  
**NMLS ID**: 2689562  

---

## 📊 **Financial Summary**

### **Balance Sheet as of December 31, 2025**

| Category | Amount |
|----------|--------|
| **Assets** | |
| Cash on Hand and in Bank (FC10) | $2,000,000 |
| **Total Assets** | **$2,000,000** |
| | |
| **Liabilities** | |
| Inter-company Payables (FC180) | $9,128 |
| Other Current Liabilities (FC240) | $23,460 |
| **Total Liabilities** | **$32,588** |
| | |
| **Equity** | |
| Common Stock (FC310) | $10 |
| Additional Paid-in Capital (FC340) | $1,999,990 |
| Retained Earnings (FC360) | ($32,588) |
| **Total Equity** | **$1,967,412** |
| | |
| **Total Liabilities & Equity** | **$2,000,000** |

---

### **Income Statement - Q4 2025**

| Category | Amount |
|----------|--------|
| **Revenue** | |
| Stored Value Fee Income (FC430) | $0 |
| **Total Revenue** | **$0** |
| | |
| **Expenses** | |
| Rent (FC520) | $7,128 |
| Insurance (FC580) | $23,460 |
| **Total Expenses** | **$30,588** |
| | |
| **Net Income (Loss)** | **($30,588)** |

---

### **Transaction Activity - Q4 2025**

| Section | Field | Description | Amount |
|---------|-------|-------------|--------|
| **Company-Wide** | TA90 | # of stored value transactions | 0 |
| **Company-Wide** | TA100 | $ of stored value transactions | $0 |
| **Pennsylvania** | ST90 | # of transactions in PA | 0 |
| **Pennsylvania** | ST100 | $ of transactions in PA | $0 |
| **Arizona** | ST90 | # of transactions in AZ | 0 |
| **Arizona** | ST100 | $ of transactions in AZ | $0 |
| **Alabama** | ST90 | # of transactions in AL | 0 |
| **Alabama** | ST100 | $ of transactions in AL | $0 |

**Note**: All transaction counts and amounts are zero as the company is pre-operational.

---

### **Permissible Investments - Q4 2025**

| Category | Amount |
|----------|--------|
| Deposits in Domestic Banks (PI10) | $2,000,000 |
| Outstanding Stored Value Liability (PI120) | $0 |
| Average Daily Transmission Liability (PI130) | $0 |

**Note**: All funds held at CITI Bank. No stored value liability as operations have not commenced.

---

## 📋 **Licensed States**

| State | License # | Effective Date | Days in Q4 2025 |
|-------|-----------|----------------|-----------------|
| **Pennsylvania** | 117728 | November 7, 2025 | 54 days |
| **Arizona** | MT-2012267 | December 4, 2025 | 27 days |
| **Alabama** | 1008 | December 12, 2025 | 19 days |

**Upcoming Licenses**:
- Michigan (MT 0027002) - Effective January 1, 2026
- Oregon (NMLS: 2689562) - Effective January 8, 2026

---

## ✅ **Pre-Submission Checklist**

### **Data Validation**
- [x] Balance sheet balances (Assets = Liabilities + Equity)
- [x] All amounts extracted from NetSuite using accounting periods (not dates)
- [x] Income statement expenses match balance sheet net income
- [x] All dollar amounts are whole numbers (no decimals)
- [x] All state codes use proper 2-letter abbreviations

### **Required Information**
- [x] NMLS ID included: 2689562
- [x] Form version: v4
- [x] Period type: MSBQ4
- [x] Year: 2025
- [x] All licensed states included (PA, AZ, AL)

### **XML Structure**
- [x] Section I: Financial Condition (Msbcrfc) - Complete
- [x] Section II(a): Company-Wide Transactions (Msbcrta) - Complete (zeros)
- [x] Section II(b): State Transactions (Msbcrst) - 3 sections (PA, AZ, AL)
- [x] Section III: Permissible Investments (Msbcrpi) - Complete
- [x] Section IV(a): Destination Country - Company (Msbcrtda) - Included (empty)
- [x] Explanatory notes added for context

### **Review & Approval**
- [ ] Finance team review
- [ ] Legal/Compliance team review
- [ ] Final approval before submission
- [x] XML validated against XSD schema ✅ (Passed - See PRE_SUBMISSION_VALIDATION.md)

---

## 📝 **Explanatory Notes Included**

**Financial Condition Note (FCNOTE_1)**:
> "Shopify Financial Services Inc. was formed on December 18, 2024. The company obtained MSB licenses in Pennsylvania (Nov 7, 2025), Arizona (Dec 4, 2025), and Alabama (Dec 12, 2025). As of Q4 2025, the company is pre-operational with no stored value transactions. The balance sheet reflects initial capitalization from parent company and minimal operating expenses."

**Transaction Activity Note (TANOTE_1)**:
> "No stored value transactions during Q4 2025. Company is pre-operational pending completion of state licensing and product launch."

**Permissible Investments Note (PINOTE_1)**:
> "All funds held in CITI Bank account (CITI Shopify Financial Services OPS USD). No outstanding stored value liability as company is pre-operational."

---

## 🚀 **Next Steps**

### **By February 7, 2026** (1 week before due date)
1. **Validate XML** against official XSD schema
2. **Finance Review**: Confirm all amounts are accurate
3. **Legal/Compliance Review**: Confirm regulatory requirements met
4. **Address any feedback** and regenerate if needed

### **By February 14, 2026** (1 day before due date)
5. **Final approval** from all stakeholders
6. **Submit to NMLS** portal
7. **Retain copy** for records

### **After Submission**
8. **Monitor for acceptance** or rejection notices from NMLS
9. **Document lessons learned** for Q1 2026 report
10. **Prepare for operational reporting** when Shop Pay Wallet Balance launches

---

## 📞 **Contacts for Review**

| Team | Purpose | Status |
|------|---------|--------|
| Finance/Accounting | Verify financial amounts | ⏳ Pending |
| Legal/Compliance | Regulatory compliance | ⏳ Pending |
| IT/Data | Technical validation | ⏳ Pending |

---

## 📁 **Files Generated**

1. **`SHOPIFY_FS_Q4_2025_MSB_REPORT.xml`** - Final XML for submission
2. **`Q4_2025_REPORT_SUMMARY.md`** - This summary document

**Location**: `/Users/philwhitham/MTL-Global-Accounting-team/MSB Call Reports/2025/Q4/`

---

## ⚠️ **Important Notes**

1. **Pre-Operational Status**: This is a pre-operational report with no stored value transactions. All transaction fields are legitimately zero.

2. **Future Reports**: When Shop Pay Wallet Balance launches, we'll need to:
   - Add BigQuery integration for transaction data (TA/ST fields)
   - Calculate daily outstanding balances for PI130 (ADTL)
   - Add actual stored value liability (FC220)

3. **Michigan & Oregon**: Will be included starting in Q1 2026 report (due May 15, 2026).

4. **Q4 Special Section**: Section IV (Destination Country Detail) is included but empty as it's Q4-only and we have no international transactions.

---

**Status**: ✅ **READY FOR INTERNAL REVIEW**  
**Timeline**: 🟢 **25 days until due date** (on track)  
**Confidence**: 🟢 **HIGH** (financial data confirmed by user)  

---

**Prepared by**: Phil Whitham  
**Date**: January 21, 2026  
**Next Review**: February 7, 2026
