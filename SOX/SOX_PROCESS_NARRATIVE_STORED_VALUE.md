# SOX Process Narrative – Stored Value (Shop Pay Wallet Balance and Merchant User Stored Value)

**Entity:** Shopify Financial Services Inc.

**Process:** End-to-end stored value lifecycle — transaction initiation through financial close and regulatory reporting; covers both Buyer and Merchant stored value.

**Document type:** ICFR process narrative

**Status:** Draft — pending chart of accounts mapping (product in build; account numbers to be confirmed in NetSuite once operational; descriptive names used throughout)

**Last updated:** February 2026

---

## 1. Purpose

This narrative documents the end-to-end process for Shopify Financial Services Inc.'s stored value product, from transaction initiation through general ledger recording, period-end close, and MSB Call Report submission. It is designed to support ICFR design and documentation, and to establish a clear description of systems, data flows, and control points for each stage.

**Two stored value liabilities are in scope:**

1. **Buyer Stored Value Liability** — funds loaded into and held in the Shop Pay Wallet Balance (Shop Dollars) by Buyers. Created by ACH deposits from Buyer's external bank account; extinguished by Shop Dollars payments to Merchants, withdrawals to external bank (confirm current product scope; see §8), or breakage.

2. **Merchant Stored Value Liability** — funds credited to the Merchant User Stored Value (merchant wallet) from buyer payments. Created by card settlement proceeds or Shop Dollars redemptions; extinguished by merchant payouts to external bank, card-funded refunds, or (future state) application toward Shopify-billed obligations such as subscription fees, MCA repayments, or loan repayments.

Both liabilities are held within the same FBO account pool at the Bank Partner (Citi). The FBO bank balance should equal the sum of both liabilities at all times, subject to timing items (ACH in-transit, card settlements in-transit) and accrued interest not yet swept.

---

## 2. Overview – Systems of Record

| System | Role | Owned by |
|--------|------|----------|
| **Shop App / Shopify platform** | Source of truth for individual Buyer and Merchant balances and transaction history (current state; may transition to Standalone Ledger — see below) | Shopify Inc. (product/engineering) |
| **Standalone Ledger** (in build) | Product-level financial ledger being built as part of the Shopify FS product; will record individual wallet transactions at granular level; how and at what level it pushes data to NetSuite is to be determined | Shopify Inc. (product/engineering) |
| **FBO Bank Account(s)** (Citi, IDs: 11623 CLE USD, 11624 OPS USD) | Omnibus account holding all Buyer and Merchant funds; third-party independent verification source | Bank Partner (Citi) |
| **Payment Partner** (e.g. Stripe, PayPal) | Settles card-funded buyer payments into FBO (inflow); processes merchant payouts from FBO (outflow) | Third party |
| **NetSuite** (Subsidiary ID: 87 – Shopify Financial Services Inc.) | Accounting general ledger; records both stored value liabilities, FBO cash, and revenue | Shopify Finance / Accounting |
| **BigQuery** | Transaction data warehouse; supports extraction of transaction counts and volumes for TA/ST MSB Call Report fields; not a financial ledger | Shopify Data Engineering |
| **NMLS Portal** | Submission platform for MSB Call Reports | NMLS (external) |

**General ledger of record:** NetSuite is the accounting general ledger of record for Shopify FS. All stored value liability balances and FBO cash balances are authoritative in NetSuite. The Standalone Ledger (once built) will be the product-level transaction ledger; the relationship between the Standalone Ledger and NetSuite (including how journal entries are generated and at what level of aggregation) is an open item — see §8. BigQuery is a data warehouse, not a ledger, and transaction counts and volumes from BigQuery must reconcile to NetSuite-recorded balances at each period-end. There shall be no parallel shadow books or off-system spreadsheets used as the authoritative record for any balance that feeds consolidated reporting or MSB Call Reports.

---

## 3. Transaction Types and Funds Flow

The stored value lifecycle involves two parties — Buyers and Merchants — each with their own stored value balance within the same FBO pool. **Sections 3.1–3.5** cover Buyer wallet transactions. **Section 3.5** covers FBO interest income (applies across both wallets). **Sections 3.6–3.7** cover Merchant wallet transactions. All transactions ultimately affect one or both stored value liabilities and/or the FBO cash balance.

### 3.1 Funding (ACH Deposit — Buyer Stored Value Liability Created)

**Trigger:** Buyer initiates an ACH debit from their external bank account via Shop App.

**Step-by-step:**

1. Buyer requests to add funds to their Shop Pay Wallet Balance in Shop App.
2. Shop App instructs Bank Partner (acting as ODFI) to initiate an ACH debit from the Buyer's bank.
3. ACH settles (typically 2–3 business days); funds arrive in the FBO account at Citi.
4. Shop App credits the Buyer's individual balance in the product system.
5. NetSuite records:
   - **Debit:** FBO Cash – Citi `[CLE USD or OPS USD, to be confirmed]`
   - **Credit:** Buyer Stored Value Liability
6. Buyer Stored Value Liability is now outstanding (FC220 increases — confirm whether FC220 includes Merchant Stored Value Liability; see §8).

**Note on funding mechanism:** The original business plan documents ACH as the funding method. Confirm with Product/Engineering whether buyers may also fund via credit/debit card processed by Stripe/PayPal, and if so, update this section accordingly — see §8.

**MSB fields impacted:** FC220 (↑), TA90 (count ↑), TA100 ($ ↑), ST90/ST100 (by Buyer's state)

**Control points:** MTL-SV-01 (liability recon), MTL-SV-02 (cut-off), MTL-SV-04 (total liability vs FBO bank), MTL-REG-01 (MSB recon), MTL-REG-03 (TA90/100 vs bank/processor)

---

### 3.2 Shop Dollars Redemption (Merchant Payment) — Internal Transfer to Merchant Wallet

**Trigger:** Buyer uses Shop Pay Wallet Balance (Shop Dollars) at checkout to pay a Merchant.

**Step-by-step:**

1. Buyer selects Shop Pay Wallet Balance at checkout; Shopify FS confirms sufficient funds.
2. Product system debits the Buyer's individual balance (Buyer Stored Value decreases).
3. Product system credits the Merchant's individual balance in Merchant User Stored Value.
4. **No external funds movement** — this is an internal transfer within the FBO account; FBO bank balance is unchanged.
5. NetSuite records:
   - **Debit:** Buyer Stored Value Liability
   - **Credit:** Merchant Stored Value Liability
6. Buyer Stored Value Liability is extinguished for this payment; Merchant Stored Value Liability increases by the same amount.

**Note:** FBO cash does not change at this step. Funds remain in the FBO until the Merchant requests a payout (§3.7). Total stored value liability (Buyer + Merchant combined) is unchanged.

**MSB fields impacted:** FC220 (net zero change if both liabilities are included in FC220; see §8)

**Control points:** MTL-SV-01 (both sides of internal transfer must reconcile), MTL-SV-02 (cut-off for period-end payments)

---

### 3.3 Split Payment

**Trigger:** Buyer uses Shop Pay Wallet Balance plus a card or other payment method.

**Step-by-step:**

1. Buyer allocates a portion of payment to Shop Pay Wallet Balance; remainder processed via card/other.
2. Shop Dollars portion follows the same flow as §3.2 above (internal transfer to Merchant wallet; FBO cash unchanged for this portion).
3. Card portion is processed by Payment Partner; card settlement proceeds flow into FBO and credit Merchant wallet per §3.6.
4. NetSuite records the Shop Dollars portion per §3.2; the card settlement portion is recorded per §3.6.

**Note:** Only the Shop Dollars portion of a split payment constitutes a stored value redemption for Shopify FS liability purposes. Cut-off controls (MTL-SV-02) must correctly capture the stored value amount and card amount separately.

**Control points:** Same as §3.2 for the Shop Dollars portion; §3.6 for the card settlement portion.

---

### 3.4 Refund (Liability Flows Vary by Original Payment Method)

**Trigger:** Merchant issues a refund to the original payment method.

#### Case A — Original payment was Shop Dollars (§3.2)

1. Merchant initiates refund via Payment Partner or Shopify platform.
2. Product system credits the Buyer's individual balance; debits the Merchant's individual balance.
3. **No external funds movement** — internal FBO transfer, the reverse of §3.2.
4. NetSuite records:
   - **Debit:** Merchant Stored Value Liability
   - **Credit:** Buyer Stored Value Liability
5. Buyer Stored Value Liability re-created; Merchant Stored Value Liability decreases.

#### Case B — Original payment was card-funded (§3.6)

1. Merchant initiates refund via Payment Partner.
2. Payment Partner processes refund back to buyer's original card (outside Shopify FS scope for the card leg).
3. Merchant's individual balance in Merchant User Stored Value is debited; funds leave FBO back to Payment Partner.
4. NetSuite records:
   - **Debit:** Merchant Stored Value Liability
   - **Credit:** FBO Cash – Citi
5. Both Merchant Stored Value Liability and FBO Cash decrease.

**Note:** Refund classification (Case A vs Case B) is critical for accurate reconciliation of both liabilities and for the FBO bank reconciliation. Confirm with Data Engineering whether the original payment method is captured on the refund transaction in BigQuery (see §8).

**MSB fields impacted (Case A):** FC220 net zero; **(Case B):** FC220 (↓ if Merchant Stored Value included)

**Control points:** MTL-SV-01, MTL-SV-02 (cut-off for refunds near period end), MTL-REG-01

---

### 3.5 Withdrawal (ACH Credit — Buyer Stored Value Liability Extinguished)

**Note — confirm current product scope:** The original business plan includes withdrawal to external bank as an explicit Buyer use case. Confirm with Product/Engineering whether this feature is in scope for the current build — see §8. If confirmed out of scope, this section will be removed.

**Trigger:** Buyer requests withdrawal of their Shop Pay Wallet Balance to their external bank account.

**Step-by-step:**

1. Buyer initiates withdrawal in Shop App.
2. Shopify FS (via Bank Partner as ODFI) initiates an ACH credit to the Buyer's bank.
3. Product system debits the Buyer's individual balance.
4. ACH settles (2–3 business days); funds leave FBO account.
5. NetSuite records:
   - **Debit:** Buyer Stored Value Liability
   - **Credit:** FBO Cash – Citi
6. Buyer Stored Value Liability extinguished (FC220 decreases).

**Control points:** MTL-SV-01, MTL-SV-02, MTL-SV-04, MTL-CASH-01

---

### 3.6 Interest Income on FBO (Revenue)

**Trigger:** Bank Partner pays interest on FBO account balances.

**Step-by-step:**

1. Citi calculates and pays interest on the FBO account balance (per bank agreement).
2. Interest credited to FBO account.
3. NetSuite records:
   - **Debit:** FBO Cash – Citi
   - **Credit:** Interest Income on FBO (FC430)
4. Revenue recognized in the period earned.

**Note:** Interest income belongs to Shopify FS, not to Buyers or Merchants. The FBO bank balance will temporarily exceed total stored value liabilities until interest is swept or recognized as revenue. The intercompany agreement with Shopify Inc. governs how interest income flows through the corporate structure.

**Control points:** MTL-REV-01 (fee/interest revenue recognition and reconciliation)

---

### 3.7 Card Settlement — Merchant User Stored Value Funded

**Trigger:** A buyer pays a Merchant using a card (not Shop Pay Wallet Balance), processed by Stripe/PayPal or another Payment Partner; net proceeds settle into FBO and are credited to the Merchant's wallet.

**Step-by-step:**

1. Buyer completes a purchase using a debit or credit card at a Shopify Merchant checkout.
2. Payment Partner (Stripe, PayPal, or other) authorizes and processes the card payment; net proceeds (after applicable fees) settle to the FBO account at Citi.
3. Shopify FS credits the Merchant's individual balance in Merchant User Stored Value within the product system.
4. NetSuite records:
   - **Debit:** FBO Cash – Citi
   - **Credit:** Merchant Stored Value Liability
5. Merchant Stored Value Liability increases; FBO Cash increases.

**Note on MSB reporting:** Whether card settlement inflows to the Merchant wallet constitute "stored value issuance" for TA90/TA100 purposes (vs. money transmission or a different classification) is a regulatory interpretation question requiring Legal/Compliance confirmation. See §8.

**Control points:** MTL-SV-01 (merchant liability recon), MTL-SV-04 (total FBO bank vs total liability), MTL-REG-03 (card settlement report vs merchant wallet credits, once reporting classification is confirmed)

---

### 3.8 Merchant Payout (ACH Credit — Merchant Stored Value Liability Extinguished)

**Trigger:** Merchant requests payout of their Merchant User Stored Value to their external bank account.

**Step-by-step:**

1. Merchant initiates a payout request via Shopify admin or API.
2. Shopify FS (via Payment Partner) initiates a payout (ACH credit or equivalent) to the Merchant's external bank account.
3. Product system debits the Merchant's individual balance in Merchant User Stored Value.
4. Funds leave FBO account; FBO bank balance decreases.
5. NetSuite records:
   - **Debit:** Merchant Stored Value Liability
   - **Credit:** FBO Cash – Citi
6. Merchant Stored Value Liability extinguished for this payout amount (FC220 decreases, subject to MSB mapping confirmation in §8).

**Control points:** MTL-SV-01 (merchant liability recon), MTL-SV-04 (total FBO bank vs total liability), MTL-CASH-01, MTL-REG-04 (payout volume vs payment partner payout report)

---

## 4. Period-End Close Process

The following steps apply at the end of each accounting period (monthly; mandatory at quarter-end).

### Step 1 — Transaction Cut-Off Review
- Confirm all ACH transactions (buyer fundings, buyer withdrawals if in scope, merchant payouts) and card settlements that initiated before period-end are included in the correct period, including those with 2–3 day settlement lags.
- Flag and review any transactions near period-end for correct period assignment.
- **Owner:** [Accounting preparer]
- **Control:** MTL-SV-02
- **Evidence:** Cut-off review workpaper or sample log

### Step 2 — Buyer Stored Value Liability Reconciliation (Internal)
- Reconcile NetSuite Buyer Stored Value Liability balance to the sum of all individual Buyer balances in the product system (or to a net transaction rollforward: opening + fundings + Case A refunds − Shop Dollars payments − withdrawals − breakage = closing).
- Investigate and resolve variances above threshold `[threshold TBD]`.
- **Owner:** [Accounting preparer]
- **Control:** MTL-SV-01
- **Evidence:** Signed reconciliation workpaper

### Step 3 — Merchant Stored Value Liability Reconciliation (Internal)
- Reconcile NetSuite Merchant Stored Value Liability balance to the sum of all individual Merchant balances in the product system (or to a net transaction rollforward: opening + card settlements + Shop Dollars transfers in − merchant payouts − Case A refunds out − Case B refunds = closing).
- Investigate and resolve variances above threshold `[threshold TBD]`.
- **Owner:** [Accounting preparer]
- **Control:** MTL-SV-01 (applied to merchant liability)
- **Evidence:** Signed reconciliation workpaper

### Step 4 — FBO Bank Reconciliation (Third Party)
- Reconcile FBO account bank statement balance (Citi) to NetSuite FBO Cash balance.
- Reconcile FBO Cash (GL) to total stored value liability (Buyer Stored Value Liability + Merchant Stored Value Liability), documenting known timing items (ACH in-transit, card settlements in-transit, accrued interest, etc.).
- **Owner:** [Accounting preparer]; reviewed by [Accounting reviewer]
- **Controls:** MTL-CASH-01, MTL-CASH-02, MTL-SV-04
- **Evidence:** Signed bank reconciliation; total liability-to-cash tie workpaper

### Step 5 — Revenue Recognition
- Confirm interest income from FBO is recorded in the correct period and amount per bank statement.
- If applicable, calculate and record breakage per policy.
- **Owner:** [Accounting preparer]
- **Controls:** MTL-REV-01, MTL-REV-02 (if breakage)
- **Evidence:** Interest income reconciliation to bank statement; breakage workpaper (when applicable)

### Step 6 — Management Review of Combined Liability Rollforward
- Designated manager reviews the stored value liability rollforward for both wallets and approves:
  - **Buyer:** Opening + fundings + Case A refunds − Shop Dollars payments − withdrawals − breakage = closing
  - **Merchant:** Opening + card settlements + Shop Dollars transfers in − merchant payouts − Case A refunds out − Case B refunds = closing
- **Owner:** [Designated manager]
- **Control:** MTL-SV-03
- **Evidence:** Signed management review memo or checklist

---

## 5. MSB Call Report Preparation Process (Quarterly)

The following additional steps apply at each quarter-end, after the period-end close steps in §4 are complete.

### Step 7 — MSB Data Extraction
- Extract transaction data from BigQuery for the quarter: count and sum of all Shop Pay Wallet Balance funding transactions (TA90, TA100) and by Buyer state (ST90, ST100).
- Extract NetSuite balances: FC220 (total outstanding stored value liability at quarter-end — confirm whether this includes Merchant Stored Value Liability; see §8), FC430 (interest income for quarter), PI fields (permissible investments — FBO account balance).
- **Owner:** [Accounting preparer / NMLS preparer]
- **Evidence:** Data extraction workpaper (queries, outputs, dates)

### Step 8 — MSB Call Report Reconciliation to GL (Internal)
- Reconcile key MSB Call Report fields to NetSuite and BigQuery:
  - FC220 = NetSuite total stored value liability at quarter-end (Buyer + Merchant, subject to mapping confirmation)
  - FC430 = NetSuite interest income for the quarter
  - TA90 / TA100 = BigQuery count/sum of buyer funding transactions for the quarter
  - ST90 / ST100 (by state) = BigQuery count/sum by Buyer state
  - PI10 / PI120 = NetSuite FBO account balance
- Document and resolve all variances.
- **Owner:** [Accounting preparer]
- **Control:** MTL-REG-01
- **Evidence:** MSB-to-GL reconciliation workpaper; pre-submission checklist

### Step 9 — MSB Transaction Volume Reconciliation to Third Party
- Reconcile TA90/TA100 (buyer funding count and $) to bank or payment processor funding report (ACH credits to FBO from buyer fundings).
- Reconcile card settlement volume to payment partner settlement report (card-funded inflows to FBO for merchant wallet).
- Reconcile merchant payout volume to payment partner payout report.
- Document and resolve variances (timing, fees, etc.).
- **Owner:** [Accounting preparer]
- **Controls:** MTL-REG-03, MTL-REG-04
- **Evidence:** Third-party reconciliation workpaper

### Step 10 — Report Generation
- Generate MSB Call Report XML per NMLS specifications (XSD schema v4).
- Validate XML against schema; confirm no structural errors.
- Prepare Report Summary for reviewer.
- **Owner:** [Accounting preparer / NMLS preparer]
- **Evidence:** XML file; validation output; Report Summary

### Step 11 — Review and Approval
- Designated reviewer reviews the MSB Call Report (XML and Report Summary) and reconciliation workpapers (Steps 8–9).
- Reviewer confirms accuracy and completeness; signs off.
- Perform escalation check: does this submission involve a material restatement, material error, or other material matter? If yes, escalate to a Board member per Financial Reporting Policy before submitting.
- **Owner:** [Designated reviewer]
- **Control:** MTL-REG-02
- **Evidence:** GitHub issue (or equivalent) approval sign-off; escalation record if applicable

### Step 12 — Submission and Retention
- NMLS Filer submits the XML to NMLS by the deadline (45 days after quarter-end).
- Retain filed XML, submission confirmation, all workpapers and sign-offs in accordance with Financial Reporting Policy and Company retention schedule (minimum 7 years for ICFR evidence).
- **Owner:** [NMLS Filer]
- **Evidence:** NMLS submission confirmation; file history PDF

---

## 6. Process Flow Summary

```
BUYER WALLET
    │
    ├── Funding (ACH in)             → FBO Cash ↑, Buyer SV Liability ↑
    ├── Shop Dollars payment          → Buyer SV Liability ↓, Merchant SV Liability ↑ (FBO unchanged)
    ├── Case A Refund (→ buyer)       → Merchant SV Liability ↓, Buyer SV Liability ↑ (FBO unchanged)
    ├── Withdrawal (ACH out)          → Buyer SV Liability ↓, FBO Cash ↓  [confirm in scope — see §8]
    └── Interest on FBO               → FBO Cash ↑, Interest Income ↑

MERCHANT WALLET
    │
    ├── Card settlement (in)          → FBO Cash ↑, Merchant SV Liability ↑
    ├── Shop Dollars transfer in      → Merchant SV Liability ↑ (see Buyer side above)
    ├── Case B Refund (→ card)        → Merchant SV Liability ↓, FBO Cash ↓
    └── Merchant payout (out)         → Merchant SV Liability ↓, FBO Cash ↓
    │
    ▼
GENERAL LEDGER (NetSuite — Subsidiary 87)
    │  Buyer SV Liability + Merchant SV Liability = FBO Cash (± timing items + accrued interest)
    │
    ├── THIRD-PARTY VERIFICATION
    │       FBO Bank Statement (Citi) ←──────── independent
    │       Payment Partner Settlement Report ←── card-funded merchant wallet inflows
    │       Payment Partner Payout Report ←────── merchant payouts
    │       Bank / Processor Funding Report ←───── buyer ACH fundings
    │
    ├── PERIOD-END CLOSE (Monthly / Quarterly)
    │       Cut-off review ─────────────────────── MTL-SV-02
    │       Buyer liability recon ──────────────── MTL-SV-01
    │       Merchant liability recon ─────────────── MTL-SV-01
    │       FBO bank recon (total liability) ──────── MTL-CASH-01/02, MTL-SV-04
    │       Revenue recognition ───────────────────── MTL-REV-01
    │       Management review ────────────────────── MTL-SV-03
    │
    └── MSB CALL REPORT (Quarterly)
            BigQuery extraction (TA/ST)
            MSB-to-GL recon ──────────── MTL-REG-01
            Volume-to-3rd-party recon ── MTL-REG-03/04
            XML generation → validation
            Review & approval ────────── MTL-REG-02
            NMLS submission
```

---

## 7. Open Items — Accounts (Descriptive Names; Numbers to Be Confirmed)

The following GL accounts are referenced throughout this narrative using descriptive names. NetSuite account numbers are to be confirmed once the chart of accounts is finalized for the product launch.

| Account (Descriptive Name) | Description | MSB Field | Status |
|---------------------------|-------------|-----------|--------|
| **Buyer Stored Value Liability** | Outstanding balances owed to Buyers (Shop Pay Wallet Balance / Shop Dollars) | FC220 (primary; see §8) | Account number TBD |
| **Merchant Stored Value Liability** | Outstanding balances owed to Merchants (Merchant User Stored Value / merchant wallet) | FC220 (confirm inclusion; see §8) | Account number TBD |
| **FBO Cash – Citi CLE USD** | FBO operating cash account (Citi account 11623) | PI10, PI120 | Account number TBD |
| **FBO Cash – Citi OPS USD** | FBO cash account (Citi account 11624) | PI10, PI120 | Account number TBD |
| **Interest Income on FBO** | Interest earned on FBO account balances | FC430 | Account number TBD |
| **Breakage Revenue** | Breakage on forfeited or expired balances (if applicable) | FC430 or separate | Account number TBD |

**Action:** Update this narrative and `SOX_MTL_CONTROL_MATRIX.md` with confirmed account numbers before first operational quarter.

---

## 8. Open Items — Regulatory Classification and Systems

| Item | Description | Status |
|------|-------------|--------|
| **Buyer wallet funding mechanism** | Original business plan documents ACH as the funding method. Confirm with Product/Engineering whether buyers may also fund via credit/debit card processed by Stripe/PayPal; if so, update §3.1 and related MSB reporting classification accordingly | To be confirmed with Product/Engineering |
| **Buyer withdrawal feature** | Original business plan includes withdrawal to external bank as an explicit buyer use case. Confirm with Product/Engineering whether this feature is in scope for the current build; if confirmed out of scope, remove §3.5 and update rollforward formulas | To be confirmed with Product/Engineering |
| **Standalone Ledger → NetSuite relationship** | Shopify FS product build includes a Standalone Ledger for individual wallet transactions. Confirm: (a) how and at what level (individual transactions vs aggregated summaries) data flows from the Standalone Ledger to NetSuite; (b) how journal entries are generated in NetSuite; (c) whether BigQuery receives data from the Standalone Ledger or directly from the product system | To be confirmed with Product/Engineering / Finance |
| **FC220 scope — Merchant Stored Value** | Confirm whether Merchant Stored Value Liability is included in FC220 (outstanding stored value) for MSB reporting, or classified and reported separately | To be confirmed with Legal/Compliance |
| **TA90/TA100 scope — card settlements** | Confirm whether card settlement inflows to Merchant User Stored Value are included in TA90/TA100 (stored value issuance) or classified under a different field (e.g., money transmission TA10/TA20) | To be confirmed with Legal/Compliance |
| **BigQuery table(s)** | Tables containing Shop Pay Wallet Balance funding transactions (buyer ACH fundings) and Merchant User Stored Value transactions for TA/ST fields | To be confirmed with Data Engineering |
| **Refund classification** | How Case A vs Case B refunds are distinguished in BigQuery (original payment method flag); how refunds are identified separately from new buyer fundings | To be confirmed with Data Engineering |
| **State field** | Field name for Buyer's state in BigQuery transaction data; state determination methodology (billing vs. shipping address) | To be confirmed with Data Engineering |
| **Bank/processor reports** | Format and availability of: (a) ACH funding report from Citi for buyer fundings (MTL-REG-03); (b) card settlement report from payment partner for merchant wallet inflows | To be confirmed with Citi/Banking team and Payment Partner |
| **Payment partner payout report** | Format and availability of merchant payout report from Stripe/PayPal for MTL-REG-04 | To be confirmed with Payment Partner |
| **Variance thresholds** | Define materiality thresholds for investigating variances in Buyer and Merchant liability reconciliations | To be confirmed with Finance/Accounting |
| **Merchant Shopify bill payments (future state)** | When merchants use stored value to pay Shopify subscription fees, MCA repayments, or loan repayments, confirm the accounting treatment, extinguishment flow, and MSB reporting classification for this transaction type | To be confirmed with Product/Legal/Compliance when feature is ready for launch |

---

## 9. Relationship to Other Documents

| Document | Relationship |
|----------|-------------|
| `SOX_CONTROL_FRAMEWORK_MTL.md` | Control categories and governance framework that this narrative operationalizes |
| `SOX_MTL_CONTROL_MATRIX.md` | Detailed key controls; each step in §4–5 maps to one or more controls in the matrix |
| `FLOW_OF_FUNDS_MTL.md` | Visual/tabular funds flow for both wallet sides; source reference for §3 of this narrative |
| `docs/Financial_Reporting_Policy_DRAFT.md` | Governance, roles, escalation, and retention requirements referenced in Steps 11–12 |
| `docs/SHOPIFY_STORED_VALUE_MAPPING.md` | MSB field-to-GL mapping detail |
| `docs/BUSINESS_PLAN_ANALYSIS.md` | Source for buyer funds flow and business model detail |
| `MSB Call Reports/2025/Q4/` | Filed Q4 2025 report; first operational example of Steps 7–12 |

---

**Owner:** [Global Accounting / Finance Lead]

**Review cadence:** Update whenever product features, systems, or account mappings change (MTL-CHG-01); confirm current as of each quarter-end close.

**Classification:** Internal use — Shopify Financial Services Inc. Confidential
