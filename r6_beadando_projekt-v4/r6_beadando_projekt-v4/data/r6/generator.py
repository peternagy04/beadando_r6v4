import random
from faker import Faker
from faker.providers import BaseProvider

from data.r6.model import Person, Operator, MatchRecord


class R6Provider(BaseProvider):
    ATTACKERS = [
        ("Ash", "FBI SWAT", 3, 1),
        ("Thermite", "FBI SWAT", 2, 2),
        ("Sledge", "SAS", 2, 2),
        ("Thatcher", "SAS", 2, 2),
        ("Hibana", "SAT", 3, 1),
        ("Buck", "JTF2", 2, 2),
    ]
    DEFENDERS = [
        ("Jäger", "GSG 9", 2, 2),
        ("Bandit", "GSG 9", 3, 1),
        ("Mute", "SAS", 2, 2),
        ("Smoke", "SAS", 2, 2),
        ("Valkyrie", "Navy SEALs", 2, 2),
        ("Rook", "GIGN", 1, 3),
    ]
    MAPS = [
        "Clubhouse",
        "Oregon",
        "Bank",
        "Chalet",
        "Kafe Dostoyevsky",
        "Consulate",
        "Villa",
        "Border",
    ]

    def r6_operator_spec(self, side: str) -> tuple[str, str, int, int]:
        pool = self.ATTACKERS if side == "ATK" else self.DEFENDERS
        return self.random_element(pool)

    def r6_map(self) -> str:
        return self.random_element(self.MAPS)


def generate_people(
    n: int,
    male_ratio: float = 0.5,
    locale: str = "en_US",
    unique: bool = False,
    min_age: int = 16,
    max_age: int = 40,
) -> list[Person]:
    assert n > 0
    assert 0.0 <= male_ratio <= 1.0
    assert 0 <= min_age <= max_age <= 120

    fake = Faker(locale)
    faker_gen = fake.unique if unique else fake
    people: list[Person] = []

    for i in range(n):
        male = random.random() < male_ratio
        name = faker_gen.name_male() if male else faker_gen.name_female()
        people.append(
            Person(
                id=f"P-{str(i + 1).zfill(6)}",
                name=name,
                age=random.randint(min_age, max_age),
                male=male,
            )
        )
    return people


def generate_operators(
    n: int,
    atk_ratio: float = 0.5,
    locale: str = "en_US",
    unique: bool = False,
) -> list[Operator]:
    assert n > 0
    assert 0.0 <= atk_ratio <= 1.0

    fake = Faker(locale)
    fake.add_provider(R6Provider)
    used_names: set[str] = set()
    operators: list[Operator] = []

    for i in range(n):
        side = "ATK" if random.random() < atk_ratio else "DEF"
        base_name, squad, speed, armor = fake.r6_operator_spec(side)
        name = base_name
        if unique:
            counter = 2
            while name in used_names:
                name = f"{base_name} #{counter}"
                counter += 1
            used_names.add(name)

        operators.append(
            Operator(
                id=f"OP-{str(i + 1).zfill(6)}",
                name=name,
                side=side,
                squad=squad,
                speed=speed,
                armor=armor,
            )
        )
    return operators


def generate_match_records(
    n: int,
    people: list[Person] | None = None,
    operators: list[Operator] | None = None,
    win_ratio: float = 0.5,
    max_kills: int = 16,
    max_deaths: int = 10,
    max_assists: int = 10,
    locale: str = "en_US",
) -> list[MatchRecord]:
    assert n > 0
    assert 0.0 <= win_ratio <= 1.0
    assert max_kills >= 0 and max_deaths >= 0 and max_assists >= 0

    if not people:
        people = generate_people(max(3, n // 2))
    if not operators:
        operators = generate_operators(max(4, n // 2))

    fake = Faker(locale)
    fake.add_provider(R6Provider)

    person_ids = [p.id for p in people]
    operator_ids = [op.id for op in operators]
    records: list[MatchRecord] = []

    for i in range(n):
        records.append(
            MatchRecord(
                id=f"MR-{str(i + 1).zfill(6)}",
                person_id=random.choice(person_ids),
                operator_id=random.choice(operator_ids),
                map_name=fake.r6_map(),
                kills=random.randint(0, max_kills),
                deaths=random.randint(0, max_deaths),
                assists=random.randint(0, max_assists),
                won=random.random() < win_ratio,
            )
        )
    return records
