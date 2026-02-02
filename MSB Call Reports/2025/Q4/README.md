# Q4 2025 MSB Call Report

**Reporting Entity**: Shopify Financial Services Inc. (NMLS ID: 2689562)  
**Reporting Period**: Q4 2025 (October 1 - December 31, 2025)  
**Report Status**: ✅ **SUBMITTED** (January 30, 2026)  
**Submission Deadline**: February 15, 2026 (45 days after quarter-end)  

---

## 📋 **Report Summary**

This is Shopify Financial Services Inc.'s **first MSB Call Report** filed with the NMLS (Nationwide Multistate Licensing System & Registry).

### **Key Highlights**

- **Pre-Operational Status**: SFS Inc. had no stored value transactions during Q4 2025
- **Licensed States**: Pennsylvania, Arizona, Alabama (licenses effective November-December 2025)
- **Total Assets**: $2,000,000
- **Total Liabilities**: $32,588
- **Shareholders' Equity**: $1,967,412
- **Surety Bonds**: $2,025,000 (PA: $1M, AZ: $25K, AL: $1M)

---

## 📄 **Files in This Folder**

### **1. SHOPIFY_FS_Q4_2025_MSB_REPORT.xml**
**Purpose**: The final XML file submitted to NMLS  
**Status**: ✅ Submitted and accepted  
**Contents**:
- Section I: Financial Condition (FC) - Balance sheet, income statement, equity
- Section II(a): Company-Wide Transactions (TA) - All transaction types (zeros for pre-operational)
- Section II(b): State Transactions (ST) - Separate sections for PA, AZ, AL with surety bond disclosures
- Section III: Permissible Investments (PI) - Investment holdings
- Section IV(a): Transaction Destination (TD-A) - Destination country details (empty for pre-operational)

**Key Features**:
- All 186+ fields properly populated (zeros or actual values)
- Surety bonds disclosed for all 3 states
- Explanatory notes for pre-operational status
- FC240NOTE explaining accrued liabilities (72% ratio)

---

### **2. Q4_2025_REPORT_SUMMARY.md**
**Purpose**: Human-readable summary of the Q4 2025 report  
**Read this if**: You want a quick overview of the financials and filing details  
**Contents**:
- Financial highlights (balance sheet, P&L, equity)
- Transaction activity (zeros for pre-operational)
- Licensed states and effective dates
- Surety bond details
- Pre-submission checklist status

---

### **3. PRE_SUBMISSION_VALIDATION.md**
**Purpose**: Comprehensive validation report covering all 22 pre-submission checklist items  
**Read this if**: You want to understand the validation steps performed before submission  
**Contents**:
- Level 1: XSD Schema Validation (passed)
- Level 2: Field Completeness Check (passed)
- Level 3: Data Integrity Check (passed)
- Level 4: Business Logic Validation (passed)
- State-specific validation for PA, AZ, AL
- Technical validation results

---

### **4. SUBMISSION_TIMELINE.md**
**Purpose**: Detailed submission timeline with 9-day buffer period  
**Read this if**: You want to understand the submission process and deadlines  
**Contents**:
- Quarter-end date (December 31, 2025)
- NMLS portal deadline (February 15, 2026)
- Internal review timeline (January 20-30, 2026)
- Buffer period built in for quality assurance

---

### **5. NMLS_CORRECTIONS_v2.md**
**Purpose**: Detailed changelog of all corrections made after initial NMLS upload  
**Read this if**: You want to understand what issues were found and how they were fixed  
**Contents**:
- Root cause analysis (missing transaction type fields)
- All sections updated (TA, ST, FC)
- Surety bond disclosures added
- Field count changes (~81 fields → ~186 fields)
- Step-by-step corrections made

---

### **6. FINAL_XML_SUMMARY.md**
**Purpose**: Comprehensive summary of the final XML ready for upload  
**Read this if**: You want a complete reference of all changes and final report statistics  
**Contents**:
- All changes made based on NMLS feedback
- Surety bond amounts by state
- Final XML statistics (186 fields)
- What passed without changes (PI, TD-A)
- Next steps for upload and submission
- Confidence assessment

---

## 🔄 **What Happened: The Story**

### **Phase 1: Initial Report Generation** (January 20-25, 2026)
1. ✅ Extracted Q4 2025 financial data from NetSuite
2. ✅ Generated initial XML with pre-operational data (zeros for transactions)
3. ✅ Created human-readable summary and validation reports
4. ✅ Uploaded XML to NMLS portal

### **Phase 2: NMLS Completeness Checks** (January 30, 2026)
1. ⚠️ NMLS flagged missing fields across multiple sections
2. 🔍 Analyzed completeness check PDFs for all 6 sections
3. 🛠️ Identified root cause: XML only included relevant fields, but NMLS requires ALL fields

**Issues Found**:
- **ST sections** (PA, AZ, AL): Missing ST10-ST40, ST360-361
- **TA section**: Missing TA10-TA330 (only had TA90-TA100)
- **FC Assets**: Missing FC20-FC100
- **FC Liabilities**: Missing FC240NOTE (required due to 72% ratio)

### **Phase 3: Corrections & Re-Upload** (January 30, 2026)
1. ✅ Added all missing transaction type fields (zeros for non-applicable)
2. ✅ Added surety bond amounts (ST360) for all 3 states
3. ✅ Added FC240NOTE explaining accrued liabilities
4. ✅ Completed FC Assets section with all required fields
5. ✅ Re-uploaded corrected XML to NMLS portal

### **Phase 4: Final Submission** (January 30, 2026)
1. ✅ All 6 sections passed completeness checks
2. ✅ Marked all sections "Ready to Submit"
3. ✅ **SUBMITTED** Q4 2025 MSB Call Report
4. 🎉 **SUCCESS**: First quarterly report filed on time!

---

## 📊 **Data Sources**

### **Financial Data (Section I: FC, Section III: PI)**
- **Source**: NetSuite (via NetSuite MCP)
- **Date**: December 31, 2025 (quarter-end balances)
- **Validation**: Confirmed accurate by Accounting team

**Key NetSuite Accounts**:
- Cash: $2,000,000
- Inter-company payables: $9,128
- Other current liabilities: $23,460 (accrued professional fees + surety bond costs)
- Common stock: $10
- Paid-in capital: $1,999,990
- Retained earnings: $(32,588)

### **Transaction Data (Section II: TA, ST)**
- **Source**: N/A (pre-operational, no transactions)
- **Values**: All transaction fields set to 0
- **Explanatory Notes**: Added to explain pre-operational status

### **Surety Bond Data (ST360)**
- **Source**: Google Sheets "Surety Bond Status as of 10/4/25"
- **Provider**: Liberty Mutual (via Marsh USA)
- **Placed Date**: September 2, 2025

---

## 🔑 **Key Learnings for Future Reports**

### **1. NMLS Requires ALL Fields**
Even if you're only conducting stored value business, you must include fields for:
- Money transmission (TA10-TA60, ST10-ST60)
- Payment instruments (TA70-TA80, ST70-ST80)
- Check cashing (TA110-TA140, ST110-ST140)
- Currency exchange (TA150-TA170, ST150-ST170)
- Virtual currency (TA180-TA350, ST180-ST350)

**Solution**: Set all non-applicable fields to zero, don't omit them.

---

### **2. Surety Bonds Must Be Disclosed**
Even though surety bonds are part of the licensing application, they must be reported in the MSB Call Report.

**Field**: ST360 (per state)  
**Frequency**: Every quarter (as long as bond is active)

---

### **3. Explanatory Notes Are Critical**
When ratios exceed thresholds (e.g., FC240 > 20% of FC250), explanatory notes are **required**.

**Our Example**: FC240 = $23,460 (72% of Total Current Liabilities)  
**Note Required**: FC240NOTE explaining the nature of accrued liabilities

---

### **4. State-Level Reporting**
Each licensed state requires its own `<Msbcrst>` section with all ST fields, even if transaction activity is zero.

**Q4 2025**: PA, AZ, AL (3 sections)  
**Future Quarters**: Will expand as more licenses become effective

---

## 🚀 **Next Quarter: Q1 2026**

### **What Will Change**

**Q1 2026 Report** (due May 15, 2026):
- ✅ **Likely to have real transaction data** (Shop Dollars launch expected)
- ✅ **TA90/TA100**: Will show actual purchase counts and amounts
- ✅ **ST90/ST100**: Will show state-level transaction activity
- ✅ **FC220**: Will show outstanding stored value liability
- ✅ **FC430**: Will show stored value fee income
- ✅ **PI fields**: Will show where Shop Dollars funds are invested

### **Action Items for Q1 2026**

1. **Product Team**: Ensure transaction data capture per `PRODUCT_TEAM_DATA_REQUIREMENTS.md`
2. **Data Engineering**: Build quarterly aggregation queries (TA90/TA100, ST90/ST100)
3. **Accounting**: Monitor outstanding stored value liability (FC220) monthly
4. **Compliance**: Confirm all state licenses are active and up-to-date

---

## 📞 **Questions or Issues?**

If you have questions about this report or need access to supporting documentation:

**Contact**: Phil Whitham (Global Accounting Team)  
**GitHub**: [MTL-Global-Accounting-team](https://github.com/philwhitham/MTL-Global-Accounting-team)  
**Reference Docs**: See `/docs` folder for detailed mappings and requirements

---

## 📚 **Related Documentation**

For more context, see the following documents in the main `/docs` folder:

1. **`SHOPIFY_STORED_VALUE_MAPPING.md`** - Complete MSB field mapping for Shop Dollars
2. **`SHOPIFY_FS_REFERENCE_DATA.md`** - SFS Inc. legal entity details, NMLS ID, licensed states
3. **`BUSINESS_PLAN_ANALYSIS.md`** - Shop Dollars business plan and funds flow
4. **`XML_SCHEMA_ANALYSIS.md`** - NMLS XML schema and validation rules
5. **`DATA_COVERAGE_ASSESSMENT.md`** - Shopify data platform capabilities vs. MSB requirements
6. **`PRODUCT_TEAM_DATA_REQUIREMENTS.md`** - Data capture requirements for product teams

---

**Last Updated**: January 30, 2026  
**Report Status**: ✅ SUBMITTED  
**Next Report Due**: Q1 2026 (by May 15, 2026)
