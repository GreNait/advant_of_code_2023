from src.trebuchet import Trebuchet

class TrebuchetLetters(Trebuchet):

    __letter_numbers = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    __letter_lookup = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    def _first_digit(self, value: str) -> str:
        letter_number_indices = self.__letter_number_indices(value, find=value.find)
        number_index = self.__number_index(value=value, number=super()._first_digit(value), find=value.find)
        self.__check_for_no_indices(letter_number_indices, number_index)
        return self.__search_first_number(letter_number_indices, number_index)
    
    def _last_digit(self, value: str) -> str:
        letter_number_indices = self.__letter_number_indices(value, find=value.rfind)
        number_index = self.__number_index(value=value, number=super()._last_digit(value), find=value.rfind)
        self.__check_for_no_indices(letter_number_indices, number_index)
        return self.__search_last_number(letter_number_indices, number_index)

    def __search_first_number(self, letter_number_indices: list[dict], number_index: dict) -> str:
        if len(letter_number_indices) > 0 and number_index["Number"] is None:
            return self.__letter_lookup[letter_number_indices[0]["Number"]]
        
        if number_index["Number"] is not None and len(letter_number_indices) == 0:
            return number_index["Number"]

        if letter_number_indices[0]["Index"] > number_index["Index"]:
            return number_index["Number"]
        
        return self.__letter_lookup[letter_number_indices[0]["Number"]]
    
    def __search_last_number(self, letter_number_indices: list[dict], number_index: dict) -> str:
        if len(letter_number_indices) > 0 and number_index["Number"] is None:
            return self.__letter_lookup[letter_number_indices[-1]["Number"]]
        
        if number_index["Number"] is not None and len(letter_number_indices) == 0:
            return number_index["Number"]

        if letter_number_indices[-1]["Index"] < number_index["Index"]:
            return number_index["Number"]
        
        return self.__letter_lookup[letter_number_indices[-1]["Number"]]

    def __check_for_no_indices(self, letter_number_indices, number_index):
        if len(letter_number_indices) == 0 and number_index["Number"] is None:
            raise ValueError("Neither number nor letter number found.") from None

    def __letter_number_indices(self, value: str, find) -> list[dict]:
        letter_number_indices = []
        for number in self.__letter_numbers:
            if value.find(number) > -1:
                letter_number_indices.append({"Number": number, "Index": find(number)})

        letter_number_indices = sorted(letter_number_indices, key=lambda d: d['Index'])
        return letter_number_indices 
    
    def __number_index(self, value: str, number: str, find) -> dict:
        if number:
            return {"Number": number, "Index": find(number)}
        
        return {"Number": None, "Index": None}
    

        



