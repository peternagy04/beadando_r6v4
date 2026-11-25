from dataclasses import dataclass
from functools import total_ordering


@total_ordering
@dataclass
class Person:
    id: str
    name: str
    age: int
    male: bool = True

    def __str__(self) -> str:
        return f"#{self.id}: {self.name} ({self.age}, {self.male})"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Person) and self.id == o.id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.id < other.id

    def __hash__(self) -> int:
        return hash(self.id)


@total_ordering
@dataclass
class Operator:
    id: str
    name: str
    side: str
    squad: str
    speed: int
    armor: int

    def __str__(self) -> str:
        return (
            f"#{self.id}: {self.name} [{self.side} - {self.squad}] "
            f"(SPD:{self.speed}, ARM:{self.armor})"
        )

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Operator) and self.id == o.id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Operator):
            return NotImplemented
        return self.id < other.id

    def __hash__(self) -> int:
        return hash(self.id)


@total_ordering
@dataclass
class MatchRecord:
    id: str
    person_id: str
    operator_id: str
    map_name: str
    kills: int
    deaths: int
    assists: int
    won: bool

    def __str__(self) -> str:
        res = "WIN" if self.won else "LOSS"
        return (
            f"#{self.id}: P={self.person_id} OP={self.operator_id} "
            f"Map={self.map_name} K/D/A={self.kills}/{self.deaths}/{self.assists} ({res})"
        )

    def __eq__(self, o: object) -> bool:
        return isinstance(o, MatchRecord) and self.id == o.id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, MatchRecord):
            return NotImplemented
        return self.id < other.id

    def __hash__(self) -> int:
        return hash(self.id)
