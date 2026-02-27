# SOX Control Matrix – MTL / Stored Value

**Entity:** Shopify Financial Services Inc.
**Purpose:** Key controls to build now for MTL transactions; specific examples and evidence.
**Last updated:** February 2026

---

## How to use this matrix

- **Control ID:** Use for tracking and cross-reference (e.g. MTL-SV-01).
- **Example transaction:** Concrete MTL/Shop Dollars example to test or evidence the control.
- **Status:** Update as each control is designed (D), implemented (I), and in operation (O).
- **Source type:** **Internal** = reconciliation between company systems (e.g. GL to transaction ledger). **External / third party** = reconciliation to a source outside the company (e.g. bank, processor), which provides independent verification and is stronger for SOX.

---

## Internal vs external / third‑party reconciliations

Many of the controls below reconcile **internal** sources (e.g. GL to transaction ledger). Reconciliations to **external / third‑party** sources are stronger because they are independent of company systems and reduce the risk that the same error appears in both sides of the recon.

| What we're verifying | Internal-only (weaker) | External / third party (stronger) |
|----------------------|------------------------|------------------------------------|
| **Shopper stored value liability** | GL Shopper SV Liability vs sum of individual Shopper balances | **FBO bank balance** (bank statement) – total FBO should equal Shopper SV + Merchant SV liabilities combined |
| **Merchant stored value liability** | GL Merchant SV Liability vs sum of individual Merchant balances | **FBO bank balance** (same bank rec; total liability vs FBO cash) |
| **Shopper issuance volume (TA90/TA100)** | MSB report vs internal transaction ledger | **Bank or payment processor ACH funding report** – shopper ACH credits to FBO |
| **Card settlement inflows (merchant wallet funding)** | Merchant SV Liability credits vs internal transaction ledger | **Payment partner settlement report** – card settlement proceeds to FBO |
| **Merchant payout volume** | Internal Merchant SV Liability debits | **Payment partner payout report** – FBO outflows to merchant external banks |
| **FBO cash** | GL cash vs total liability | **Bank statement** – already third party (bank rec) |
| **Interest revenue** | GL vs internal interest calculation | **Bank statement** – interest credited to FBO account |

**Recommendation:** Build both (1) **internal** recs for process discipline and (2) **third‑party** recs where a reliable external source exists. The controls in **§ 1–4** below are labeled **Internal** or **Third party**; **§ 1a** and **§ 4a** add dedicated third‑party reconciliation controls.

---

## 1. Stored value liability (Shopper and Merchant wallets)

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-SV-01** | Stored value liability (both wallets) | Both stored value liabilities are completely and accurately recorded from all transaction events | Perform two separate reconciliations at a defined point in time: **(1) Shopper Stored Value Liability:** Reconcile GL balance to the sum of individual Shopper balances in the product system (or to a net rollforward: opening + fundings + Case A refunds − Shop Dollars payments − withdrawals = closing). **(2) Merchant Stored Value Liability:** Reconcile GL balance to the sum of individual Merchant balances (or to a net rollforward: opening + card settlements + Shop Dollars transfers in − merchant payouts − Case A refunds out − Case B refunds = closing). Investigate and resolve variances above a set threshold for each liability. | Period-end: GL Shopper SV Liability $300K reconciles to sum of all Shopper balances in product system $300K. GL Merchant SV Liability $250K reconciles to sum of all Merchant balances $250K. Any variance investigated and documented per threshold. | At least monthly (e.g. after close); before quarter-end close and before MSB Call Report submission | [Accounting preparer] | Signed reconciliation for each liability (GL vs transaction ledger / balance rollforward); variance log and resolution notes | D / I / O |
| **MTL-SV-02** | Stored value liability (both wallets) | Individual transactions are recorded in the correct period and amount across both wallets | Review a sample of **transactions across both wallets** (by date and amount) to confirm they hit the correct period: shopper ACH fundings, Shop Dollars payments (internal transfers), card settlements, merchant payouts, and refunds (Case A and Case B). Focus on period-end cut-off (e.g. transactions near quarter-end). Confirm amounts agree to source (product ledger). | Shopper example: "Shopper C funded $100 Shop Dollars on 3/31/26 11:58 PM UTC" — confirm included in Q1 2026 Shopper SV Liability and in Q1 MSB Call Report (TA90/TA100, ST90/ST100), not Q2. Merchant example: "Card settlement $500 to Merchant D on 3/31/26" — confirm included in Q1 Merchant SV Liability, not Q2. | Monthly or quarterly sample; mandatory for quarter-end close | [Accounting reviewer] | Sample selection log; evidence that each sampled transaction is in correct period and amount; reviewer sign-off | D / I / O |
| **MTL-SV-03** | Stored value liability (both wallets) | Total liability movement across both wallets is understood and reviewed by management | Designated **management reviewer** reviews the stored value liability rollforward for **both wallets** and approves before financial close and/or regulatory submission. **Shopper rollforward:** opening + fundings + Case A refunds − Shop Dollars payments − withdrawals − breakage = closing. **Merchant rollforward:** opening + card settlements + Shop Dollars transfers in − merchant payouts − Case A refunds out − Case B refunds = closing. | Shopper wallet: Opening $250K; +$200K fundings; −$100K Shop Dollars payments; −$50K withdrawals = $300K closing. Merchant wallet: Opening $200K; +$100K card settlements; +$100K Shop Dollars transfers in; −$150K merchant payouts = $250K closing. Management reviews both rollforwards and signs off. | Before each quarter-end close and before MSB Call Report submission | [Designated manager, e.g. Accounting lead] | Signed management review memo or checklist; reference to both rollforwards and combined total | D / I / O |

### 1a. Stored value liability – reconciliation to third party

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-SV-04** | Stored value liability (total) | Total stored value liability is independently verified by third-party FBO bank balance | Reconcile **total stored value liability (GL)** — being the sum of Shopper Stored Value Liability and Merchant Stored Value Liability — to **FBO account balance per bank statement** (third party). Document known timing/operating differences (e.g. ACH in-transit, card settlements in-transit, accrued interest not yet swept). Investigate unexplained variances above threshold. | Month-end: GL Shopper SV Liability $300K + Merchant SV Liability $250K = $550K total. FBO bank statement balance $549K; difference $1K = ACH in transit (documented). Recon workpaper shows total liability vs FBO bank with clear explanation of each timing item. | At least monthly; before quarter-end and MSB submission | [Accounting preparer] | Signed reconciliation (total liability vs FBO bank statement); variance log with explanations | D / I / O |

---

## 2. Revenue (fees and breakage)

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-REV-01** | Stored value fee revenue / interest income (FC430) | Fee and interest revenue is recognized in the correct period and amount per policy | Apply a **defined policy** for recognition of interest income on FBO balances and any fees on Shop Dollars (e.g. load fees, inactivity fees). Record revenue in the period earned; reconcile to underlying transaction or bank statement. | Example: Interest income of $15K earned on FBO balance in Q1 2026. Reconcile to Citi bank statement interest credit. If a load fee applies in future: "Shopper D pays $2 load fee for $50 Shop Dollars" — revenue of $2 recorded in the period and reconciled to fee transaction log. | Each period where fee or interest revenue exists; review at quarter-end | [Accounting preparer / reviewer] | Revenue reconciliation (GL revenue to bank statement or fee transaction detail); policy document | D / I / O |
| **MTL-REV-02** | Breakage (unclaimed stored value) | Breakage is estimated and recognized in accordance with policy and consistently applied | Document a **breakage policy** (e.g. when balance is deemed abandoned, lookback period, method). Calculate breakage (e.g. by cohort or rate) and record to revenue and reduction of liability. **Management review** of breakage estimate and liability impact before close. Applies to Shopper Stored Value Liability (and Merchant, if applicable per policy). | Example: $10K of Shop Dollars balances are deemed abandoned per policy (e.g. 12 months inactive). Reduce Shopper SV Liability $10K, recognize $10K breakage revenue; management reviews and approves. | At least quarterly when breakage is material; otherwise per policy (e.g. annual) | [Accounting preparer]; [Designated manager] | Breakage policy; calculation workpaper; management sign-off on estimate and journal entry | D / I / O |

---

## 3. Cash / FBO accounts

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-CASH-01** | FBO bank account(s) | FBO cash balance per bank agrees to books and is reconciled to total stored value liability | Perform **bank reconciliation** for each FBO account: bank statement balance vs GL FBO Cash. Reconcile **FBO Cash (GL)** to **total stored value liability** (Shopper Stored Value Liability + Merchant Stored Value Liability), or explain timing differences (e.g. ACH in-transit, card settlements in-transit, accrued interest not yet swept). Investigate and resolve variances above threshold. | Period-end: Shopper SV Liability $300K + Merchant SV Liability $250K = $550K total. FBO Cash (GL) = $550K. FBO bank statement = $549K; $1K difference = ACH in transit (documented). Bank rec and liability-to-cash tie signed off. | At least monthly; before quarter-end and before MSB submission | [Accounting preparer] | Signed bank reconciliation; total liability vs FBO cash reconciliation; variance log | D / I / O |
| **MTL-CASH-02** | FBO cash | Reconciliations are reviewed and approved by someone other than preparer | A **reviewer** (different from preparer) reviews the FBO bank reconciliation and liability-to-cash reconciliation for completeness, reasonableness, and resolution of variances. Signs off before close. | Same as MTL-CASH-01; reviewer confirms total Shopper + Merchant liability ties to FBO bank and GL cash, and that all variances are explained. | Same as MTL-CASH-01 | [Accounting reviewer] | Reviewer sign-off on reconciliation package (date, name) | D / I / O |

---

## 4. Data feeding MSB Call Report (regulatory vs books)

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-REG-01** | MSB Call Report (FC220, TA90/100, ST90/100) | Figures in the MSB Call Report agree to the general ledger and supporting schedules | Before NMLS submission, **reconcile** key MSB Call Report fields to GL and workpapers: **FC220** (outstanding stored value) = total GL stored value liability (Shopper Stored Value Liability + Merchant Stored Value Liability; confirm with Legal/Compliance whether both are included in FC220 or reported separately — see process narrative §8 open items); **TA90/TA100** = count/sum of shopper funding transactions for the quarter from transaction ledger; **ST90/ST100** = same by Shopper state; **PI10/PI120** = NetSuite FBO account balance. Document in a pre-submission checklist or reconciliation. | Q1 2026 report. FC220 = $550K must equal total GL stored value liability (Shopper $300K + Merchant $250K, or shopper-only if Merchant SV is classified differently for MSB — confirm with Legal/Compliance before first operational filing). TA90 = 15,000 and TA100 = $1.2M must equal count and sum of all completed shopper funding transactions in the quarter. ST90 for PA = 3,000 must equal count of those where shopper_state = PA. | Every quarter before MSB Call Report submission | [NMLS preparer / Accounting] | Reconciliation workpaper (MSB fields to GL/ledger); pre-submission checklist with sign-off | D / I / O |
| **MTL-REG-02** | MSB Call Report submission | Submission is reviewed and approved by designated person; restatement/escalation per policy | Per **Financial Reporting Policy**: (1) Designated **reviewer/approver** reviews the MSB Call Report (and reconciliation in MTL-REG-01) before submission. (2) If the report includes a **material restatement**, **material error**, or other **material matter**, escalate to a Board member before submission. Document review and any escalation. | Example: Q1 2026 report prepared. Reviewer confirms FC220, TA90/100, ST90/100 tie to GL and transaction ledger. No restatement → approve and submit. If a prior quarter were being restated, escalation to Board per policy before submitting. | Every quarter | [Designated reviewer]; [NMLS filer] | Review sign-off; escalation log if applicable | D / I / O |

### 4a. MSB / transaction volume – reconciliation to third party

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-REG-03** | Shopper issuance volume (TA90, TA100) and card settlement inflows | Shopper funding volume and card settlement inflows are independently verified by third-party reports | **(1) Shopper fundings:** Reconcile **TA90 (count) and TA100 (dollar sum)** of Shop Pay Wallet Balance ACH fundings to **bank or processor ACH funding report** (credits to FBO from shopper ACH). **(2) Card settlements:** Reconcile **card settlement inflows** to FBO (which fund Merchant Stored Value Liability) to **payment partner settlement report**, once the MSB reporting classification of card settlements is confirmed with Legal/Compliance. Document and resolve variances (timing, fees, etc.) for both. | Q1 2026 shopper fundings: Internal ledger 15,000 fundings, $1.2M. Bank ACH funding report 15,000 credits, $1.198M ($2K timing difference — documented). Card settlements: Payment partner settlement report shows $5M settled to FBO; Merchant SV Liability shows $5M card settlement credits — reconciled. | Every quarter before MSB submission | [Accounting preparer] | Reconciliation workpaper (TA90/TA100 vs bank/processor report; card settlements vs payment partner settlement report); variance explanation | D / I / O |
| **MTL-REG-04** | Merchant payout volume | Merchant payouts from FBO are independently verified by payment partner payout report | Reconcile **Merchant Stored Value Liability payout debits** (dollar amount and optionally count) to **payment partner payout report** — being the outflows from FBO to merchant external banks (process narrative §3.8). Note: Shop Dollars payments (§3.2) are internal FBO transfers between Shopper and Merchant wallets and do not correspond to this external payout report. Document timing differences and reconciling items. | Q1 2026: Merchant payout ledger shows $3M in merchant payouts (Merchant SV Liability debited, FBO Cash credited). Payment partner payout report shows $3M paid out to merchant external banks (or $2.997M with timing). Recon documents alignment and explains variance. | Every quarter (or monthly when volume is material) | [Accounting preparer] | Reconciliation workpaper (Merchant SV payout ledger vs partner payout report) | D / I / O |

---

## 5. Segregation of duties and access

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-SOD-01** | All MTL financial processes | No single person can initiate, record, reconcile, and approve the same flow | Document and enforce **role split**: (1) **Preparer** – runs reports, prepares reconciliations, drafts MSB Call Report. (2) **Reviewer** – reviews reconciliations and report. (3) **Approver** – approves submission (or delegates per policy). (4) **NMLS filer** – submits in NMLS (may be same as approver but not same as sole preparer for same report). For journal entries: person who posts is different from person who approves, where feasible. | Example: Person A prepares Shopper and Merchant liability reconciliations and MSB Call Report; Person B reviews and approves; Person B (or designated filer) submits to NMLS. Person A cannot submit without B's review. | Ongoing; reviewed when roles change | [Management / Compliance] | Role matrix (names/roles); access review log | D / I / O |
| **MTL-SOD-02** | Transaction / ledger systems | Access to systems that can change financial data or submit reports is limited and reviewed | **Access controls**: Only authorized personnel have access to (a) post or adjust stored value liabilities (Shopper or Merchant) or revenue in the GL, (b) modify transaction data that feeds liability/TA/ST, (c) submit MSB Call Report in NMLS. Periodic **access review** (e.g. quarterly or at role change). | Example: Only designated accounting and product support roles can affect Shop Dollars or Merchant wallet balances or reporting data; NMLS credentials limited to designated filer(s). Access list reviewed quarterly. | At least quarterly access review; when roles change | [IT or process owner; Management] | Access list; access review sign-off | D / I / O |

---

## 6. Change management

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-CHG-01** | Calculation logic, mappings, reports | Changes that affect liability, revenue, or MSB reporting are documented and reviewed before go-live | **Change process**: Any change to (a) how Shopper or Merchant stored value liability or revenue is calculated, (b) mapping from product/ledger to GL or to MSB Call Report fields, or (c) logic of reports used for close or submission must be **documented** (what changed, why) and **reviewed/approved** by a designated person (e.g. Accounting lead) before production. Where applicable, test with sample MTL transactions. | Example: New product feature adds a "partial redemption" (e.g. use $10 of $50 Shopper balance). Change to Shopper SV Liability calculation and to TA/ST logic is documented; Accounting reviews and approves before release; post-release spot-check that a $10 Shop Dollars payment reduces Shopper SV Liability by $10 and increases Merchant SV Liability by $10. | Per change | [Product/Eng for build]; [Accounting for review] | Change log; review/approval; test results if applicable | D / I / O |

---

## 7. Summary – what to build now

| Priority | Control IDs | What to build |
|----------|-------------|----------------|
| **1** | MTL-SV-01, MTL-CASH-01, MTL-REG-01 | **Reconciliations (internal):** (1) GL Shopper SV Liability to shopper balance rollforward; GL Merchant SV Liability to merchant balance rollforward. (2) FBO bank to GL FBO Cash; GL FBO Cash to total stored value liability (Shopper + Merchant). (3) MSB Call Report (FC220, TA90/100, ST90/100) to GL and transaction ledger. Templates, owner, reviewer, sign-off. |
| **1a** | **MTL-SV-04, MTL-REG-03, MTL-REG-04** | **Reconciliations (third party):** (1) Total stored value liability to **FBO bank balance**. (2) Shopper fundings (TA90/TA100) to **bank or processor ACH funding report**; card settlements to **payment partner settlement report**. (3) Merchant payout volume to **payment partner payout report**. Stronger evidence; build where external source is available. |
| **2** | MTL-SV-03, MTL-CASH-02, MTL-REG-02 | **Review and approval:** Management review of combined liability rollforward (both Shopper and Merchant); reviewer sign-off on FBO and liability reconciliations; designated review and approval of MSB Call Report before submission (and escalation per Financial Reporting Policy). |
| **3** | MTL-SV-02, MTL-REV-01, MTL-REV-02 | **Cut-off and revenue:** Sample review of transactions across both wallets for period and amount; interest income reconciliation to bank statement; breakage policy, calculation, and management review. |
| **4** | MTL-SOD-01, MTL-SOD-02 | **Segregation and access:** Role matrix (preparer, reviewer, approver, NMLS filer); access rights to GL (both liabilities), transaction data, NMLS; periodic access review. |
| **5** | MTL-CHG-01 | **Change management:** Process for documenting and reviewing changes to Shopper or Merchant liability/revenue logic and to MSB report mappings. |

### Control source – internal vs third party

| Control ID | Source | Third-party source (where applicable) |
|------------|--------|--------------------------------------|
| MTL-SV-01, MTL-SV-02, MTL-SV-03 | Internal | — |
| **MTL-SV-04** | **Third party** | FBO bank statement (total Shopper + Merchant liability vs FBO balance) |
| MTL-REV-01, MTL-REV-02 | Internal / Third party | Interest revenue: bank statement (FBO interest credit) |
| MTL-CASH-01, MTL-CASH-02 | Third party | Bank statement (FBO) |
| MTL-REG-01, MTL-REG-02 | Internal | — |
| **MTL-REG-03** | **Third party** | Bank/processor ACH funding report (shopper fundings); payment partner settlement report (card settlements) |
| **MTL-REG-04** | **Third party** | Payment partner payout report (merchant payouts FBO → external bank) |
| MTL-SOD-01, MTL-SOD-02, MTL-CHG-01 | Process / governance | — |

---

## 8. Example MTL transactions – quick reference

| Example | Control(s) it supports |
|---------|-------------------------|
| Shopper funds $50 Shop Dollars (ACH deposit → FBO) | MTL-SV-01 (shopper), MTL-SV-02, MTL-SV-03, MTL-SV-04, MTL-CASH-01, MTL-REG-01, **MTL-REG-03** (shopper funding vs bank/processor report) |
| Shopper pays merchant with Shop Dollars (internal FBO transfer: Shopper SV Liability ↓, Merchant SV Liability ↑) | MTL-SV-01 (both sides), MTL-SV-02, MTL-SV-03 |
| Card settlement from Payment Partner into FBO → Merchant wallet credited (Merchant SV Liability ↑) | MTL-SV-01 (merchant), MTL-SV-02, MTL-SV-03, MTL-SV-04, MTL-CASH-01, **MTL-REG-03** (card settlement vs payment partner settlement report) |
| Merchant payout from FBO to merchant external bank (Merchant SV Liability ↓, FBO Cash ↓) | MTL-SV-01 (merchant), MTL-SV-02, MTL-SV-03, MTL-SV-04, MTL-CASH-01, **MTL-REG-04** (payout vs payment partner payout report) |
| Quarter-end liability rollforward — Shopper and Merchant wallets | MTL-SV-01, MTL-SV-03, MTL-REG-01 (FC220) |
| Total stored value liability $550K vs FBO bank balance $549K ($1K ACH in transit) | **MTL-SV-04** (third party), MTL-CASH-01 |
| FBO bank statement vs GL FBO Cash vs total liability | MTL-CASH-01, MTL-CASH-02 |
| TA90/TA100 vs bank/processor ACH funding report (shopper fundings) | **MTL-REG-03** (third party) |
| Card settlement inflows vs payment partner settlement report (merchant wallet funding) | **MTL-REG-03** (third party) |
| Merchant payout ledger vs payment partner payout report | **MTL-REG-04** (third party) |
| MSB Call Report FC220 = $550K; TA90 = 15,000; ST90 PA = 3,000 | MTL-REG-01, MTL-REG-02 |
| Breakage: $10K abandoned Shopper balance recognized as revenue | MTL-REV-02, MTL-SV-03 |
| New product feature changes how Shop Dollars payments affect both liabilities | MTL-CHG-01 |

---

**Owner:** [Global Accounting / Finance Lead]
**Review:** Update control owners and status (D/I/O) as controls are implemented; align with Internal Audit when SFS/MTL is in SOX scope.
