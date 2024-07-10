from abc import ABC, abstractmethod

class Scanner(ABC):
    @abstractmethod
    def scan(self, target):
        pass

class ScanResult:
    def __init__(self, scanner_name, findings):
        self.scanner_name = scanner_name
        self.findings = findings