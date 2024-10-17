from Types import DataTypeJson


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
