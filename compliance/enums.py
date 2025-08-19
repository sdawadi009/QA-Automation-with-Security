from enum import Enum

class ComplianceStandard(Enum):

    GDPR = "gdpr"
    CCPA = "ccpa"
    NIST = "nist"
    ISO27001 = "iso 27001"
    EPRIVACY = "eprivacy_directive"

class ViolationSeverity(Enum):

    """How serious is the violation"""

    LOW = "low"
    MEDIUM= "medium"
    HIGH = "high"
    CRITICAL = "critical"

class CookieCategory (Enum):
    """Types of Cookies"""

    NECESSARY = "necessary"
    FUNCTIONAL = "functional"
    ANALYTICS = "analystics"
    MARKETING = "marketing"