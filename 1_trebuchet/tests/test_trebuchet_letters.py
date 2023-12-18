from src.trebuchet_letters import TrebuchetLetters

import pytest

test_batch = [
    ("two1nine", "2", "9", 29),
    ("eightwothree", "8", "3", 83),
    ("abcone2threexyz", "1", "3", 13),
    ("xtwone3four", "2", "4", 24),
    ("4nineeightseven2", "4", "2", 42),
    ("zoneight234", "1", "4", 14),
    ("7pqrstsixteen", "7", "6", 76),
    ("9cbncbxclbvkmfzdnldc", "9", "9", 99),
    ("kc1", "1", "1", 11),
    ("sevenrhqt9sixthreethree", "7", "3", 73),
    ("oneight", "1", "8", 18),
    ("chphzzqb6threeqhspbgkrn6\n", "6", "6", 66)
]

sum_of_test_batch = 281
trebuchet = TrebuchetLetters()

def test_provided_list():
    test_batch = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    trebuchet = TrebuchetLetters(test_batch)
    assert sum(trebuchet.calibrations) == 281

def test_raise_exception_when_no_number():
    with pytest.raises(ValueError):
        trebuchet._first_digit(value="abcd")

@pytest.mark.parametrize("value, first, last, combined", test_batch)
class TestTrebuchetLetterSingleValue:
    def test_find_first_letter_number(self, value, first, last, combined):
        assert trebuchet._first_digit(value) == first

    def test_find_last_letter_number(self, value, first, last, combined):
        assert trebuchet._last_digit(value) == last

    def test_combinded_digits(self, value, first, last, combined):
        assert trebuchet.calculate_calibration(value) == combined

@pytest.mark.parametrize(
    "values, calibrations",
    [
        (
            ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four","4nineeightseven2", "zoneight234", "7pqrstsixteen"],
            [29,83,13,24,42,14,76]
        )
    ]
)
class TestTrebuchetLetterListOfValues:
    def test_list_of_calibrations(self, values, calibrations):
        assert trebuchet.calculate_calibrations(values) == calibrations


class TestCompareSolutions:
    # https://discord.com/channels/267624335836053506/1180009538544488478/1180030927863291934
    def part2(self, line):
        mappings = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

        line_new = [x if (x := "".join([v for k, v in mappings.items() if line[i:].startswith(k)])) else line[i] for i in range(len(line))]
        digits = [int(i) for i in line_new if i.isdigit()]
        return digits[0] * 10 + digits[-1]
    
    def test_provided_data(self):
        with open("src/calibrations.txt", "r") as file:
            list_of_codes = file.readlines()

        for line in list_of_codes:
            part2_data = self.part2(line)
            trebuchet_letters_data = trebuchet.calculate_calibration(line)

            if part2_data != trebuchet_letters_data:
                pass
