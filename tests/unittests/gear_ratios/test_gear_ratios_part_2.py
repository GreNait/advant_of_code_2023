from src.gear_ratios.gear_ratio_extended import (
    Gear,
    GearRange,
    GearRanges,
    GearRatiosExtended,
)
from src.gear_ratios.gear_ratios import Number

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
    assert gear_ratios._gear_range(gear=Gear(47)) == GearRanges(
        [GearRange(35, 37), GearRange(46, 48), GearRange(57, 59)]
    )


def test_number_in_range():
    gear_ratios = GearRatiosExtended(lines=test_example_engine_schematic)
    assert (
        gear_ratios._number_in_range(
            number=Number(number="467", position=0),
            gear_ranges=gear_ratios._gear_range(Gear(14)),
        )
        == True
    )
    assert (
        gear_ratios._number_in_range(
            number=Number(number="35", position=24),
            gear_ranges=gear_ratios._gear_range(Gear(14)),
        )
        == True
    )


def test_find_numbers_on_gear():
    gear_ratios = GearRatiosExtended(lines=test_example_engine_schematic)
    assert gear_ratios._numbers_on_gear(
        gear=Gear(14), lines=test_example_engine_schematic
    ) == Gear(
        14, numbers=[Number(number="467", position=0), Number(number="35", position=24)]
    )
    assert gear_ratios._numbers_on_gear(
        gear=Gear(47), lines=test_example_engine_schematic
    ) == Gear(47, numbers=[Number(number="617", position=44)])
    assert gear_ratios._numbers_on_gear(
        gear=Gear(93), lines=test_example_engine_schematic
    ) == Gear(
        93,
        numbers=[Number(number="755", position=83), Number(number="598", position=104)],
    )


def test_calculate_power_of_gear_numbers():
    gear_ratios = GearRatiosExtended(lines=test_example_engine_schematic)
    gear: Gear = gear_ratios._numbers_on_gear(
        gear=Gear(14), lines=test_example_engine_schematic
    )
    assert gear.ratio == 16345

    gear: Gear = gear_ratios._numbers_on_gear(
        gear=Gear(47), lines=test_example_engine_schematic
    )
    assert gear.ratio == 0

    gear: Gear = gear_ratios._numbers_on_gear(
        gear=Gear(93), lines=test_example_engine_schematic
    )
    assert gear.ratio == 451490


def test_power_of_all_gears_combined():
    gear_ratios = GearRatiosExtended(lines=test_example_engine_schematic)
    assert gear_ratios.power_all_gears == 467835


# def test_power_of_gear_reald_data():
#     real_data = """...........................775.651...............887....79...946...921...493.....942..942.....151....155....................................
# ......240...................*.....-......................$..*...................*.......%.....+....................956.549.*290.......834...
# .485...+............437......906......%..608.805.725..72.....242....745..61......440................................*..*.........515...*....
# ..........917.......&....146........790.....*......*....*..........*.....*...............207*......................796..116......../...924..
# 722...323.-................./...410.............72..748.442............384.708...............849..%............................470..........
# .....*..........................*.....271..691....-...............4*...........388.................448......&........*....848&......751.....
# ....370..$....639.748.......*...467....*.....*........921*909.....................*...32.....................165..452.30....................
# ........984....*.....*...782........711.....50.172...............61&..........415.803.*.........524.......................203.......106*643.
# ...............57..433.........390....................&../.............*122...........674.........*.........................................
# 379..................../.........*........908..477...305.876..*..............297.415*......+.......94........../.....@378.......226..56*....
# ...*..-......82.......167...936.17..958...=....*...............196......+......*.......-...380.992.............989.........29......*....301.
# ..124..317.....*....................*..........839.......................191.882......231.........+......976.................+......469.....
# ............643................*........778............541........655..............*............*........./............*.................515
# .....&............498#...&....726.774..............111....*378..................723.221.......473............752....523.638.......789...*...
# """
#     gear_ratios = GearRatiosExtended(lines=real_data)
#     gear_ratios.
