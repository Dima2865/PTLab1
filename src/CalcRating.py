from Types import DataType, DataTypeJson

RatingType = dict[str, float]


class CalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
        return self.rating


RatingTypeJson = dict[str, float]


class CalcRatingJson:
    def __init__(self, data: DataTypeJson) -> None:
        self.data: DataTypeJson = data
        self.rating: RatingTypeJson = {}

    def calc_json(self) -> RatingTypeJson:
        for key in self.data:
            scores = self.data[key]
            total_score = 0.0

            for subject, score in scores.items():
                total_score += score

            # Проверяем, что у студента есть предметы
            # с оценками, чтобы избежать деления на ноль
            if scores:
                self.rating[key] = total_score / len(scores)
            else:
                self.rating[key] = 0.0  # Если предметов нет, рейтинг 0.0

        return self.rating
