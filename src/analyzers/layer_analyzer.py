from src.core.analyzer import Analyzer, AnalyzerResult

class LayerAnalyzer(Analyzer):
    def analyze(self, image_layers):
        findings = {
            'layer_count': len(image_layers),
            'large_layers': self._find_large_layers(image_layers),
            'suspicious_commands': self._find_suspicious_commands(image_layers)
        }
        return AnalyzerResult('LayerAnalyzer', findings)

    def _find_large_layers(self, layers):
        return [layer for layer in layers if layer['Size'] > 100 * 1024 * 1024]  # Layers larger than 100MB

    def _find_suspicious_commands(self, layers):
        suspicious = []
        keywords = ['curl', 'wget', 'nc', 'nmap', 'ssh-keygen'] # ... add more
        for layer in layers:
            for keyword in keywords:
                if keyword in layer['CreatedBy']:
                    suspicious.append(layer['CreatedBy'])
        return suspicious