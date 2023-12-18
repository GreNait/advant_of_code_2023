from src.gear_ratios import GearRatios

with open("src/gear_ratio.txt", "r") as file:
    content = file.read()

gear_ratios = GearRatios(lines = content)
print(gear_ratios.sum_adjacent_numbers)