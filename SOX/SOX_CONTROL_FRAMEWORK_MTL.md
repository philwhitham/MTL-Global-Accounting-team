# SOX Control Framework – MTL / Stored Value

**Entity:** Shopify Financial Services Inc.  
**Scope:** Money transmitter and stored value (Shop Dollars) processes that will feed consolidated financial reporting  
**Approach:** Build and document SOX-relevant controls **before** amounts reach material thresholds  
**Last updated:** February 2026  

---

## 1. Objective

Design, document, and operate internal controls over financial reporting (ICFR) for MTL-related processes **in advance of materiality**, so that when SFS Inc. (or MTL-related balances) becomes material to Shopify Inc.’s consolidated financial statements, the control environment is already in place and can be assessed under SOX 404.

---

## 2. In-Scope Processes and Accounts

| Process / account | Financial statement impact | Control focus |
|-------------------|----------------------------|----------------|
| **Stored value liability** (Shop Dollars customer balance) | Consolidated balance sheet – liability | Recording, reconciliation, valuation (including breakage) |
| **Revenue from stored value** (fees, breakage) | Consolidated income statement – revenue | Recognition, measurement, cut-off |
| **Cash / FBO accounts** (where Shop Dollars funds are held) | Consolidated balance sheet – cash | Existence, completeness, reconciliation to liability |
| **Permissible investments** (if applicable) | Consolidated balance sheet – investments | Existence, valuation, reconciliation |
| **Data feeding MSB Call Reports** (same source as books) | Consistency between regulatory and SEC reporting | Data integrity, completeness, reconciliation to general ledger |

---

## 3. Control Categories to Build Now

### 3.1 Process and system documentation

- **Narrative / process flow:** Transaction initiation → product system → ledger/subsystem → reconciliation → general ledger → consolidation (and MSB Call Report where same source).
- **System of record:** Clearly define which system(s) are the source of truth for stored value liability, related revenue, and cash; ensure one set of books for both regulatory and SEC reporting.
- **Roles and responsibilities:** Who owns data entry, reconciliation, review, approval, and submission (e.g. NMLS); document in policy (e.g. Financial Reporting Policy) and role matrix.

### 3.2 Key controls (design and operate)

| Control area | Control objective | Example control activities |
|--------------|-------------------|----------------------------|
| **Stored value liability** | Liability is complete, accurate, and reconciled to underlying data | Reconcile stored value liability to transaction ledger / product data; reconcile to FBO account balance; management review of significant movements. |
| **Revenue (fees / breakage)** | Revenue is recognized in correct period and amount | Policy for recognition and breakage; review of revenue and breakage by management; reconciliation to liability movements. |
| **Cash / FBO** | Cash balances are complete and agree to liability and bank | Reconcile FBO bank statements to general ledger and to stored value liability; review and sign-off of reconciliations. |
| **Regulatory vs books** | MSB Call Report figures agree to books | Reconcile MSB Call Report data (e.g. FC220, FC430, TA/ST) to general ledger and supporting schedules before submission; review by accountable person. |
| **Segregation of duties** | No single person can initiate, record, reconcile, and approve | Separate roles: preparer, reviewer, approver, NMLS filer vs person who can post entries; access controls where applicable. |
| **Change management** | Changes to logic or systems don’t introduce errors | Document changes to calculation logic, mappings, or report logic; review/approval for changes that affect financial output. |

### 3.3 Governance and oversight

- **Board update:** Annual (or more frequent if needed) update to the Board on financial reports filed and material issues (per Financial Reporting Policy).
- **Restatement / material error escalation:** Escalation to a Board member before submission when a report includes material restatement, material error, or other material matters (per Financial Reporting Policy).
- **Management review:** Designated management review of material balances, reconciliations, and submissions (e.g. before quarter-end close and before NMLS submission).

### 3.4 Retention and evidence

- Retain documentation that supports control operation: reconciliations, review sign-offs, policy versions, and escalation records, in line with Company retention and SOX expectations (e.g. 7 years for ICFR evidence where applicable).

---

## 4. Implementation Checklist

Use this to track building and documenting controls **before** materiality:

- [x] **Process documentation** – End-to-end narrative/flow for stored value liability, revenue, and cash (and link to MSB Call Report where same source). See **SOX_PROCESS_NARRATIVE_STORED_VALUE.md** in this folder. *Note: chart of accounts and BigQuery table placeholders to be confirmed once product is operational.*
- [ ] **Control matrix** – List of key controls by process/account with owner, frequency, and evidence (see **SOX_MTL_CONTROL_MATRIX.md** in this folder).
- [ ] **Reconciliation discipline** – Stored value liability vs ledger/product data; liability vs FBO; MSB Call Report vs GL/supporting schedules; all reviewed and signed off.
- [ ] **Segregation of duties** – Roles defined and documented (preparer, reviewer, approver, NMLS filer); access limited appropriately.
- [ ] **Management review** – Formal review of material MTL balances and reconciliations before close and before regulatory submission.
- [ ] **Policy alignment** – Financial Reporting Policy and related procedures reflect who does what and escalation; Board update and restatement escalation in place.
- [ ] **Data and systems** – Single source of truth for MTL financial data; no parallel spreadsheets or shadow books for amounts that could hit consolidated reporting.
- [ ] **Change management** – Process for changes that affect financial logic or reporting (document, review, test where appropriate).

---

## 5. Relationship to Other Documents

| Document | How it supports SOX |
|----------|----------------------|
| **SOX_MTL_CONTROL_MATRIX.md** (this folder) | Key controls with MTL transaction examples, owners, evidence, and build priority. |
| **docs/Financial_Reporting_Policy_DRAFT.md** | Governance, Board update, escalation; defines roles and submission discipline. |
| **docs/PRODUCT_TEAM_DATA_REQUIREMENTS.md** | Transaction-level data capture (state, amount, timestamp) supports ledger integrity and reconciliations. |
| **docs/SHOPIFY_STORED_VALUE_MAPPING.md** | Mapping of MSB/GL fields keeps regulatory and books consistent. |
| **MSB Call Reports/** | Filed reports and supporting work papers are evidence of consistent, controlled reporting. |

---

## 6. When Amounts Become Material

- Reassess **materiality** for SFS Inc. and MTL-related accounts as part of consolidated materiality.
- Ensure **control matrix** and **process documentation** are current and cover all material processes and accounts.
- Coordinate with **internal audit** and **external auditor** on scope and testing of ICFR for MTL-related processes.
- No change to **control design intent**—controls built now should already align with SOX 404 expectations; the focus will be on formal assessment, testing, and any scaling of evidence.

---

**Owner:** [Global Accounting / Finance Lead]  
**Review:** Align with Internal Audit and external auditor when SFS Inc. or MTL balances approach materiality.  
**Classification:** Internal use; align with Company document retention and confidentiality.
