from src.Types import DataType, DataTypeJson
from src.CalcRating import CalcRating, CalcRatingJson
import pytest
import json

RatingsType = dict[str, float]

RatingsTypeJson = dict[str, float]


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


class TestCalcRatingJson:
    @pytest.fixture()
    def input_data(self) -> tuple[DataTypeJson, RatingsTypeJson]:
        # Представление данных в формате JSON
        json_data = {
            "Абрамов Петр Сергеевич": [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100)
            ],
            "Петров Игорь Владимирович": [
                ("математика", 61),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97)
            ]
        }

        # Конвертируем данные в JSON-строку
        json_content = json.dumps(json_data, ensure_ascii=False)

        # Ожидаемые рейтинговые оценки
        rating_scores: RatingsTypeJson = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000
        }

        return json.loads(json_content), rating_scores

    def test_init_calc_rating(self, input_data: tuple[DataTypeJson, RatingsTypeJson]) -> None:
        # Инициализируем CalcRating и проверяем корректность данных
        calc_rating = CalcRatingJson(input_data[0])
        assert input_data[0] == calc_rating.dataJson

    def test_calc(self, input_data: tuple[DataTypeJson, RatingsTypeJson]) -> None:
        # Проверяем корректность расчета рейтингов
        rating = CalcRatingJson(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score, abs=0.001) == input_data[1][student]