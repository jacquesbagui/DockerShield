import json
from src.core.report import Reporter

class JsonReporter(Reporter):
    def generate_report(self, results):
        report = {
            'timestamp': self.get_timestamp(),
            'results': {}
        }
        for result in results:
            report['results'][result.name] = result.findings
        return json.dumps(report, indent=2)