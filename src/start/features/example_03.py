from plateforme import Plateforme

# Create application
app = Plateforme(
    debug=True,
    logging={'level': 'DEBUG'},
    database_engines='plateforme.db',
)

# Example
# --8<-- [start:snippet]
from plateforme import BaseResource, Field
from plateforme.api import AsyncSessionDep, route
from plateforme.database import func, select

class Material(BaseResource):
    code: str = Field(unique=True)
    name: str

    @route.post()  # (1)!
    async def update_name(self, name: str) -> str:
        self.name = name
        return f'Material name updated to {name!r}.'

    @route.get()  # (2)!
    @classmethod
    async def count(cls, session: AsyncSessionDep) -> int:
        query = select(func.count()).select_from(cls)
        result = await session.execute(query)
        return result.scalar()
# --8<-- [end:snippet]

# Setup database
if __name__ == '__main__':
    app.metadata.create_all()
