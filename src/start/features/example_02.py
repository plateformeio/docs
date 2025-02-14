from plateforme import Plateforme

# Create application
app = Plateforme(
    debug=True,
    logging={'level': 'DEBUG'},
    database_engines='plateforme.db',
)

# Example
# --8<-- [start:snippet]
from plateforme import ConfigDict, CRUDResource, Field

class Material(CRUDResource):
    code: str = Field(unique=True)
    name: str
    rocket_parts: list['RocketPart'] = Field(default_factory=list)  # (1)!

class Rocket(CRUDResource):
    code: str = Field(unique=True)
    name: str
    parts: list['RocketPart'] = Field(default_factory=list)  # (2)!

class RocketPart(CRUDResource):
    __config__ = ConfigDict(indexes=[{'rocket', 'material'}])  # (3)!

    rocket: Rocket  # (4)!
    material: Material
    quantity: int
# --8<-- [end:snippet]

# Setup database
if __name__ == '__main__':
    app.metadata.create_all()
