from src.core.scanner import Scanner, ScanResult

class ComplianceScanner(Scanner):
    def __init__(self):
        self.compliance_checks = {
            'PCI-DSS': self._check_pci_dss,
            'HIPAA': self._check_hipaa,
            'GDPR': self._check_gdpr
        }

    def scan(self, image_config):
        findings = {}
        for standard, check_function in self.compliance_checks.items():
            findings[standard] = check_function(image_config)
        return ScanResult('ComplianceScanner', findings)

    def _check_pci_dss(self, config):
        issues = []
        if 'root' in config.get('User', ''):
            issues.append("Running as root user violates PCI-DSS requirement 2.2")
        if not config.get('Healthcheck'):
            issues.append("No healthcheck defined, may violate PCI-DSS requirement 6.2")
        return issues

    def _check_hipaa(self, config):
        issues = []
        if not config.get('Labels', {}).get('encryption'):
            issues.append("No encryption label found, may violate HIPAA encryption requirements")
        return issues

    def _check_gdpr(self, config):
        issues = []
        if 'EU' in config.get('Env', []):
            if not config.get('Labels', {}).get('data_protection'):
                issues.append("Processing EU data without data protection measures may violate GDPR")
        return issues