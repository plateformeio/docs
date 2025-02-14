"""
The application main entry point.
This is where you can configure your application and also add resources.
"""

# --8<-- [start:app]
from plateforme import Plateforme

# Create application
app = Plateforme(
    title='My App',
    database_engines='plateforme.db',  # (1)!
)
# --8<-- [end:app]

# Add resources...
# --8<-- [start:imports]
from plateforme import ConfigDict, CRUDResource, Field, route
# --8<-- [end:imports]

# --8<-- [start:add-material]
class Material(CRUDResource):  # (1)!
    code: str = Field(unique=True)  # (2)!
    name: str
    rocket_parts: list['RocketPart'] = Field(default_factory=list)  # (3)!
# --8<-- [end:add-material]

# --8<-- [start:add-custom-route]
    @route.post()  # (1)!
    async def update_name(self, name: str) -> str:  # (2)!
        self.name = name  # (3)!
        return f'Material name updated to {name!r}.'
# --8<-- [end:add-custom-route]

# --8<-- [start:add-rocket]
class Rocket(CRUDResource):
    code: str = Field(unique=True)
    name: str
    parts: list['RocketPart'] = Field(default_factory=list)  # (1)!

class RocketPart(CRUDResource):
    __config__ = ConfigDict(indexes=[{'rocket', 'material'}])  # (2)!

    rocket: Rocket  # (3)!
    material: Material  # (4)!
    quantity: int
# --8<-- [end:add-rocket]
