from src.trebuchet.trebuchet_letters import TrebuchetLetters

with open("src/calibrations.txt", "r", encoding="UTF-8") as file:
    list_of_codes = file.readlines()


def calculate_sum_of_code(letters):
    return sum(trebuchet_letters)


test_batch = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

print(sum(TrebuchetLetters(values=test_batch).calibrations))

trebuchet_letters = TrebuchetLetters(values=list_of_codes)
sum_of_calibrations = sum(trebuchet_letters.calibrations)
print(sum_of_calibrations)
