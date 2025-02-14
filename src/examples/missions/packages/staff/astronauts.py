import typing
from typing import Literal
from plateforme import CRUDResource, Field

if typing.TYPE_CHECKING:
    from .crews import Crew

class Astronaut(CRUDResource):
    code: str = Field(unique=True, max_length=10)
    name: str = Field(max_length=100)
    role: Literal['doctor', 'engineer', 'pilot', 'technician']
    crews: list['Crew'] = Field(default_factory=list)
