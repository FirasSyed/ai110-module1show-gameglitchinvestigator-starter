from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_secret_as_string():
    # If the secret is provided as a string, comparisons should still work
    result = check_guess(60, "50")
    assert result == "Too High"


def test_parse_guess_valid_integer():
    # A normal integer string should parse successfully
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty_string():
    # An empty input should fail with an error message
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_non_numeric():
    # A non-numeric string should fail with an error message
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_decimal():
    # A decimal input should be truncated to an integer
    ok, value, _ = parse_guess("7.9")
    assert ok is True
    assert value == 7
