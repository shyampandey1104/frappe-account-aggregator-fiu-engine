# Frappe RBI Account Aggregator (AA) FIU Engine

[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-blue.svg)](https://frappeframework.com/)
[![RBI AA Master Direction](https://img.shields.io/badge/RBI-Account%20Aggregator%20NBFC-purple.svg)]()
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📌 Executive Overview & Real-World Client Problem

Under the **Reserve Bank of India (RBI) Account Aggregator (AA)** regulatory framework, financial entities operating as **Financial Information Users (FIUs)** can access cryptographically verified, tamper-proof bank statements directly from Financial Information Providers (FIPs) upon user consent.

**The Client Problem:**
B2B credit sellers, digital lenders, and vendor financing teams using ERPNext currently:
1. Rely on fraud-prone PDF bank statement uploads that are easily forged.
2. Spend hours calculating Average Daily Balance (ADB), turnover trends, and NACH/cheque bounce ratios manually.
3. Lack an automated underwriting engine to recommend scientifically backed credit limits before approving high-value Sales Orders.

This Frappe application functions as an institutional FIU engine that connects with authorized AAs (Sahamati ecosystem) to fetch financial data and automate credit underwriting.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["Customer Loan / Credit Limit Request"] -->|Generate Consent Handle| B["RBI Account Aggregator (AA) Gateway"]
    B -->|Digital Consent on Mobile App| C["Customer Approves via OTP"]
    C -->|Fetch Encrypted Bank Statements| D["FIU Decryption & Ingestion Engine"]
    D -->|Extract Transactions| E["Financial Health Analyzer"]
    E -->|Analyze Credits, Debits & ADB| F{"Cheque/NACH Bounce Check"}
    F -->|>= 3 Bounces in 3 Months| G["High Risk: Underwriting Rejected"]
    F -->|< 3 Bounces (Healthy Cashflow)| H["Calculate Recommended Credit Limit"]
    H -->|Update Customer Profile| I["ERPNext Automated Credit Limit Sanction"]
```

---

## 🚀 Key Engineering Capabilities

- **Consent Lifecycle Orchestration:** Initiates, tracks, and revokes AA consent requests conforming to ReBIT standards.
- **Automated Cash Flow Diagnostics:** Computes monthly turnover run-rates, median credit frequency, and average daily balances.
- **Delinquency Early Warning:** Flags return clearing codes (insufficient funds, mandate failed) instantly.
- **Dynamic B2B Credit Limit Engine:** Programmatically sets `credit_limit` on ERPNext Customer Masters.

---

## 📂 Frappe DocType Schema & Data Structure

```text
account_aggregator_fiu/
├── account_aggregator_fiu_core/
│   ├── doctype/
│   │   ├── aa_consent_request/
│   │   │   ├── aa_consent_request.json
│   │   │   ├── aa_consent_request.py
│   │   │   └── aa_consent_request.js
│   │   └── aa_underwriting_assessment/
│   │       └── aa_underwriting_assessment.json
│   └── workspace/
│       └── account_aggregator_fiu_workspace/
│           └── account_aggregator_fiu_workspace.json
```

---

## ⚡ Frappe Hooks & Whitelisted APIs

- **REST Endpoint:** `POST /api/method/account_aggregator_fiu.api.ingest_monthly_summary`
- **Whitelisted Method:** `@frappe.whitelist() def evaluate_financial_health_and_credit_limit()`
- **Hooks Event:** `on_update` of `Customer` checks for expired AA consent mandates.

---

## 🛠️ Installation & Bench Setup

```bash
bench get-app https://github.com/shyampandey1104/frappe-account-aggregator-fiu-engine
bench --site erp.yourdomain.com install-app account_aggregator_fiu
bench --site erp.yourdomain.com migrate
python3 -m unittest discover tests
```

---

## 📄 License
MIT License. Optimized for Fintech NBFCs, B2B wholesale distributors, and corporate credit desks.
