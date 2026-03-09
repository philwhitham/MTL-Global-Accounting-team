# Wind-Down Plan — Shopify Financial Services (UK and EU/Luxembourg)

**Entity (UK):** [UK Entity Name TBD] — see Gap 1
**Entity (EU/Luxembourg):** [Luxembourg Entity Name TBD] — see Gap 1
**Ultimate parent:** Shopify Inc. (NASDAQ: SHOP), a publicly traded Canadian corporation
**Regulator (UK):** Financial Conduct Authority (FCA)
**Regulator (EU/Luxembourg):** Commission de Surveillance du Secteur Financier (CSSF)
**Document type:** Wind-down plan
**Status:** Initial draft — significant gaps remain; see Gap Register at end of document
**Last updated:** March 2026
**Classification:** Confidential

---

> **How to read this document:** Content drawn directly from existing internal documentation is marked with its source in parentheses. Proposed or designed treatment not yet confirmed in a source document is marked **[DESIGNED]**. Information required to complete this section but not yet available is marked **[GAP: n]** referencing the Gap Register at the end of the document.

---

## Part A — Entity and Business Overview

### A.1 Corporate structure

The following group structure is confirmed in the Shopify Financial Services Inc. Business Plan:

```
Shopify Inc. (Canadian public company, NASDAQ: SHOP)
    ↓
Shopify Holdings (USA) 2 Inc. (Delaware corporation)
    ↓
Shopify Financial Services Inc. (Delaware corporation, formed 18 December 2024)
    ↓
[UK Entity] — [GAP: 1]
[Luxembourg Entity] — [GAP: 1]
```

*Source: Business Plan, Section 1 and Section 7*

**[GAP: 1]** The legal names, jurisdiction of incorporation, date of formation, and precise position in the corporate group of the UK entity and the Luxembourg entity are not yet documented in any internal source. These must be confirmed and inserted before this plan is submitted to either regulator.

### A.2 Business model — products and services

The following is confirmed for the US entity (Shopify Financial Services Inc.) from the Business Plan and SOX Process Narrative. **[DESIGNED]** The UK and Luxembourg entities are expected to operate materially similar stored value products within their respective regulatory perimeters, subject to local regulatory requirements.

**Product:** Stored value digital wallet (known in the US as "Shop Pay Wallet Balance"). Integrated into the Shop App and Shop Pay checkouts. Enables buyers to pre-fund purchases and make payments to merchants.

**Two stored value liabilities are in scope** *(SOX Process Narrative, §1)*:

1. **Buyer Stored Value Liability** — funds loaded into and held in the Shop Pay Wallet Balance by buyers. Created by ACH deposits from the buyer's external bank account; extinguished by payments to merchants, withdrawals to external bank, or breakage.

2. **Merchant Stored Value Liability** — funds credited to the merchant wallet from buyer payments. Created by card settlement proceeds or Shop Dollars redemptions; extinguished by merchant payouts to external bank, card-funded refunds, or (future state) application toward Shopify-billed obligations.

**Transaction types in scope** *(SOX Process Narrative, §3)*:
- Buyer ACH funding (liability created; 2–3 business day settlement)
- Merchant payment (internal transfer; no external funds movement)
- Split payment (stored value portion + card portion in parallel)
- Refunds — Case A (original payment was stored value; internal reversal) and Case B (original payment was card; funds leave FBO)
- Buyer withdrawal via ACH credit (liability extinguished; 2–3 business day settlement)
- Card settlement into merchant wallet (Merchant Stored Value Liability created)
- Merchant payout (Merchant Stored Value Liability extinguished)
- Interest income on FBO balances

**Revenue model** *(Business Plan, Section 4)*: Shopify FS offers the wallet to buyers free of charge and generates income from interest on funds held in FBO accounts. Shopify Inc. reimburses Shopify FS for its costs plus a profit element pursuant to one or more intercompany agreements. **[GAP: 2]** Confirm whether the UK and Luxembourg entities will operate the same revenue model, and whether separate intercompany agreements will be in place for each entity.

**Restrictions on use** *(Business Plan, Section 3.1)*: Buyers may only withdraw funds to their own external bank accounts or use funds to pay merchants. P2P transfers are not permitted. Buyers cannot transact with merchants that are not Shopify merchants.

**[GAP: 3]** Confirm the geographic scope of the UK and Luxembourg products — which countries, currencies, and merchant types will be in scope for each entity.

### A.3 Capitalization

*(Business Plan, Section 5)*: "Shopify will support the ongoing capital requirements of Shopify FS, and will provide capital infusions into Shopify FS as needed in order for Shopify FS to maintain its minimum net worth requirements."

**[GAP: 4]** Confirm: (a) whether the same capital support commitment applies to the UK and Luxembourg entities; (b) whether this commitment is documented in a binding legal instrument for each entity; (c) the minimum regulatory capital requirements for each entity under FCA and CSSF rules respectively. The FCA's TR22/1 guidance requires that intragroup capital support be documented as committed and not merely assumed.

### A.4 Intercompany services and intragroup dependencies

*(Business Plan, Section 7)*: Shopify FS (US) and Shopify Inc. have entered into an Intercompany Services Agreement under which Shopify Inc. provides the following services to Shopify FS:

| Service | Description |
|---|---|
| Administrative services | Mail, facilities, benefits administration, HR administration |
| Accounting and treasury services | General accounting, accounts payable, invoicing, tax, treasury |
| Technical services | Telecommunications, hardware/software, network services, data warehousing, platform integration |
| Fraud and risk monitoring | Access to Shopify Inc. fraud and risk monitoring systems and infrastructure |
| Cybersecurity services | Cybersecurity program protecting confidentiality, integrity, and availability of information systems |

Shopify FS relies on shared employees with Shopify Inc. Shopify Inc. employs approximately 8,100 full-time employees (as of the Business Plan date). Shopify FS intends to make dedicated employee hires as necessary to support its business volume.

**[GAP: 5]** Confirm: (a) whether equivalent intercompany service agreements will be in place for the UK and Luxembourg entities; (b) which services each entity will be dependent on Shopify Inc. for; (c) whether any services will be provided locally or via a different group entity. This is a required input for the FCA intragroup dependency analysis (Section H of this plan) and for the CSSF outsourcing exit plan (Circular CSSF 22/806).

---

## Part B — Customer Fund Identification and Prompt Return

*Addresses: Overlapping requirement 1.1 — FCA "Our Approach" paras 3.73–3.76; CSSF Circular 26/906 Chapter 8*

### B.1 System of record for individual customer balances

*(SOX Process Narrative, §2)*: Individual buyer balances and individual merchant balances are recorded in the product system (currently the Shop App / Shopify platform; transitioning to a Standalone Ledger that is being built as part of the Shopify FS product). The accounting general ledger of record is NetSuite.

The FBO bank account(s) at the bank partner hold all buyer and merchant funds in an omnibus account. The FBO bank balance should equal the sum of both liabilities (Buyer Stored Value Liability + Merchant Stored Value Liability) at all times, subject to timing items (ACH in-transit, card settlements in-transit) and accrued interest not yet swept. *(SOX Process Narrative, §1)*

For the US entity, the FBO accounts are held at Citi (accounts 11623 CLE USD and 11624 OPS USD). *(SOX Process Narrative, §2)*

**[GAP: 6]** Confirm the banking partner(s) for the UK and Luxembourg entities and the account structure. The FCA's Resolution Pack requirement (PS25/12, effective 7 May 2026) requires identification of all banking partners and custodians holding safeguarded funds. This cannot be completed until UK and Luxembourg banking arrangements are confirmed.

### B.2 Fund segregation

*(Business Plan, Section 3.1)*: All funds received in connection with the stored value product are held in segregated omnibus FBO accounts at one or more federally insured financial institutions, titled in Shopify FS's name and held for the benefit of buyers. FBO accounts are fully segregated from Shopify FS operating funds.

**[DESIGNED]** The UK and Luxembourg entities will maintain equivalent segregation of customer funds in safeguarding accounts per FCA and CSSF requirements respectively, separate from the entities' own operating funds.

### B.3 Process for extracting all customer balances on demand

*(SOX Process Narrative, §4 Step 2 and Step 3)*: At each period-end, the accounting team performs separate reconciliations of:
- Buyer Stored Value Liability (GL balance vs sum of individual buyer balances in the product system or rollforward)
- Merchant Stored Value Liability (GL balance vs sum of individual merchant balances in the product system or rollforward)

**[GAP: 7]** Document the specific process and system capability for extracting a complete, individual-level balance file for all buyers and all merchants on demand — not just at period-end. The FCA's primary requirement for a PI/EMI wind-down plan is that customer funds can be identified and returned promptly, without needing to reconstruct data. The extraction process, responsible system, responsible team, and estimated time to complete a full extraction must be documented. The Standalone Ledger (in build) is expected to be the system capable of this — confirm once built.

### B.4 Fund return process and estimated timeline

**[DESIGNED]** Upon a wind-down decision:

1. No new buyer funding transactions will be accepted.
2. Existing buyer balances will be returned via ACH credit to the buyer's linked external bank account (mirroring the existing withdrawal process documented in SOX Process Narrative §3.5). Settlement time: 2–3 business days per transaction.
3. Merchant balances will be paid out to merchant external bank accounts (mirroring the existing merchant payout process documented in SOX Process Narrative §3.8).
4. Any in-flight ACH transactions at the time of wind-down will be completed before the FBO account is closed.

**[GAP: 8]** The following must be determined and documented:
- Maximum total volume of buyer balances and merchant balances at any point in time (used to estimate return timeline and resource requirements)
- Whether buyer return can be processed automatically through the existing ACH infrastructure or requires manual processing
- Timeline for processing all returns (number of transactions × settlement time)
- Process for buyers who cannot be reached or whose linked bank account is closed
- Treatment of unclaimed balances (applicable state escheatment law for UK; applicable Luxembourg law for EU)

---

## Part C — Wind-Down Scenarios and Triggers

*Addresses: Overlapping requirements 1.2 and 1.4; FCA-specific requirements 2.1 and 2.4*

### C.1 Wind-down scenarios

**[DESIGNED]** Two distinct wind-down scenarios are contemplated, consistent with the FCA WDPG and multi-firm review requirements:

**Scenario 1 — Solvent wind-down (primary scenario):** The entity voluntarily exits the market with sufficient resources to meet all obligations. All customer funds are returned in full. All contractual obligations are met. The wind-down is completed before the entity's resources are exhausted.

**Scenario 2 — Insolvent wind-down (accelerated liquidation):** The entity cannot meet all obligations. An insolvency practitioner is appointed. Customer funds held in the FBO account remain segregated and are returned to customers as a priority claim. The entity's own creditors are settled from remaining assets.

**Note:** In both scenarios, customer funds (FBO account balance) are not available to meet the entity's own obligations — they are held for the benefit of customers and must be returned regardless of the entity's solvency position. This is a function of the segregation structure described in Part B.

**[GAP: 9]** For each scenario, the following sub-analyses are required (FCA multi-firm review requirement):
- Separate cashflow model (see Part H)
- Identification of which wind-down triggers would most likely lead to each scenario
- Insolvency practitioner identified or engagement process documented for Scenario 2

### C.2 Wind-down triggers

**[GAP: 10]** No wind-down triggers are currently documented in any internal source for the UK or Luxembourg entities. This is a required element of the wind-down plan for both the FCA (TR22/1 specifically criticized firms for using vague triggers) and the CSSF (Circular CSSF 26/906 requires an "appropriate response capability in the event of a crisis," which requires pre-defined activation criteria).

The following trigger categories are proposed as a starting framework **[DESIGNED]** and must be reviewed, quantified, and approved by the Board before this plan is submitted:

| Trigger category | Proposed metric | Amber threshold | Red threshold |
|---|---|---|---|
| Regulatory capital | Own funds as % of minimum requirement | [TBD] | [TBD] |
| Liquidity | Operational cash (excluding FBO) relative to 90-day projected operating costs | [TBD] | [TBD] |
| Regulatory standing | Loss of licence / material regulatory action | N/A — immediate escalation | Licence suspended or revoked |
| Banking partner | Loss of primary banking partner with no confirmed replacement | Notice of termination received | Termination effective |
| Intragroup support | Withdrawal or reduction of Shopify Inc. intercompany support | Notice of material reduction | Effective withdrawal |
| Reputational | Material regulatory enforcement action or public enforcement notice | [TBD] | [TBD] |

Each trigger must have: a defined monitoring frequency, a responsible owner, and an escalation path to Board.

### C.3 Reverse stress testing

*Applies to UK plan only — FCA requirement: TR22/1; FG20/1*

**[GAP: 11]** A reverse stress test has not been performed. The reverse stress test must work backwards from the point of non-viability to identify which combination of events would render the entity unable to complete an orderly wind-down. Results must be used to calibrate capital buffer sizing and trigger thresholds. This requires input from Finance and must be reviewed and approved by the Board.

---

## Part D — Operational Wind-Down Procedures

*Addresses: Overlapping requirement 1.3 — termination of contracts and pending operations*

### D.1 Contract register

**[GAP: 12]** A register of all material contracts for the UK and Luxembourg entities, including termination notice periods and break costs, does not exist in any current internal document. This is a required deliverable. For the UK entity, contract termination costs were identified by the FCA multi-firm review as a frequently underestimated liability in wind-down cashflow models.

The following contract categories are expected to be in scope **[DESIGNED]**:

| Contract category | Counterparty type | Notes |
|---|---|---|
| Banking / FBO account | Bank partner (UK/EU equivalent of Citi for US entity) | [GAP: 6] |
| Payment processing | Payment partners (Stripe, PayPal, or equivalent) | [GAP: 5] |
| Intercompany services | Shopify Inc. | [GAP: 5] |
| Technology / platform | Shopify Inc. (Shop App, Standalone Ledger) | [GAP: 5] |
| Regulatory / legal advisers | External counsel | [GAP: 14] |
| Premises | Registered office / operational premises | [GAP: 1] |
| Data processing / cloud | Third-party data processors | [GAP: 5] |

### D.2 Sequencing of contract terminations

**[DESIGNED]** The following sequencing is proposed and must be confirmed with legal counsel:

1. Notify FCA and/or CSSF of wind-down decision (before counterparties)
2. Suspend acceptance of new buyer funding transactions
3. Complete all in-flight transactions (ACH fundings, merchant payouts, withdrawals)
4. Return all buyer balances via ACH credit
5. Return all merchant balances via payout
6. Terminate merchant agreements
7. Terminate payment partner agreements
8. Close FBO account(s) once balance is zero
9. Terminate banking partner agreement
10. Terminate intercompany services agreement with Shopify Inc.
11. Terminate remaining contracts (legal, premises, data processors)
12. Deregister / surrender licences

### D.3 Handling of in-flight transactions at point of closure

*(SOX Process Narrative, §3.1 and §3.5)*: ACH transactions settle in 2–3 business days. At the point of wind-down, any ACH transactions initiated but not yet settled must be completed before the FBO account can be closed. The number of days required to clear in-flight transactions before closure can begin is therefore a minimum of 3 business days from the date the last transaction is initiated.

**[GAP: 13]** Define the cut-off procedure for in-flight transactions at point of wind-down: at what point does the entity stop accepting new transactions, and what is the process for monitoring and confirming all in-flight transactions have settled before the FBO account is closed.

---

## Part E — IT and Operational Resilience

*Addresses: Overlapping requirement 1.5 — FCA multi-firm review; TR22/1; CSSF Circular CSSF 20/750*

### E.1 Critical IT systems and dependencies

*(SOX Process Narrative, §2 and Business Plan, Section 7)*: The following systems are critical to the stored value product:

| System | Owner | Wind-down relevance |
|---|---|---|
| Shop App / Shopify platform | Shopify Inc. (product/engineering) | Source of individual buyer and merchant balance data; must remain accessible for customer balance extraction |
| Standalone Ledger (in build) | Shopify Inc. (product/engineering) | Will be the product-level transaction ledger; must remain accessible post-closure for balance extraction and audit trail |
| NetSuite (Subsidiary 87) | Shopify Finance / Accounting | Accounting GL; must remain accessible for period-end close and regulatory reporting during wind-down |
| BigQuery | Shopify Inc. (Data Engineering) | Transaction data warehouse; must remain accessible for transaction-level data during wind-down |
| FBO account(s) | Bank partner | Must remain operational until all customer funds are returned and balance is zero |
| Payment Partners (Stripe, PayPal) | Third party | Must remain operational until all merchant payouts and buyer withdrawals are processed |

**[GAP: 5]** All critical systems listed above (except the FBO account and payment partners) are provided by Shopify Inc. under the Intercompany Services Agreement. The wind-down plan must document: (a) whether Shopify Inc. is contractually required to maintain system access during a wind-down period; (b) the minimum duration of continued access required; (c) whether system access can be maintained if Shopify Inc. itself is in financial distress.

### E.2 Data retention

**[GAP: 15]** A data retention policy for the post-wind-down period is not currently documented for the UK or Luxembourg entities. The following minimum requirements apply:

- **UK (FCA):** Regulatory records must be retained for the period specified by FCA rules — typically 5 years for payment service records, longer for AML/financial crime records.
- **Luxembourg (CSSF):** Equivalent retention periods apply under Luxembourg law and CSSF requirements.
- Customer transaction records, customer identity records, and all wind-down workpapers must be retained for the minimum required period after the last transaction date.

### E.3 Cyber controls during wind-down

*(Business Plan, Section 7)*: Shopify Inc. provides cybersecurity services to Shopify FS under the Intercompany Services Agreement, "including support to Shopify FS in maintaining a cybersecurity program that protects the confidentiality, integrity, and availability of Shopify FS' information systems."

**[GAP: 16]** Document which specific cyber controls must remain active during a wind-down period and how they will be maintained as staff numbers reduce. The FCA multi-firm review specifically required firms to address cybersecurity during wind-down — not only during normal operations.

---

## Part F — Non-Financial Resources

*Addresses: Overlapping requirement 1.6 — WDPG "resources" element; CSSF Circular CSSF 26/906*

### F.1 Key roles required for wind-down execution

**[GAP: 17]** No organisational structure for the UK or Luxembourg entities has been documented in any internal source. The following roles are expected to be required for wind-down execution **[DESIGNED]**:

| Role | Function during wind-down |
|---|---|
| Managing Director / CEO (UK or LU entity) | Overall wind-down decision authority and regulatory liaison |
| Chief Financial Officer / Finance Lead | Cashflow monitoring, FBO balance management, regulatory reporting during wind-down |
| Compliance Officer | Regulatory notifications, AML/CTF obligations during wind-down, licence surrender |
| Legal Counsel | Contract terminations, regulatory correspondence, insolvency proceedings if applicable |
| Accounting (preparer) | Customer balance extraction, reconciliations, financial reporting |
| Technology / Engineering | System access management, data extraction, system decommissioning |
| External — Insolvency Practitioner | Required for Scenario 2 (insolvent wind-down) only |
| External — Legal Counsel | Contract terminations, regulatory filings |

### F.2 Staff retention

*(Business Plan, Section 7)*: Shopify FS relies on shared employees with Shopify Inc. under the Intercompany Services Agreement. No dedicated employee headcount for the UK or Luxembourg entities is documented.

**[GAP: 18]** Define: (a) the minimum staffing required to execute a wind-down; (b) whether shared Shopify Inc. employees would remain available to the UK/Luxembourg entities during a wind-down; (c) any retention arrangements for key individuals. The FCA multi-firm review found that firms frequently assumed staff availability during wind-down when in practice key staff had already left.

### F.3 External advisers

**[GAP: 14]** Identify and document: (a) legal counsel for each entity (UK and Luxembourg); (b) insolvency practitioner for the insolvent wind-down scenario; (c) regulatory contacts at FCA and CSSF; (d) banking contacts at the UK and Luxembourg banking partners.

---

## Part G — Stakeholder Communication Plan

*Addresses: Overlapping requirement 1.7 — FCA multi-firm review; CSSF Circular CSSF 26/906*

### G.1 Notification sequence

**[DESIGNED]** The following notification sequence is proposed and must be reviewed by legal counsel and the Board:

1. **FCA / CSSF** — notify before any counterparties or customers; FCA must be informed promptly upon the decision to wind down
2. **Shopify Inc.** — notify as parent and intercompany services provider
3. **Banking partner(s)** — notify FBO account bank
4. **Payment partners** — notify Stripe, PayPal, or equivalent
5. **Merchants** — notify that the stored value product will be wound down; inform of the timeline for final payouts
6. **Buyers** — notify that the wallet will be closed; instruct on the process for fund return; provide timeline

### G.2 Customer communication

**[GAP: 19]** Draft communication templates for each stakeholder group must be prepared. These must include:
- Key messages for buyers (funds are safe; how to receive return of balance; timeline)
- Key messages for merchants (wallet product closing; final payout process; timeline)
- Regulatory notification letters for FCA and CSSF
- Internal communications to Shopify Inc. management

### G.3 Complaint handling during wind-down

**[GAP: 20]** Define the complaint handling process that will operate during the wind-down period. The FCA specifically requires that firms address how customer complaints will be handled after a wind-down decision is made.

---

## Part H — Cashflow and Liquidity Modelling

*Applies to UK plan only — FCA requirement: TR22/1; FG20/1*

**[GAP: 21]** A wind-down cashflow model does not currently exist. This is a required deliverable for the UK plan. The model must:

- Project inflows and outflows on a month-by-month basis for approximately 9 months
- Cover both Scenario 1 (solvent) and Scenario 2 (insolvent) separately
- Demonstrate the entity remains cash-positive at all times (not merely at period-end)
- Exclude customer funds (FBO balance) from the entity's own liquidity analysis
- Quantify the TC 2.4 wind-down capital buffer required

**Confirmed inputs available for the model:**

| Input | Source | Notes |
|---|---|---|
| Revenue model | Business Plan, Section 4 | Interest income on FBO balances only; no transaction fees |
| Capital support | Business Plan, Section 5 | Shopify Inc. commits to provide capital infusions as needed — however, the FCA requires this to be documented as a committed facility, not assumed. See [GAP: 4] |
| Operating cost structure | [GAP: 22] | Operating costs for UK/Luxembourg entities not documented |
| Contract termination costs | [GAP: 12] | Requires contract register — see Part D |
| Redundancy costs | [GAP: 18] | Requires headcount plan — see Part F |
| Regulatory filing costs during wind-down | [GAP: 14] | Requires external adviser identification |

---

## Part I — Intragroup Dependency Analysis

*Applies to UK plan only — FCA requirement: TR22/1*

### I.1 Known intragroup dependencies

*(Business Plan, Section 7)*: The following services are provided by Shopify Inc. to Shopify FS (US) under the Intercompany Services Agreement. **[DESIGNED]** Equivalent dependencies are expected to exist for the UK and Luxembourg entities.

| Dependency | Type | Would it continue during wind-down? |
|---|---|---|
| Administrative services (HR, facilities, mail) | Operational | [GAP: 5] |
| Accounting and treasury services | Financial / operational | [GAP: 5] |
| Technical services (IT, platform, data) | Operational | [GAP: 5] |
| Fraud and risk monitoring | Operational | [GAP: 5] |
| Cybersecurity services | Operational | [GAP: 5] |
| Capital support | Financial | Committed per Business Plan but not confirmed as a legally binding facility — see [GAP: 4] |
| Intercompany receivables / payables | Financial | [GAP: 23] |

### I.2 Standalone viability assessment

**[GAP: 24]** The FCA requires the plan to demonstrate that the entity can execute a wind-down on a standalone basis — without assuming that Shopify Inc. will provide continued support. A standalone viability analysis must assess: which of the above dependencies can be replaced with third-party arrangements during wind-down; what the cost and time of doing so would be; and whether the entity can complete the wind-down if Shopify Inc. support is withdrawn simultaneously.

---

## Gap Register

The following gaps must be resolved before this plan is submitted to the FCA or CSSF. Gaps are listed in the order they appear in the plan.

| Gap | Description | Section | Owner | Priority |
|---|---|---|---|---|
| 1 | Legal name, jurisdiction, date of formation, and position in corporate group of UK entity and Luxembourg entity | A.1 | Legal | Critical — cannot submit without |
| 2 | Confirm revenue model and intercompany agreement structure for UK and Luxembourg entities | A.2 | Finance / Legal | High |
| 3 | Confirm geographic scope of UK and Luxembourg products (countries, currencies, merchant types) | A.2 | Product / Legal | High |
| 4 | Confirm capital support commitment for UK/Luxembourg entities; confirm whether commitment is in a binding legal instrument; confirm minimum regulatory capital requirements | A.3, H | Finance / Legal | Critical |
| 5 | Confirm intercompany services arrangements for UK/Luxembourg entities; identify which services are dependent on Shopify Inc. and whether those services would continue during wind-down | A.4, D.1, E.1, I.1 | Legal / Operations | Critical |
| 6 | Confirm banking partner(s) for UK and Luxembourg entities and FBO account structure | B.1, D.1 | Treasury / Banking | Critical |
| 7 | Document process and system for extracting individual-level customer balance file on demand; confirm system capability and responsible team | B.3 | Product / Engineering | Critical |
| 8 | Determine maximum expected customer fund volume; document process for returning funds to unreachable customers; confirm escheatment obligations | B.4 | Finance / Legal / Compliance | High |
| 9 | Complete sub-analysis for each scenario (cashflow model, trigger mapping, insolvency practitioner) | C.1 | Finance / Legal | High |
| 10 | Define and quantify wind-down triggers with amber and red thresholds for each metric; obtain Board approval | C.2 | Finance / Risk / Board | Critical |
| 11 | Perform reverse stress test; link results to capital buffer sizing and trigger thresholds; obtain Board sign-off (UK only) | C.3 | Finance / Risk | High (UK only) |
| 12 | Prepare contract register for UK and Luxembourg entities with termination notice periods and break costs | D.1 | Legal | Critical |
| 13 | Define in-flight transaction cut-off procedure for wind-down | D.3 | Product / Operations | Medium |
| 14 | Identify legal counsel and insolvency practitioner for each entity | F.3 | Legal | High |
| 15 | Prepare data retention policy for post-wind-down period for UK and Luxembourg entities | E.2 | Legal / Compliance / IT | High |
| 16 | Document cyber controls to remain active during wind-down as staff reduce | E.3 | IT / Security | Medium |
| 17 | Document organisational structure for UK and Luxembourg entities including headcount and reporting lines | F.1 | HR / Legal | Critical |
| 18 | Define minimum staffing for wind-down execution; confirm availability of shared Shopify Inc. employees; document any retention arrangements | F.2 | HR / Legal | High |
| 19 | Draft stakeholder communication templates (buyers, merchants, FCA, CSSF, Shopify Inc.) | G.2 | Legal / Compliance / Communications | High |
| 20 | Define complaint handling process during wind-down | G.3 | Compliance / Operations | Medium |
| 21 | Build wind-down cashflow model for approximately 9 months; cover both scenarios; size TC 2.4 buffer (UK only) | H | Finance | Critical (UK only) |
| 22 | Document operating cost structure for UK and Luxembourg entities | H | Finance | Critical |
| 23 | Document intercompany receivable/payable balances and treatment in own funds calculation | I.1 | Finance | High (UK only) |
| 24 | Perform standalone viability analysis — assess ability to wind down without Shopify Inc. group support | I.2 | Finance / Legal | Critical (UK only) |

---

## Resolution Pack Index

*Applies to UK entity only — FCA PS25/12, effective 7 May 2026. This section lists the components required for the Resolution Pack, which is a separate living document from this wind-down plan.*

| Component | Status |
|---|---|
| Master document indexing all Resolution Pack components | [GAP: 6, 17 — entity and banking details needed first] |
| Records differentiating safeguarded funds from operational funds at any point in time | [GAP: 7 — balance extraction process needed] |
| Identity of all banking partners and custodians holding safeguarded funds | [GAP: 6] |
| Identity of all group entities involved in safeguarding operations | [GAP: 1, 5] |
| All third parties supporting safeguarding operations, with access and transfer procedures | [GAP: 5, 6] |
| List of critical personnel essential to safeguarding | [GAP: 17] |
| Standard terms and conditions in client contracts | [GAP: 1 — entity name needed] |
| All safeguarding policies and procedures | [DESIGNED — to be drafted once entity is established] |
| Named SMF accountable for safeguarding (with Board approval) | [GAP: 17] |

---

*This document was prepared using content from the following internal documents: Shopify Financial Services Inc. Business Plan (reviewed January 2026); SOX Process Narrative – Stored Value (February 2026); Financial Reporting Policy Draft (January 2026); WIND_DOWN_PLAN_REQUIREMENTS.md (March 2026). All claims marked as fact-based are drawn from these sources. Content marked [DESIGNED] reflects proposed or intended treatment not yet confirmed in a source document. Content marked [GAP] identifies information required to complete the plan that is not currently available in any internal source.*
