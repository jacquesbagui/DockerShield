import re
from src.core.scanner import Scanner, ScanResult

class SecretScanner(Scanner):
    def __init__(self):
        self.patterns = {
            'aws_key': r'AKIA[0-9A-Z]{16}',
            'private_key': r'-----BEGIN PRIVATE KEY-----',
            'github_token': r'github_pat_[a-zA-Z0-9]{22,}',
            'password': r'(?i)password\s*[=:]\s*\S+'
        }

    def scan(self, image_layers):
        findings = []
        for layer in image_layers:
            for secret_type, pattern in self.patterns.items():
                matches = re.findall(pattern, layer)
                if matches:
                    findings.append({
                        'type': secret_type,
                        'matches': len(matches),
                        'layer': layer[:50] + '...'
                    })
        return ScanResult('SecretScanner', findings)