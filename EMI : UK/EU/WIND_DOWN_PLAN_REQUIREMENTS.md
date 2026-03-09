# Wind-Down Plan Requirements — UK (FCA) and EU/Luxembourg (CSSF)

**Entity:** Shopify Financial Services Inc. (UK) / Luxembourg EMI applicant entity (EU)
**Purpose:** Requirements analysis to support minimal-compliance wind-down plan design for UK and Luxembourg EMI licensing applications
**Last updated:** March 2026
**Status:** Draft — see flagged uncertainties at end of document

---

## How to use this document

This document maps the wind-down plan requirements of two regulators:

- **UK:** Financial Conduct Authority (FCA) — Payment Institution / EMI authorisation under the Payment Services Regulations 2017 and Electronic Money Regulations 2011
- **EU/Luxembourg:** Commission de Surveillance du Secteur Financier (CSSF) — EMI authorisation under the Law of 10 November 2009 on Payment Services (as amended by the Law of 20 July 2018 transposing PSD2), and EBA Guidelines on authorisation under PSD2 (EBA/GL/2017/09)

**Important structural difference from Latvia:** The CSSF has no single regulatory instrument equivalent to Latvia's Regulation No. 270 Annex 10. Luxembourg's requirements are dispersed across the primary law, binding EBA guidelines, and three CSSF circulars. There is no CSSF-prescribed annex format for a standalone wind-down plan. This affects both how requirements are interpreted and how the deliverable document is structured for the Luxembourg submission.

The document is structured in three sections:

1. **Overlapping requirements** — elements required by both regulators; a single well-drafted section can satisfy both
2. **UK-only requirements** — FCA-specific elements not expressly required by the CSSF
3. **Luxembourg-only requirements** — CSSF-specific elements not expressly required by the FCA

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
| Law of 10 November 2009 on Payment Services (as amended) | CSSF / Luxembourg | Primary Luxembourg legislation governing EMI/PI authorisation; transposition of PSD1, EMD2, and PSD2 |
| EBA/GL/2017/09 – Guidelines on Information to be Provided for Authorisation under PSD2 (11 July 2017) | EBA (applied by CSSF) | Binding authorisation information requirements applied by the CSSF; the primary instrument governing what must be submitted in the EMI application |
| Circular CSSF 26/906 – Central Administration, Internal Governance and Risk Management (20 January 2026) | CSSF | New governance framework for PIs and EMIs; effective 30 June 2026; requires Board-level business continuity and crisis management as an ongoing obligation |
| Circular CSSF 20/750 – ICT and Security Risk Management | CSSF | ICT-focused business continuity plan requirement; implements EBA ICT guidelines |
| Circular CSSF 22/806 – Outsourcing Arrangements (as amended by 25/883) | CSSF | Requires exit plans for each critical or important outsourced function |

---

## Section 1 — Overlapping requirements (both jurisdictions)

A single plan section addressing each of these requirements will satisfy both the FCA and the CSSF. Unlike Latvia's Reg. 270, the CSSF has no prescribed annex format — the Luxembourg submission can reference the same underlying document.

---

### 1.1 Customer fund identification and prompt return

| | |
|---|---|
| **FCA source** | "Our Approach" paras 3.73–3.76 |
| **CSSF source** | Circular CSSF 26/906, Chapter 8 (safeguarding requirements); EBA/GL/2017/09 |

**Description:** Records must allow the regulator or an insolvency practitioner to identify each customer's balance and return it without needing to reconstruct data from scratch. For Shopify FS this means individual buyer wallet balances and individual merchant wallet balances must be identifiable at all times from a single authoritative source. The FCA has emphasised this is the **primary focus** of the PI/EMI wind-down plan. The CSSF addresses this through Circular 26/906 Chapter 8, which requires daily reconciliation of client funds, strict legal segregation in dedicated safeguarding accounts, and an obligation to safeguard client funds "at all times" — including in adverse scenarios.

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
| **CSSF source** | Circular CSSF 26/906 (Board obligation for business continuity and crisis management); Circular CSSF 20/750 (ICT-focused BCP) |

**Description:** A documented plan covering how the business continues to operate or winds down under defined stress scenarios, covering people, systems, and processes across all payment services. Emergency plans must be effective and supported by regular review procedures. Under Circular CSSF 26/906, the Board bears "overall responsibility for the PI/EMI and must ensure the sound and prudent management of the institution, the preservation of its continuity and the protection of its reputation." Management information systems must function in both normal and crisis conditions. Under Circular CSSF 20/750, BCPs must be based on Business Impact Analyses, cover extreme but plausible scenarios (including cyber-attack), and be tested periodically.

**What needs to be produced:**
1. Scenario library (minimum 3–5 plausible scenarios including: financial distress, loss of banking partner, IT failure, loss of key licence)
2. Documented procedures for each scenario
3. Record of testing and review cycles — frequency and responsible party
4. Board-level approval of the plan (required under Circular 26/906)

---

### 1.3 Termination of contracts and pending operations

| | |
|---|---|
| **FCA source** | WDPG (processes element) |
| **CSSF source** | Circular CSSF 22/806 Section 4.3.4 (outsourcing exit plans); EBA/GL/2017/09 |

**Description:** Procedures to: (1) complete all pending payment transactions at point of wind-down without creating new obligations; (2) terminate contracts with merchants, buyers, banking partners, and technology providers in the correct sequence; (3) manage prolonged system downtime without leaving obligations unresolved. The FCA multi-firm review identified contract termination costs as a frequently underestimated liability. Circular CSSF 22/806 requires a specific exit plan for each critical or important outsourced function — this exit plan "shall allow the entity to exit without undue disruption to business activities, without limiting compliance with regulatory requirements, and without any detriment to the continuity and quality of the provision of services to clients."

**What needs to be produced:**
1. Register of all material contracts with termination notice periods and break costs
2. Sequencing plan for contract terminations (which counterparties are terminated in which order)
3. Procedure for completing in-flight transactions at point of closure
4. Process for handling disputed or unresolved transactions during wind-down
5. For each critical or important outsourced function: a dedicated exit plan per Circular CSSF 22/806 Section 4.3.4

---

### 1.4 Wind-down triggers and monitoring strategy

| | |
|---|---|
| **FCA source** | TR22/1; FG20/1 |
| **CSSF source** | Circular CSSF 26/906 (crisis management; Board obligation to ensure preservation of continuity) |

**Description:** Defined conditions that would cause management to initiate a wind-down, supported by a monitoring framework to detect those conditions in advance. The FCA expects triggers to be specific and measurable — qualitative descriptions are not sufficient. Triggers must be actively monitored with defined escalation paths and linked to the firm's risk appetite statement. Under Circular CSSF 26/906, the CSSF requires "an appropriate response capability in the event of a crisis" — this requires pre-defined criteria for what constitutes a crisis and how the Board responds.

**What needs to be produced:**
1. Minimum 3–5 quantified triggers with defined threshold levels (amber early warning + red action threshold for each)
2. Monitoring frequency and responsible owner for each trigger
3. Escalation path from breach of trigger → Board notification → wind-down decision
4. Description of how triggers are reviewed and updated (minimum annually, and after any material business change)

---

### 1.5 IT and operational resilience

| | |
|---|---|
| **FCA source** | FCA multi-firm review; TR22/1 |
| **CSSF source** | Circular CSSF 20/750 (ICT business continuity); Circular CSSF 26/906 |

**Description:** Controls to ensure systems remain operational or fail safely during a wind-down period — covering cybersecurity, system access, data integrity, and continuity of critical processes. Must address: what happens to data after wind-down is complete; how system access is managed when staff numbers reduce; how third-party IT dependencies (e.g. Shopify Inc. shared infrastructure) would be managed. The FCA treats IT failure as a distinct wind-down trigger scenario. Circular CSSF 20/750 requires BCPs to protect and re-establish "the confidentiality, integrity, and availability" of business functions and information assets, and to demonstrate the ability to "sustain the viability of their businesses until critical operations are re-established."

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
| **CSSF source** | Circular CSSF 26/906 (governance and organisational requirements; Board responsibility for sound management) |

**Description:** Identification of the key people and third-party cooperation required to execute a wind-down. The FCA multi-firm review found that firms frequently underestimate people requirements — assuming staff will be available when in practice key staff may have already left. Must consider staff retention incentives during wind-down; identification of roles that cannot be vacated; external advisers already engaged or on retainer. Circular CSSF 26/906 places overall responsibility on the Board for ensuring sound management of the institution, which includes ensuring adequate human resources are available in adverse scenarios.

**What needs to be produced:**
1. Named roles (not individuals) essential to wind-down execution
2. Staff retention strategy (e.g. retention bonuses, extended notice periods)
3. List of external parties required: legal counsel, insolvency practitioner, banking contacts, CSSF and FCA regulatory contacts
4. Plan for knowledge transfer if key staff depart before or during wind-down

---

### 1.7 Stakeholder communication plan

| | |
|---|---|
| **FCA source** | FCA multi-firm review |
| **CSSF source** | Circular CSSF 26/906 (crisis management; Board obligation for reputation protection) |

**Description:** A sequenced plan covering how and when merchants, buyers, regulators, banking partners, and other counterparties are notified. The FCA specifically requires: notification sequence (regulator first, then counterparties, then customers); key messages for each audience; how customer complaints during wind-down are handled; and data retention obligations post-closure. Circular CSSF 26/906 requires the Board to protect the institution's reputation — a crisis communication plan is an implicit component of that obligation.

**What needs to be produced:**
1. Stakeholder map with notification sequence
2. Draft communication templates for each stakeholder group (FCA, CSSF, merchants, buyers, banking partners, technology partners)
3. Regulatory notification obligations and timelines for both FCA and CSSF
4. Customer complaint handling procedure during wind-down
5. Data retention schedule post-closure

---

## Section 2 — UK-only requirements (FCA)

These elements are expressly required by the FCA and have no confirmed equivalent in CSSF instruments. They are required for the UK application only.

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

**Description:** A living document — **separate from the wind-down plan** — containing all information needed by a resolution authority or insolvency practitioner to identify and return safeguarded funds. Must be retrievable within 48 hours of a request. A named Senior Management Function (SMF) holder is accountable. Board approval required. Inaccuracies must be corrected within 5 business days of discovery. This is a UK-only obligation with no CSSF equivalent currently in force.

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

## Section 3 — Luxembourg-only requirements (CSSF)

These are requirements arising specifically from CSSF instruments that go beyond or differ from the FCA framework.

---

### 3.1 CSSF application form — EBA/GL/2017/09 business plan submission

| | |
|---|---|
| **CSSF source** | EBA/GL/2017/09 (applied by CSSF); CSSF EMI application form |

**Description:** The Luxembourg EMI licensing application must be submitted using the CSSF's official EMI application form and must comply with EBA/GL/2017/09, which sets out the detailed information requirements for authorisation under PSD2. Unlike the FCA's standalone WDPG, the CSSF does not have a dedicated wind-down plan instrument. Wind-down and continuity content is expected to be embedded within the business plan submission. The CSSF application form must be downloaded directly from the CSSF website and reviewed to confirm whether it contains an explicitly labelled wind-down or continuity section.

**What needs to be produced:**
1. Review of the CSSF EMI application form (.docx, available at cssf.lu) to confirm whether an explicit wind-down plan section exists — this is an outstanding action (see below)
2. Business plan submission per EBA/GL/2017/09 requirements, incorporating continuity and orderly exit content
3. Programme of operations covering all payment services to be provided and how they would be wound down

---

### 3.2 Circular CSSF 26/906 compliance — effective 30 June 2026

| | |
|---|---|
| **CSSF source** | Circular CSSF 26/906 (20 January 2026) |

**Description:** Effective 30 June 2026, all Luxembourg PIs and EMIs must comply with Circular CSSF 26/906 on Central Administration, Internal Governance and Risk Management. This circular requires the Board to approve and annually review guiding principles covering business continuity and crisis management. The Board bears overall responsibility for "the preservation of the institution's continuity." Annual compliance attestations signed by all members of the Management Body must be submitted to the CSSF. Chapter 8 introduces enhanced safeguarding requirements directly relevant to wind-down: daily reconciliation of client funds and strict legal segregation in dedicated safeguarding accounts.

**What needs to be produced:**
1. Board-approved guiding principles document covering business continuity and crisis management (per Circular 26/906)
2. Annual compliance attestation signed by all Management Body members (post-authorisation ongoing obligation)
3. Daily client fund reconciliation procedure (Chapter 8)
4. Dedicated safeguarding account structure documentation (Chapter 8)

---

### 3.3 Outsourcing exit plans — Circular CSSF 22/806

| | |
|---|---|
| **CSSF source** | Circular CSSF 22/806 Section 4.3.4 (as amended by 25/883) |

**Description:** For each critical or important outsourced function, a dedicated exit plan must be maintained. This is more prescriptive than the FCA equivalent in that each outsourced function requires its own exit plan. The exit plan must allow the entity to exit without undue disruption to business activities or detriment to service continuity. It should not be treated as a backup solution — a transition plan must also be developed alongside it.

**What needs to be produced:**
1. Register of all critical or important outsourced functions
2. For each: a dedicated exit plan and transition plan per Circular 22/806 Section 4.3.4

---

### 3.4 PSD3 — forward-looking obligation (not yet in force)

| | |
|---|---|
| **Source** | PSD3 provisional political agreement, 27 November 2025; expected implementation ~end 2027 |

**Description:** Under PSD3, EMI and PI applicants will be required to submit a formal **winding-up plan** as part of the authorisation application. The winding-up plan must be proportionate to the size and business model of the institution and must define suitable measures to be undertaken in the case of failure, ensuring an orderly wind-up of activities in accordance with applicable national legislation. PSD3 has not yet been formally adopted or implemented in Luxembourg. Full compliance is not expected to be mandatory until approximately end-2027. **This is a forward-looking item only — no action required for the current application, but plan design should anticipate this requirement to avoid rework at transposition.**

---

## Outstanding actions

| Action | Owner | Notes |
|---|---|---|
| Review CSSF EMI application form (.docx) | Legal / Regulatory counsel | Download from cssf.lu and confirm whether the application form contains an explicit wind-down plan section or whether this content is embedded within the business plan. This determines whether the Luxembourg submission requires a standalone wind-down document or an embedded section. |
| Confirm CSSF pre-application meeting expectations | Legal / Regulatory counsel | Some EU NCAs informally require wind-down planning content in the business plan even before PSD3 formalises this requirement. Confirm whether the CSSF has the same informal expectation — best clarified in a pre-application meeting with the CSSF. |
| Monitor PSD3 transposition timeline | Legal / Regulatory counsel | Provisional agreement reached November 2025; expected implementation ~end 2027. The winding-up plan requirement under PSD3 should be anticipated in the current plan design to avoid rework at transposition. |

---

*Document prepared based on publicly available regulatory sources. All claims are fact-based and sourced to the specific regulatory documents identified in the Key Regulatory Sources table above. Where CSSF practice could not be confirmed from public sources (e.g. application form content, informal expectations), this is explicitly flagged as an outstanding action.*
