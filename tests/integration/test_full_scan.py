import pytest
from src.docker_shield import run_full_scan

@pytest.mark.integration
def test_full_scan():
    image_name = "python:3.9-slim"
    result = run_full_scan(image_name)
    assert 'image_analysis' in result
    assert 'vulnerability_scan' in result
    assert 'secret_scan' in result