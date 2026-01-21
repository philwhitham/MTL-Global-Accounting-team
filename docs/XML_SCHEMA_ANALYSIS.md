# MSB Call Report XML Schema - Detailed Analysis

**Date**: January 20, 2026  
**Purpose**: Comprehensive analysis of the official NMLS MSB Call Report XML schema and specifications  
**Status**: Initial Analysis Complete - Ready for Implementation  

## Executive Summary

I've reviewed all the XML specification files you provided and have a complete understanding of the NMLS MSB Call Report XML structure. This document provides a detailed breakdown of the schema, data types, and requirements.

## 📋 **Files Reviewed**

1. **`MSB Call Report XML Schema - EXTERNAL_MSBCR_2024_Q4.xml`** - Sample XML with populated data
2. **`Data Specification File - ExternalMsbcrBatchFileSchemaV4.txt`** - Complete XSD schema definition
3. **`MSBCR Data Specification v4.xlsx`** - Field descriptions and mappings (pending review)
4. **`MSB Call Report Sample Form Version 4 (clean) (2).xlsx`** - Sample form (pending review)
5. **`MSB Call Report XML Upload Specifications v4 (1).pdf`** - Complete specifications

## 🏗️ **XML Structure Overview**

### **Root Element: `<MsbcrFiling>`**

**Required Attributes:**
- `year` - Reporting year (integer, minimum 2021, 4 digits)
- `formVersion` - Must be "v4" or "V4"
- `periodType` - Must be "MSBQ1", "MSBQ2", "MSBQ3", or "MSBQ4"

**Example:**
```xml
<MsbcrFiling year="2024" formVersion="v4" periodType="MSBQ4">
```

### **Main Sections**

The XML contains six main sections, each optional:

1. **`<Msbcrfc>`** - Financial Condition (Section I)
2. **`<Msbcrta>`** - Company-Wide Transactions (Section II(a))
3. **`<Msbcrst>`** - State Transactions (Section II(b)) - Can have multiple instances
4. **`<Msbcrpi>`** - Permissible Investments (Section III)
5. **`<Msbcrtda>`** - Destination Country Detail - Company (Section IV(a))
6. **`<Msbcrtdb>`** - Destination Country Detail - State (Section IV(b)) - Can have multiple instances

## 📊 **Section I: Financial Condition (`<Msbcrfc>`)**

This section contains three subsections:

### **A. Assets**
**Fields**: FC10, FC20, FC30, FC40, FC50, FC60, FC70, FC80, FC90, FC100, FC120, FC130, FC140, FC150
**Data Type**: Dollar (signed, 13 digits)
**Notes**: FC100NOTE, FC150NOTE (ExplanatoryText, max 4000 chars)

**Likely Asset Categories:**
- FC10-FC100: Various asset types (cash, receivables, investments, etc.)
- FC120-FC150: Additional asset categories

### **B. Liabilities and Equity**
**Fields**: FC170-FC380
**Data Type**: Dollar (signed, 13 digits)
**Notes**: FC240NOTE, FC270NOTE (ExplanatoryText)

**Structure:**
- FC170-FC240: Liability categories
- FC260-FC380: Equity and additional liability items

### **C. Income Statement**
**Fields**: FC410-FC670
**Data Type**: Dollar (signed, 13 digits)
**Notes**: FC480NOTE, FC590NOTE (ExplanatoryText)

**Structure:**
- FC410-FC590: Income and expense items
- FC620-FC670: Net income calculations

### **D. Explanatory Notes**
**Field**: FCNOTE_1 (ExplanatoryText, max 4000 chars)

---

## 💰 **Section II(a): Company-Wide Transactions (`<Msbcrta>`)**

### **Transaction Fields**
**Pattern**: Alternating Count and Dollar amounts
- TA10, TA30, TA70, TA90, TA110, TA150, TA180, TA200, TA220, TA240, TA280, TA300, TA320 = **Count** (transaction counts)
- TA20, TA40, TA80, TA100, TA120, TA160, TA170, TA190, TA210, TA230, TA250, TA290, TA310, TA330 = **PositiveDollar** (amounts)

**Special Fields:**
- TA130 - PositiveDollar (likely a subtotal)
- TA140 - **Hundredth** (percentage or rate with 2 decimal places)

### **Likely Transaction Categories**
Based on the pattern, these likely represent:
- Money transmission volumes and counts
- Check cashing volumes and counts
- Money order volumes and counts
- Traveler's check volumes and counts
- Foreign currency exchange volumes and counts
- Stored value/prepaid access volumes and counts
- Virtual currency volumes and counts

---

## 🗺️ **Section II(b): State Transactions (`<Msbcrst>`)**

**Key Feature**: Can have **multiple instances** (unbounded) - one per state

**Required Attribute**: `stateCode` - Two-letter state code (AL, AK, AZ, ... WY)

### **Transaction Fields**
**Same pattern as Company-Wide:**
- ST10, ST30, ST70, ST90, ST110, ST150, ST180, ST200, ST220, ST240, ST280, ST300, ST320 = **Count**
- ST20, ST40, ST80, ST100, ST120, ST160, ST170, ST190, ST210, ST230, ST250, ST290, ST310, ST330 = **PositiveDollar**

**Special Fields:**
- ST130 - PositiveDollar (subtotal)
- ST140 - **Hundredth** (percentage)
- ST360, ST361 - PositiveDollar (additional state-specific fields)

**Example:**
```xml
<Msbcrst stateCode="CA">
    <TransactionsStateSpecificSection>
        <ST10>1000</ST10>
        <ST20>500000</ST20>
        <!-- ... -->
    </TransactionsStateSpecificSection>
</Msbcrst>
```

---

## 💼 **Section III: Permissible Investments (`<Msbcrpi>`)**

### **Investment Fields**
**All fields are PositiveDollar type:**
- PI10, PI20, PI21, PI30, PI31, PI32 - Investment categories 1-3
- PI50, PI60, PI61, PI62 - Investment categories 4-5
- PI70-PI76 - Investment category 6 with subcategories
- PI80, PI90, PI100, PI110, PI120, PI130, PI140, PI150, PI160, PI180 - Additional investment types

**Notes**: PI100NOTE, PI160NOTE (ExplanatoryText)

**Likely Investment Categories:**
- Cash and cash equivalents
- U.S. Government securities
- State and municipal securities
- Investment-grade securities
- Certificates of deposit
- Money market funds
- Other permissible investments

---

## 🌍 **Section IV(a): Destination Country Detail - Company (`<Msbcrtda>`)**

**Structure**: List of transactions by country

### **Company Transactions Item**
Can have up to **10,000 items**

**Fields per item:**
- TDA - Country code (ShortText, max 150 chars, ISO country code)
- TDA_1 - Transaction amount (PositiveDollar)
- TDA_2 - Transaction count (Count)

**Example:**
```xml
<Msbcrtda>
    <ListSectionOfCompanyTransactionsItem>
        <DetailItemList>
            <CompanyTransactionsItem>
                <TDA>CA</TDA>
                <TDA_1>100000</TDA_1>
                <TDA_2>50</TDA_2>
            </CompanyTransactionsItem>
            <CompanyTransactionsItem>
                <TDA>GB</TDA>
                <TDA_1>75000</TDA_1>
                <TDA_2>35</TDA_2>
            </CompanyTransactionsItem>
        </DetailItemList>
    </ListSectionOfCompanyTransactionsItem>
</Msbcrtda>
```

---

## 🌍 **Section IV(b): Destination Country Detail - State (`<Msbcrtdb>`)**

**Key Feature**: Can have **multiple instances** (unbounded) - one per state

**Required Attribute**: `stateCode` - Two-letter state code

**Same structure as Section IV(a) but for state-specific foreign transactions**

---

## 📏 **Data Types Defined**

### **1. PositiveDollar**
- Type: Long integer
- Total Digits: 13
- Fraction Digits: 0 (no decimals)
- Min Value: 0
- **Usage**: Transaction amounts, investment amounts (must be positive)

### **2. Dollar**
- Type: Long integer
- Total Digits: 13
- Fraction Digits: 0 (no decimals)
- **No minimum** (can be negative)
- **Usage**: Financial condition items (assets, liabilities, income, expenses)

### **3. Count**
- Type: Long integer
- Total Digits: 13
- Fraction Digits: 0
- Min Value: 0
- **Usage**: Transaction counts

### **4. Hundredth**
- Type: Decimal
- Total Digits: 13
- **Pattern**: `\d+\.\d{2}` (exactly 2 decimal places)
- **Usage**: Percentages and rates

### **5. ShortText**
- Type: String
- Max Length: 150 characters
- **Pattern**: `[^<>%]*` (no <, >, or % characters)
- **Usage**: Country codes, short descriptions

### **6. ExplanatoryText**
- Type: String
- Max Length: 4000 characters
- **Pattern**: `[^<>%]*` (no <, >, or % characters)
- **Usage**: Explanatory notes

---

## ✅ **Validation Rules**

### **Required Fields**
- Root element must have year, formVersion, periodType attributes
- formVersion must be "v4" or "V4"
- periodType must be one of: MSBQ1, MSBQ2, MSBQ3, MSBQ4
- year must be 2021 or later (4 digits)
- State elements must have stateCode attribute
- State codes must be valid US state/territory codes

### **Optional Fields**
- **ALL data fields are optional** (minOccurs="0")
- **ALL sections are optional** (minOccurs="0")
- This allows for partial updates and amendments

### **Cardinality**
- Msbcrfc: 0-1 instance
- Msbcrta: 0-1 instance
- **Msbcrst: 0-unbounded instances** (one per state)
- Msbcrpi: 0-1 instance
- Msbcrtda: 0-1 instance
- **Msbcrtdb: 0-unbounded instances** (one per state)

---

## 🎯 **Implementation Requirements**

### **Immediate Next Steps**

1. **Map Field Numbers to Descriptions**
   - Need to review the Excel files to understand what each field number represents
   - Create a complete field mapping document
   - Example: FC10 = "Cash and due from banks" (hypothetical)

2. **Data Source Mapping**
   - Map each XML field to Shopify data sources:
     - NetSuite for Financial Condition (FC fields)
     - Data warehouse for Transaction Activity (TA/ST fields)
     - Balance data for Permissible Investments (PI fields)
     - Transaction data for Destination Country (TDA/TDB fields)

3. **Update XML Generator**
   - Rewrite generator to match exact schema structure
   - Implement proper data type validation
   - Add state code handling for multiple state instances
   - Implement country list handling for TDA/TDB sections

4. **Data Extraction Queries**
   - Create NetSuite queries for FC fields
   - Create BigQuery queries for TA/ST fields
   - Create aggregation logic for country-level data

---

## 🔍 **Key Observations**

### **Strengths of the Schema**
✅ Well-structured with clear sections
✅ All fields optional (flexible for partial updates)
✅ Strong data type validation
✅ Supports multiple states and countries
✅ Allows explanatory notes throughout

### **Complexity Areas**
🟡 Need to understand exact field mappings (FC10, TA10, etc.)
🟡 State-level reporting requires accurate state mapping
🟡 Country-level reporting requires currency conversion
🟡 Multiple instances of state sections require iteration logic

### **Data Availability Assessment**
✅ **Financial Condition (FC)**: NetSuite MCP now available!
✅ **Company Transactions (TA)**: Data warehouse has transaction data
🟡 **State Transactions (ST)**: Need state mapping logic
🟡 **Permissible Investments (PI)**: Need investment classification
🟡 **Destination Country (TDA/TDB)**: Need country-level aggregation

---

## 📝 **Questions for Follow-Up**

1. **Field Mappings**: What do the specific field numbers represent?
   - Need to review: `MSBCR Data Specification v4.xlsx`
   - Need to review: `MSB Call Report Sample Form Version 4 (clean) (2).xlsx`

2. **Shopify's MSB Activities**: Which transaction types does Shopify perform?
   - Money transmission? ✓ (likely yes - Shopify Balance)
   - Check cashing? (need to confirm)
   - Money orders? (need to confirm)
   - Stored value/prepaid? (need to confirm)
   - Virtual currency? (need to confirm)

3. **State Licensing**: Which states require reporting?
   - Need list of states where Shopify holds MSB licenses
   - This determines how many `<Msbcrst>` sections to create

4. **Quarterly vs Annual Reporting**: 
   - Sections IV(a) and IV(b) are Q4 only (annual data)
   - Confirm this with the team

---

## 🚀 **Next Actions**

### **Immediate (Today)**
1. ✅ Analyze XML schema structure - **COMPLETE**
2. ⏳ Review Excel field mapping files
3. ⏳ Create complete field mapping document
4. ⏳ Update TODO list with specific tasks

### **Short Term (This Week)**
1. Map each XML field to description
2. Map each field to Shopify data source
3. Test NetSuite MCP for FC field data
4. Create sample data extraction queries
5. Update XML generator with correct schema

### **Medium Term (Next 2 Weeks)**
1. Implement complete data extraction
2. Test XML generation with real data
3. Validate against XSD schema
4. Prepare for Q1 2025 reporting (due May 15)

---

## 💡 **Recommendations**

1. **Prioritize NetSuite Integration**: With NetSuite MCP now available, focus on extracting Financial Condition data first (Section I)

2. **Create Field Mapping Master Document**: Review the Excel files to create a comprehensive mapping of all field codes to their descriptions

3. **Define Shopify's MSB Activities**: Work with compliance/legal team to confirm which MSB activities Shopify performs

4. **Build State Licensing Table**: Create a reference table of states where Shopify holds MSB licenses

5. **Test Early, Test Often**: Generate sample XML files and validate against the XSD schema frequently

---

**Status**: Ready to proceed with detailed field mapping and data extraction implementation!
