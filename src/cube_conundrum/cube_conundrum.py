import pathlib

class LoadGames:

    def __init__(self, path_to_list: pathlib.Path=None):
        if path_to_list:
            self._games = self._load_list_of_games(path_to_list)

    @property
    def games(self):
        return self._games

    def _load_list_of_games(self, path_to_list: pathlib.Path):
        with path_to_list.open("r") as file:
            list_of_games = file.readlines()

        formated_list_of_games = {}
        for game in list_of_games:
            formated_list_of_games = formated_list_of_games | self.format_game(game)

        return formated_list_of_games

    def format_game(self, line):
        formated_game = {}
        
        line = line.replace(";", ",")
        game, content = line.split(":")
        content = content.split(",")

        entries = []
        for entry in content:
            a,b = entry.strip().split(" ")
            entries.append((int(a), b))

        formated_game[game] = entries
        return formated_game

class CubeConundrum:

    def __init__(self, games: dict = None, limits:list[tuple] = None):
        if games is not None and limits is not None:
            self._games = games
            self._validates = [self._valid_game(games[game], limits) for game in games]
            self._sum_ids = self._calculate_ids(validations=self._validates)

    @property
    def validates(self) -> list[bool]:
        return self._validates
    
    @property
    def sum_ids(self) -> int:
        return self._sum_ids

    def _valid_game(self, game: list[tuple], limits:list[tuple]) -> bool:
        for limit in limits:
            for entry in game:
                if limit[1] == entry[1]:
                    if limit[0] < entry[0]:
                        return False
        
        return True
    
    def _calculate_ids(self, validations:list) -> int:
        sum_validations = 0

        for entry, validation in enumerate(validations, start=1):
            if validation:
                sum_validations+=entry

        return sum_validations
    

class CubeConundrumExtended(CubeConundrum):

    @property
    def overall_power_of_cubes(self):
        return sum(self.power_of_cubes)

    @property
    def power_of_cubes(self):

        cubes = []
        for game in self._games:
            cubes.append(self._calculate_power_of_cubes(cubes=self._min_cubes_of_game(game=self._games[game])))

        return cubes

    def _calculate_power_of_cubes(self, cubes: list[tuple]) -> int:
        sum_of_cubes = 1

        for cube in cubes:
            sum_of_cubes *= cube[0]

        return sum_of_cubes

    def _min_cubes_of_game(self, game: list[tuple]) -> dict:
        sorted_cubes = sorted(game, reverse=True)
        
        blue_cubes = self.__get_highest_cube(sorted_cubes=sorted_cubes, cube_color="blue")
        green_cubes = self.__get_highest_cube(sorted_cubes=sorted_cubes, cube_color="green")
        red_cubes = self.__get_highest_cube(sorted_cubes=sorted_cubes, cube_color="red")

        return [blue_cubes, green_cubes, red_cubes]

    def __get_highest_cube(self, sorted_cubes: list, cube_color: str):
        for cubes in sorted_cubes:
            if cubes[1] == cube_color:
                return cubes