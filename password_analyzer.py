import math
import secrets
import string

COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "admin",
    "admin123",
    "welcome",
    "letmein",
    "iloveyou",
    "abc123",
    "monkey",
    "dragon",
}


def calculate_entropy(password: str) -> float:
    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if not password or pool_size == 0:
        return 0.0

    return len(password) * math.log2(pool_size)


def has_repeated_pattern(password: str) -> bool:
    for char in set(password):
        if char * 3 in password:
            return True

    for size in (2, 3):
        for i in range(len(password) - size * 2 + 1):
            chunk = password[i:i + size]
            if chunk * 2 in password:
                return True

    return False


def has_sequential_pattern(password: str) -> bool:
    sequences = [
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789",
        "9876543210",
    ]

    lower_password = password.lower()

    for sequence in sequences:
        for i in range(len(sequence) - 2):
            if sequence[i:i + 3] in lower_password:
                return True

    return False


def calculate_score(password: str) -> int:
    if password.lower() in COMMON_PASSWORDS:
        return 0

    score = 0

    if any(c.islower() for c in password):
        score += 10
    if any(c.isupper() for c in password):
        score += 10
    if any(c.isdigit() for c in password):
        score += 10
    if any(c in string.punctuation for c in password):
        score += 10
    if len(password) >= 8:
        score += 10
    if len(password) >= 12:
        score += 15
    if len(password) >= 16:
        score += 15

    if has_repeated_pattern(password):
        score -= 10
    if has_sequential_pattern(password):
        score -= 10

    return max(0, min(100, score))


def get_verdict(score: int) -> str:
    if score < 40:
        return "Weak"
    if score < 60:
        return "Moderate"
    if score < 80:
        return "Strong"
    return "Very Strong"


def analyze_password(password: str) -> dict:
    result = {
        "length": len(password),
        "entropy": calculate_entropy(password),
        "score": calculate_score(password),
        "verdict": get_verdict(calculate_score(password)),
        "is_common": password.lower() in COMMON_PASSWORDS,
        "suggestions": [],
    }

    if len(password) < 8:
        result["suggestions"].append("Use at least 8 characters.")
    elif len(password) < 12:
        result["suggestions"].append("Use 12 or more characters for better security.")

    if not any(c.islower() for c in password):
        result["suggestions"].append("Add lowercase letters.")
    if not any(c.isupper() for c in password):
        result["suggestions"].append("Add uppercase letters.")
    if not any(c.isdigit() for c in password):
        result["suggestions"].append("Add numbers.")
    if not any(c in string.punctuation for c in password):
        result["suggestions"].append("Add special characters.")
    if result["is_common"]:
        result["suggestions"].append("Avoid common passwords such as 'admin' or 'password'.")
    if has_repeated_pattern(password):
        result["suggestions"].append("Avoid repeated characters or repeated short patterns.")
    if has_sequential_pattern(password):
        result["suggestions"].append("Avoid predictable sequences such as 123 or abc.")

    return result


def generate_password(length: int = 20) -> str:
    if length < 12:
        raise ValueError("Password length should be at least 12.")

    alphabet = string.ascii_letters + string.digits + string.punctuation
    required = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    password_chars = required + [
        secrets.choice(alphabet) for _ in range(length - len(required))
    ]
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)
