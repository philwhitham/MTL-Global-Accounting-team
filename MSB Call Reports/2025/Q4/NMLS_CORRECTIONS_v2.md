# Q4 2025 MSB Call Report - NMLS Corrections (Version 2)

**Date**: January 30, 2026  
**Reason**: NMLS completeness check requirements  
**Status**: Ready for re-upload  

---

## 🔧 **Changes Made**

### **Issue**: NMLS completeness checks showed "Values are missing for one or more highlighted fields"

### **Root Cause**: 
- Original XML only included fields relevant to stored value business
- NMLS requires **ALL transaction type fields** to be present, even if zero

---

## ✅ **Sections Updated**

### **1. Company-Wide Transactions (Msbcrta)**

**Added all transaction type fields**:

**Money Transmission**:
- TA10-TA40: All zeros (not performing money transmission)

**Payment Instruments**:
- TA70-TA80: All zeros (not issuing money orders/travelers checks)

**Stored Value**:
- TA90-TA100: Already present, kept at 0

**Check Cashing**:
- TA110-TA140: All zeros (not cashing checks)

**Currency Exchange**:
- TA150-TA170: All zeros (not exchanging currency)

**Virtual Currency**:
- TA180-TA330: All zeros (not dealing with cryptocurrency)

**Total TA fields**: 29 fields (was 2, now 29)

---

### **2. State Transactions (ST sections) - All 3 States**

**For Pennsylvania, Arizona, and Alabama**, added all transaction type fields:

**Money Transmission**:
- ST10-ST40: All zeros

**Payment Instruments**:
- ST70-ST80: All zeros

**Stored Value**:
- ST90-ST100: Already present, kept at 0

**Check Cashing**:
- ST110-ST140: All zeros (ST140 = 0.00 for percentage)

**Currency Exchange**:
- ST150-ST170: All zeros

**Virtual Currency**:
- ST180-ST330: All zeros

**Transmission Liability**:
- **ST360: Surety Bond amount** (SEE BELOW)
- **ST361: Average Daily Transmission Liability** - 0

**Total ST fields per state**: 31 fields (was 2, now 31)

---

### **3. Surety Bond Amounts Added (ST360)**

Based on surety bond spreadsheet:

| State | Field | Bond Amount | Notes |
|-------|-------|-------------|-------|
| **Pennsylvania** | ST360 | **$1,000,000** | Liberty Mutual bond placed 9/2/2025 |
| **Arizona** | ST360 | **$25,000** | Liberty Mutual bond placed 9/2/2025 |
| **Alabama** | ST360 | **$1,000,000** | Liberty Mutual bond placed 9/2/2025 |

**ST361** (ADTL) = $0 for all states (pre-operational, no outstanding liability)

---

### **4. Assets Section (Msbcrfc) - Completed**

**Added missing asset fields**:
- FC20: Due from agents - 0
- FC30: Allowance for doubtful accounts - 0
- FC40: Accounts receivable - 0
- FC50: Allowance (AR) - 0
- FC60: Inter-company receivables - 0
- FC70: Notes/other receivables - 0
- FC80: Investments - 0
- FC90: Virtual currency - 0
- FC100: Other current assets - 0

**Total FC Asset fields**: 14 fields (was 5, now 14)

---

## 📊 **Updated Field Counts**

| Section | Original | Updated | Change |
|---------|----------|---------|--------|
| **FC Assets** | 5 fields | 14 fields | +9 |
| **FC Liabilities** | 10 fields | 10 fields | No change |
| **FC Equity** | 9 fields | 9 fields | No change |
| **FC Income** | 14 fields | 14 fields | No change |
| **TA (Company)** | 2 fields | 29 fields | +27 |
| **ST (per state)** | 2 fields | 31 fields | +29 |
| **PI** | 18 fields | 18 fields | No change |
| **TDA** | Empty | Empty | No change |

**Total XML fields**: ~81 → ~186 fields

---

## ✅ **What Stays the Same**

- ✅ All financial amounts (unchanged)
- ✅ Licensed states (PA, AZ, AL only)
- ✅ NMLS ID: 2689562
- ✅ Period: Q4 2025
- ✅ Form Version: v4
- ✅ Explanatory notes (updated with bond mentions)

---

## 🎯 **Next Steps**

### **For You**:
1. **Download** the updated XML from: `MSB Call Reports/2025/Q4/SHOPIFY_FS_Q4_2025_MSB_REPORT.xml`
2. **Re-upload** to NMLS portal
3. **Run completeness checks** again on each section
4. **Should now pass** all sections!

### **Expected Results**:
- ✅ ST - Alabama: Should pass (has all ST fields + surety bond)
- ✅ ST - Arizona: Should pass (has all ST fields + surety bond)
- ✅ ST - Pennsylvania: Should pass (has all ST fields + surety bond)
- ✅ FC: Should pass (has all required asset fields)
- ✅ PI: Should pass (no changes needed)
- ✅ TD-A: Should pass (no changes needed)

---

## 📝 **Summary of Surety Bonds Reported**

**Total Surety Bonds**: $2,025,000

- Pennsylvania: $1,000,000
- Arizona: $25,000
- Alabama: $1,000,000

**Note**: These amounts are now properly disclosed in the MSB Call Report as required by NMLS.

---

## ⚠️ **If Issues Persist**

If NMLS still shows missing fields after re-upload:
1. Take screenshot of the specific error
2. Let me know which section and field
3. I'll make targeted corrections

---

**Status**: ✅ **XML Updated and Ready for Re-upload**  
**Changes**: Added ~105 fields (all with appropriate zeros or bond amounts)  
**Confidence**: 🟢 **HIGH** - Should resolve all completeness check issues
