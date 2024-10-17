import argparse
import sys

from src.CalcRating import CalcRating
from src.CalcRatingJson import CalcRatingJson
from src.CalculateLowScores import CalculateLowScores
from src.TextDataReader import TextDataReader
from src.TextDataReaderJson import TextDataReaderJson


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    #
    # reader = TextDataReader()
    # students = reader.read(path)
    # print("Students: ", students)
    #
    # rating = CalcRating(students).calc()
    # print("Rating: ", rating)

    print("-------------------New functional------------------------")

    readerJson = TextDataReaderJson()
    studentsJson = readerJson.read(path)
    print("Students: ", studentsJson)
    ratingJson = CalcRatingJson(studentsJson).calc_json()
    print("Rating: ", ratingJson)

    print("--------------Проверка на академ. долги-------------------")

    calculator = CalculateLowScores(studentsJson)
    result = calculator.count_students_with_low_scores()
    print(f'Студенты с баллом <61 хотя бы по одному предмету: {result}')


if __name__ == "__main__":
    main()
