import argparse
import logging
from .analyzers import ImageAnalyzer, DockerfileAnalyzer
from .scanners import VulnerabilityScanner, SecretScanner
from .reporters import JsonReporter
from src.utils.logging_utils import setup_logging

def run_full_scan(image_name):
    image_analyzer = ImageAnalyzer()
    vulnerability_scanner = VulnerabilityScanner()
    secret_scanner = SecretScanner()

    results = {
        'image_analysis': image_analyzer.analyze(image_name),
        'vulnerability_scan': vulnerability_scanner.scan(image_name),
        'secret_scan': secret_scanner.scan(image_name),
    }

    return results

def generate_report(scan_results, format='json'):
    if format == 'json':
        reporter = JsonReporter()
        return reporter.generate_report(scan_results)
    else:
        raise ValueError(f"Unsupported report format: {format}")

def main():
    setup_logging()
    logger = logging.getLogger('dockershield')
    logger.info("DockerShield démarré")
    parser = argparse.ArgumentParser(description="DockerShield - Docker Image Security Scanner")
    parser.add_argument('--image', required=True, help="Name of the Docker image to scan")
    parser.add_argument('--report-format', default='json', choices=['json'], help="Report format")
    
    args = parser.parse_args()

    scan_results = run_full_scan(args.image)
    report = generate_report(scan_results, format=args.report_format)
    
    print(report)

if __name__ == "__main__":
    main()