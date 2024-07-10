import pytest
import json
from src.docker_shield import run_full_scan, generate_report

@pytest.mark.integration
def test_report_generation():
    image_name = "python:3.9-slim"
    scan_result = run_full_scan(image_name)
    report = generate_report(scan_result, format='json')
    
    assert isinstance(report, str)
    report_dict = json.loads(report)
    assert 'image_analysis' in report_dict
    assert 'vulnerability_scan' in report_dict
    assert 'secret_scan' in report_dict