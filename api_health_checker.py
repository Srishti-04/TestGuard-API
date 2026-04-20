import requests
import time
import json

APIS = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/comments"
]

results = []
passed = 0
failed = 0


def check_api(url):
    global passed, failed

    try:
        start = time.time()
        response = requests.get(url)
        end = time.time()

        response_time = round(end - start, 3)

        print(f"\nAPI: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time} sec")

        if response.status_code == 200:
            print("✅ API Healthy")
            passed += 1
        else:
            print("❌ API Issue Detected")
            failed += 1

        # Save result for JSON
        results.append({
            "url": url,
            "status": response.status_code,
            "response_time": response_time
        })

    except Exception as e:
        print(f"\nAPI: {url}")
        print(f"⚠️ Error: {e}")
        failed += 1

        results.append({
            "url": url,
            "status": "ERROR",
            "response_time": None
        })


def run_health_check():
    print("🚀 Running API Health Check...\n")

    for api in APIS:
        check_api(api)

    print("\n===== SUMMARY =====")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    # Save JSON report
    with open("report.json", "w") as f:
        json.dump(results, f, indent=4)

    print("\n📄 Report saved as report.json")


if __name__ == "__main__":
    run_health_check()