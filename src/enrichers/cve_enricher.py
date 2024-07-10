import requests
from src.core.enricher import Enricher, EnrichmentResult

class CVEEnricher(Enricher):
    def __init__(self):
        self.nvd_api_url = "https://services.nvd.nist.gov/rest/json/cve/1.0/"

    def enrich(self, vulnerability_data):
        enriched_data = []
        for vuln in vulnerability_data:
            cve_id = vuln.get('VulnerabilityID')
            if cve_id and cve_id.startswith('CVE-'):
                details = self._get_cve_details(cve_id)
                enriched_data.append({**vuln, **details})
            else:
                enriched_data.append(vuln)
        return EnrichmentResult('CVEEnricher', enriched_data)

    def _get_cve_details(self, cve_id):
        response = requests.get(f"{self.nvd_api_url}{cve_id}")
        if response.status_code == 200:
            data = response.json()
            return {
                "description": data["result"]["CVE_Items"][0]["cve"]["description"]["description_data"][0]["value"],
                "cvss_score": data["result"]["CVE_Items"][0]["impact"]["baseMetricV3"]["cvssV3"]["baseScore"],
                "references": [ref["url"] for ref in data["result"]["CVE_Items"][0]["cve"]["references"]["reference_data"]]
            }
        return {}