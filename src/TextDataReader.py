from abc import ABC
from Types import DataType, DataTypeJson
from DataReader import DataReader, DataReaderJson
import json


class TextDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            for line in file:
                if not line.startswith(" "):
                    self.key = line.strip()
                    self.students[self.key] = []
                else:
                    subj, score = line.split(":", maxsplit=1)
                    self.students[self.key].append(
                        (subj.strip(), int(score.strip())))
        return self.students


class TextDataReaderJson(DataReaderJson, ABC):
    def __init__(self) -> None:
        self.students: DataTypeJson = {}

    def read(self, path: str) -> DataTypeJson:
        with open(path, encoding='utf-8') as file:
            self.students = json.load(file)
        return self.students
