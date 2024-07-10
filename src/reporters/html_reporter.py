from src.core.report import Reporter
from jinja2 import Template

class HtmlReporter(Reporter):
    def generate_report(self, results):
        template = Template("""
        <html>
        <head>
            <title>Docker Security Audit Report</title>
            <style>
                body { font-family: Arial, sans-serif; }
                .result { margin-bottom: 20px; }
                .finding { margin-left: 20px; }
            </style>
        </head>
        <body>
            <h1>Docker Security Audit Report</h1>
            <p>Generated on: {{ timestamp }}</p>
            {% for result in results %}
            <div class="result">
                <h2>{{ result.name }}</h2>
                {% for key, value in result.findings.items() %}
                <div class="finding">
                    <strong>{{ key }}:</strong> {{ value }}
                </div>
                {% endfor %}
            </div>
            {% endfor %}
        </body>
        </html>
        """)
        
        return template.render(timestamp=self.get_timestamp(), results=results)