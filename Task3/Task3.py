import json
import sys

def load_values(values_file):
    with open(values_file) as f:
        return json.load(f)

def load_tests(tests_file):
    with open(tests_file) as f:
        return json.load(f)


def fill_values(tests, values_dict):
    if "id" in tests:
        if tests["id"] in values_dict:
            tests["value"] = values_dict[tests["id"]]
    if "values" in tests:
        for test in tests["values"]:
            fill_values(test, values_dict)


def main(values_file, tests_file, report_file):
    values_data = load_values(values_file)
    tests_data = load_tests(tests_file)

    values_dict = {item['id']: item['value'] for item in values_data['values']}

    for test in tests_data['tests']:
        fill_values(test, values_dict)

    with open(report_file, 'w') as f:
        json.dump(tests_data, f, indent=2)

if __name__ == "__main__":
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    main(values_file, tests_file, report_file)
