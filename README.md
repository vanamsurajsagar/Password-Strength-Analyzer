# 🔐 Password Strength Analyzer

Tutorial-aligned Python cybersecurity project based on the provided password-string-checker tutorial, extended with a Streamlit UI, password generator, password-history hashing, and automated pytest testing.

## Tutorial concepts

- Password length
- Entropy
- Rule-based score
- Common-password comparison
- Final verdict

## Verdict thresholds

```text
0–39   → Weak
40–59  → Moderate
60–79  → Strong
80–100 → Very Strong
```

## Project structure

```text
Password-Strength-Analyzer/
├── app.py
├── password_analyzer.py
├── database.py
├── requirements.txt
├── pytest.ini
├── README.md
└── tests/
    ├── conftest.py
    ├── test_password_analyzer.py
    └── test_database.py
```

## Install

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```powershell
streamlit run app.py
```

## Test

```powershell
pytest -v
```

## Coverage

```powershell
pytest --cov=. --cov-report=term-missing
```

## Important testing fix

`pytest.ini` includes:

```ini
pythonpath = .
```

and `tests/conftest.py` adds the project root to `sys.path`. This prevents the `ModuleNotFoundError` that occurs when pytest cannot import `database` and `password_analyzer`.

## Security

Password history stores bcrypt hashes, not plaintext passwords. Password generation uses `secrets`.

This is an educational project and not a complete production password-security solution.
