import json
import os
from data.r6.model import Person, Operator, MatchRecord


def write_people(
    people: list[Person],
    path: str,
    file_name: str = "people",
    extension: str = ".json",
) -> None:
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, file_name + extension)
    with open(full_path, "w", encoding="utf-8") as file:
        json.dump([p.__dict__ for p in people], file, ensure_ascii=False, indent=2)


def read_people(
    path: str,
    file_name: str = "people",
    extension: str = ".json",
) -> list[Person]:
    full_path = os.path.join(path, file_name + extension)
    with open(full_path, encoding="utf-8") as file:
        data = json.load(file)
    return [
        Person(item["id"], item["name"], int(item["age"]), bool(item["male"]))
        for item in data
    ]


def write_operators(
    operators: list[Operator],
    path: str,
    file_name: str = "operators",
    extension: str = ".json",
) -> None:
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, file_name + extension)
    with open(full_path, "w", encoding="utf-8") as file:
        json.dump([op.__dict__ for op in operators], file, ensure_ascii=False, indent=2)


def read_operators(
    path: str,
    file_name: str = "operators",
    extension: str = ".json",
) -> list[Operator]:
    full_path = os.path.join(path, file_name + extension)
    with open(full_path, encoding="utf-8") as file:
        data = json.load(file)
    return [
        Operator(
            item["id"],
            item["name"],
            item["side"],
            item["squad"],
            int(item["speed"]),
            int(item["armor"]),
        )
        for item in data
    ]


def write_match_records(
    records: list[MatchRecord],
    path: str,
    file_name: str = "match_records",
    extension: str = ".json",
) -> None:
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, file_name + extension)
    with open(full_path, "w", encoding="utf-8") as file:
        json.dump([r.__dict__ for r in records], file, ensure_ascii=False, indent=2)


def read_match_records(
    path: str,
    file_name: str = "match_records",
    extension: str = ".json",
) -> list[MatchRecord]:
    full_path = os.path.join(path, file_name + extension)
    with open(full_path, encoding="utf-8") as file:
        data = json.load(file)
    return [
        MatchRecord(
            item["id"],
            item["person_id"],
            item["operator_id"],
            item["map_name"],
            int(item["kills"]),
            int(item["deaths"]),
            int(item["assists"]),
            bool(item["won"]),
        )
        for item in data
    ]
