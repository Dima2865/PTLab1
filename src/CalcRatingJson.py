from Types import DataTypeJson


# словари для хранения имени студентов и еих среднего балла по предметам
RatingTypeJson = dict[str, float]


# Класс для расчета рейтинга из json файла
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
                # Если предметов нет, рейтинг 0.0
                self.rating[key] = 0.0

        return self.rating
