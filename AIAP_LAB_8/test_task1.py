import pytest
from task1 import is_valid_email

@pytest.mark.parametrize("email,expected", [
    ("user@example.com", True),
    ("john_doe123@mail.co", True),
    ("alice.bob@domain.org", True),
    ("user_name@sub.domain.com", True),
    ("a@b.co", True),
    (".user@domain.com", False),        # starts with '.'
    ("user@domain.com.", False),        # ends with '.'
    ("user@@domain.com", False),        # multiple '@'
    ("userdomain.com", False),          # missing '@'
    ("user@domaincom", False),          # missing '.' in domain
    ("user@.com", False),               # domain starts with '.'
    ("user@domain..com", False),        # double dot in domain
    ("user..name@domain.com", False),   # consecutive dots in local part
])
def test_is_valid_email_cases(email, expected):
    assert is_valid_email(email) == expected, f"Email: {email} expected {expected}"
    @pytest.mark.parametrize("email,expected", [
        ("user@example.com", True),
        ("john_doe123@mail.co", True),
        ("alice.bob@domain.org", True),
        ("user_name@sub.domain.com", True),
        ("a@b.co", True),
        (".user@domain.com", False),        # starts with '.'
        ("user@domain.com.", False),        # ends with '.'
        ("user@@domain.com", False),        # multiple '@'
        ("userdomain.com", False),          # missing '@'
        ("user@domaincom", False),          # missing '.' in domain
        ("user@.com", False),               # domain starts with '.'
        ("user@domain..com", False),        # double dot in domain
        ("user..name@domain.com", False),   # consecutive dots in local part
        ("user-name@domain.com", True),     # hyphen in username
        ("-user@domain.com", False),        # starts with hyphen
        ("user@domain-name.com", True),     # hyphen in domain
        ("user@-domain.com", False),        # domain starts with hyphen
        ("user_@domain.com", False),        # ends with underscore before @
        ("_user@domain.com", False),        # starts with underscore
        ("user@domain.c", True),            # minimal valid format
    ])
    def test_is_valid_email_cases(email, expected):
        assert is_valid_email(email) == expected, f"Email: {email} expected {expected}"


    def test_is_valid_email_empty_string():
        assert is_valid_email("") == False


    def test_is_valid_email_only_special_chars():
        assert is_valid_email("@.") == False


    def test_is_valid_email_spaces():
        assert is_valid_email("user @domain.com") == False
        assert is_valid_email("user@ domain.com") == False
