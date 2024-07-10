from src.core.analyzer import Analyzer, AnalyzerResult
import docker
import psutil
import time

class DynamicAnalyzer(Analyzer):
    def __init__(self):
        self.client = docker.from_env()

    def analyze(self, image_name, duration=60):
        container = self.client.containers.run(image_name, detach=True)
        try:
            findings = self._monitor_container(container, duration)
        finally:
            container.stop()
            container.remove()
        return AnalyzerResult('DynamicAnalyzer', findings)

    def _monitor_container(self, container, duration):
        start_time = time.time()
        cpu_usage = []
        memory_usage = []
        network_io = []

        while time.time() - start_time < duration:
            stats = container.stats(stream=False)
            cpu_usage.append(self._calculate_cpu_percent(stats))
            memory_usage.append(stats['memory_stats']['usage'])
            network_io.append(stats['networks']['eth0'])
            time.sleep(1)

        return {
            'avg_cpu_usage': sum(cpu_usage) / len(cpu_usage),
            'max_memory_usage': max(memory_usage),
            'total_network_in': network_io[-1]['rx_bytes'] - network_io[0]['rx_bytes'],
            'total_network_out': network_io[-1]['tx_bytes'] - network_io[0]['tx_bytes']
        }

    def _calculate_cpu_percent(self, stats):
        cpu_delta = stats['cpu_stats']['cpu_usage']['total_usage'] - \
                    stats['precpu_stats']['cpu_usage']['total_usage']
        system_delta = stats['cpu_stats']['system_cpu_usage'] - \
                       stats['precpu_stats']['system_cpu_usage']
        return (cpu_delta / system_delta) * psutil.cpu_count() * 100