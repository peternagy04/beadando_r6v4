import openpyxl
from data.r6.model import Person, Operator, MatchRecord


def _to_bool(val) -> bool:
    if isinstance(val, bool):
        return val
    return str(val).strip().lower() in ("true", "1", "yes", "t")


def write_people(
    people: list[Person],
    workbook: openpyxl.Workbook,
    sheet_name: str = "people",
    heading: bool = True,
) -> None:
    sheet = workbook.create_sheet(sheet_name if sheet_name is not None else "people")
    offset = 1
    if heading:
        field_names = ["id", "name", "age", "male"]
        for col, name in enumerate(field_names, start=1):
            sheet.cell(row=1, column=col, value=name)
        offset = 2

    for idx, person in enumerate(people):
        r = idx + offset
        sheet.cell(row=r, column=1, value=person.id)
        sheet.cell(row=r, column=2, value=person.name)
        sheet.cell(row=r, column=3, value=person.age)
        sheet.cell(row=r, column=4, value=person.male)


def read_people(
    workbook: openpyxl.Workbook,
    sheet_name: str = "people",
    heading: bool = True,
) -> list[Person]:
    sheet = workbook[sheet_name]
    people: list[Person] = []
    row = 2 if heading else 1
    while sheet.cell(row=row, column=1).value is not None:
        people.append(
            Person(
                str(sheet.cell(row=row, column=1).value),
                str(sheet.cell(row=row, column=2).value),
                int(sheet.cell(row=row, column=3).value),
                _to_bool(sheet.cell(row=row, column=4).value),
            )
        )
        row += 1
    return people


def write_operators(
    operators: list[Operator],
    workbook: openpyxl.Workbook,
    sheet_name: str = "operators",
    heading: bool = True,
) -> None:
    sheet = workbook.create_sheet(sheet_name if sheet_name is not None else "operators")
    offset = 1
    if heading:
        field_names = ["id", "name", "side", "squad", "speed", "armor"]
        for col, name in enumerate(field_names, start=1):
            sheet.cell(row=1, column=col, value=name)
        offset = 2

    for idx, op in enumerate(operators):
        r = idx + offset
        sheet.cell(row=r, column=1, value=op.id)
        sheet.cell(row=r, column=2, value=op.name)
        sheet.cell(row=r, column=3, value=op.side)
        sheet.cell(row=r, column=4, value=op.squad)
        sheet.cell(row=r, column=5, value=op.speed)
        sheet.cell(row=r, column=6, value=op.armor)


def read_operators(
    workbook: openpyxl.Workbook,
    sheet_name: str = "operators",
    heading: bool = True,
) -> list[Operator]:
    sheet = workbook[sheet_name]
    operators: list[Operator] = []
    row = 2 if heading else 1
    while sheet.cell(row=row, column=1).value is not None:
        operators.append(
            Operator(
                str(sheet.cell(row=row, column=1).value),
                str(sheet.cell(row=row, column=2).value),
                str(sheet.cell(row=row, column=3).value),
                str(sheet.cell(row=row, column=4).value),
                int(sheet.cell(row=row, column=5).value),
                int(sheet.cell(row=row, column=6).value),
            )
        )
        row += 1
    return operators


def write_match_records(
    records: list[MatchRecord],
    workbook: openpyxl.Workbook,
    sheet_name: str = "match_records",
    heading: bool = True,
) -> None:
    sheet = workbook.create_sheet(sheet_name if sheet_name is not None else "match_records")
    offset = 1
    if heading:
        field_names = ["id", "person_id", "operator_id", "map_name", "kills", "deaths", "assists", "won"]
        for col, name in enumerate(field_names, start=1):
            sheet.cell(row=1, column=col, value=name)
        offset = 2

    for idx, rec in enumerate(records):
        r = idx + offset
        sheet.cell(row=r, column=1, value=rec.id)
        sheet.cell(row=r, column=2, value=rec.person_id)
        sheet.cell(row=r, column=3, value=rec.operator_id)
        sheet.cell(row=r, column=4, value=rec.map_name)
        sheet.cell(row=r, column=5, value=rec.kills)
        sheet.cell(row=r, column=6, value=rec.deaths)
        sheet.cell(row=r, column=7, value=rec.assists)
        sheet.cell(row=r, column=8, value=rec.won)


def read_match_records(
    workbook: openpyxl.Workbook,
    sheet_name: str = "match_records",
    heading: bool = True,
) -> list[MatchRecord]:
    sheet = workbook[sheet_name]
    records: list[MatchRecord] = []
    row = 2 if heading else 1
    while sheet.cell(row=row, column=1).value is not None:
        records.append(
            MatchRecord(
                str(sheet.cell(row=row, column=1).value),
                str(sheet.cell(row=row, column=2).value),
                str(sheet.cell(row=row, column=3).value),
                str(sheet.cell(row=row, column=4).value),
                int(sheet.cell(row=row, column=5).value),
                int(sheet.cell(row=row, column=6).value),
                int(sheet.cell(row=row, column=7).value),
                _to_bool(sheet.cell(row=row, column=8).value),
            )
        )
        row += 1
    return records
