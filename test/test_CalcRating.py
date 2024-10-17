from src.Types import DataType, DataTypeJson
from src.CalcRating import CalcRating
from src.CalcRatingJson import CalcRatingJson
from src.CalculateLowScores import CalculateLowScores
import pytest


RatingsType = dict[str, float]


class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000
        }

        return data, rating_scores

    def test_init_calc_rating(self, input_data: tuple[DataType,
                              RatingsType]) -> None:
        calc_rating = CalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType,
                  RatingsType]) -> None:
        rating = CalcRating(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]


# ----------------------------
# Тест класса CalcRatingJson.py
class TestCalcRatingJson:
    @pytest.fixture()
    def input_data(self) -> tuple[DataTypeJson, dict[str, float]]:
        data: DataTypeJson = {
            "Абрамов Петр Сергеевич": {
                "математика": 80,
                "русский язык": 76,
                "программирование": 100
            },
            "Петров Игорь Владимирович": {
                "математика": 61,
                "русский язык": 80,
                "программирование": 78,
                "литература": 97
            },
            "Сидоров Алексей": {
                "математика": 90
            },
            "Кузнецова Анна": {}
        }

        expected_ratings = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0,
            "Сидоров Алексей": 90.0,
            "Кузнецова Анна": 0.0
        }

        return data, expected_ratings

    # Данный тест проверяет, что данные инициализации
    # корректно сохраняются в экземпляре класса.
    def test_init_calc_rating_json(self, input_data: tuple[
                DataTypeJson, dict[str, float]]) -> None:
        calc_rating = CalcRatingJson(input_data[0])
        assert input_data[0] == calc_rating.data

    # Данный тест проверяет, правильно ли
    # рассчитывается рейтинг студентов
    def test_calc_json(self, input_data: tuple[
                DataTypeJson, dict[str, float]]) -> None:
        calc_rating = CalcRatingJson(input_data[0])
        ratings = calc_rating.calc_json()
        for student in ratings.keys():
            rating_score = ratings[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]


# Тест класса calculateLowScores
class TestCalculateLowScores:
    @pytest.fixture()
    def input_data(self) -> tuple[DataTypeJson, int]:
        data: DataTypeJson = {
            "Абрамов Петр Сергеевич": {
                "математика": 80,
                "русский язык": 76,
                "программирование": 100
            },
            "Петров Игорь Владимирович": {
                "математика": 58,
                "русский язык": 80,
                "программирование": 78,
                "литература": 97
            },
            "Сидоров Алексей": {
                "математика": 50
            },
            "Кузнецова Анна": {}
        }

        expected_count = 2

        return data, expected_count

    # Данный тест проверяет, что данные инициализации корректно
    # сохраняются в экземпляре класса.
    def test_init_calculate_low_scores(self, input_data: tuple[
                DataTypeJson, int]) -> None:
        calc_low_scores = CalculateLowScores(input_data[0])
        assert input_data[0] == calc_low_scores.data

    # Данный тест проверяет, правильно ли метод
    # count_students_with_low_scores считает студентов с низкими оценками.
    def test_count_students_with_low_scores(self, input_data: tuple[
                DataTypeJson, int]) -> None:
        calc_low_scores = CalculateLowScores(input_data[0])
        count = calc_low_scores.count_students_with_low_scores()
        assert count == input_data[1]
