class Trebuchet:

    __digits = range(10)

    def __init__(self, values: list[str] = None):
        if values:
            self.calculate_calibrations(values)

    @property
    def calibrations(self):
        return self._calibrations
    
    @calibrations.setter
    def calibrations(self, value):
        raise ValueError("Cannot set calibrations manually.") from None

    def calculate_calibrations(self, values: list[str]) -> list[int]:
        self._calibrations = [self.calculate_calibration(value) for value in values]
        return self._calibrations

    def calculate_calibration(self, value: str) -> int:
        first = self._first_digit(value)
        last = self._last_digit(value)

        return int(first+last)

    def _first_digit(self, value: str) -> str:
        for char in value:
            if self.__check_for_number(char):
                return char
            
    def _last_digit(self, value: str) -> str:
        for char in value[::-1]:
            if self.__check_for_number(char):
                return char
            
    def __check_for_number(self, char: str):
        try:
            if int(char) in self.__digits:
                return True
        except ValueError:
            pass
        
        return False