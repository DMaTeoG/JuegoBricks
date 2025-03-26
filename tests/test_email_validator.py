# tests/test_email_validator.py
from src.email_validator import is_valid_email

def test_valid_emails():
    assert is_valid_email("test@example.com") == True
    assert is_valid_email("user.name@domain.co") == True

def test_invalid_emails():
    assert is_valid_email("invalid-email") == False
    assert is_valid_email("user@domain") == False
    assert is_valid_email("user@.com") == False

