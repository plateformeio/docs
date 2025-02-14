from pathlib import Path

from plateforme import ConfigDict, CRUDResource, Field, Plateforme
from plateforme.api import AsyncSessionDep, route
from plateforme.database import func, select

dirname = Path(__file__).parent

# Create application
app = Plateforme(
    debug=True,
    logging={'level': 'DEBUG'},
    database_engines=dirname / 'plateforme.db',
)

# Example
# --8<-- [start:snippet]
class Material(CRUDResource):
    code: str = Field(unique=True)
    name: str
    rocket_parts: list['RocketPart'] = Field(default_factory=list)  # (1)!

    @route.post()  # (2)!
    async def update_name(self, name: str) -> str:
        self.name = name
        return f'Material name updated to {name!r}.'

    @route.get()  # (3)!
    @classmethod
    async def count(cls, session: AsyncSessionDep) -> int:
        query = select(func.count()).select_from(cls)
        result = await session.execute(query)
        return result.scalar()

class Rocket(CRUDResource):
    code: str = Field(unique=True)
    name: str
    parts: list['RocketPart'] = Field(default_factory=list)  # (4)!

class RocketPart(CRUDResource):
    __config__ = ConfigDict(indexes=[{'rocket', 'material'}])  # (5)!

    rocket: Rocket  # (6)!
    material: Material
    quantity: int
# --8<-- [end:snippet]

# Setup database
if __name__ == '__main__':
    app.metadata.create_all()
