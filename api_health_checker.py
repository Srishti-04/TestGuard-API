import requests
import json
from utils.validator import validate_status_code, validate_response_time

URL = "https://jsonplaceholder.typicode.com/posts"

def log_bug(issue, value):
    with open("reports/bugs.txt", "a") as f:
        f.write(f"{issue} -> {value}\n")

def check_api():
    response = requests.get(URL)

    result = {
        "status_code": response.status_code,
        "response_time": response.elapsed.total_seconds()
    }

    # Validation
    if not validate_status_code(response):
        log_bug("Status Code Issue", response.status_code)

    if not validate_response_time(response):
        log_bug("Slow Response", response.elapsed.total_seconds())

    # Save report
    with open("report.json", "w") as f:
        json.dump(result, f, indent=4)

    print("API Check Completed")

if __name__ == "__main__":
    check_api()