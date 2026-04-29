# 🚀 TestGuard-API

## 📌 Overview

TestGuard-API is a lightweight API health monitoring and testing tool built using Python. It validates API responses, checks performance, and logs issues for debugging, making it useful for backend validation and QA workflows.

---

## 🧪 Features

* 🔌 API Testing using Python requests
* 📊 Status code and response time validation
* 🧠 Custom validation utilities
* 🐞 Bug logging system for failed checks
* ⚡ Automated test execution using PyTest
* 📄 JSON-based reporting

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
│   └── validator.py
├── reports/
│   └── bugs.txt
├── report.json
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run

### 1. Setup Environment

```
py -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run API Checker

```
python api_health_checker.py
```

### 4. Run Tests

```
pytest -v
```

---

## 📊 Output

* `report.json` → contains API status and response time
* `reports/bugs.txt` → logs detected issues

---

## 🎯 Use Cases

* API health monitoring
* Regression testing
* Backend validation

---

## 👨‍💻 Author

Srishti Jaiswal

