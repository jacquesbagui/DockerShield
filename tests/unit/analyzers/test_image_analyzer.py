import pytest
from src.analyzers.image_analyzer import ImageAnalyzer

@pytest.fixture
def image_analyzer():
    return ImageAnalyzer()

def test_analyze_image(image_analyzer):
    result = image_analyzer.analyze("python:3.9-slim")
    assert 'size' in result.findings
    assert 'layers' in result.findings
    assert isinstance(result.findings['size'], int)
    assert isinstance(result.findings['layers'], list)

def test_analyze_nonexistent_image(image_analyzer):
    with pytest.raises(Exception):
        image_analyzer.analyze("nonexistent:image")