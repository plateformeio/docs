from plateforme import CRUDResource, Field

class Material(CRUDResource):
    code: str = Field(unique=True, max_length=10)
    name: str = Field(max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    price: float = Field(gt=0)
