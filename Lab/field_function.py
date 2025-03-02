from dataclasses import dataclass, field

@dataclass
class Employee:
    lemp: list = field(default_factory=list)
