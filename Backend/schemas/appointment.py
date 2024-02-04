from __future__ import annotations

from typing import TYPE_CHECKING, Optional
import argon2
from uuid import UUID

from datetime import date

from litestar.dto import DTOConfig
from litestar.contrib.pydantic import PydanticDTO
from .schema import Schema



class AppointmentSchema(Schema):
    id: UUID
    
    user_id: UUID
    doctor_id: UUID

    date: date
    description: str




# Define a DTO for user data
class AppointmentDTO(PydanticDTO[AppointmentSchema]):
    config = DTOConfig(
        max_nested_depth=2,
    )

class CreateAppointmentDTO(AppointmentDTO):
    config = DTOConfig(
        include={'doctor_id', 'date', 'description'}
    )


AppointmentSchema.model_rebuild()

