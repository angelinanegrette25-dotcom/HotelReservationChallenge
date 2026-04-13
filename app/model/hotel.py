from dataclasses import dataclass, field
from datetime import date
from typing import List
from app.services.util import generate_unique_id, guest_not_found_error

class Guest:
    # Variables de clase (Constantes)
    REGULAR: str = "regular"
    VIP: str = "vip"
    name: str
    email: str
    type_: str = REGULAR

    def __str__(self) -> str:
        return f"Guest {self.name} ({self.email}) of type {self.type_}"


class Reservation:
    guest_name: str
    description: str
    check_in: date
    check_out: date
    guests: List[Guest] = field(init=False, default_factory=list)
    id: str = field(default_factory=generate_unique_id)