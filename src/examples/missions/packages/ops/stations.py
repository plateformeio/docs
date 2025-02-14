import typing
from plateforme import CRUDResource, Field

if typing.TYPE_CHECKING:
    from .missions import Mission

class Station(CRUDResource):
    code: str = Field(unique=True, max_length=10)
    name: str = Field(max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    coordinates: str | None = Field(default=None)
    missions: list['Mission'] = Field(default_factory=list)
