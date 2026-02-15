import csv
import io
import datetime
import json

def export_to_csv(data, filename="test_cases.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Scenario", "Steps", "Expected", "Type", "Priority", "Severity"])

        for tc in data.test_cases:
            writer.writerow([
                tc.id,
                tc.scenario,
                " | ".join(tc.steps),
                tc.expected_result,
                tc.type,
                tc.priority,
                tc.severity
            ])

    return filename


def export_to_csv_string(data):
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["ID", "Scenario", "Steps", "Expected", "Type", "Priority", "Severity"])

    for tc in data.test_cases:
        writer.writerow([
            tc.id,
            tc.scenario,
            " | ".join(tc.steps),
            tc.expected_result,
            tc.type,
            tc.priority,
            tc.severity
        ])

    return output.getvalue()


def export_to_json(data, filename=None):
    """
    Save test cases to a JSON file.
    """

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"test_cases_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data.dict(), f, indent=2)

    return filename