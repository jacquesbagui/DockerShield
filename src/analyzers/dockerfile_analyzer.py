from src.core.analyzer import Analyzer, AnalyzerResult
import re

class DockerfileAnalyzer(Analyzer):
    def analyze(self, dockerfile_content):
        findings = {
            'base_image': self._get_base_image(dockerfile_content),
            'exposed_ports': self._get_exposed_ports(dockerfile_content),
            'user': self._get_user(dockerfile_content),
            'env_vars': self._get_env_vars(dockerfile_content),
            'issues': self._check_best_practices(dockerfile_content)
        }
        return AnalyzerResult('DockerfileAnalyzer', findings)

    def _get_base_image(self, content):
        match = re.search(r'FROM\s+(\S+)', content)
        return match.group(1) if match else None

    def _get_exposed_ports(self, content):
        return re.findall(r'EXPOSE\s+(\d+)', content)

    def _get_user(self, content):
        match = re.search(r'USER\s+(\S+)', content)
        return match.group(1) if match else 'root'

    def _get_env_vars(self, content):
        return re.findall(r'ENV\s+(\w+)(?:\s+|=)(\S+)', content)

    def _check_best_practices(self, content):
        issues = []
        if 'apt-get update' in content and 'apt-get install' in content:
            if content.index('apt-get update') > content.index('apt-get install'):
                issues.append("'apt-get update' should come before 'apt-get install'")
        if 'ADD' in content:
            issues.append("Consider using COPY instead of ADD")
        if 'sudo' in content:
            issues.append("Avoid using sudo in Dockerfiles")
        return issues