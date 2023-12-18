from src.gear_ratios.gear_ratio_extended import GearRatiosExtended
from src.gear_ratios.gear_ratios import GearRatios

with open("src/gear_ratios/gear_ratio.txt", "r", encoding="UTF-8") as file:
    content = file.read()

gear_ratios = GearRatios(lines=content)
print(gear_ratios.sum_adjacent_numbers)

gear_ratios = GearRatiosExtended(lines=content)
print(gear_ratios.power_all_gears)
