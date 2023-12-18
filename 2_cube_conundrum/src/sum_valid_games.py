import pathlib
from cube_conundrum import CubeConundrum, CubeConundrumExtended
from cube_conundrum import LoadGames

limits = [(12, "red"),(13, "green"),(14, "blue")]

loaded_games = LoadGames(pathlib.Path("src/list_of_games.txt")).games
print(CubeConundrum(games=loaded_games, limits=limits).sum_ids)

cube_conundrum = CubeConundrumExtended(games=loaded_games, limits=limits)
print(cube_conundrum.overall_power_of_cubes)