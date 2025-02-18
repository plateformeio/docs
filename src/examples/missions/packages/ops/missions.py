import datetime
from plateforme import CRUDResource, Field

from ..assets import Rocket
from ..staff import Crew
from .stations import Station

class Mission(CRUDResource):
    code: str = Field(unique=True, max_length=10)
    name: str = Field(max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    crew: Crew
    rocket: Rocket
    station: Station
    launch_date: datetime.date = Field(default_factory=datetime.date.today)
