# 🔐 Password Strength Analyzer

> A Python-based cybersecurity tool that evaluates password strength using **length, entropy, character complexity, common-password detection, and rule-based scoring**.

This project was developed as a cybersecurity learning project inspired by a password-strength-checker tutorial and extended with a **Streamlit web interface, secure password generation, bcrypt-based password history, SQLite storage, and automated testing with pytest**.

---

## 📌 Overview

Weak and reused passwords are common security risks. This project provides a simple way to evaluate a password before using it.

The analyzer examines:

* Password length
* Character composition
* Estimated entropy
* Common-password usage
* Repeated patterns
* Sequential patterns
* Rule-based security score

The application then produces a final strength verdict.

---

## ✨ Features

### 🔎 Password Analysis

* Password length calculation
* Lowercase character detection
* Uppercase character detection
* Number detection
* Special-character detection
* Common-password detection
* Repeated-pattern detection
* Sequential-pattern detection
* Estimated entropy calculation

### 📊 Strength Scoring

The analyzer produces a score from **0 to 100**.

|  Score | Verdict        |
| -----: | -------------- |
|   0–39 | 🔴 Weak        |
|  40–59 | 🟠 Moderate    |
|  60–79 | 🟢 Strong      |
| 80–100 | 🔵 Very Strong |

A password found in the application's common-password list receives a score of **0**.

### 💡 Security Suggestions

The application provides recommendations such as:

* Increase password length
* Add uppercase letters
* Add lowercase letters
* Add numbers
* Add special characters
* Avoid common passwords
* Avoid repeated characters
* Avoid predictable sequences

### 🔐 Strong Password Generator

The application can generate strong passwords using Python's `secrets` module.

Users can select a password length between **12 and 40 characters**.

### 🗄️ Password History

An optional local password-history feature is included.

Passwords are **not stored as plaintext**. Password-history entries are stored using **bcrypt password hashes**.

### 🧪 Automated Testing

The project includes automated tests using **pytest**.

Tests cover:

* Weak/common passwords
* Password scoring
* Strength verdict thresholds
* Entropy calculation
* Character complexity
* Repeated patterns
* Sequential patterns
* Password generation
* Invalid generator input
* Password-history functionality
* Verification that plaintext passwords are not stored

---

## 🛠️ Tech Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Core application logic          |
| Streamlit  | Web interface                   |
| SQLite     | Local password-history database |
| bcrypt     | Secure password hashing         |
| pytest     | Automated testing               |
| pytest-cov | Test coverage                   |

---

## 📁 Project Structure

```text
Password-Strength-Analyzer/
│
├── app.py
├── password_analyzer.py
├── database.py
├── requirements.txt
├── pytest.ini
├── README.md
│
└── tests/
    ├── conftest.py
    ├── test_password_analyzer.py
    └── test_database.py
```

### File Description

| File                              | Description                                              |
| --------------------------------- | -------------------------------------------------------- |
| `app.py`                          | Streamlit application and user interface                 |
| `password_analyzer.py`            | Password analysis, entropy, scoring, and generator logic |
| `database.py`                     | SQLite database and bcrypt password-history functions    |
| `tests/test_password_analyzer.py` | Tests for password-analysis functionality                |
| `tests/test_database.py`          | Tests for password-history and hashing                   |
| `tests/conftest.py`               | Pytest project-path configuration                        |
| `pytest.ini`                      | Pytest configuration                                     |
| `requirements.txt`                | Required Python packages                                 |

---

## ⚙️ How the Analyzer Works

### 1. Character Pool

The application estimates the available character pool based on the characters used in the password.

| Character Type     |    Possible Characters |
| ------------------ | ---------------------: |
| Lowercase          |                     26 |
| Uppercase          |                     26 |
| Digits             |                     10 |
| Special characters | Python punctuation set |

### 2. Entropy

Estimated entropy is calculated using:

```text
Entropy = Password Length × log₂(Character Pool Size)
```

A larger character pool and longer password generally increase the theoretical search space.

### 3. Rule-Based Score

The analyzer awards points for password characteristics such as:

```text
Lowercase character  → +10
Uppercase character  → +10
Digit                → +10
Special character    → +10
Length ≥ 8           → +10
Length ≥ 12          → +15
Length ≥ 16          → +15
```

Additional penalties are applied for obvious repeated and sequential patterns.

---

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed:

```powershell
python --version
```

Python 3.10+ is recommended for this project.

### 1. Clone the Repository

```powershell
git clone https://github.com/vanamsurajsagar/Password-Strength-Analyzer.git
cd Password-Strength-Analyzer
```

### 2. Create a Virtual Environment

```powershell
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
venv\Scripts\activate
```

### 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 5. Run the Application

```powershell
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🧪 Running Tests

Run the complete test suite:

```powershell
pytest -v
```

Run tests with coverage:

```powershell
pytest --cov=. --cov-report=term-missing
```

Example successful test result:

```text
13 passed
```

---

## 🔒 Security Considerations

This project is designed for **educational and portfolio purposes**.

### Password Privacy

The application does not store passwords as plaintext in the password-history database.

Instead, password-history entries are stored as **bcrypt hashes**.

### Secure Password Generation

Password generation uses Python's `secrets` module instead of the standard `random` module.

### Local Processing

Password analysis is performed locally by the application.

### Important Limitation

The common-password dataset included in this project is intentionally small for demonstration. A production security system should use a more comprehensive password-strength and compromised-password detection strategy.

Entropy is also a theoretical estimate and should not be interpreted as a guarantee against real-world attacks.

---

## 🧪 Testing Philosophy

Automated tests help verify that security-related functionality behaves as expected.

The test suite validates both normal functionality and security-related behavior, including:

```text
Password analysis
       ↓
Score calculation
       ↓
Verdict classification
       ↓
Password generation
       ↓
Hash storage
       ↓
Password reuse detection
```

This provides a repeatable way to detect regressions when the project is modified.

---

## 📈 Future Improvements

Planned improvements could include:

* Larger compromised-password dataset
* Have I Been Pwned k-anonymity integration
* Argon2id password hashing
* Improved password-strength heuristics
* GitHub Actions CI/CD testing
* User authentication
* Password manager integration
* Streamlit Cloud deployment
* More detailed security reports

---

## 🎓 Learning Outcomes

This project demonstrates practical understanding of:

* Python programming
* Cybersecurity fundamentals
* Password security
* Entropy and search-space concepts
* Secure password generation
* Hashing and salting
* SQLite database operations
* Streamlit application development
* Unit testing with pytest
* Test coverage
* Basic secure software-development practices

---

## 📚 Tutorial Reference

This project was developed as an extended implementation of the password-string-checker concepts presented in the tutorial provided for the internship task.

The tutorial focuses on password **length, entropy, rule-based scoring, common-password comparison, and final strength classification**. This repository extends those concepts with a web UI, password generation, password-history hashing, and automated tests.

---

## 👨‍💻 Author

**Suraj Sagar**

GitHub: [@vanamsurajsagar](https://github.com/vanamsurajsagar)

Repository: [Password-Strength-Analyzer](https://github.com/vanamsurajsagar/Password-Strength-Analyzer)

---

## ⚠️ Disclaimer

This project is intended for **educational and cybersecurity-learning purposes**.

It is not intended to replace production-grade authentication, password-management, or enterprise password-security systems.
