import csv
import os
from data.r6.model import Person, Operator, MatchRecord


def _parse_bool(value: str) -> bool:
    return value.strip().lower() in ("true", "1", "yes", "t")


def write_people(
    people: list[Person],
    path: str,
    file_name: str = "people",
    extension: str = ".csv",
    heading: bool = True,
    delimiter: str = ";",
) -> None:
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, file_name + extension)
    fieldnames = ["id", "name", "age", "male"]
    with open(full_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=delimiter, fieldnames=fieldnames)
        if heading:
            writer.writeheader()
        for person in people:
            writer.writerow(person.__dict__)


def read_people(
    path: str,
    file_name: str = "people",
    extension: str = ".csv",
    delimiter: str = ";",
) -> list[Person]:
    full_path = os.path.join(path, file_name + extension)
    with open(full_path, newline="", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [
            Person(
                row["id"],
                row["name"],
                int(row["age"]),
                _parse_bool(row["male"]),
            )
            for row in rows
        ]


def write_operators(
    operators: list[Operator],
    path: str,
    file_name: str = "operators",
    extension: str = ".csv",
    heading: bool = True,
    delimiter: str = ";",
) -> None:
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, file_name + extension)
    fieldnames = ["id", "name", "side", "squad", "speed", "armor"]
    with open(full_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=delimiter, fieldnames=fieldnames)
        if heading:
            writer.writeheader()
        for op in operators:
            writer.writerow(op.__dict__)


def read_operators(
    path: str,
    file_name: str = "operators",
    extension: str = ".csv",
    delimiter: str = ";",
) -> list[Operator]:
    full_path = os.path.join(path, file_name + extension)
    with open(full_path, newline="", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [
            Operator(
                row["id"],
                row["name"],
                row["side"],
                row["squad"],
                int(row["speed"]),
                int(row["armor"]),
            )
            for row in rows
        ]


def write_match_records(
    records: list[MatchRecord],
    path: str,
    file_name: str = "match_records",
    extension: str = ".csv",
    heading: bool = True,
    delimiter: str = ";",
) -> None:
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, file_name + extension)
    fieldnames = ["id", "person_id", "operator_id", "map_name", "kills", "deaths", "assists", "won"]
    with open(full_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=delimiter, fieldnames=fieldnames)
        if heading:
            writer.writeheader()
        for rec in records:
            writer.writerow(rec.__dict__)


def read_match_records(
    path: str,
    file_name: str = "match_records",
    extension: str = ".csv",
    delimiter: str = ";",
) -> list[MatchRecord]:
    full_path = os.path.join(path, file_name + extension)
    with open(full_path, newline="", encoding="utf-8") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [
            MatchRecord(
                row["id"],
                row["person_id"],
                row["operator_id"],
                row["map_name"],
                int(row["kills"]),
                int(row["deaths"]),
                int(row["assists"]),
                _parse_bool(row["won"]),
            )
            for row in rows
        ]
