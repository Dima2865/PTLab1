from Types import DataType


# словари для хранения имени студентов и еих среднего балла по предметам
RatingType = dict[str, float]


# Исходный класс для подсчета рейтинга
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
