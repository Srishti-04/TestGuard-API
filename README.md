# 🚀 TestGuard-API

## 📌 Overview

TestGuard-API is a lightweight API health monitoring and testing tool built using Python. It validates API responses, checks performance, and logs issues for debugging, making it suitable for backend validation and QA workflows.

---

## 🧪 Features

* 🔌 API Testing using Python `requests`
* 📊 Status code and response time validation
* 🧠 Custom validation utilities
* 🐞 Bug logging system for failure scenarios
* ⚡ Automated test execution using PyTest
* 📄 JSON-based reporting for API health

---

## 🛠 Tech Stack

* Python
* Requests
* PyTest

---

## 📁 Project Structure

```
TestGuard_API/
├── api_health_checker.py
├── testcases/
│   └── test_api.py
├── utils/
│   ├── __init__.py
│   └── validator.py
├── reports/
│   └── bugs.txt
├── report.json
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run

### 1. Setup Virtual Environment

```
py -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run API Health Checker

```
python api_health_checker.py
```

### 4. Run Test Cases

```
pytest -v
```

---

## 📊 Sample Output

### report.json

```
{
  "status_code": 200,
  "response_time": 0.25
}
```

---

## 🐞 Bug Logging Example

To simulate failure scenarios, invalid endpoints or thresholds were used.

### Sample bugs.txt

```
[ERROR] Status Code Issue -> 404
[WARNING] Slow Response -> 3.2 sec
```

---

## 🎯 Use Cases

* API health monitoring
* Backend validation
* Regression testing
* Detecting API failures and performance issues

---

## 💡 Key Highlights

* Designed for real-world QA workflows
* Demonstrates test case validation and bug tracking
* Includes both automated testing and monitoring logic
* Simulates failure scenarios for robust testing

---

## 👨‍💻 Author

Srishti Jaiswal
