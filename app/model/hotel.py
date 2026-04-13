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

    def add_guest(self, name: str, email: str, type_: str = Guest.REGULAR):
        new_guest = Guest(name=name, email=email, type_=type_)
        self.guests.append(new_guest)

    def delete_guest(self, guest_index: int):
        if 0 <= guest_index < len(self.guests):
            self.guests.pop(guest_index)
        else:
            guest_not_found_error()

    def __len__(self) -> int:
        return (self.check_out - self.check_in).days

    def __str__(self) -> str:
        return (
            f"ID: {self.id}\n"
            f"Guest: {self.guest_name}\n"
            f"Description: {self.description}\n"
            f"Dates: {self.check_in} - {self.check_out}"
        )