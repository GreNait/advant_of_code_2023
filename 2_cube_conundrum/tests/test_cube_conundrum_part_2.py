import pathlib
import pytest

from src.cube_conundrum import CubeConundrumExtended, LoadGames

test_batch = {
    "Game 1": [(3, "blue"), (4, "red"), (1, "red"), (2, "green"), (6, "blue"), (2, "green")],
    "Game 2": [(1, "blue"),(2, "green"), (3, "green"), (4, "blue"), (1, "red"),  (1, "green"), (1, "blue")],
    "Game 3": [(8, "green"), (6, "blue"), (20, "red"), (5, "blue"), (4, "red"), (13, "green"), (5, "green"), (1, "red")],
    "Game 4": [(1, "green"), (3, "red"), (6, "blue"), (3, "green"), (6, "red"), (3, "green"), (15, "blue"), (14, "red")],
    "Game 5": [(6, "red"), (1, "blue"), (3, "green"), (2, "blue"), (1, "red"), (2, "green")],
    }

test_limits = [
    (12, "red"),
    (13, "green"),
    (14, "blue"),
]

test_validation = [True,True,False,False,True]
test_minimum_cubes = [
    [(4, "red"), (2, "green"), (6, "blue")],
    [(3, "green"), (4, "blue"), (1, "red"),],
    [(6, "blue"), (20, "red"), (13, "green")],
    [(3, "green"),(15, "blue"), (14, "red")],
    [(6, "red"),(3, "green"), (2, "blue")],
]

test_power_of_cubes = [
    48,
    12,
    1560,
    630,
    36
]

def test_get_minimum_cubes_of_game():
    # path_to_list = pathlib.Path("tests/list_of_test_games.txt")
    # assert path_to_list.is_file()

    # load_games = LoadGames(path_to_list)
    cube_conundrum = CubeConundrumExtended() #games=load_games.games, limits=test_limits
    for game, minimum_cubes in zip(test_batch, test_minimum_cubes):
        assert sorted(cube_conundrum._min_cubes_of_game(game=test_batch[game])) == sorted(minimum_cubes)

def test_calculate_power_of_cubes():
    cube_conundrum = CubeConundrumExtended()

    for cubes, power_of_cubes in zip(test_minimum_cubes, test_power_of_cubes):
        assert cube_conundrum._calculate_power_of_cubes(cubes=cubes) == power_of_cubes

def test_get_power_of_cubes_with_test_data():
    cube_conundrum = CubeConundrumExtended(games=test_batch, limits=test_limits)
    assert sorted(cube_conundrum.power_of_cubes) == sorted(test_power_of_cubes)

def test_calculate_overall_power_of_cubes():
    cube_conundrum = CubeConundrumExtended(games=test_batch, limits=test_limits)
    assert cube_conundrum.overall_power_of_cubes == 2286 == sum(test_power_of_cubes)