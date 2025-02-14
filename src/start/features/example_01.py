from plateforme import Plateforme

# Create application
app = Plateforme(
    debug=True,
    logging={'level': 'DEBUG'},
    database_engines='plateforme.db',
)

# Example
# --8<-- [start:snippet]
from plateforme import CRUDResource, Field

class Material(CRUDResource):  # (1)!
    name: str

class Rocket(CRUDResource):
    name: str
    parts: list[Material] = Field(default_factory=list)  # (2)!
# --8<-- [end:snippet]

# Setup database
if __name__ == '__main__':
    app.metadata.create_all()
