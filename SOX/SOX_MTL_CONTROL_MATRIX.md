# SOX Control Matrix – MTL / Stored Value

**Entity:** Shopify Financial Services Inc.  
**Purpose:** Key controls to build now for MTL transactions; specific examples and evidence.  
**Last updated:** January 2026  

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
| **Stored value liability** | GL vs transaction ledger / customer balance sum | **FBO bank balance** (bank statement) – funds held at bank; liability should approximate bank balance subject to timing/operating differences |
| **Issuance volume (TA90/TA100)** | MSB report vs internal transaction ledger | **Bank or payment processor** – funding into FBO (e.g. ACH credits, card settlement) from processor/bank report |
| **Redemption volume** | Internal ledger redemptions | **Payment partner** – payout report (e.g. payouts to Stripe for merchant settlements) |
| **FBO cash** | GL cash vs liability | **Bank statement** – already third party (bank rec) |
| **Fee revenue** (if any) | GL vs internal fee log | **Processor fee report** or **bank deposits** (if fees are identifiable) |

**Recommendation:** Build both (1) **internal** recs for process discipline and (2) **third‑party** recs where a reliable external source exists. The controls in **§ 1–4** below are labeled **Internal** or **Third party**; **§ 1a** and **§ 4a** add dedicated third‑party reconciliation controls.

---

## 1. Stored value liability (Shop Dollars customer balance)

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-SV-01** | Stored value liability | Liability is completely and accurately recorded from all issuance and redemption events | Reconcile the **general ledger stored value liability balance** to the **sum of individual customer Shop Dollars balances** (or to the transaction-ledger total) at a defined point in time. Investigate and resolve variances above a set threshold (e.g. $X or X%). | Shopper A purchases $50 Shop Dollars; Shopper B redeems $25. Liability should increase by $50 then decrease by $25. Reconciliation compares GL liability to sum of all customer balances (or to net of purchases minus redemptions in the transaction system). | At least monthly (e.g. after close); before quarter-end close and before MSB Call Report submission | [Accounting preparer] | Signed reconciliation (GL vs transaction ledger / customer balance rollforward); variance log and resolution notes | D / I / O |
| **MTL-SV-02** | Stored value liability | Individual MTL transactions are recorded in the correct period and amount | Review a sample of **issuance and redemption transactions** (by date and amount) to confirm they hit the correct period and that amounts agree to source (product/ledger). Focus on period-end cut-off (e.g. transactions near quarter-end). | Transaction: "Shopper C purchased $100 Shop Dollars on 3/31/26 11:58 PM UTC." Confirm this is included in Q1 2026 liability and in Q1 MSB Call Report (TA90/TA100, ST90/ST100), not Q2. | Monthly or quarterly sample; mandatory for quarter-end close | [Accounting reviewer] | Sample selection log; evidence that each sampled transaction is in correct period and amount; reviewer sign-off | D / I / O |
| **MTL-SV-03** | Stored value liability | Liability movement is understood and reviewed by management | Designated **management reviewer** reviews the **stored value liability rollforward** (opening balance + purchases − redemptions − refunds/expiry/breakage = closing balance) and approves before financial close and/or regulatory submission. | Example: Opening liability $500K; +$200K purchases, −$150K redemptions, −$2K breakage = $548K closing. Management reviews rollforward and signs off. | Before each quarter-end close and before MSB Call Report submission | [Designated manager, e.g. Accounting lead] | Signed management review memo or checklist; reference to rollforward and key metrics | D / I / O |

### 1a. Stored value liability – reconciliation to third party

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-SV-04** | Stored value liability | Liability is independently verified by third-party cash balance | Reconcile **stored value liability (GL)** to **FBO account balance per bank statement** (third party). Document known timing/operating differences (e.g. ACH in transit, fees, sweep to/from interest-bearing placement). Investigate unexplained variances above threshold. Where 100% of customer funds are held in FBO, liability and bank balance should align apart from documented items. | Month-end: GL liability $548K; FBO bank statement balance $547K; difference $1K = ACH in transit (documented). Recon workpaper shows liability vs bank with clear explanation of variance. | At least monthly; before quarter-end and MSB submission | [Accounting preparer] | Signed reconciliation (liability vs bank statement); variance log with explanations | D / I / O |

---

## 2. Revenue (fees and breakage)

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-REV-01** | Stored value fee revenue (e.g. FC430) | Fee revenue is recognized in the correct period and amount per policy | Apply a **defined policy** for recognition of any fees on Shop Dollars (e.g. load fees, inactivity fees). Record revenue in the period earned; reconcile fee revenue to underlying transaction or billing data. | Example: No fee on load today; if later "Shopper D pays $2 load fee for $50 Shop Dollars," revenue of $2 is recorded in the period the fee is charged and reconciled to fee transaction log. | Each period where fee revenue exists; review at quarter-end | [Accounting preparer / reviewer] | Revenue reconciliation (GL fee revenue to fee transaction detail); policy document | D / I / O |
| **MTL-REV-02** | Breakage (unclaimed stored value) | Breakage is estimated and recognized in accordance with policy and consistently applied | Document a **breakage policy** (e.g. when balance is deemed abandoned, lookback period, method). Calculate breakage (e.g. by cohort or rate) and record to revenue and reduction of liability. **Management review** of breakage estimate and liability impact before close. | Example: $10K of Shop Dollars balances are deemed abandoned per policy (e.g. 12 months inactive). Reduce liability $10K, recognize $10K breakage revenue; management reviews and approves. | At least quarterly when breakage is material; otherwise per policy (e.g. annual) | [Accounting preparer]; [Designated manager] | Breakage policy; calculation workpaper; management sign-off on estimate and journal entry | D / I / O |

---

## 3. Cash / FBO accounts

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-CASH-01** | FBO bank account(s) | Cash balance per bank agrees to books and is reconciled to stored value liability | Perform **bank reconciliation** for each FBO account: bank statement balance vs GL cash. Reconcile **FBO cash (GL)** to **stored value liability** (or explain timing differences, e.g. in-transit, fees). Investigate and resolve variances above threshold. | Example: Shopper A's $50 purchase results in $50 in FBO; Shopper B's $25 redemption reduces FBO by $25. Reconciliation shows FBO bank = $X, GL cash = $X, liability = $X; any difference (e.g. ACH in transit) documented. | At least monthly; before quarter-end and before MSB submission | [Accounting preparer] | Signed bank reconciliation; liability vs cash reconciliation; variance log | D / I / O |
| **MTL-CASH-02** | FBO cash | Reconciliations are reviewed and approved by someone other than preparer | A **reviewer** (different from preparer) reviews the FBO bank reconciliation and liability-to-cash reconciliation for completeness, reasonableness, and resolution of variances. Signs off before close. | Same as MTL-CASH-01; reviewer confirms $50 purchase and $25 redemption are reflected in bank and GL and that liability ties. | Same as MTL-CASH-01 | [Accounting reviewer] | Reviewer sign-off on reconciliation package (date, name) | D / I / O |

---

## 4. Data feeding MSB Call Report (regulatory vs books)

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-REG-01** | MSB Call Report (FC220, TA90/100, ST90/100) | Figures in the MSB Call Report agree to the general ledger and supporting schedules | Before NMLS submission, **reconcile** key MSB Call Report fields to GL and workpapers: e.g. **FC220** (outstanding stored value) = GL stored value liability; **TA90/TA100** = count/sum of issuance transactions for the quarter from transaction ledger; **ST90/ST100** = same by state. Document in a pre-submission checklist or reconciliation. | Example: Q1 2026 report. FC220 = $548K must equal GL liability at 3/31/26. TA90 = 15,000 and TA100 = $1.2M must equal count and sum of all completed Shop Dollars purchase transactions in the quarter from the transaction system. ST90 for PA = 3,000 must equal count of those purchases where user_state = PA. | Every quarter before MSB Call Report submission | [NMLS preparer / Accounting] | Reconciliation workpaper (MSB fields to GL/ledger); pre-submission checklist with sign-off | D / I / O |
| **MTL-REG-02** | MSB Call Report submission | Submission is reviewed and approved by designated person; restatement/escalation per policy | Per **Financial Reporting Policy**: (1) Designated **reviewer/approver** reviews the MSB Call Report (and reconciliation in MTL-REG-01) before submission. (2) If the report includes a **material restatement**, **material error**, or other **material matter**, escalate to a Board member before submission. Document review and any escalation. | Example: Q1 2026 report prepared. Reviewer confirms FC220, TA90/100, ST90/100 tie to GL and transaction ledger. No restatement → approve and submit. If Q4 2025 were being restated, escalation to Board per policy before submitting. | Every quarter | [Designated reviewer]; [NMLS filer] | Review sign-off; escalation log if applicable | D / I / O |

### 4a. MSB / transaction volume – reconciliation to third party

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-REG-03** | Issuance volume (TA90, TA100) | Issuance count and dollar volume are independently verified by bank or processor | Reconcile **TA90 (count)** and **TA100 (dollar sum)** of Shop Dollars purchases to **third-party source**: e.g. **bank statement** (count/sum of ACH credits or identified funding transactions into FBO) or **payment processor report** (e.g. card funding transactions into FBO). Document and resolve variances (e.g. timing, fees, refunds). | Q1 2026: Internal ledger shows 15,000 purchases, $1.2M. Bank or processor report shows 15,000 credits to FBO, $1.198M (e.g. $2K fees netted). Recon documents alignment and explains $2K. | Every quarter before MSB submission | [Accounting preparer] | Reconciliation workpaper (TA90/TA100 vs bank/processor report); variance explanation | D / I / O |
| **MTL-REG-04** | Redemption volume | Redemption outflow is independently verified by payment partner | Reconcile **total redemptions** (dollar amount and optionally count) from internal ledger to **payment partner report** (e.g. payouts from SFS/Shop Dollars to Stripe or other partner for merchant settlements). Document timing and any reconciling items. | Q1 2026: Internal ledger shows $150K redemptions (Shoppers paid merchants via Shop Dollars). Payment partner payout report shows $150K (or $149.5K with timing). Recon documents alignment. | Every quarter (or monthly when volume is material) | [Accounting preparer] | Reconciliation workpaper (redemption ledger vs partner payout report) | D / I / O |

---

## 5. Segregation of duties and access

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-SOD-01** | All MTL financial processes | No single person can initiate, record, reconcile, and approve the same flow | Document and enforce **role split**: (1) **Preparer** – runs reports, prepares reconciliations, drafts MSB Call Report. (2) **Reviewer** – reviews reconciliations and report. (3) **Approver** – approves submission (or delegates per policy). (4) **NMLS filer** – submits in NMLS (may be same as approver but not same as sole preparer for same report). For journal entries: person who posts is different from person who approves, where feasible. | Example: Person A prepares liability reconciliation and MSB Call Report; Person B reviews and approves; Person B (or designated filer) submits to NMLS. Person A cannot submit without B's review. | Ongoing; reviewed when roles change | [Management / Compliance] | Role matrix (names/roles); access review log | D / I / O |
| **MTL-SOD-02** | Transaction / ledger systems | Access to systems that can change financial data or submit reports is limited and reviewed | **Access controls**: Only authorized personnel have access to (a) post or adjust stored value liability/revenue in the GL, (b) modify transaction data that feeds liability/TA/ST, (c) submit MSB Call Report in NMLS. Periodic **access review** (e.g. quarterly or at role change). | Example: Only designated accounting and product support roles can affect Shop Dollars balances or reporting data; NMLS credentials limited to designated filer(s). Access list reviewed quarterly. | At least quarterly access review; when roles change | [IT or process owner; Management] | Access list; access review sign-off | D / I / O |

---

## 6. Change management

| Control ID | Process / account | Control objective | Control description | Example MTL transaction | Frequency | Owner | Evidence | Status |
|------------|-------------------|-------------------|---------------------|-------------------------|-----------|--------|----------|--------|
| **MTL-CHG-01** | Calculation logic, mappings, reports | Changes that affect liability, revenue, or MSB reporting are documented and reviewed before go-live | **Change process**: Any change to (a) how stored value liability or revenue is calculated, (b) mapping from product/ledger to GL or to MSB Call Report fields, or (c) logic of reports used for close or submission must be **documented** (what changed, why) and **reviewed/approved** by a designated person (e.g. Accounting lead) before production. Where applicable, test with sample MTL transactions. | Example: New product feature adds a "partial redemption" (e.g. use $10 of $50 balance). Change to liability calculation and to TA/ST logic is documented; Accounting reviews and approves before release; post-release spot-check that a $10 redemption reduces liability by $10 and appears in TA/ST correctly. | Per change | [Product/Eng for build]; [Accounting for review] | Change log; review/approval; test results if applicable | D / I / O |

---

## 7. Summary – what to build now

| Priority | Control IDs | What to build |
|----------|-------------|----------------|
| **1** | MTL-SV-01, MTL-CASH-01, MTL-REG-01 | **Reconciliations (internal):** (1) GL stored value liability to transaction ledger / customer balance rollforward. (2) FBO bank to GL; GL cash to liability. (3) MSB Call Report (FC220, TA90/100, ST90/100) to GL and transaction ledger. Templates, owner, reviewer, sign-off. |
| **1a** | **MTL-SV-04, MTL-REG-03, MTL-REG-04** | **Reconciliations (third party):** (1) Stored value liability to **FBO bank balance**. (2) TA90/TA100 to **bank or payment processor** funding report. (3) Redemption volume to **payment partner** payout report. Stronger evidence; build where external source is available. |
| **2** | MTL-SV-03, MTL-CASH-02, MTL-REG-02 | **Review and approval:** Management review of liability rollforward; reviewer sign-off on FBO and liability reconciliations; designated review and approval of MSB Call Report before submission (and escalation per Financial Reporting Policy). |
| **3** | MTL-SV-02, MTL-REV-01, MTL-REV-02 | **Cut-off and revenue:** Sample review of issuance/redemption period and amount; fee revenue policy and reconciliation; breakage policy, calculation, and management review. |
| **4** | MTL-SOD-01, MTL-SOD-02 | **Segregation and access:** Role matrix (preparer, reviewer, approver, NMLS filer); access rights to GL, transaction data, NMLS; periodic access review. |
| **5** | MTL-CHG-01 | **Change management:** Process for documenting and reviewing changes to liability/revenue logic and to MSB report mappings. |

### Control source – internal vs third party

| Control ID | Source | Third-party source (where applicable) |
|------------|--------|--------------------------------------|
| MTL-SV-01, MTL-SV-02, MTL-SV-03 | Internal | — |
| **MTL-SV-04** | **Third party** | FBO bank statement |
| MTL-REV-01, MTL-REV-02 | Internal | (Fee revenue: consider processor fee report or bank if fees identifiable) |
| MTL-CASH-01, MTL-CASH-02 | Third party | Bank statement (FBO) |
| MTL-REG-01, MTL-REG-02 | Internal | — |
| **MTL-REG-03** | **Third party** | Bank or payment processor funding report |
| **MTL-REG-04** | **Third party** | Payment partner payout report |
| MTL-SOD-01, MTL-SOD-02, MTL-CHG-01 | Process / governance | — |

---

## 8. Example MTL transactions – quick reference

| Example | Control(s) it supports |
|---------|-------------------------|
| Shopper purchases $50 Shop Dollars (issuance) | MTL-SV-01, MTL-SV-02, MTL-SV-03, MTL-SV-04, MTL-CASH-01, MTL-REG-01, **MTL-REG-03** (issuance to bank/processor) |
| Shopper redeems $25 Shop Dollars at merchant (redemption) | MTL-SV-01, MTL-SV-02, MTL-SV-03, MTL-SV-04, MTL-CASH-01, **MTL-REG-04** (redemptions to payment partner) |
| Quarter-end liability rollforward (opening + purchases − redemptions − breakage = closing) | MTL-SV-01, MTL-SV-03, MTL-REG-01 (FC220) |
| Stored value liability $548K vs FBO bank balance $547K (e.g. $1K in transit) | **MTL-SV-04** (third party) |
| FBO bank statement vs GL cash vs liability | MTL-CASH-01, MTL-CASH-02 (bank = third party) |
| TA90/TA100 vs bank or processor funding report | **MTL-REG-03** (third party) |
| Redemption ledger vs payment partner payout report | **MTL-REG-04** (third party) |
| MSB Call Report FC220 = $548K; TA90 = 15,000; ST90 PA = 3,000 | MTL-REG-01, MTL-REG-02 |
| Breakage: $10K abandoned balance recognized as revenue | MTL-REV-02, MTL-SV-03 |
| New product feature changes how redemptions reduce liability | MTL-CHG-01 |

---

**Owner:** [Global Accounting / Finance Lead]  
**Review:** Update control owners and status (D/I/O) as controls are implemented; align with Internal Audit when SFS/MTL is in SOX scope.
