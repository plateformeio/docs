from pathlib import Path
from plateforme import Plateforme

dirname = Path(__file__).parent

# Create application
app = Plateforme(
    debug=True,
    logging={'level': 'DEBUG'},
    database_engines=dirname / 'plateforme.db',
)

# Example
# --8<-- [start:snippet-services]
from plateforme import BaseServiceWithSpec, BaseSpec
from plateforme.api import AsyncSessionDep, route
from plateforme.database import select

class OrderableSpec(BaseSpec):
    """An orderable specification."""
    price: float

class SimpleSpecService(BaseServiceWithSpec[OrderableSpec]):
    """A service with a simple specification."""

    @route.post()
    async def buy(
        self,
        session: AsyncSessionDep,
        payload: dict[str, int],
    ) -> float:
        ids = [int(k) for k in payload.keys()]
        query = select(self.resource).filter(self.resource.id.in_(ids))
        buffer = await session.execute(query)
        result = buffer.scalars().all()

        if len(result) != len(payload):
            raise ValueError('Invalid payload')

        total = 0
        for item in result:
            total += item.price * payload[str(item.id)]

        await session.commit()
        return total
# --8<-- [end:snippet-services]

# --8<-- [start:snippet-resources]
from plateforme import ConfigDict, CRUDResource, Field

class Material(CRUDResource):
    __config__ = ConfigDict(services=[..., SimpleSpecService])

    code: str = Field(unique=True)
    name: str
    price: float

class Rocket(CRUDResource):
    __config__ = ConfigDict(services=[..., SimpleSpecService])

    code: str = Field(unique=True)
    name: str
    price: float
# --8<-- [end:snippet-resources]

# Setup database
if __name__ == '__main__':
    app.metadata.create_all()
