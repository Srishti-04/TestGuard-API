# Test Cases - TestGuard API

---

## TC_01 - Validate GET /posts API

- Method: GET  
- URL: https://jsonplaceholder.typicode.com/posts  
- Steps:
  1. Send GET request to /posts  
- Expected Result:
  - Status code should be 200  
  - Response should be a list  
- Actual Result:
  - Status code 200  
  - Response is list  
- Status: Pass  

---

## TC_02 - Invalid Endpoint Check

- Method: GET  
- URL: https://jsonplaceholder.typicode.com/invalid  
- Steps:
  1. Send GET request to invalid endpoint  
- Expected Result:
  - Status code should be 404  
- Actual Result:
  - Status code 404  
- Status: Pass  

---

## TC_03 - Response Time Validation

- Method: GET  
- URL: https://jsonplaceholder.typicode.com/posts  
- Steps:
  1. Send GET request  
  2. Measure response time  
- Expected Result:
  - Response time < 2 seconds  
- Actual Result:
  - Response time within limit  
- Status: Pass  