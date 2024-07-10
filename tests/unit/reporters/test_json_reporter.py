import json
from src.reporters.json_reporter import JsonReporter

def test_generate_report():
    reporter = JsonReporter()
    test_results = [
        {'name': 'Test1', 'findings': {'issue1': 'detail1'}},
        {'name': 'Test2', 'findings': {'issue2': 'detail2'}}
    ]
    report = reporter.generate_report(test_results)
    assert isinstance(report, str)
    report_dict = json.loads(report)
    assert 'timestamp' in report_dict
    assert 'results' in report_dict
    assert len(report_dict['results']) == 2