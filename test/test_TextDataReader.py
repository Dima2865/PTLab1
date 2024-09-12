from typing import Tuple, Dict, List

import pytest
from src.Types import DataType, DataTypeJson
from src.TextDataReader import TextDataReader, TextDataReaderJson
import json


class TestTextDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "Иванов Константин Дмитриевич\n" + \
                "   математика:91\n" + " химия:100\n" + \
                "Петров Петр Семенович\n" + \
                "   русский язык:87\n" + " литература:78\n"
        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = TextDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]


class TestDataReaderJson:
    @pytest.fixture()
    def json_data_content(self) -> tuple[str, DataTypeJson]:
        json_data = {
            "Иванов Константин Дмитриевич": {
                "математика": 91,
                "химия": 100
            },
            "Петров Петр Семенович": {
                "русский язык": 87,
                "литература": 78
            }
        }
        json_content = json.dumps(json_data, ensure_ascii=False)
        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return json_content, data

    @pytest.fixture()
    def filepath_and_data(self,
                          json_data_content: tuple[str, DataTypeJson],
                          tmpdir) -> tuple[str, DataTypeJson]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(json_data_content[0], encoding='utf-8')
        return str(p), json_data_content[1]

    def test_read(self, filepath_and_data: Tuple[str, DataTypeJson]) -> None:
        json_reader = TextDataReaderJson()
        file_content = json_reader.read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
