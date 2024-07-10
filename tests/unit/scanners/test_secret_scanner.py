import pytest
from src.scanners.secret_scanner import SecretScanner

@pytest.fixture
def secret_scanner():
    return SecretScanner()

def test_scan_for_aws_key(secret_scanner):
    test_data = "This is a test AKIAIOSFODNN7EXAMPLE string"
    result = secret_scanner.scan(test_data)
    assert any(finding['type'] == 'aws_key' for finding in result.findings)

def test_scan_no_secrets(secret_scanner):
    test_data = "This is a test string with no secrets"
    result = secret_scanner.scan(test_data)
    assert len(result.findings) == 0