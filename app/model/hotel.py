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