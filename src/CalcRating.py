from Types import DataType, DataTypeJson


# словари для хранения имени студентов и еих среднего балла по предметам
RatingType = dict[str, float]
RatingTypeJson = dict[str, float]


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


# Класс подсчитывающий студентов, у которых балл меньше 61
class CalculateLowScores:
    def __init__(self, data: DataTypeJson) -> None:
        self.data: DataTypeJson = data

    def count_students_with_low_scores(self) -> int:
        count = 0

        # Перебираем каждого студента
        for student_scores in self.data.values():
            # Проверяем, есть ли хотя бы одна оценка < 61
            if any(score < 61 for score in student_scores.values()):
                count += 1

        return count
