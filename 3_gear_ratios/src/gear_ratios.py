# 467..114..
# ...*......

from dataclasses import dataclass
import re

@dataclass
class Number:
    number: str
    position: int

    def __post_init__(self):
        self.number_range = set(range(self.position, self.position + len(self.number)))

@dataclass
class Symbol:
    symbol: str
    position: int

class GearRatios:

    def __init__(self, lines: str = None):
        if lines:
            self._all_numbers = self._find_all_numbers(lines=lines)
            self._adjacent_numbers = [number for number in self._all_numbers if number[1] is True]

    @property
    def all_numbers(self) -> list[tuple]:
        return self._all_numbers
    
    @property
    def adjacent_numbers(self):
        return self._adjacent_numbers

    @property
    def sum_adjacent_numbers(self):
        numbers, adjacency = zip(*self.adjacent_numbers)
        return sum(numbers)

    def _find_all_numbers(self, lines: str):
        numbers = self._get_numbers(lines)
        numbers = self._find_symbols_by_numbers(numbers, lines)
        return numbers

    def _find_symbols_by_numbers(self, numbers: list, lines: str) -> list[tuple]:
        
        number_symbol = []
        
        for number in numbers:
            number_symbol.append((int(number.number), self._find_adjacent_symbol(lines=lines, number=number)))

        return number_symbol

    def _get_numbers(self, lines: str) -> list:
        numbers: list = []
        for match in re.finditer(r'\d+', lines):
            numbers.append(Number(match.group(), match.start()))
        return numbers

    def _find_adjacent_symbol(self, lines: str, number):
        line_length = len(lines[:lines.find("\n",1)])+1
        ranges = self.__calculate_search_ranges(lines, number, line_length)
        symbols = self.__get_all_symbols(lines)  # TODO: search only for symbols in range

        for symbol in symbols:
            for possible_range in ranges:
                if possible_range[0] <= symbol.position <= possible_range[1]:
                    return True
                    
        return False
    
    def __get_all_symbols(self, lines):
        symbols: list[Symbol] = []
        for index, char in enumerate(lines):
            if not char.isalnum() and char != "." and char != "\n":
                symbols.append(Symbol(char, index))

        return symbols
    

    def __calculate_search_ranges(self, lines, number, line_length):
        front = number.position - 1
        end = number.position + len(number.number)

        return [
            (front,end),
            (front - line_length, end - line_length),
            (front + line_length, end + line_length)
            ]
