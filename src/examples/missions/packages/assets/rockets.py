from plateforme import BaseResource, CRUDResource, ConfigDict, Field
from plateforme.schema import computed_field

from .materials import Material

class Rocket(CRUDResource):
    code: str = Field(unique=True, max_length=10)
    name: str = Field(max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    parts: list['RocketPart'] = Field(default_factory=list)

    @computed_field
    @property
    def price(self) -> float:
        return sum(part.material.price * part.quantity for part in self.parts)

class RocketPart(BaseResource):
    __config__ = ConfigDict(
        indexes=[
            {'rocket', 'code'},
            {'rocket', 'material'}
        ],
    )
    code: str = Field(max_length=10)
    rocket: Rocket
    material: Material
    quantity: int
