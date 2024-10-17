from abc import ABC
from Types import DataTypeJson
from src.DataReaderJson import DataReaderJson
import json


# Класс считывающий данные из .json файла
# (используется библиотека для работы с json)
class TextDataReaderJson(DataReaderJson, ABC):
    def __init__(self) -> None:
        self.students: DataTypeJson = {}

    def read(self, path: str) -> DataTypeJson:
        with open(path, encoding='utf-8') as file:
            self.students = json.load(file)
        return self.students
