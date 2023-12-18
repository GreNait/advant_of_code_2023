from dataclasses import dataclass, field
import math
import re

from src.gear_ratios.gear_ratios import Number

GEAR_SYMBOL = "*"


@dataclass
class Gear:
    position: int
    numbers: list = field(default_factory=list)

    def __post_init__(self):
        self.symbol = "*"

    @property
    def ratio(self):
        if len(self.numbers) == 2:
            numbers = [int(number.number) for number in self.numbers]
            return math.prod(numbers)

        return 0


@dataclass
class GearRange:
    start: int
    stop: int

    def __post_init__(self):
        self.gear_range = set(range(self.start, self.stop + 1))


class GearRanges:
    def __init__(self, gear_ranges: list[GearRange] = None):
        self.gear_ranges = []

        for gear_range in gear_ranges:
            self.gear_ranges.append(gear_range)

    def __add__(self, gear: Gear):
        self.gear_ranges.append(gear)

    def __eq__(self, other):
        return self.gear_ranges == other.gear_ranges

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.gear_ranges):
            return self.gear_ranges[self.current]
        raise StopIteration


class GearRatiosExtended:
    def __init__(self, lines: str = None):
        if lines:
            self._line_length = self._calculate_line_length(lines)
            self._gears = self._find_gears(lines=lines)
            self._gears = [self._numbers_on_gear(gear, lines) for gear in self._gears]

            sum = 0
            for gear in self._gears:
                try:
                    sum += int(gear.numbers[0].number) * int(gear.numbers[1].number)
                except IndexError:
                    pass

            self._power_all_gears = sum
        else:
            self._line_length = None

    @property
    def power_all_gears(self):
        return self._power_all_gears

    @property
    def line_length(self):
        return self._line_length

    def _find_gears(self, lines: str):
        gears: list = []
        for match in re.finditer(r"\*", lines):
            gears.append(Gear(match.start()))

        return gears

    def _numbers_on_gear(self, gear: Gear, lines: str):
        gear_ranges = self._gear_range(gear=gear)

        # start = lines.rfind("\n", 0, gear.position-self.line_length)
        # stop = lines.find("\n", gear.position+self.line_length)+1

        # if start < 0:
        #     start = 0

        for match in re.finditer(r"\d+", lines):
            number = Number(match.group(), match.start())

            if self._number_in_range(number=number, gear_ranges=gear_ranges):
                gear.numbers.append(number)

        return gear

    def _gear_range(self, gear: Gear) -> GearRanges:
        front = gear.position - 1
        tail = gear.position + 1

        front_range = GearRange(front - self.line_length, tail - self.line_length)
        current_line_range = GearRange(front, tail)
        tail_range = GearRange(front + self.line_length, tail + self.line_length)

        gear_ranges = GearRanges([front_range, current_line_range, tail_range])
        return gear_ranges

    def _number_in_range(self, number: Number, gear_ranges: GearRanges):
        for gear_range in gear_ranges:
            if number.number_range.intersection(gear_range.gear_range):
                return True

    def _calculate_line_length(self, lines: str) -> int:
        line_length = len(lines[: lines.find("\n")]) + 1
        return line_length
