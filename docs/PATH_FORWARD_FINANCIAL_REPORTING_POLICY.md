# Path Forward: Financial Reporting Policy

**Requested by**: Legal Team  
**Prepared for**: Board Resolution alignment and policy governance  
**Date**: January 30, 2026  
**Status**: Suggested approach and draft for review  

---

## 1. Request Summary

Legal is working through the Board Resolution. In parallel, a **Financial Reporting Policy** is needed to:

- Cover the activities the Accounting team performs each quarter/year for regulatory financial reporting.
- Be approved by the Board.
- Address the gap that **MSB Call Reports were filed without formal Board review or a policy governing how/when we report**.

**Two mandatory elements** (moved from the Board Resolution into the policy):

1. **Annual Board update**: The Board will be provided an update **no less than annually** on financial reports filed.
2. **Restatement escalation**: If any report needs to be restated (or involves material error or other material matters), a Board member will be notified prior to submission, to the extent practicable.

---

## 2. Reference Materials

All project documentation, including policy materials, lives in **`docs/`** (this folder).

### 2.1 Policy template and peer policies (when available)

Place the following in **`docs/`** for alignment with the official template and peer policies:

| Document | Purpose |
|----------|---------|
| **Official policy template** | Ensures format, headings, and approval fields match company standard. |
| **Vendor Management Policy** (finalized) | Reference for structure, tone, and level of detail. |
| **AML Policy** (finalized) | Reference for regulatory-facing policy language. |
| **IT Security Policy** (finalized) | Reference for roles, review cycles, and approval language. |

### 2.2 Existing project docs (reporting context)

These docs in **`docs/`** and the repo support the policy and reporting process:

| Document | Use |
|----------|-----|
| **SHOPIFY_FS_REFERENCE_DATA.md** | Legal entity (SFS Inc.), NMLS ID 2689562, licensed states, NetSuite mapping. |
| **SHOPIFY_STORED_VALUE_MAPPING.md** | MSB Call Report field mapping, data sources (NetSuite, BigQuery). |
| **PRODUCT_TEAM_DATA_REQUIREMENTS.md** | Data capture requirements for quarterly reporting (TA/ST). |
| **BUSINESS_PLAN_ANALYSIS.md** | Business plan and funds flow context. |
| **MSB Call Reports/** (repo root) | Filed reports, summaries, validation (e.g. `MSB Call Reports/2025/Q4/README.md`). |

---

## 3. Suggested Path Forward

### Step 1: Align to official template (Legal + Accounting)

- **Who**: Legal (owner of template), Accounting (content owner for this policy).
- **What**: Map the draft policy sections to the official policy template (headings, numbering, approval block, version control).
- **Output**: A version of the Financial Reporting Policy that matches the template layout and company style.

### Step 2: Incorporate the two Board-related provisions

- **Annual Board update**: Add a clear policy statement and procedure that the Board receives an update on financial reports filed **at least annually** (e.g., as part of an annual compliance or reporting summary).
- **Restatement escalation**: Add a policy statement and procedure that any submission that includes:
  - a **material restatement** of prior reporting,
  - disclosure of a **material error**, or
  - any other matters pertaining to the Reporting Functions that an individual with access to the NMLS system **reasonably believes may be material** to the Company  
  shall be **escalated to a Board member prior to submission**, to the extent practicable.

These two items should appear as explicit policy statements and, where the template allows, in a “Procedures” or “Escalation” section.

### Step 3: Define “Reporting Functions” and scope

- **Reporting Functions**: Define to include at least **MSB Call Reports** (NMLS) and any other regulatory financial reports that the Company is required to file (e.g., state-specific or other NMLS-related filings). Optionally include other periodic financial regulatory reports if Legal agrees.
- **Scope**: Confirm that the policy applies to **Shopify Financial Services Inc.** and to personnel responsible for preparing, reviewing, or submitting these reports (and NMLS system access, where relevant).

### Step 4: Describe quarterly and annual activities

- **Quarterly**:  
  - Preparation and review of MSB Call Report (data collection, XML generation, validation).  
  - Internal review and, if applicable, approval workflow (e.g., per existing GitHub/approval process in this repo).  
  - Submission to NMLS by the required deadline (45 days after quarter-end).  
  - Retention of filed reports and supporting work papers (see e.g. `MSB Call Reports/2025/Q4/`).
- **Annual**:  
  - Preparation of the **annual update to the Board** on financial reports filed (list of reports, periods, submission dates, and any material issues or restatements).  
  - Delivery of that update to the Board (timing to align with Board calendar).

### Step 5: Roles and responsibilities

- **Policy Owner**: e.g., Global Accounting or designated Finance lead.  
- **Preparer**: Team members who compile data and generate reports.  
- **Reviewer/Approver**: Who must review before submission (e.g., Accounting lead, and if desired, Compliance).  
- **NMLS Filer**: Who is permitted to submit in NMLS (and thus subject to the “reasonably believes may be material” escalation obligation).  
- **Board**: Receives annual update and is notified in the event of restatement/material error escalation.

### Step 6: Legal and Board review

- Legal reviews for consistency with Board Resolution (once finalized) and other policies.  
- Policy is submitted for Board approval as part of the policy approval process.  
- After approval: publish, communicate to relevant personnel, and add to the Company’s policy index.

### Step 7: Implementation and first annual cycle

- Follow the new policy for the next MSB Call Report cycle (e.g., Q1 2026).  
- Schedule and prepare the **first annual Board update** on financial reports filed (e.g., for the first full year of reporting or next Board meeting after approval).

---

## 4. Draft Policy Document

A full draft policy is in:

**`docs/Financial_Reporting_Policy_DRAFT.md`**

It includes:

- Purpose, scope, and definitions.
- Policy statements covering:
  - Governance and Board oversight.
  - Annual Board update (no less than annually).
  - Restatement and material error escalation to a Board member prior to submission, to the extent practicable.
- Roles and responsibilities.
- Procedures: quarterly reporting process, annual Board update, and restatement escalation.
- Documentation and retention.
- Policy review and approval.

You can copy the content into the official .docx template and adjust headings/formatting to match the template and the reference policies (Vendor Management, AML, IT Security).

---

## 5. Timeline Suggestion (By Next Week)

| By | Action |
|----|--------|
| **Day 1** | Confirm location of template and reference policies; place in `docs/` if not already. |
| **Day 2–3** | Map draft to official template; insert the two Board provisions in the correct sections. |
| **Day 4** | Legal review of draft (scope, definitions, escalation language). |
| **Day 5** | Incorporate Legal comments and finalize draft for internal sign-off. |
| **Next week** | Submit draft to Legal for Board approval process (or as agreed with Legal). |

---

## 6. Open Points for Legal

1. **Exact scope of “Reporting Functions”**: MSB Call Reports only, or also other NMLS/state financial reports?  
2. **Who “a Board member” means**: Specific role (e.g., Chair, Audit Committee Chair) or any Board member?  
3. **“To the extent practicable”**: Keep as-is for flexibility, or define (e.g., “within X business days”)?  
4. **Format of annual Board update**: Standalone memo, part of a broader compliance report, or slide deck?  
5. **Placement of restatement language**: Only in policy, or also referenced in Board Resolution (or both)?

---

## 7. Next Steps

1. Add the official policy template and reference policies (Vendor Management, AML, IT Security) to **`docs/`** when available.  
2. Use **`docs/Financial_Reporting_Policy_DRAFT.md`** as the basis for the policy; align structure and wording to the template and references.  
3. Confirm with Legal the open points above and the timeline for Board approval.  
4. After Board approval, publish the policy, train relevant staff, and implement the first annual Board update cycle.

---

**Document owner**: Accounting (with Legal review)  
**Last updated**: January 30, 2026
