from src.trebuchet.trebuchet import Trebuchet

import pytest

trebuchet = Trebuchet()

test_batch = [
    ("1abc2", "1", "2", 12),
    ("pqr3stu8vwx", "3", "8", 38),
    ("a1b2c3d4e5f", "1", "5", 15),
    ("treb7uchet", "7", "7", 77),
]


@pytest.mark.parametrize("value, first, last, combined", test_batch)
class TestTrebuchetSingleValues:
    def test_find_first_digit(self, value, first, last, combined):
        assert trebuchet._first_digit(value) == first

    def test_find_last_digit(self, value, first, last, combined):
        assert trebuchet._last_digit(value) == last

    def test_combine_digits(self, value, first, last, combined):
        assert trebuchet.calculate_calibration(value) == combined


@pytest.mark.parametrize(
    "values, calibrations",
    [(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], [12, 38, 15, 77])],
)
class TestTrebuchetListOfValues:
    def test_list_of_calibrations(self, values, calibrations):
        assert trebuchet.calculate_calibrations(values) == calibrations

    def test_list_of_calibrations_by_initialised_trebuchet(self, values, calibrations):
        trebuchet = Trebuchet(values)
        assert trebuchet.calibrations == calibrations

    def test_set_list_of_calibrations(self, values, calibrations):
        trebuchet = Trebuchet(values=values)

        with pytest.raises(ValueError):
            trebuchet.calibrations = "test"

        assert trebuchet.calibrations == calibrations
