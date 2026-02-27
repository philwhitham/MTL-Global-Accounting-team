# Flow of Funds – MTL / Stored Value (Phase 2 – Merchant Payout)

**Entity:** Shopify Financial Services Inc.  
**Purpose:** Step-by-step flow of funds from shopper payment through merchant wallet and optional payout, for control design and third-party reconciliation.  
**Last updated:** January 2026  

---

## Overview

This document details the **flow of funds** discussed for MTL stored value: from **Shop User** payment options (card vs Shop Wallet) through **settlements** and **Shop User Stored Value** (ledger), then into **Merchant User Stored Value** (merchant wallet, all in FBO), and optionally **payout to external bank**. It supports SOX control design (see [SOX_MTL_CONTROL_MATRIX.md](SOX_MTL_CONTROL_MATRIX.md)) and third-party reconciliation opportunities.

---

## Flow of funds – step-by-step

| Step | Description | System / account impact | Control / reconciliation link |
|------|-------------|-------------------------|-------------------------------|
| **1** | **Shop User chooses payment** | Shopper pays with **card** (e.g. via Stripe) or **Shop Wallet** (Shop Dollars). | Distinguishes funding source: card → processor settlement; Shop Wallet → redemption of existing stored value. |
| **2** | **Card: PayPal / Stripe (or other processor) settlement** | Processor settles card-funded transactions. Funds move from processor into the **FBO (for-benefit-of) environment**. | **Third-party rec:** Processor funding report vs internal issuance (TA90/TA100). |
| **3** | **Shop User Stored Value (ledger)** | When shopper uses **Shop Wallet**, ledger reflects **redemption** (decrease in Shop User Stored Value). When shopper **loads** Shop Dollars (e.g. via card), ledger reflects **issuance** (increase in Shop User Stored Value). | **MTL-SV-01, MTL-SV-02, MTL-SV-04:** Liability vs ledger vs FBO bank. **MTL-REG-03 / MTL-REG-04:** Issuance and redemption vs processor/partner. |
| **4** | **Merchant User Stored Value (merchant wallet)** | Funds from the sale (after settlement) are credited to **Merchant User Stored Value** – the merchant’s balance held **in FBO**. All such balances are part of the same FBO structure. | **Liability:** Merchant wallet is a **stored value liability** (merchant claim on SFS Inc.); same FBO account holds both shop-user and merchant balances. |
| **5** | **Merchant choice: leave in wallet or payout** | **Option A:** Merchant **leaves funds in Merchant User Stored Value** (merchant wallet). **Option B:** Merchant **opts to payout** to an external bank account. | **Option B** creates an outflow from FBO; **third-party rec** to **payment partner** payout report (MTL-REG-04). |
| **6** | **Payout to external bank** (if elected) | When merchant requests payout, funds move from **Merchant User Stored Value** (FBO) to the merchant’s **external bank account** via the payout/payment partner. | **MTL-REG-04:** Reconcile redemption/payout volume to payment partner report. **MTL-CASH-01 / MTL-SV-04:** FBO balance and liability vs bank. |

---

## Summary diagram (narrative)

```
[Shop User] Payment (card or Shop Wallet)
       │
       ├── Card ──► PayPal/Stripe settlement ──► FBO
       │
       └── Shop Wallet ──► Redemption (ledger) ──► Decrease Shop User Stored Value
       
Settlement / ledger adjustment
       │
       ▼
[Merchant User Stored Value] (all in FBO)  ◄── Merchant wallet liability
       │
       ├── Leave in wallet (no further movement)
       │
       └── Payout ──► Payment partner ──► Merchant external bank
```

---

## Implications for controls

- **Shop User Stored Value:** Liability and issuance/redemption are in scope for MTL-SV-01 through MTL-SV-04, MTL-REG-01 to MTL-REG-04 (see [SOX_MTL_CONTROL_MATRIX.md](SOX_MTL_CONTROL_MATRIX.md)).
- **Merchant User Stored Value:** Same FBO pool; **merchant wallet liability** should be included in stored value liability reconciliation and in FBO vs bank rec (MTL-SV-04, MTL-CASH-01).
- **Third-party reconciliations:**
  - **Settlements in (issuance):** Bank or payment processor funding report → TA90/TA100 (MTL-REG-03).
  - **Payouts out (redemptions):** Payment partner payout report → redemption volume (MTL-REG-04).
  - **FBO balance:** Bank statement → liability and cash (MTL-SV-04, MTL-CASH-01).

---

**Note:** This flow was captured from discussion and a shared screenshot. If your product flow differs (e.g. additional steps or entities), this doc can be updated so controls stay aligned with the actual flow.

**Related:** [SOX_MTL_CONTROL_MATRIX.md](SOX_MTL_CONTROL_MATRIX.md) · [SOX_CONTROL_FRAMEWORK_MTL.md](SOX_CONTROL_FRAMEWORK_MTL.md) · [../docs/PRODUCT_TEAM_DATA_REQUIREMENTS.md](../docs/PRODUCT_TEAM_DATA_REQUIREMENTS.md)
