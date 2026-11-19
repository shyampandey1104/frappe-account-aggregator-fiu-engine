import unittest
from account_aggregator_fiu.engine import BankStatementMonthlySummary, AccountAggregatorFIUEngine

class TestAccountAggregatorFIUEngine(unittest.TestCase):
    def test_approved_underwriting(self):
        engine = AccountAggregatorFIUEngine("CONSENT-HDFC-9912", "AAAFB1234K")
        engine.ingest_monthly_summary(BankStatementMonthlySummary("2026-01", 500000.0, 420000.0, 0, 85000.0))
        engine.ingest_monthly_summary(BankStatementMonthlySummary("2026-02", 600000.0, 510000.0, 0, 92000.0))
        engine.ingest_monthly_summary(BankStatementMonthlySummary("2026-03", 550000.0, 480000.0, 0, 90000.0))

        res = engine.evaluate_financial_health_and_credit_limit()
        self.assertEqual(res["decision"], "APPROVED_WORKING_CAPITAL")
        self.assertGreater(res["recommended_credit_limit_inr"], 0)

    def test_rejected_due_to_bounces(self):
        engine = AccountAggregatorFIUEngine("CONSENT-ICICI-0041", "AAAFC5678L")
        engine.ingest_monthly_summary(BankStatementMonthlySummary("2026-01", 300000.0, 290000.0, 2, 10000.0))
        engine.ingest_monthly_summary(BankStatementMonthlySummary("2026-02", 250000.0, 245000.0, 2, 8000.0))

        res = engine.evaluate_financial_health_and_credit_limit()
        self.assertEqual(res["decision"], "REJECTED_FREQUENT_BOUNCES")
        self.assertEqual(res["recommended_credit_limit_inr"], 0.0)

if __name__ == "__main__":
    unittest.main()
