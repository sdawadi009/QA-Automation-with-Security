from dataclasses import dataclass
from typing import Optional
from compliance.enums import ViolationSeverity, ComplianceStandard

@dataclass

class Violation:

    """Represents a single compliance violation found in a cookie"""

    cookie_name: str
    violation_type: str
    description: str
    severity : ViolationSeverity
    standard: ComplianceStandard
    remediation:str
    risk_score: int
    article_referecne: Optional[str] = None

    def get_summary(self)->str:
        """Get a human-readable summary of the violation"""
        return f"{self.cookie_name}: {self.description} [{self.severity.value}]"
    
    def serialise(self) -> dict:
        """Convert to dictionary for JSON export"""
        return {
            'cookie_name': self.cookie_name,
            'violation_type': self.violation_type,
            'description': self.description,
            'severity': self.severity.value,
            'standard': self.standard.value,
            'remediation': self.remediation,
            'risk_score': self.risk_score,
            'article_reference': self.article_reference
        }
    
    def print_details(self):
        """Print detailed information about this violation"""
        print(f"Cookie: {self.cookie_name}")
        print(f"Issue: {self.description}")
        print(f"Severity: {self.severity.value}")
        print(f"How to fix: {self.remediation}")
        if self.article_reference:
            print(f"Legal reference: {self.article_reference}")