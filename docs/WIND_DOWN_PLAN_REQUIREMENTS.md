# Wind-Down Plan Requirements — UK (FCA) and EU/Latvia (Bank of Latvia Reg. 270)

**Entity:** Shopify Financial Services Inc. (UK) / Latvian applicant entity (EU)
**Purpose:** Requirements analysis to support minimal-compliance wind-down plan design for UK and EU/Latvia licensing applications
**Last updated:** March 2026
**Status:** Draft — Latvian Reg. 270 Annex 10 full text (Latvian-language) not yet reviewed; see outstanding action at end of document

---

## How to use this document

This document maps the wind-down plan requirements of two regulators:

- **UK:** Financial Conduct Authority (FCA) — Payment Institution / EMI authorisation under the Payment Services Regulations 2017 and Electronic Money Regulations 2011
- **EU/Latvia:** Latvijas Banka (Bank of Latvia) — Payment Institution / EMI authorisation under Bank of Latvia Regulation No. 270, governed by the Law on Payment Services and Electronic Money

The document is structured in three sections:

1. **Overlapping requirements** — elements required by both regulators; a single well-drafted section can satisfy both
2. **UK-only requirements** — FCA-specific elements not expressly required by Reg. 270
3. **Latvia-only requirements** — Reg. 270 structural/documentary elements not expressly required by the FCA

**Design principle:** This is a minimal compliance initiative. The plan will be built to meet the requirements of both regulators and nothing more.

---

## Key regulatory sources

| Document | Regulator | Relevance |
|---|---|---|
| Payment Services and Electronic Money – Our Approach (2017, updated 2024) | FCA | Paras 3.73–3.76: primary PI/EMI wind-down plan requirements |
| FCA Handbook – Wind-down Planning Guide (WDPG) | FCA | Core four-component framework (scenarios, plan, resources, processes) |
| Finalised Guidance FG20/1 – Assessing Adequate Financial Resources (2020) | FCA | Prudential risk, capital, liquidity, reverse stress testing |
| TR22/1 – Observations on Wind-Down Planning: Liquidity, Triggers & Intragroup Dependencies (April 2022) | FCA | Specific observations on deficiencies in liquidity modelling, trigger design, and intragroup analysis |
| Multi-Firm Review – Risk Management and Wind-Down Planning at E-Money and Payment Firms | FCA | Good practice benchmarks and common deficiencies observed across PI/EMI firms |
| Policy Statement PS25/12 – Changes to the Safeguarding Regime (August 2025) | FCA | Resolution Pack requirements — effective 7 May 2026; separate from wind-down plan |
| Bank of Latvia Regulation No. 270 (5 December 2022) | Latvijas Banka | Licensing and documentation requirements for PIs and EMIs in Latvia, including Annex 10 (business continuity / wind-down) |
| Law on Payment Services and Electronic Money (Latvia) | Latvijas Banka | Primary legislation underpinning Reg. 270 |

---

## Section 1 — Overlapping requirements (both jurisdictions)

A single plan section addressing each of these requirements will satisfy both the FCA and Latvijas Banka, subject to Latvia's annex formatting requirements (see Section 3).

---

### 1.1 Customer fund identification and prompt return

| | |
|---|---|
| **FCA source** | "Our Approach" paras 3.73–3.76 |
| **Latvia source** | Reg. 270 Annex 6 (safeguarding of user funds) |

**Description:** Records must allow the regulator or an insolvency practitioner to identify each customer's balance and return it without needing to reconstruct data from scratch. For Shopify FS this means individual buyer wallet balances and individual merchant wallet balances must be identifiable at all times from a single authoritative source. The FCA has emphasised this is the **primary focus** of the PI/EMI wind-down plan — unlike general firms, the defining risk for a payment firm is delay in returning customer money.

**What needs to be produced:**
1. Description of the system of record for individual wallet balances (Standalone Ledger / product system)
2. Process for extracting a complete customer balance file on demand
3. Estimated timeline to return all funds to buyers and merchants respectively
4. Confirmation of where funds are held (FBO account at Citi) and how they would be distributed upon wind-down

---

### 1.2 Business continuity and emergency planning

| | |
|---|---|
| **FCA source** | WDPG; "Our Approach" paras 3.73–3.76 |
| **Latvia source** | Reg. 270 Annex 10 |

**Description:** A documented plan covering how the business continues to operate or winds down under defined stress scenarios, covering people, systems, and processes across all payment services. Emergency plans must be effective and supported by regular review procedures to confirm they remain fit for purpose.

**What needs to be produced:**
1. Scenario library (minimum 3–5 plausible scenarios including: financial distress, loss of banking partner, IT failure, loss of key licence)
2. Documented procedures for each scenario
3. Record of testing and review cycles (frequency and responsible party)

---

### 1.3 Termination of contracts and pending operations

| | |
|---|---|
| **FCA source** | WDPG (processes element) |
| **Latvia source** | Reg. 270 Annex 10 Item 5 (Latvian-language text only; description per Latvijas Banka application materials) |

**Description:** Procedures to: (1) complete all pending payment transactions at point of wind-down without creating new obligations; (2) terminate contracts with merchants, buyers, banking partners, and technology providers in the correct sequence; (3) manage prolonged system downtime without leaving obligations unresolved. The FCA multi-firm review identified contract termination costs as a frequently underestimated liability in cashflow models.

**What needs to be produced:**
1. Register of all material contracts with termination notice periods and break costs
2. Sequencing plan for contract terminations (which counterparties are terminated in which order)
3. Procedure for completing in-flight transactions at point of closure
4. Process for handling disputed or unresolved transactions during wind-down

---

### 1.4 Wind-down triggers and monitoring strategy

| | |
|---|---|
| **FCA source** | TR22/1; FG20/1 |
| **Latvia source** | Reg. 270 Annex 10 (emergency plan activation criteria) |

**Description:** Defined conditions that would cause management to initiate a wind-down, supported by a monitoring framework to detect those conditions in advance. The FCA expects triggers to be specific and measurable — qualitative descriptions (e.g. "significant financial difficulty") are not sufficient. Triggers must be actively monitored with defined escalation paths and linked to the firm's risk appetite statement.

**What needs to be produced:**
1. Minimum 3–5 quantified triggers with defined threshold levels (amber early warning + red action threshold for each)
2. Monitoring frequency and responsible owner for each trigger
3. Escalation path from breach of trigger → board notification → wind-down decision
4. Description of how triggers are reviewed and updated (minimum annually)

---

### 1.5 IT and operational resilience

| | |
|---|---|
| **FCA source** | FCA multi-firm review; TR22/1 |
| **Latvia source** | Reg. 270 Annex 11 (IT security policy) |

**Description:** Controls to ensure systems remain operational or fail safely during a wind-down period — covering cybersecurity, system access, data integrity, and continuity of critical processes. Must address: what happens to data after wind-down is complete; how system access is managed when staff numbers reduce; how third-party IT dependencies (e.g. Shopify Inc. shared infrastructure) would be managed. The FCA treats IT failure as a distinct wind-down trigger scenario.

**What needs to be produced:**
1. Description of critical IT systems and dependencies (including intragroup / Shopify Inc. dependencies)
2. Data retention policy covering the post-wind-down period
3. Access control procedures during staff reduction
4. Plan for managing or terminating intragroup IT dependencies on a standalone basis
5. Cyber controls that remain active during wind-down

---

### 1.6 Non-financial resources

| | |
|---|---|
| **FCA source** | WDPG ("resources" element); multi-firm review |
| **Latvia source** | Reg. 270 Annex 10 (continuity arrangements) |

**Description:** Identification of the key people and third-party cooperation required to execute a wind-down. The FCA multi-firm review found that firms frequently underestimate people requirements — assuming staff will be available when in practice key staff may have already left. Must consider staff retention incentives during wind-down; identification of roles that cannot be vacated; external advisers already engaged or on retainer.

**What needs to be produced:**
1. Named roles (not individuals) essential to wind-down execution
2. Staff retention strategy (e.g. retention bonuses, extended notice periods)
3. List of external parties required: legal counsel, insolvency practitioner, banking contacts, regulatory contacts
4. Plan for knowledge transfer if key staff depart before or during wind-down

---

### 1.7 Stakeholder communication plan

| | |
|---|---|
| **FCA source** | FCA multi-firm review |
| **Latvia source** | Reg. 270 Annex 10 (continuity arrangements) |

**Description:** A sequenced plan covering how and when merchants, buyers, regulators, banking partners, and other counterparties are notified. The FCA specifically requires the plan to address: notification sequence (regulator first, then counterparties, then customers); key messages for each audience; how customer complaints during wind-down are handled; and data retention obligations post-closure.

**What needs to be produced:**
1. Stakeholder map with notification sequence
2. Draft communication templates for each stakeholder group (FCA / Latvijas Banka, merchants, buyers, banking partners, technology partners)
3. Regulatory notification obligations and timelines (FCA must be notified promptly upon decision to wind down)
4. Customer complaint handling procedure during wind-down
5. Data retention schedule post-closure

---

## Section 2 — UK-only requirements (FCA)

These elements are expressly required by the FCA and have no direct equivalent in Reg. 270. They are required for the UK application only but should be documented in a way that does not conflict with the Latvia plan.

---

### 2.1 Quantified triggers with specific thresholds

| | |
|---|---|
| **FCA source** | TR22/1; FG20/1 |

**Description:** Triggers must be expressed as measurable metrics with defined numeric thresholds — not qualitative descriptions. TR22/1 specifically criticised firms for using vague triggers. Triggers should cover at minimum: capital adequacy, liquidity, loss of key client or partner, regulatory action, and reputational events. Each trigger should have an early warning indicator (amber) and an action trigger (red). Triggers must be reviewed at least annually and after any material business change.

**What needs to be produced:**
1. Trigger register with: metric, amber threshold, red threshold, monitoring frequency, responsible owner
2. Description of link between triggers and the firm's risk appetite statement
3. Board approval of trigger levels
4. Annual review procedure for trigger levels

---

### 2.2 Detailed cashflow and liquidity modelling

| | |
|---|---|
| **FCA source** | TR22/1; FG20/1 |

**Description:** A bottom-up cashflow model projecting inflows and outflows through the full wind-down period — the FCA expects firms to model approximately 9 months. TR22/1 found that firms frequently: (1) overestimate inflows during wind-down; (2) underestimate contract termination and redundancy costs; (3) fail to model cash timing mismatches. The model must demonstrate the firm remains cash-positive at all times — not merely at period-end. A dedicated wind-down capital buffer (TC 2.4 buffer) must be held and reflected in the model. Customer funds must be excluded from the firm's own liquidity analysis.

**What needs to be produced:**
1. Month-by-month cashflow model for the wind-down period (approximately 9 months)
2. Clearly labelled assumptions for each line item
3. Sensitivity analysis demonstrating the model remains viable under adverse assumptions
4. Identification and sizing of the TC 2.4 wind-down capital buffer
5. Confirmation that customer funds (FBO balance) are excluded from the firm's own liquidity

---

### 2.3 Intragroup dependency analysis

| | |
|---|---|
| **FCA source** | TR22/1 |

**Description:** A complete mapping of all financial and operational dependencies on Shopify Inc. or other group entities. TR22/1 found that firms frequently assumed group support would be available during wind-down without documenting whether it would be contractually committed. The FCA requires the plan to demonstrate the entity can execute a wind-down on a standalone basis. Intragroup receivables must be excluded from own funds. Uncommitted intragroup liquidity facilities cannot be counted as available resources.

**What needs to be produced:**
1. Intragroup dependency register covering: shared IT systems, shared HR/payroll, intercompany loans or credit facilities, shared banking arrangements, treasury support
2. For each dependency: assessment of whether it would continue during wind-down or be withdrawn
3. Standalone wind-down viability assessment (i.e. can the entity wind down without group support?)
4. Treatment of intragroup receivables in own funds calculation

---

### 2.4 Reverse stress testing

| | |
|---|---|
| **FCA source** | TR22/1; FG20/1 |

**Description:** Working backwards from the point of non-viability to identify which combination of events would render the firm unable to wind down in an orderly way. Used to calibrate capital buffers and triggers — if the reverse stress test identifies a scenario that could plausibly occur, the firm's capital buffer or triggers must be adjusted accordingly. Must be reviewed at least annually.

**What needs to be produced:**
1. Documented reverse stress test exercise identifying the combination of events that would cause failure of an orderly wind-down
2. Assessment of the plausibility of each identified scenario
3. Link to capital buffer sizing (how the reverse stress test informed the TC 2.4 buffer level)
4. Board sign-off on the reverse stress test results

---

### 2.5 Solvent vs. insolvent scenario distinction

| | |
|---|---|
| **FCA source** | WDPG; multi-firm review |

**Description:** Two separate and distinct scenario assessments are required. **Solvent wind-down:** the firm voluntarily exits with sufficient resources to meet all obligations — the primary planning scenario. **Insolvent wind-down (accelerated liquidation):** the firm cannot meet all obligations; no buyer is found; an insolvency practitioner is appointed. The FCA multi-firm review specifically identified the accelerated liquidation scenario as frequently absent from firm plans. Each scenario requires different procedures, timelines, resource requirements, and counterparty impacts.

**What needs to be produced:**
1. Separate narrative and cashflow model for each scenario (solvent and insolvent)
2. Identification of which scenario each wind-down trigger would most likely lead to
3. Insolvency practitioner identified (or engagement process described) for the insolvent scenario
4. Customer fund return procedure under each scenario

---

### 2.6 Operability testing

| | |
|---|---|
| **FCA source** | TR22/1; multi-firm review |

**Description:** The plan must be tested — typically through a structured tabletop exercise or run-through — to confirm it is executable. The FCA multi-firm review explicitly criticised firms for submitting generic or off-the-shelf plans not tailored to the firm's actual business model and not tested. Testing must involve the board and key senior management. Results of the test must be documented and gaps remediated. The plan must be reviewed and re-tested after any material change to the business.

**What needs to be produced:**
1. Record of at least one documented testing exercise (tabletop or structured run-through)
2. Participants list (must include board or senior management)
3. Issues or gaps identified during testing
4. Remediation actions taken in response
5. Schedule for future testing (minimum annually and after material business change)

---

### 2.7 Resolution Pack (separate from wind-down plan)

| | |
|---|---|
| **FCA source** | PS25/12 — **effective 7 May 2026** |

**Description:** A living document — **separate from the wind-down plan** — containing all information needed by a resolution authority or insolvency practitioner to identify and return safeguarded funds. Must be retrievable within 48 hours of a request. A named Senior Management Function (SMF) holder is accountable. Board approval required. Inaccuracies must be corrected within 5 business days of discovery.

**What needs to be produced:**
1. Master document indexing all component documents within the Resolution Pack
2. Records differentiating safeguarded funds from operational funds at any point in time
3. Identity of all banking partners and custodians holding safeguarded funds (FBO account details)
4. Identity of all group entities involved in safeguarding operations (entity type, jurisdiction, functions)
5. All third parties supporting safeguarding operations, with access and transfer procedures
6. List of critical personnel essential to safeguarding operations
7. Standard terms and conditions in client contracts
8. All safeguarding policies and procedures
9. Named SMF accountable for safeguarding (with board approval)

---

## Section 3 — Latvia-only requirements (Reg. 270)

These are primarily documentary and structural requirements for the Latvia application package. They do not add substantive wind-down content beyond what is addressed in Sections 1 and 2, but they affect how the content must be packaged and formatted for the Latvijas Banka submission.

---

### 3.1 Annex-based documentary structure

| | |
|---|---|
| **Latvia source** | Reg. 270 licensing process |

**Description:** The wind-down and business continuity content must be presented as **Annex 10** within the Reg. 270 licensing application package. Reg. 270 prescribes a specific numbered annex format — content cannot simply be lifted from the UK wind-down plan document. The Annex 10 must include: description of continuity arrangements, effective emergency plans, and description of regular verification and review procedures. The full Latvian-language text of Annex 10 (including all sub-items beyond Item 5) must be reviewed directly from [vestnesis.lv](https://www.vestnesis.lv) before the Latvia submission is finalised.

**What needs to be produced:**
1. Annex 10 document formatted per Reg. 270 requirements
2. Structured per the numbered sub-items of Annex 10 (Item 5 confirmed to address: termination measures, pending operations, contract termination, prolonged downtime)
3. Cross-referenced to the full Latvia application package

---

### 3.2 Formal AML/CTF procedures (standalone annex)

| | |
|---|---|
| **Latvia source** | Reg. 270 Annex 13 |

**Description:** A dedicated AML/CTF procedures document submitted as Annex 13 — not embedded within other documents. For wind-down purposes, this must address how AML/CTF obligations continue to be met during a wind-down period (e.g. transaction monitoring, suspicious activity reporting obligations that persist after closure decision).

**What needs to be produced:**
- Annex 13 document covering AML/CTF policies and procedures, including continuity of AML obligations during wind-down

---

### 3.3 Sensitive payment data access controls

| | |
|---|---|
| **Latvia source** | Reg. 270 Annex 12 |

**Description:** Documentation of controls governing access to sensitive payment data, submitted as Annex 12. For wind-down purposes, this must address how access to payment data is managed as staff numbers reduce and how access is fully revoked upon wind-down completion.

**What needs to be produced:**
- Annex 12 document covering: access control framework for sensitive payment data; revocation procedures upon wind-down; audit trail requirements; post-wind-down data retention and destruction

---

## Outstanding actions before Latvia section can be finalised

| Action | Owner | Notes |
|---|---|---|
| Obtain and review full Latvian-language text of Reg. 270 Annex 10 | Legal / Regulatory counsel | Available at vestnesis.lv — search "Latvijas Bankas noteikumi Nr. 270". Required to confirm all sub-items beyond Item 5 before finalising the Latvia annex structure. |
| Confirm licence type for Latvia entity | Legal / Regulatory counsel | Reg. 270 applies to both licensed and registered PIs/EMIs; required annexes differ by category. Full annex set (1–16) applies to licensed entities; registered entities require Annexes 3, 4, 6, 10, 11, 13, 14, 15 only. |

---

*Document prepared based on publicly available regulatory sources. All claims are fact-based and sourced to the specific regulatory documents identified in the Key Regulatory Sources table above. The description of Reg. 270 Annex 10 Item 5 is consistent with Latvijas Banka's published English-language application materials but the full Latvian-language sub-item text has not been independently verified in English.*
