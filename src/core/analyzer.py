from abc import ABC, abstractmethod

class Analyzer(ABC):
    @abstractmethod
    def analyze(self, target):
        pass

class AnalyzerResult:
    def __init__(self, analyzer_name, findings):
        self.analyzer_name = analyzer_name
        self.findings = findings