
import pytest
from bill import calc, calc2


def test_household_exactly_100_units():
    assert calc("A", "x", 100, "H", 0, 0) == pytest.approx(354.0)


def test_household_101_units():
    assert calc("A", "x", 101, "H", 0, 0) == pytest.approx(359.9)


def test_household_150_units():
    assert calc("A", "x", 150, "H", 0, 0) == pytest.approx(649.0)


def test_household_exactly_300_units():
    assert calc("A", "x", 300, "H", 0, 0) == pytest.approx(1534.0)


def test_household_301_units():
    assert calc("A", "x", 301, "H", 0, 0) == pytest.approx(1543.44)


def test_commercial_150_units():
    assert calc("A", "x", 150, "C", 0, 0) == pytest.approx(1239.0)


def test_senior_household_gets_discount():
    assert calc("A", "x", 150, "H", 0, 1) == pytest.approx(621.5)


def test_senior_commercial_gets_no_discount():
    assert calc("A", "x", 150, "C", 0, 1) == pytest.approx(1239.0)


def test_zero_previous_due():
    assert calc("A", "x", 150, "H", 0, 0) == pytest.approx(649.0)


def test_positive_previous_due_household():
    assert calc("A", "x", 200, "H", 200, 0) == pytest.approx(1148.0)


def test_positive_previous_due_commercial():
    assert calc("A", "x", 350, "C", 100, 0) == pytest.approx(3642.0)


def test_invalid_type_return_value(capsys):
    result = calc("A", "x", 50, "Z", 0, 0)

    assert result == -1
    assert capsys.readouterr().out == (
        "Customer: A\n"
        "Address: x\n"
        "bad type\n"
    )


def test_calc_prints_expected_output(capsys):
    result = calc("A", "x", 150, "H", 0, 0)

    assert result == pytest.approx(649.0)
    assert capsys.readouterr().out == (
        "Customer: A\n"
        "Address: x\n"
        "Total: 649.0\n"
    )


def test_calc2_returns_receipt_text():
    assert calc2("Ravi", "Noida", 150, "H", 0, 0) == (
        "Customer: Ravi\n"
        "Address: Noida\n"
        "Total: 649.0"
    )


def test_calc2_invalid_type_returns_text():
    assert calc2("Ravi", "Noida", 50, "Z", 0, 0) == "bad type"


def test_calc2_positive_previous_due():
    assert calc2("A", "x", 200, "H", 200, 0) == (
        "Customer: A\n"
        "Address: x\n"
        "Total: 1148.0"
    )


def test_senior_flag_other_than_one_gets_no_discount():
    assert calc("A", "x", 150, "H", 0, 2) == pytest.approx(649.0)


def test_negative_previous_due_is_added_without_surcharge():
    assert calc("A", "x", 150, "H", -100, 0) == pytest.approx(549.0)


def test_zero_units():
    assert calc("A", "x", 0, "H", 0, 0) == pytest.approx(0.0)
