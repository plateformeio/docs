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
from plateforme import BaseService, route

class NoSpecService(BaseService):
    """A service without specification."""

    @route.post()
    async def hello(self) -> str:  # (1)!
        return 'Hello, world!'
# --8<-- [end:snippet-services]

# --8<-- [start:snippet-resources]
from plateforme import BaseResource, ConfigDict

class Material(BaseResource):
    __config__ = ConfigDict(services=[NoSpecService])
# --8<-- [end:snippet-resources]

# Setup database
if __name__ == '__main__':
    app.metadata.create_all()
