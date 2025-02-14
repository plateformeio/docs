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
from plateforme import BaseServiceWithSpec, BaseSpec, Key, KeyList
from plateforme.api import AsyncSessionDep, Selection, route

class DescriptionSpec(BaseSpec):
    """A description specification."""
    code: str
    name: str

class SelectionSpecService(BaseServiceWithSpec[DescriptionSpec]):
    """A service with a selection specification."""

    @route.get(path='/describe')
    async def describe_one(
        self,
        session: AsyncSessionDep,
        selection: Key[DescriptionSpec] = Selection(),
    ) -> str:
        result = await selection.resolve(session)
        return f"{result.name} ({result.code})"

    @route.get(path='/describe')
    async def describe_many(
        self,
        session: AsyncSessionDep,
        selection: KeyList[DescriptionSpec] = Selection(),
    ) -> list[str]:
        result = await selection.resolve(session)
        descriptions = []
        for item in result:
            descriptions.append(f"{item.name} ({item.code})")
        return descriptions
# --8<-- [end:snippet-services]

# --8<-- [start:snippet-resources]
from plateforme import ConfigDict, CRUDResource, Field

class Material(CRUDResource):
    __config__ = ConfigDict(services=[..., SelectionSpecService])

    code: str = Field(unique=True)
    name: str

class Rocket(CRUDResource):
    __config__ = ConfigDict(services=[..., SelectionSpecService])

    code: str = Field(unique=True)
    name: str
# --8<-- [end:snippet-resources]

# Setup database
if __name__ == '__main__':
    app.metadata.create_all()
