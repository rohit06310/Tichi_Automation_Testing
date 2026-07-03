# Tichi Web Application – QA Automation Testing

## Project Overview

This project contains automated UI test cases for the **Tichi Web Application** using **Python**, **Pytest**, and **Playwright**. The automation validates the core user journey from the Landing Page to Logout.

## Tech Stack

- Python 3.12+
- Pytest
- Playwright
- pytest-html
- Firefox Browser

---

## Project Structure

```
Tichi/
│
├── main.py                 # All automation test classes
├── conftest.py             # Playwright fixture
├── requirements.txt
├── pyproject.toml
├── README.md
│
├── reports/
│   ├── landing.html
│   ├── login.html
│   ├── signup.html
│   ├── forgot_password.html
│   ├── logout.html
│   └── final_report.html
│
├── Test_Cases.xlsx
└── Bug_Report.docx
```

---

## Test Modules

- Landing Page
- Login Page
- Signup Page
- Forgot Password Page
- Logout Page

---

## Features Automated

### Landing Page

- Verify page loads successfully
- Verify page title
- Verify Sign In button
- Verify Sign Up button
- Verify Hero Section
- Verify Key Features
- Verify FAQ Section
- Verify Footer
- Verify Social Media Links

### Login Page

- Verify Login page loads
- Verify UI elements
- Verify empty email validation
- Verify invalid email
- Verify registered email flow
- Verify Forgot Password navigation
- Verify password field
- Verify successful login

### Signup Page

- Verify Signup page loads
- Verify UI elements
- Verify empty form validation
- Verify invalid email
- Verify password mismatch
- Verify existing user validation
- Verify Terms & Conditions
- Verify successful signup

### Forgot Password Page

- Verify Forgot Password page
- Verify email field
- Verify Send Verification button
- Verify Back button
- Verify registered email reset flow

### Logout Page

- Verify Profile icon
- Verify Sign Out option
- Verify Sign Out confirmation popup
- Verify successful logout
- Verify redirect to Login page

---

# Running Individual Test Modules

## Landing Page

```bash
pytest main.py::TestLandingPage --browser firefox --headed --html=reports/landing.html --self-contained-html
```

---

## Login Page

```bash
pytest main.py::TestLoginPage --browser firefox --headed --html=reports/login.html --self-contained-html
```

---

## Signup Page

```bash
pytest main.py::TestSignupPage --browser firefox --headed --html=reports/signup.html --self-contained-html
```

---

## Forgot Password Page

```bash
pytest main.py::TestForgotPasswordPage --browser firefox --headed --html=reports/forgot_password.html --self-contained-html
```

---

## Logout Page

```bash
pytest main.py::TestLogoutPage --browser firefox --headed --html=reports/logout.html --self-contained-html
```

---

# Generate Complete Test Report

```bash
pytest main.py --browser firefox --headed --html=reports/final_report.html --self-contained-html
```

---

## HTML Reports

All execution reports are generated inside the **reports/** folder.

Example:

```
reports/
│── landing.html
│── login.html
│── signup.html
│── forgot_password.html
│── logout.html
└── final_report.html
```

---

## Test Documentation

This project also includes:

- Test Case Document (Excel)
- Bug Report Document (Word)
- HTML Execution Reports
- Automation Source Code

---

## Author

**Rohit K**

QA Automation Engineer (Fresher)

Built using **Python + Playwright + Pytest**.# Tichi_Automation_Testing
