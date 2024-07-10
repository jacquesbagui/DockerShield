from src.core.analyzer import Analyzer, AnalyzerResult
import docker

class NetworkAnalyzer(Analyzer):
    def __init__(self):
        self.client = docker.from_env()

    def analyze(self, container_id):
        container = self.client.containers.get(container_id)
        network_settings = container.attrs['NetworkSettings']
        
        findings = {
            'network_mode': network_settings['NetworkMode'],
            'exposed_ports': network_settings['Ports'],
            'networks': list(network_settings['Networks'].keys())
        }

        # Check for potential issues
        issues = []
        if network_settings['NetworkMode'] == 'bridge':
            issues.append("Using default bridge network - consider using user-defined networks for better isolation")
        
        for port, bindings in network_settings['Ports'].items():
            if bindings and bindings[0]['HostIp'] == '0.0.0.0':
                issues.append(f"Port {port} is exposed to all interfaces. Consider restricting to specific IP")

        findings['issues'] = issues
        return AnalyzerResult('NetworkAnalyzer', findings)