# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "account_aggregator_fiu"
app_title = "Frappe Account Aggregator Fiu Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Account Aggregator Fiu Engine - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/account_aggregator_fiu/css/account_aggregator_fiu.bundle.css"
app_include_js = "/assets/account_aggregator_fiu/js/account_aggregator_fiu.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Account Aggregator Fiu Engine Entry": {
        "validate": "account_aggregator_fiu.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "account_aggregator_fiu.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "account_aggregator_fiu.tasks.hourly_sync"
    ],
    "daily": [
        "account_aggregator_fiu.tasks.daily_reconciliation"
    ],
    "weekly": [
        "account_aggregator_fiu.tasks.weekly_digest"
    ]
}
