PACKAGES = {
    'marketing': ('marketing/dist', ''),
}
"""Additional internal packages to include in the documentation."""

TAGS = [
    'API',
    'CLI',
    'Core',
    'Database',
    'Schema',
    'Types',
    'Plateforme',
    'FastAPI',
    'Pydantic',
    'SQLAlchemy',
    'Starlette',
    'External',
    'Internal',
    'Draft',
]
"""Allowed tags for the documentation."""


def tag_name_index(tag):
    """Resolves the index of a tag name.

    It is used to sort tags based on their position in the configured `TAGS`
    list first, otherwise alphabetically for tags not in the list.
    """
    if tag.name in TAGS:
        return TAGS.index(tag.name)
    return tag.name
