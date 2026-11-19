from setuptools import setup, find_packages

setup(
    name="frappe-account-aggregator-fiu-engine",
    version="1.0.0",
    description="Frappe RBI Account Aggregator (AA) FIU Engine: Bank Statement Ingestion, Cash Flow Analysis & Credit Underwriting.",
    author="Shyam Kumar Pandey",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
