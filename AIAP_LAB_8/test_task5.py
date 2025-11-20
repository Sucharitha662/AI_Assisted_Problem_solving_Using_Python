import pytest
from task5 import convert_date_format

@pytest.mark.parametrize("input_date, expected", [
    # Valid formats (structure correct, digits only) -> converted
    ("2023-10-15", "15-10-2023"),
    ("1999-01-01", "01-01-1999"),
    ("2020-12-31", "31-12-2020"),
    # Correct format but semantically invalid month -> function only checks format, so it will convert
    ("2023-13-01", "01-13-2023"),
])
def test_convert_date_format_valid(input_date, expected):
    assert convert_date_format(input_date) == expected

@pytest.mark.parametrize("input_date", [
    # Wrong separators or order
    "2023/10/15",
    "15-10-2023",
    # Missing zero-padding
    "2023-2-5",
    # No separators
    "20231015",
    # Non-digit components
    "abcd-ef-gh",
    # Empty string
    "",
    # Too many components -> ValueError in split unpacking handled by function
    "2023-10-15-00",
    # Leading/trailing whitespace breaks the digit checks
    " 2023-10-15",
])
def test_convert_date_format_invalid(input_date):
    assert convert_date_format(input_date) == "Invalid date format"