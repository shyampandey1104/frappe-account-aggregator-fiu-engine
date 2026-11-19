"""RBI Account Aggregator (AA) Financial Information User (FIU) Underwriting Engine."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional

@dataclass
class BankStatementMonthlySummary:
    month_year: str
    total_inward_credits_inr: float
    total_outward_debits_inr: float
    cheque_or_nach_bounce_count: int
    average_daily_balance_inr: float

class AccountAggregatorFIUEngine:
    def __init__(self, consent_handle: str, entity_pan: str):
        self.consent_handle = consent_handle
        self.entity_pan = entity_pan
        self.monthly_statements: List[BankStatementMonthlySummary] = []

    def ingest_monthly_summary(self, summary: BankStatementMonthlySummary):
        self.monthly_statements.append(summary)

    def evaluate_financial_health_and_credit_limit(self) -> Dict[str, Any]:
        if not self.monthly_statements:
            raise ValueError("No bank statements ingested to evaluate credit profile.")

        total_credits = sum(s.total_inward_credits_inr for s in self.monthly_statements)
        total_bounces = sum(s.cheque_or_nach_bounce_count for s in self.monthly_statements)
        months_count = len(self.monthly_statements)
        avg_monthly_turnover = round(total_credits / months_count, 2)
        avg_daily_bal = round(sum(s.average_daily_balance_inr for s in self.monthly_statements) / months_count, 2)

        # Underwriting logic: High bounces disqualify borrower
        if total_bounces >= 3:
            underwriting_decision = "REJECTED_FREQUENT_BOUNCES"
            recommended_credit_limit = 0.0
        else:
            underwriting_decision = "APPROVED_WORKING_CAPITAL"
            # 20% of average monthly verified turnover or 2x ADB
            recommended_credit_limit = round(min(avg_monthly_turnover * 0.20, avg_daily_bal * 2.5), 2)

        return {
            "consent_handle": self.consent_handle,
            "entity_pan": self.entity_pan,
            "months_analyzed": months_count,
            "average_monthly_turnover_inr": avg_monthly_turnover,
            "average_daily_balance_inr": avg_daily_bal,
            "total_bounces": total_bounces,
            "decision": underwriting_decision,
            "recommended_credit_limit_inr": recommended_credit_limit
        }
