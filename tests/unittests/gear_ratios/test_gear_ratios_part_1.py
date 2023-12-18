import pytest
from src.gear_ratios.gear_ratios import GearRatios, Number

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

test_example_eninge_schematic_shortened = """..........
467..114..
...*......
"""

test_example_engine_schematic_longer = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...*.*....
.664.598..
"""

test_numbers = [
    (467, True),
    (114, False),
    (35, True),
    (633, True),
    (617, True),
    (58, False),
    (592, True),
    (755, True),
    (664, True),
    (598, True),
]

test_numbers_shortend = [(467, True), (114, False)]

test_numbers_longer = [
    (467, True),
    (114, False),
    (35, True),
    (633, True),
    (617, True),
    (58, False),
    (592, True),
    (755, True),
    (664, True),
    (598, True),
    (467, True),
    (114, False),
    (35, True),
    (633, True),
    (617, True),
    (58, False),
    (592, True),
    (755, True),
    (664, True),
    (598, True),
]

test_number_adjacent_short = [(467, True)]

test_number_adjacent = [
    (467, True),
    (35, True),
    (633, True),
    (617, True),
    (592, True),
    (755, True),
    (664, True),
    (598, True),
]

test_real_data_batch = """...........................775.651...............887....79...946...921...493.....942..942.....151....155....................................
......240...................*.....-......................$..*...................*.......%.....+....................956.549.*290.......834...
.485...+............437......906......%..608.805.725..72.....242....745..61......440................................*..*.........515...*....
..........917.......&....146........790.....*......*....*..........*.....*...............207*......................796..116......../...924..
722...323.-................./...410.............72..748.442............384.708...............849..%............................470..........
"""

test_real_data_number_adjacent = [
    (775, True),
    (651, True),
    (79, True),
    (946, True),
    (942, True),
    (942, True),
    (151, True),
    (240, True),
    (956, True),
    (549, True),
    (290, True),
    (834, True),
    (437, True),
    (906, True),
    (608, True),
    (805, True),
    (725, True),
    (72, True),
    (242, True),
    (745, True),
    (61, True),
    (440, True),
    (515, True),
    (917, True),
    (146, True),
    (790, True),
    (207, True),
    (796, True),
    (116, True),
    (924, True),
    (748, True),
    (442, True),
    (384, True),
    (849, True),
]

test_rea_data_sum = 19_230

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


def test_find_symbols_in_range():
    gear_ratios = GearRatios()
    assert (
        gear_ratios._find_adjacent_symbol(
            lines=test_example_eninge_schematic_shortened, number=Number("467", 12)
        )
        == True
    )
    assert (
        gear_ratios._find_adjacent_symbol(
            lines=test_example_eninge_schematic_shortened, number=Number("114", 17)
        )
        == False
    )


def test_get_list_of_numbers():
    gear_ratios = GearRatios()
    assert gear_ratios._get_numbers(lines=test_example_eninge_schematic_shortened) == [
        Number("467", 11),
        Number("114", 16),
    ]


def test_find_symbols_by_list():
    gear_ratios = GearRatios()
    assert (
        gear_ratios._find_symbols_by_numbers(
            numbers=[Number("467", 12), Number("114", 17)],
            lines=test_example_eninge_schematic_shortened,
        )
        == test_numbers_shortend
    )


def test_find_numbers_adjacent_by_lines():
    gear_ratios = GearRatios()
    assert (
        gear_ratios._find_all_numbers(lines=test_example_eninge_schematic_shortened)
        == test_numbers_shortend
    )


@pytest.mark.parametrize(
    "lines, test_numbers, adjacent_numbers",
    [
        (
            test_example_eninge_schematic_shortened,
            test_numbers_shortend,
            test_number_adjacent_short,
        ),
        (test_example_engine_schematic, test_numbers, test_number_adjacent),
    ],
)
def test_gear_ratios(lines, test_numbers, adjacent_numbers):
    gear_ratios = GearRatios(lines=lines)
    assert gear_ratios.all_numbers == test_numbers
    assert gear_ratios.adjacent_numbers == adjacent_numbers


def test_sum_adjacent_numbers():
    gear_ratios = GearRatios(lines=test_example_engine_schematic)
    assert gear_ratios.sum_adjacent_numbers == 4361


def test_adjacency_real_data():
    gear_ratios = GearRatios(lines=test_real_data_batch)
    assert gear_ratios.adjacent_numbers == test_real_data_number_adjacent

    assert gear_ratios.sum_adjacent_numbers == test_rea_data_sum
