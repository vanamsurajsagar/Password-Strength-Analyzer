import string
import pytest

from password_analyzer import (
    analyze_password,
    calculate_entropy,
    generate_password,
    get_verdict,
    has_repeated_pattern,
    has_sequential_pattern,
)


def test_admin_is_weak_and_zero_score():
    result = analyze_password("admin")
    assert result["score"] == 0
    assert result["verdict"] == "Weak"
    assert result["is_common"] is True


def test_password_1234_is_weak():
    result = analyze_password("pass1234")
    assert result["score"] < 40
    assert result["verdict"] == "Weak"


def test_strong_password():
    result = analyze_password("T9!vQ2#xLm7@Kp4$")
    assert result["score"] >= 60
    assert result["verdict"] in {"Strong", "Very Strong"}


def test_complexity():
    result = analyze_password("AbcdEF12!xyz")
    assert result["length"] == 12
    assert result["entropy"] > 0


def test_entropy():
    assert calculate_entropy("") == 0.0
    assert calculate_entropy("aaaa") > 0
    assert calculate_entropy("Aa1!") > calculate_entropy("aaaa")


def test_verdict_thresholds():
    assert get_verdict(0) == "Weak"
    assert get_verdict(39) == "Weak"
    assert get_verdict(40) == "Moderate"
    assert get_verdict(59) == "Moderate"
    assert get_verdict(60) == "Strong"
    assert get_verdict(79) == "Strong"
    assert get_verdict(80) == "Very Strong"


def test_repeated_pattern():
    assert has_repeated_pattern("aaaPassword!")
    assert not has_repeated_pattern("Qx7!Lm2@Za9#")


def test_sequential_pattern():
    assert has_sequential_pattern("abcXYZ!789")
    assert not has_sequential_pattern("Qm8!Rt2#Lp")


def test_generator_length():
    password = generate_password(20)
    assert len(password) == 20


def test_generator_contains_character_types():
    password = generate_password(20)
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in string.punctuation for c in password)


def test_generator_rejects_short_password():
    with pytest.raises(ValueError):
        generate_password(8)
