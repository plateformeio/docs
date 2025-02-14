from typing import Self
from plateforme import CRUDResource, Key, Field, route

from .astronauts import Astronaut

class Crew(CRUDResource):
    code: str = Field(unique=True, max_length=10)
    name: str = Field(max_length=100)
    astronauts: list[Astronaut] = Field(
        default_factory=list,
        rel_load='selectin',
    )
    lead: Astronaut | None = Field(
        default=None,
        init=False,
        association_alias='crew_lead',
    )

    @route.post()
    async def assign_lead(self, astronaut: Key[Astronaut]) -> Self:
        lead = await astronaut.resolve()
        if lead not in self.astronauts:
            raise ValueError('The lead must be part of the crew')
        self.lead = lead
        return self
