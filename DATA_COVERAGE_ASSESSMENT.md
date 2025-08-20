# MSB Call Report XML - Data Coverage Assessment

**Date**: January 2025  
**Purpose**: Analyze Shopify's current data coverage for MSB Call Report requirements  
**Status**: Initial Assessment - Ready for Engineering Team Discussion  

## Executive Summary

Based on our analysis of Shopify's data platform and MSB Call Report requirements, we have identified **strong data coverage** for most MSB activities, with **some gaps** that require engineering team discussion. Shopify's financial services data infrastructure provides a solid foundation for regulatory reporting.

## Current Data Coverage Analysis

### ✅ **Strong Coverage Areas**

#### 1. **Money Transmission Services** - EXCELLENT COVERAGE
- **Data Source**: `shopify-dw.money_products.shopify_payments_balance_transactions`
- **Coverage**: Complete transaction tracking for money transmission activities
- **Key Fields Available**:
  - Transaction amounts (USD and local currency)
  - Transaction types and statuses
  - Shop identification
  - Timestamps and processing dates
  - Transfer status and failure tracking

#### 2. **Financial Condition Data** - GOOD COVERAGE
- **Data Sources**: 
  - `shopify-dw.finance.gross_merchandise_volume`
  - `shopify-dw.money_products.banking_balance_transactions`
- **Coverage**: Transaction volumes, financial flows, balance tracking
- **Available Metrics**:
  - GMV by shop and time period
  - Payment processing volumes
  - Balance account statuses

#### 3. **Transaction Detail Tracking** - EXCELLENT COVERAGE
- **Data Sources**:
  - `shopify-dw.money_products.banking_balance_posted_transactions`
  - `shopify-dw.money_products.banking_balance_transactions`
- **Coverage**: Detailed transaction categorization and tracking
- **Key Features**:
  - Action categories (card_usage, money_movement_external, financial_features)
  - Transaction types (ACH, wire, card, internal transfers)
  - Direction tracking (inflow/outflow)
  - Status monitoring (pending, posted, void)

### 🟡 **Partial Coverage Areas**

#### 1. **State-Level Transaction Aggregation** - PARTIAL COVERAGE
- **Current**: Transaction data available by shop
- **Gap**: Need to map shops to states for regulatory reporting
- **Data Source**: `shopify-dw.accounts_and_administration` (shop location data)
- **Action Required**: Engineering team to create state-level aggregation views

#### 2. **Permissible Investments** - PARTIAL COVERAGE
- **Current**: Balance account data available
- **Gap**: Investment categorization and compliance tracking
- **Data Source**: Balance transaction data exists but needs categorization
- **Action Required**: Define investment categories and compliance rules

#### 3. **Foreign Transaction Tracking** - PARTIAL COVERAGE
- **Current**: International transaction data available
- **Gap**: Country-level aggregation for Q4 reporting
- **Data Source**: Transaction data with currency information
- **Action Required**: Create country-level aggregation views

### ❌ **Gap Areas Requiring Engineering Discussion**

#### 1. **MSB License State Mapping**
- **Requirement**: Map each transaction to states where Shopify holds MSB licenses
- **Current Gap**: No direct mapping between transactions and licensed states
- **Impact**: Critical for Section II(b) - State Transaction Detail
- **Engineering Ask**: Create state licensing mapping table/view

#### 2. **Regulatory Classification**
- **Requirement**: Categorize transactions by MSB activity type
- **Current Gap**: Transactions not classified by regulatory requirements
- **Impact**: Required for all sections of MSB Call Report
- **Engineering Ask**: Add MSB activity classification to transaction models

#### 3. **Compliance Monitoring Data**
- **Requirement**: Track compliance with MSB regulations
- **Current Gap**: No compliance monitoring or reporting data
- **Impact**: Required for regulatory oversight
- **Engineering Ask**: Implement compliance monitoring data collection

## Detailed Data Mapping

### **Section I: Financial Condition Report**

| MSB Requirement | Shopify Data Source | Coverage Status | Notes |
|-----------------|---------------------|-----------------|-------|
| Total Assets | `banking_balance_transactions` | ✅ Available | Balance account totals |
| Total Liabilities | `banking_balance_transactions` | ✅ Available | Outstanding obligations |
| Net Worth | Calculated from above | ✅ Available | Simple calculation |
| Cash & Cash Equivalents | `banking_balance_transactions` | ✅ Available | Liquid balance tracking |

### **Section II(a): Company-wide Transactions Detail**

| MSB Requirement | Shopify Data Source | Coverage Status | Notes |
|-----------------|---------------------|-----------------|-------|
| Total Transaction Volume | `shopify_payments_balance_transactions` | ✅ Available | Complete coverage |
| Transaction Count | `shopify_payments_balance_transactions` | ✅ Available | Complete coverage |
| Money Transmission Volume | `shopify_payments_balance_transactions` | ✅ Available | Filter by transaction type |
| Check Cashing Volume | `banking_balance_transactions` | 🟡 Partial | Need to identify check transactions |
| Money Order Volume | `banking_balance_transactions` | 🟡 Partial | Need to identify money order transactions |

### **Section II(b): State Transaction Detail**

| MSB Requirement | Shopify Data Source | Coverage Status | Notes |
|-----------------|---------------------|-----------------|-------|
| State-by-State Volume | `shopify_payments_balance_transactions` + shop location | 🟡 Partial | Need state mapping |
| State-by-State Count | `shopify_payments_balance_transactions` + shop location | 🟡 Partial | Need state mapping |
| State Licensing Status | Not available | ❌ Gap | Critical for compliance |

### **Section III: Permissible Investments Report**

| MSB Requirement | Shopify Data Source | Coverage Status | Notes |
|-----------------|---------------------|-----------------|-------|
| Investment Categories | `banking_balance_transactions` | 🟡 Partial | Need investment classification |
| Investment Amounts | `banking_balance_transactions` | ✅ Available | Balance data exists |
| Compliance Status | Not available | ❌ Gap | Need compliance tracking |

### **Section IV: Destination Country Detail (Q4 Only)**

| MSB Requirement | Shopify Data Source | Coverage Status | Notes |
|-----------------|---------------------|-----------------|-------|
| Foreign Transaction Volume | `shopify_payments_balance_transactions` | ✅ Available | Currency data exists |
| Foreign Transaction Count | `shopify_payments_balance_transactions` | ✅ Available | Currency data exists |
| Country-Level Aggregation | `shopify_payments_balance_transactions` | 🟡 Partial | Need country mapping |

## Engineering Team Discussion Points

### **Priority 1: Critical for Q1 2025 Reporting**

#### 1. **State Licensing Mapping**
- **Ask**: Create a mapping table between Shopify shops and states where we hold MSB licenses
- **Data Source**: Combine shop location data with MSB license status
- **Output**: View/table that maps each transaction to licensed states
- **Timeline**: Required before Q1 reporting (May 15, 2025)

#### 2. **MSB Activity Classification**
- **Ask**: Add MSB activity classification to existing transaction models
- **Categories Needed**:
  - Money transmission
  - Check cashing
  - Money orders
  - Prepaid access
  - Virtual currency
- **Implementation**: Add classification fields to transaction tables
- **Timeline**: Required before Q1 reporting

#### 3. **Regulatory Compliance Tracking**
- **Ask**: Implement data collection for MSB compliance monitoring
- **Requirements**:
  - Transaction limits monitoring
  - Suspicious activity tracking
  - Compliance rule enforcement
- **Timeline**: Required for ongoing compliance

### **Priority 2: Important for Complete Reporting**

#### 4. **Investment Categorization**
- **Ask**: Create investment classification system for permissible investments
- **Categories**: Cash, securities, government bonds, etc.
- **Implementation**: Add investment type fields to balance models
- **Timeline**: Q2 2025 reporting

#### 5. **Country-Level Aggregation**
- **Ask**: Create country-level transaction aggregation views
- **Purpose**: Support Q4 destination country reporting
- **Implementation**: Geographic aggregation of international transactions
- **Timeline**: Q4 2025 reporting

#### 6. **Enhanced Transaction Monitoring**
- **Ask**: Implement real-time transaction monitoring for MSB compliance
- **Features**:
  - Transaction limit alerts
  - Suspicious activity detection
  - Compliance rule validation
- **Timeline**: Ongoing development

## Data Quality Assessment

### **Strengths**
- **Completeness**: Transaction data is comprehensive and well-tracked
- **Accuracy**: Financial data is reconciled and validated
- **Timeliness**: Real-time transaction processing
- **Consistency**: Standardized data models across financial services

### **Areas for Improvement**
- **Classification**: Need better categorization for regulatory reporting
- **Mapping**: Need state and country mapping for compliance
- **Monitoring**: Need enhanced compliance monitoring capabilities
- **Documentation**: Need better documentation of MSB-specific data

## Recommended Next Steps

### **Immediate (Next 2 Weeks)**
1. **Schedule Engineering Team Meeting** to discuss data requirements
2. **Review MSB License State Mapping** requirements
3. **Define MSB Activity Classification** schema
4. **Assess Implementation Effort** for critical gaps

### **Short Term (Next Month)**
1. **Implement State Licensing Mapping** data model
2. **Add MSB Activity Classification** to transaction models
3. **Create Compliance Monitoring** data collection
4. **Test Data Quality** for Q1 reporting

### **Medium Term (Next Quarter)**
1. **Implement Investment Categorization** system
2. **Create Country-Level Aggregation** views
3. **Enhance Transaction Monitoring** capabilities
4. **Validate Complete Data Coverage** for all MSB requirements

## Risk Assessment

### **Low Risk** ✅
- **Data Availability**: Most required data exists in current systems
- **Data Quality**: Financial data is well-validated and reliable
- **Infrastructure**: Strong data warehouse foundation exists

### **Medium Risk** 🟡
- **State Mapping**: Need to ensure accurate state licensing mapping
- **Classification**: Need to implement proper MSB activity classification
- **Timeline**: Q1 reporting deadline is tight

### **High Risk** 🔴
- **Compliance Accuracy**: Must ensure regulatory compliance in data classification
- **Engineering Capacity**: Need engineering team bandwidth for implementation
- **Regulatory Changes**: MSB requirements may evolve

## Conclusion

Shopify has **excellent data infrastructure** for MSB Call Report requirements, with most required data already available in the data warehouse. The main gaps are in **data classification** and **regulatory mapping**, which can be addressed through focused engineering work.

**Recommendation**: Proceed with implementation, focusing on state licensing mapping and MSB activity classification as priority items. The existing data quality and infrastructure provide a strong foundation for successful regulatory reporting.

---

**Next Action**: Schedule engineering team meeting to discuss implementation requirements and timeline for Q1 2025 reporting.
