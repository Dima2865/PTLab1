from Types import DataType, DataTypeJson
from abc import ABC, abstractmethod


class DataReader(ABC):
    @abstractmethod
    def read(self, path: str) -> DataType:
        pass


class DataReaderJson(DataReader, ABC):
    @abstractmethod
    def read(self, path: str) -> DataTypeJson:
        pass
