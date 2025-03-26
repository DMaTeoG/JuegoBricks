# tests/test_password_validator.py
from src.password_validator import is_valid_password

def test_valid_passwords():
    assert is_valid_password("SecurePass1") == True
    assert is_valid_password("Valid123A") == True

def test_invalid_passwords():
    assert is_valid_password("short") == False
    assert is_valid_password("nouppercase1") == False
    assert is_valid_password("NOLOWERCASE1") == False
    assert is_valid_password("NoNumbers") == False
