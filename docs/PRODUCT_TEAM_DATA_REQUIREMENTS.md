# MTL Stored Value - Product Team Data Requirements

**Audience**: Product & Engineering Teams Building Shop Dollars (Stored Value)  
**Purpose**: Define data capture requirements for MSB Call Report regulatory compliance  
**Date**: January 30, 2026  
**Status**: Required for Q1 2026 Launch  

---

## 🎯 **Executive Summary**

### **Why This Matters**

Shopify Financial Services Inc. (SFS Inc.) holds Money Transmitter Licenses (MTL) in multiple states. As a licensed entity offering **stored value** (Shop Dollars), we are **legally required** to file quarterly **MSB Call Reports** with the NMLS (Nationwide Multistate Licensing System & Registry).

**These reports are due 45 days after quarter-end** and require specific transactional data that MUST be captured at the point of transaction.

**Failure to capture this data = inability to file regulatory reports = potential license suspension/revocation.**

---

## 🔴 **CRITICAL: What Product Teams MUST Build**

### **The 3 Data Categories**

Your product flows must capture data for:

1. **Financial Accounting** (captured via NetSuite integration)
2. **Transaction Activity** (captured in your product database/logs)
3. **State-Level Tracking** (captured for each customer transaction)

**This document focuses on #2 and #3** - what YOUR product must capture.

---

## 📊 **Section 1: Transaction-Level Data Capture**

### **1.1 Every Shop Dollars Purchase (Issuance)**

When a user **purchases/loads Shop Dollars**, you MUST capture:

| Data Field | Description | Example | Regulatory Use |
|------------|-------------|---------|----------------|
| **transaction_id** | Unique identifier | `sd_txn_abc123` | Audit trail |
| **user_id** | Shopify user ID | `user_123456` | Customer tracking |
| **transaction_type** | Type of transaction | `PURCHASE`, `LOAD`, `ISSUANCE` | TA90/ST90 counting |
| **transaction_timestamp** | ISO 8601 timestamp (UTC) | `2026-03-15T14:30:00Z` | Quarter allocation |
| **amount_usd** | Dollar amount purchased | `50.00` | TA100/ST100 summing |
| **currency** | Currency code | `USD` | Currency validation |
| **user_state** | User's U.S. state (2-letter) | `CA`, `NY`, `TX` | ST90/ST100 state reporting |
| **user_country** | User's country code (ISO 3166-1 alpha-2) | `US`, `CA`, `GB` | International tracking |
| **payment_method** | How user paid | `credit_card`, `debit_card`, `bank_transfer` | Fraud/audit |
| **status** | Transaction status | `completed`, `pending`, `failed` | Only count completed |
| **shop_dollars_balance_after** | User's Shop $ balance after txn | `75.50` | Balance validation |

#### **🚨 State Field Requirements**

**CRITICAL**: `user_state` MUST be:
- ✅ **Captured at time of purchase** (not inferred later)
- ✅ **2-letter U.S. state code** (e.g., `CA`, `NY`, `TX`)
- ✅ **Validated against licensed states** (we only operate where licensed)
- ✅ **Not null for U.S. users** (required for state reporting)

**Question for Product**: How are you determining user state?
- ☐ Billing address?
- ☐ Shipping address?
- ☐ IP geolocation?
- ☐ User-selected during signup?

**ACTION**: Confirm with Legal/Compliance which state definition to use.

---

### **1.2 Every Shop Dollars Redemption (Usage)**

When a user **spends/redeems Shop Dollars**, you SHOULD capture (for audit purposes):

| Data Field | Description | Example | Regulatory Use |
|------------|-------------|---------|----------------|
| **redemption_id** | Unique identifier | `sd_redeem_xyz789` | Audit trail |
| **user_id** | Shopify user ID | `user_123456` | Customer tracking |
| **transaction_type** | Type of transaction | `REDEMPTION`, `SPEND`, `PAYMENT` | Usage tracking |
| **redemption_timestamp** | ISO 8601 timestamp (UTC) | `2026-03-20T10:15:00Z` | Quarter allocation |
| **amount_usd** | Dollar amount redeemed | `25.00` | Usage analytics |
| **order_id** | Associated Shopify order | `order_456789` | Audit linkage |
| **merchant_id** | Merchant where spent | `merchant_789` | Destination tracking |
| **merchant_country** | Merchant's country | `US`, `CA`, `GB` | TDA reporting (if applicable) |
| **user_state** | User's U.S. state | `CA` | State-level usage tracking |
| **shop_dollars_balance_after** | User's Shop $ balance after | `50.50` | Balance reconciliation |

**Note**: Redemptions are NOT currently required for MSB Call Reports, but capturing this data:
1. Enables balance reconciliation
2. Provides audit trail
3. May be required by future regulations
4. Supports product analytics

---

### **1.3 Shop Dollars Refunds/Reversals**

When Shop Dollars are **refunded or reversed**, you MUST capture:

| Data Field | Description | Example | Regulatory Use |
|------------|-------------|---------|----------------|
| **refund_id** | Unique identifier | `sd_refund_qwe456` | Audit trail |
| **original_transaction_id** | Link to original purchase | `sd_txn_abc123` | Reversal tracking |
| **refund_timestamp** | ISO 8601 timestamp (UTC) | `2026-03-18T09:00:00Z` | Quarter allocation |
| **refund_amount_usd** | Dollar amount refunded | `-50.00` | Net calculation |
| **refund_reason** | Why refunded | `user_request`, `fraud`, `error` | Audit/compliance |
| **user_state** | User's U.S. state | `CA` | State-level adjustment |

**Important**: Refunds may **reduce** TA90/TA100 and ST90/ST100 counts if they occur in the same quarter as the original purchase.

**Question for Product**: How are refunds handled?
- ☐ Instant reversal (same day)?
- ☐ Delayed reversal (next day+)?
- ☐ Credit to Shop Dollars vs. original payment method?

---

### **1.4 Expired/Forfeited Shop Dollars**

If Shop Dollars can **expire or be forfeited**, you MUST capture:

| Data Field | Description | Example | Regulatory Use |
|------------|-------------|---------|----------------|
| **expiration_id** | Unique identifier | `sd_expire_rst789` | Audit trail |
| **user_id** | Shopify user ID | `user_123456` | Customer tracking |
| **expiration_timestamp** | When expired | `2026-12-31T23:59:59Z` | Quarter allocation |
| **expired_amount_usd** | Dollar amount expired | `10.00` | Liability reduction |
| **expiration_reason** | Why expired | `inactivity`, `policy_violation` | Audit/compliance |
| **user_state** | User's U.S. state | `CA` | State-level tracking |

**Question for Product**: Do Shop Dollars expire?
- ☐ Yes, after XX months of inactivity
- ☐ Yes, on a fixed date
- ☐ No, they never expire

**Note**: Some states prohibit expiration of stored value. Confirm legal requirements.

---

## 📊 **Section 2: Aggregation Requirements (Quarterly Reporting)**

### **2.1 Company-Wide Aggregations (TA Fields)**

For **each quarter**, your system MUST be able to generate:

| Field Code | MSB Report Field | SQL-Like Query | Notes |
|------------|------------------|----------------|-------|
| **TA90** | Total # of stored value transactions | `SELECT COUNT(*) FROM shop_dollars_transactions WHERE transaction_type = 'PURCHASE' AND status = 'completed' AND transaction_timestamp BETWEEN quarter_start AND quarter_end` | Count only completed purchases |
| **TA100** | Total $ amount of stored value transactions | `SELECT SUM(amount_usd) FROM shop_dollars_transactions WHERE transaction_type = 'PURCHASE' AND status = 'completed' AND transaction_timestamp BETWEEN quarter_start AND quarter_end` | Sum only completed purchases |

**Important**:
- ✅ Only count **completed/successful** transactions
- ✅ Only count **purchases/issuances** (not redemptions)
- ✅ Use **transaction timestamp** to allocate to correct quarter
- ✅ Sum in **USD** (convert if multi-currency)

---

### **2.2 State-Level Aggregations (ST Fields)**

For **each licensed state** in **each quarter**, your system MUST be able to generate:

| Field Code | MSB Report Field | SQL-Like Query | Notes |
|------------|------------------|----------------|-------|
| **ST90** | # of stored value transactions in-state | `SELECT COUNT(*) FROM shop_dollars_transactions WHERE transaction_type = 'PURCHASE' AND status = 'completed' AND user_state = 'CA' AND transaction_timestamp BETWEEN quarter_start AND quarter_end` | Replace 'CA' with each state |
| **ST100** | $ amount of stored value transactions in-state | `SELECT SUM(amount_usd) FROM shop_dollars_transactions WHERE transaction_type = 'PURCHASE' AND status = 'completed' AND user_state = 'CA' AND transaction_timestamp BETWEEN quarter_start AND quarter_end` | Replace 'CA' with each state |

**Critical**: 
- ✅ Must report **separately for each licensed state**
- ✅ States with **zero activity** still need to be reported (ST90=0, ST100=0)
- ✅ User state determined at **time of purchase** (not at report time)

**Current Licensed States** (as of Q4 2025):
- Pennsylvania (PA)
- Arizona (AZ)
- Alabama (AL)

**Upcoming States** (license applications in progress):
- TBD (will be provided by Compliance team)

---

### **2.3 Destination Country Aggregations (TDA Fields - IF APPLICABLE)**

**Only required if Shop Dollars can be redeemed with international merchants.**

**Question for Product**: Can users spend Shop Dollars at merchants outside the U.S.?
- ☐ Yes → TDA reporting required
- ☐ No → TDA reporting NOT required

If YES, for **each destination country** in **each quarter**, your system MUST generate:

| Field Code | MSB Report Field | SQL-Like Query | Notes |
|------------|------------------|----------------|-------|
| **TDA** | Destination country code | `SELECT DISTINCT merchant_country FROM shop_dollars_redemptions WHERE redemption_timestamp BETWEEN quarter_start AND quarter_end` | ISO 3166-1 alpha-2 |
| **TDA_1** | $ amount to this country | `SELECT SUM(amount_usd) FROM shop_dollars_redemptions WHERE merchant_country = 'CA' AND redemption_timestamp BETWEEN quarter_start AND quarter_end` | Replace 'CA' with each country |
| **TDA_2** | # of transactions to this country | `SELECT COUNT(*) FROM shop_dollars_redemptions WHERE merchant_country = 'CA' AND redemption_timestamp BETWEEN quarter_start AND quarter_end` | Replace 'CA' with each country |

---

## ✅ **Section 3: Data Quality & Validation Requirements**

### **3.1 Required Field Validation**

**At transaction capture time**, validate:

| Field | Validation Rule | Error Handling |
|-------|----------------|----------------|
| **transaction_id** | Must be unique, not null | Reject transaction |
| **user_id** | Must exist in user table | Reject transaction |
| **amount_usd** | Must be > 0, numeric, max 2 decimals | Reject transaction |
| **user_state** | Must be 2-letter U.S. state code OR null (if non-U.S.) | Reject if U.S. user with null state |
| **transaction_timestamp** | Must be valid ISO 8601 UTC timestamp | Reject transaction |
| **status** | Must be one of: `completed`, `pending`, `failed`, `refunded` | Reject transaction |
| **currency** | Must be `USD` (or supported currency) | Reject if unsupported |

---

### **3.2 State Code Validation**

Valid U.S. state codes (for `user_state` field):

```
AL, AK, AZ, AR, CA, CO, CT, DE, FL, GA, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MA, MI, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, OH, OK, OR, PA, RI, SC, SD, TN, TX, UT, VT, VA, WA, WV, WI, WY, DC
```

**Action**: Implement state code validation in your transaction processing.

---

### **3.3 Data Integrity Checks**

**Daily/Weekly checks** to run:

1. **Orphaned Transactions**: Ensure all transaction IDs link to valid users
2. **Balance Reconciliation**: Sum of all purchases - redemptions - refunds = total outstanding liability
3. **Null State Audit**: Flag any U.S. users with null `user_state`
4. **Duplicate Transactions**: Check for duplicate transaction IDs
5. **Timestamp Validation**: Ensure no future-dated transactions
6. **Currency Consistency**: Ensure all amounts in USD (or properly converted)

---

## 🗺️ **Section 4: State-Level Tracking Requirements**

### **4.1 Why State Tracking is Critical**

MSB Call Reports require **separate reporting for each state** where we're licensed. This means:

- ✅ We must track **which state each customer is in** at time of purchase
- ✅ We must aggregate **transactions by state** every quarter
- ✅ We must report **states with zero activity** (can't omit)

**Failure to capture state = inability to file state reports = regulatory violation.**

---

### **4.2 State Determination Logic**

**Question for Product Team**: Which address do we use to determine user state?

**Options**:
1. **Billing Address** (most common for financial services)
2. **Shipping Address** (may differ from billing)
3. **IP Geolocation** (unreliable, users travel/VPN)
4. **User Profile Address** (if user manually enters)

**Recommendation**: Use **billing address** as primary, with fallback logic:
1. If billing address exists → use billing state
2. Else if shipping address exists → use shipping state
3. Else if user profile address exists → use profile state
4. Else → **flag as ERROR** (must have state for U.S. users)

**ACTION**: Confirm with Legal/Compliance which address to use.

---

### **4.3 Non-U.S. Users**

**Question for Product**: Can non-U.S. users purchase Shop Dollars?
- ☐ Yes, from any country
- ☐ Yes, but only from Canada
- ☐ No, U.S. only

If YES:
- ✅ `user_state` can be NULL for non-U.S. users
- ✅ `user_country` must be populated (ISO 3166-1 alpha-2)
- ✅ Non-U.S. transactions do NOT count toward state reporting (ST90/ST100)
- ✅ Non-U.S. transactions DO count toward company-wide reporting (TA90/TA100)

---

## 🔧 **Section 5: Technical Implementation Guidance**

### **5.1 Database Schema Recommendations**

**Table: `shop_dollars_transactions`**

```sql
CREATE TABLE shop_dollars_transactions (
  -- Primary Key
  transaction_id VARCHAR(255) PRIMARY KEY,
  
  -- User & Transaction Details
  user_id VARCHAR(255) NOT NULL,
  transaction_type VARCHAR(50) NOT NULL, -- 'PURCHASE', 'REDEMPTION', 'REFUND', 'EXPIRATION'
  transaction_timestamp TIMESTAMP NOT NULL,
  
  -- Financial Details
  amount_usd DECIMAL(15, 2) NOT NULL,
  currency VARCHAR(3) NOT NULL DEFAULT 'USD',
  
  -- Geographic Details
  user_state VARCHAR(2), -- NULL allowed for non-U.S.
  user_country VARCHAR(2) NOT NULL, -- ISO 3166-1 alpha-2
  
  -- Transaction Metadata
  status VARCHAR(50) NOT NULL, -- 'completed', 'pending', 'failed', 'refunded'
  payment_method VARCHAR(100),
  
  -- Balance Tracking
  shop_dollars_balance_before DECIMAL(15, 2),
  shop_dollars_balance_after DECIMAL(15, 2),
  
  -- Redemption Details (if applicable)
  order_id VARCHAR(255), -- For redemptions
  merchant_id VARCHAR(255), -- For redemptions
  merchant_country VARCHAR(2), -- For TDA reporting
  
  -- Refund Details (if applicable)
  original_transaction_id VARCHAR(255), -- For refunds
  refund_reason VARCHAR(255), -- For refunds
  
  -- Audit Trail
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  
  -- Indexes for Performance
  INDEX idx_user_id (user_id),
  INDEX idx_transaction_type (transaction_type),
  INDEX idx_transaction_timestamp (transaction_timestamp),
  INDEX idx_user_state (user_state),
  INDEX idx_status (status),
  INDEX idx_quarter (transaction_timestamp, transaction_type, status) -- For quarterly reporting
);
```

---

### **5.2 Quarterly Reporting Queries**

**Query 1: Company-Wide Transactions (TA90, TA100)**

```sql
-- TA90: Total # of stored value transactions
SELECT COUNT(*) AS TA90
FROM shop_dollars_transactions
WHERE transaction_type = 'PURCHASE'
  AND status = 'completed'
  AND transaction_timestamp >= '2026-01-01 00:00:00'
  AND transaction_timestamp < '2026-04-01 00:00:00';

-- TA100: Total $ amount of stored value transactions
SELECT SUM(amount_usd) AS TA100
FROM shop_dollars_transactions
WHERE transaction_type = 'PURCHASE'
  AND status = 'completed'
  AND transaction_timestamp >= '2026-01-01 00:00:00'
  AND transaction_timestamp < '2026-04-01 00:00:00';
```

**Query 2: State-Level Transactions (ST90, ST100)**

```sql
-- ST90/ST100: By state
SELECT 
  user_state,
  COUNT(*) AS ST90,
  SUM(amount_usd) AS ST100
FROM shop_dollars_transactions
WHERE transaction_type = 'PURCHASE'
  AND status = 'completed'
  AND user_country = 'US' -- Only U.S. transactions
  AND user_state IS NOT NULL
  AND transaction_timestamp >= '2026-01-01 00:00:00'
  AND transaction_timestamp < '2026-04-01 00:00:00'
GROUP BY user_state
ORDER BY user_state;
```

**Query 3: Destination Country (TDA, IF APPLICABLE)**

```sql
-- TDA: Destination countries (if redemptions tracked)
SELECT 
  merchant_country AS TDA,
  SUM(amount_usd) AS TDA_1,
  COUNT(*) AS TDA_2
FROM shop_dollars_redemptions
WHERE status = 'completed'
  AND merchant_country IS NOT NULL
  AND redemption_timestamp >= '2026-01-01 00:00:00'
  AND redemption_timestamp < '2026-04-01 00:00:00'
GROUP BY merchant_country
ORDER BY merchant_country;
```

---

### **5.3 Data Pipeline Considerations**

**Option 1: Real-Time Transaction Logging**
- ✅ Capture all fields at transaction time
- ✅ Write to `shop_dollars_transactions` table immediately
- ✅ Run quarterly aggregation queries at report time

**Option 2: Batch ETL (Not Recommended)**
- ⚠️ Extract transaction data from production DB
- ⚠️ Transform and load into reporting DB
- ⚠️ Risk: Missing fields, incomplete data

**Recommendation**: Option 1 (real-time) for compliance.

---

### **5.4 Reporting API/Dashboard**

**Recommendation**: Build an internal API or dashboard that:
1. Accepts quarter start/end dates as input
2. Runs aggregation queries
3. Returns TA90/TA100 and ST90/ST100 for all licensed states
4. Exports to CSV or JSON for XML generation

**Example API Endpoint**:
```
GET /api/msb-report?quarter=2026-Q1

Response:
{
  "quarter": "2026-Q1",
  "company_wide": {
    "TA90": 12345,
    "TA100": 567890.50
  },
  "by_state": {
    "PA": { "ST90": 1234, "ST100": 56789.00 },
    "AZ": { "ST90": 2345, "ST100": 67890.00 },
    "AL": { "ST90": 3456, "ST100": 78901.00 }
  }
}
```

---

## ✅ **Section 6: Testing & Validation Checklist**

### **6.1 Pre-Launch Testing**

Before Shop Dollars launches, validate:

- [ ] **Transaction capture working**: Create test purchase, verify all fields captured
- [ ] **State validation working**: Try invalid state code, ensure rejection
- [ ] **NULL state handling**: Try purchase without state, ensure proper error
- [ ] **Timestamp accuracy**: Verify timestamp is UTC and accurate
- [ ] **Status tracking**: Verify completed/pending/failed statuses work
- [ ] **Refund handling**: Create refund, verify negative amount or reversal logic
- [ ] **Balance reconciliation**: Sum purchases - redemptions = liability balance

---

### **6.2 Post-Launch Monitoring**

After Shop Dollars launches, monitor:

- [ ] **Daily transaction volume**: Are we capturing all transactions?
- [ ] **Null state rate**: What % of U.S. transactions have null state? (Should be 0%)
- [ ] **Failed transaction rate**: Are transactions failing due to validation errors?
- [ ] **Data completeness**: Are all required fields populated?
- [ ] **Balance reconciliation**: Does outstanding liability match transaction sum?

---

### **6.3 Quarterly Report Testing**

Before filing each MSB Call Report, validate:

- [ ] **TA90/TA100 queries work**: Run company-wide aggregation, verify non-zero
- [ ] **ST90/ST100 queries work**: Run state-level aggregation for each licensed state
- [ ] **State coverage**: All licensed states have data (even if zero)
- [ ] **No duplicate transactions**: Transaction IDs are unique
- [ ] **Quarter boundary accuracy**: Transactions allocated to correct quarter
- [ ] **Currency consistency**: All amounts in USD
- [ ] **Status filter accuracy**: Only 'completed' transactions counted

---

## 🗓️ **Section 7: Timeline & Milestones**

### **7.1 Product Launch Timeline**

| Milestone | Target Date | Owner | Status |
|-----------|-------------|-------|--------|
| **Data requirements finalized** | January 30, 2026 | Accounting | ✅ Done |
| **Database schema designed** | TBD | Engineering | ⏳ Pending |
| **Transaction capture implemented** | TBD | Engineering | ⏳ Pending |
| **State validation implemented** | TBD | Engineering | ⏳ Pending |
| **Reporting queries tested** | TBD | Engineering | ⏳ Pending |
| **Pre-launch testing complete** | TBD | Product + QA | ⏳ Pending |
| **Shop Dollars launches** | TBD | Product | ⏳ Pending |

---

### **7.2 First MSB Report Timeline**

Assuming Shop Dollars launches in **Q1 2026**:

| Milestone | Date | Owner | Notes |
|-----------|------|-------|-------|
| **Q1 2026 ends** | March 31, 2026 | - | Last day to capture Q1 transactions |
| **Run Q1 aggregation queries** | April 1-5, 2026 | Engineering | Generate TA/ST data |
| **Validate Q1 data** | April 5-10, 2026 | Accounting | Review for accuracy |
| **Generate Q1 XML** | April 10-15, 2026 | Accounting | Create MSB Call Report |
| **Submit Q1 report to NMLS** | **By May 15, 2026** | Accounting | **Regulatory deadline** |

**⚠️ CRITICAL**: MSB Call Reports are due **45 days after quarter-end**. Late filing = penalties.

---

## 📞 **Section 8: Open Questions for Product Team**

Please answer these questions to finalize requirements:

### **8.1 State Determination**
- [ ] Which address do we use to determine user state? (Billing? Shipping? Profile?)
- [ ] What happens if a user has no state on file?
- [ ] Can users change their state after purchase? (Does it affect past transactions?)

### **8.2 International Users**
- [ ] Can non-U.S. users purchase Shop Dollars?
- [ ] If yes, from which countries?
- [ ] Can Shop Dollars be redeemed at international merchants?

### **8.3 Expiration & Refunds**
- [ ] Do Shop Dollars ever expire?
- [ ] If yes, after how long? (Inactivity? Fixed date?)
- [ ] How are refunds handled? (Instant? Delayed? Credit back?)
- [ ] Can Shop Dollars be transferred between users?

### **8.4 Technical Implementation**
- [ ] Where will transaction data be stored? (Which database?)
- [ ] Will you create a dedicated `shop_dollars_transactions` table?
- [ ] Can you provide a reporting API for quarterly aggregation?
- [ ] What's your estimated launch date for Shop Dollars?

---

## 📚 **Section 9: Reference Documents**

For more details, see:

1. **`SHOPIFY_STORED_VALUE_MAPPING.md`** - Complete field-by-field MSB mapping
2. **`BUSINESS_PLAN_ANALYSIS.md`** - Shop Dollars business plan and funds flow
3. **`MSB Call Report XML Schema`** - Technical XML specification
4. **`SHOPIFY_FS_REFERENCE_DATA.md`** - SFS Inc. legal entity details

---

## ✅ **Section 10: Summary Checklist**

### **Must-Have for Product Launch:**

- [ ] **Transaction ID**: Unique identifier for each purchase
- [ ] **User ID**: Link to Shopify user
- [ ] **Amount (USD)**: Dollar amount purchased
- [ ] **Timestamp (UTC)**: When transaction occurred
- [ ] **User State**: U.S. state code (2-letter)
- [ ] **Status**: completed/pending/failed
- [ ] **Transaction Type**: PURCHASE/REDEMPTION/REFUND

### **Must-Have for Quarterly Reporting:**

- [ ] **TA90**: Count of all completed purchases (company-wide)
- [ ] **TA100**: Sum of all completed purchases (company-wide)
- [ ] **ST90**: Count of completed purchases per state
- [ ] **ST100**: Sum of completed purchases per state

### **Must-Have for Compliance:**

- [ ] **State validation**: Reject invalid state codes
- [ ] **NULL state handling**: Block U.S. users with no state
- [ ] **Balance reconciliation**: Purchases - redemptions = liability
- [ ] **Quarterly aggregation**: Queries ready to run at quarter-end

---

## 🚀 **Next Steps**

### **For Product Team:**
1. **Review this document** with Engineering, Product, and Legal
2. **Answer open questions** (Section 8)
3. **Design database schema** (Section 5.1)
4. **Implement transaction capture** (Section 1)
5. **Build reporting queries** (Section 5.2)
6. **Test end-to-end** (Section 6)

### **For Accounting Team:**
1. **Wait for product team responses** to open questions
2. **Review database schema** once designed
3. **Test reporting queries** once implemented
4. **Prepare for Q1 2026 report** (first report with real data)

---

**Document Owner**: Phil Whitham (Accounting) + Product Team  
**Last Updated**: January 30, 2026  
**Next Review**: Before Shop Dollars launch  

---

**Questions?** Contact Phil Whitham or the Global Accounting team.
