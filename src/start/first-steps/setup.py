"""
The application setup script used to build the database schema.
"""

# --8<-- [start:snippet]
from main import app

app.metadata.create_all()  # (1)!
# --8<-- [end:snippet]
