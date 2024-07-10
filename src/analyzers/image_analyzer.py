import docker
from src.core.analyzer import Analyzer, AnalyzerResult

class ImageAnalyzer(Analyzer):
    def __init__(self):
        self.client = docker.from_env()

    def analyze(self, image_name):
        image = self.client.images.get(image_name)
        findings = {
            'size': image.attrs['Size'],
            'layers': len(image.history()),
            'exposed_ports': image.attrs['Config'].get('ExposedPorts', {}),
            'env_vars': image.attrs['Config'].get('Env', [])
        }
        return AnalyzerResult('ImageAnalyzer', findings)