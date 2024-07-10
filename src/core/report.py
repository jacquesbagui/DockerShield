from abc import ABC, abstractmethod

class Enricher(ABC):
    @abstractmethod
    def enrich(self, data):
        pass

class EnrichmentResult:
    def __init__(self, enricher_name, enriched_data):
        self.enricher_name = enricher_name
        self.enriched_data = enriched_data