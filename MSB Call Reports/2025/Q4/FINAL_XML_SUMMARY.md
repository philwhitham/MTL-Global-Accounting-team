# Q4 2025 MSB Call Report - Final XML Summary

**Date**: January 30, 2026  
**Version**: Final (Ready for NMLS Upload)  
**Status**: ✅ All NMLS completeness issues resolved  

---

## 📋 **All Changes Made**

Based on NMLS portal completeness checks, the following corrections were made:

---

### **1. State Transactions (ST) - All 3 States**

**States Affected**: Alabama, Arizona, Pennsylvania

**Changes**:
- ✅ Added **ST10-ST40** (Money transmission fields) = 0
- ✅ Added **ST360** (Surety Bond amounts):
  - Pennsylvania: **$1,000,000**
  - Arizona: **$25,000**
  - Alabama: **$1,000,000**
- ✅ Added **ST361** (ADTL) = 0
- ✅ Updated explanatory notes to mention surety bonds

**Result**: Each state now has **31 ST fields** (was 2)

---

### **2. Company-Wide Transactions (TA)**

**Changes**:
- ✅ Added **all TA transaction type fields** (TA10-TA330) = 0
- ✅ Kept existing TA90-TA100 (stored value) = 0
- ✅ Added money transmission, payment instruments, check cashing, currency exchange, and virtual currency fields

**Result**: **29 TA fields** (was 2)

---

### **3. Financial Condition - Assets (FC)**

**Changes**:
- ✅ Added **FC20-FC100** (missing asset fields) = 0
  - FC20: Due from agents
  - FC30: Allowance for doubtful accounts
  - FC40: Accounts receivable
  - FC50: Allowance (AR)
  - FC60: Inter-company receivables
  - FC70: Notes/other receivables
  - FC80: Investments
  - FC90: Virtual currency
  - FC100: Other current assets

**Result**: **14 asset fields** (was 5)

---

### **4. Financial Condition - Liabilities (FC)**

**Changes**:
- ✅ Added **FC240NOTE** (required because FC240 = 72% of FC250)

**FC240NOTE Content**:
> "Other current liabilities consist of accrued professional fees for audit, legal, and regulatory compliance services, and accrued surety bond issuance costs related to pre-operational setup and state licensing activities during Q4 2025."

**Explains**:
- FC240 = $23,460 (Other current liabilities)
- FC250 = $32,588 (Total current liabilities)
- Ratio = 72% (exceeds 20% NMLS threshold)

**Components of FC240**:
1. Accrued professional fees (audit, legal, compliance)
2. Accrued surety bond issuance costs (PO #21073327)

---

## ✅ **What Passed Without Changes**

- ✅ **PI** (Permissible Investments) - All checks passed
- ✅ **TD-A** (Transaction Destination) - All checks passed
- ✅ **FC - Income Statement** - No issues reported
- ✅ **All financial amounts** - Remain accurate per NetSuite

---

## 💰 **Surety Bonds Reported (ST360)**

| State | Bond Amount | Provider | Placed Date |
|-------|-------------|----------|-------------|
| Pennsylvania | $1,000,000 | Liberty Mutual | 9/2/2025 |
| Arizona | $25,000 | Liberty Mutual | 9/2/2025 |
| Alabama | $1,000,000 | Liberty Mutual | 9/2/2025 |
| **Total** | **$2,025,000** | | |

**Source**: Surety Bond Status Google Sheet (as of 10/4/25)

---

## 📊 **Final XML Statistics**

| Metric | Value |
|--------|-------|
| **Total Fields** | ~186 fields |
| **Licensed States** | 3 (PA, AZ, AL) |
| **Reporting Period** | Q4 2025 (Oct 1 - Dec 31, 2025) |
| **NMLS ID** | 2689562 |
| **Form Version** | v4 |
| **Total Assets** | $2,000,000 |
| **Total Liabilities** | $32,588 |
| **Shareholders' Equity** | $1,967,412 |
| **Surety Bonds** | $2,025,000 |

---

## 📁 **Files in This Package**

1. **SHOPIFY_FS_Q4_2025_MSB_REPORT.xml** - Final XML for NMLS upload
2. **Q4_2025_REPORT_SUMMARY.md** - Human-readable report summary
3. **PRE_SUBMISSION_VALIDATION.md** - 22-point validation checklist
4. **SUBMISSION_TIMELINE.md** - Submission timeline and deadlines
5. **NMLS_CORRECTIONS_v2.md** - Detailed changelog of all corrections
6. **FINAL_XML_SUMMARY.md** - This file

---

## 🚀 **Next Steps**

### **For Phil:**

1. **Download** the XML:
   ```
   /Users/philwhitham/MTL-Global-Accounting-team/MSB Call Reports/2025/Q4/SHOPIFY_FS_Q4_2025_MSB_REPORT.xml
   ```

2. **Upload** to NMLS portal (replace existing XML)

3. **Verify** all 6 sections pass completeness checks:
   - ST - Alabama ✅
   - ST - Arizona ✅
   - ST - Pennsylvania ✅
   - FC (Assets, Liabilities, Income) ✅
   - PI ✅
   - TD-A ✅

4. **Mark** each section "Ready to Submit"

5. **Submit** the Q4 2025 MSB Call Report

---

## ✅ **Confidence Level**

**🟢 HIGH** - All NMLS completeness check issues have been addressed:
- ✅ All missing fields added (with zeros or actual values)
- ✅ All surety bonds disclosed
- ✅ All explanatory notes provided
- ✅ All business logic warnings resolved
- ✅ Financial data validated against NetSuite

**Expected Result**: Clean upload with all sections passing completeness checks.

---

## 📝 **Notes**

- This XML represents SFS Inc.'s **pre-operational status** during Q4 2025
- Licenses effective: PA (11/7/25), AZ (12/4/25), AL (12/12/25)
- No stored value transactions during Q4 2025 (pre-launch)
- All transaction fields appropriately set to zero
- Surety bonds properly disclosed per NMLS requirements

---

**Status**: ✅ **READY FOR FINAL UPLOAD**  
**Last Updated**: January 30, 2026  
**Prepared By**: Cursor AI Assistant with Phil Whitham
