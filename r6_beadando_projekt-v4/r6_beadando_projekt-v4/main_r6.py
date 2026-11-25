import os
import sys
import subprocess
from openpyxl import Workbook, load_workbook

from data.r6.generator import generate_people, generate_operators, generate_match_records
from data.r6.handler import csv_handler, json_handler, xlsx_handler


def open_file(path: str) -> None:
    abs_path = os.path.abspath(path)
    if sys.platform.startswith("win"):
        os.startfile(abs_path)
    elif sys.platform == "darwin":
        subprocess.run(["open", abs_path], check=False)
    else:
        subprocess.run(["xdg-open", abs_path], check=False)


def main() -> None:
    out_dir = "output"
    os.makedirs(out_dir, exist_ok=True)

    people = generate_people(10)
    operators = generate_operators(8)
    records = generate_match_records(25, people=people, operators=operators)

    csv_handler.write_people(people, out_dir)
    csv_handler.write_operators(operators, out_dir)
    csv_handler.write_match_records(records, out_dir)

    p_csv = csv_handler.read_people(out_dir)
    o_csv = csv_handler.read_operators(out_dir)
    r_csv = csv_handler.read_match_records(out_dir)

    json_handler.write_people(people, out_dir)
    json_handler.write_operators(operators, out_dir)
    json_handler.write_match_records(records, out_dir)

    p_json = json_handler.read_people(out_dir)
    o_json = json_handler.read_operators(out_dir)
    r_json = json_handler.read_match_records(out_dir)

    xlsx_path = os.path.join(out_dir, "r6_data.xlsx")
    wb = Workbook()
    wb.remove(wb.active)
    xlsx_handler.write_people(people, wb, sheet_name="people")
    xlsx_handler.write_operators(operators, wb, sheet_name="operators")
    xlsx_handler.write_match_records(records, wb, sheet_name="match_records")
    wb.save(xlsx_path)

    wb_read = load_workbook(xlsx_path)
    p_xlsx = xlsx_handler.read_people(wb_read, sheet_name="people")
    o_xlsx = xlsx_handler.read_operators(wb_read, sheet_name="operators")
    r_xlsx = xlsx_handler.read_match_records(wb_read, sheet_name="match_records")

    print(
        f"CSV:  Person={len(p_csv)}, Operator={len(o_csv)}, MatchRecord={len(r_csv)}\n"
        f"JSON: Person={len(p_json)}, Operator={len(o_json)}, MatchRecord={len(r_json)}\n"
        f"XLSX: Person={len(p_xlsx)}, Operator={len(o_xlsx)}, MatchRecord={len(r_xlsx)}"
    )

    open_file(xlsx_path)


if __name__ == "__main__":
    main()
