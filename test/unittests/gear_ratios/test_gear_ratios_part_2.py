from src.gear_ratio_extended import Gear, GearRange, GearRanges, GearRatiosExtended
from src.gear_ratios import Number, Symbol

# 467..114..
# ...*......
# ..35..633.

test_example_engine_schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

test_gear_positions = [Gear(14), Gear(47), Gear(93)]
test_gear_ratio_numbers = [(463, 35), (755, 598)]                         
test_gear_ratio = [16345, 451490]

def test_find_gears():
    gear_ratios = GearRatiosExtended()
    gears = gear_ratios._find_gears(lines=test_example_engine_schematic)
    assert len(gears) == len(test_gear_positions)
    assert gears == test_gear_positions

def test_calculate_line_length():
    gear_ratios = GearRatiosExtended()
    assert gear_ratios._calculate_line_length(lines=test_example_engine_schematic) == 11

    gear_ratios = GearRatiosExtended(lines=test_example_engine_schematic)
    assert gear_ratios.line_length == 11

def test_calculate_gear_ranges():
    gear_ratios = GearRatiosExtended(lines=test_example_engine_schematic)
    assert gear_ratios._gear_range(gear=Gear(47)) == GearRanges([GearRange(35,37),GearRange(46,48), GearRange(57, 59)])

def test_number_in_range():
    gear_ratios = GearRatiosExtended(lines=test_example_engine_schematic)
    assert gear_ratios._number_in_range(number=Number(number="467", position=0), gear_ranges=gear_ratios._gear_range(Gear(14))) == True
    assert gear_ratios._number_in_range(number=Number(number="35", position=24), gear_ranges=gear_ratios._gear_range(Gear(14))) == True

def test_find_numbers_on_gear():
    gear_ratios = GearRatiosExtended(lines=test_example_engine_schematic)
    assert gear_ratios._numbers_on_gear(gear=Gear(14), lines=test_example_engine_schematic) == Gear(14, numbers=[Number(number="467", position=0), Number(number="35", position=24)])
    assert gear_ratios._numbers_on_gear(gear=Gear(47), lines=test_example_engine_schematic) == Gear(47, numbers=[Number(number="617", position=44)])
    assert gear_ratios._numbers_on_gear(gear=Gear(93), lines=test_example_engine_schematic) == Gear(93, numbers=[Number(number="755", position=83), Number(number="598", position=104)])

def test_calculate_power_of_gear_numbers():
    gear_ratios = GearRatiosExtended(lines=test_example_engine_schematic)
    gear: Gear = gear_ratios._numbers_on_gear(gear=Gear(14), lines=test_example_engine_schematic)
    assert gear.ratio == 16345

    gear: Gear = gear_ratios._numbers_on_gear(gear=Gear(47), lines=test_example_engine_schematic)
    assert gear.ratio == 0

    gear: Gear = gear_ratios._numbers_on_gear(gear=Gear(93), lines=test_example_engine_schematic)
    assert gear.ratio == 451490