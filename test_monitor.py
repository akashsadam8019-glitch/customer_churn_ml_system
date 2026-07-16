from src.monitoring.drift_monitor import DriftMonitor

monitor = DriftMonitor()

report = monitor.generate_report(
    "artifacts/reference_data.csv"
)

print(report)