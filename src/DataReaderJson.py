from Types import DataTypeJson
from abc import ABC, abstractmethod
from src.DataReader import DataReader


class DataReaderJson(DataReader, ABC):
    @abstractmethod
    def read(self, path: str) -> DataTypeJson:
        pass
