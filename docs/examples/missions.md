# Missions example

!!! warning "The documentation is under heavy development!"

    The documentation is actively being developed and might not cover every feature. For full details, refer to the [source code]({{ links.repo.core }}).

## Overview

The missions example demonstrates how to build a full-featured application using Plateforme's resource management capabilities. This project showcases a space mission management system with multiple interconnected packages handling different aspects of space operations.

## Getting started

The missions example can be run using the Plateforme built-in CLI:

```bash
# Build the application and initialize the database
plateforme -p src/examples/missions build

# Start the application server
plateforme -p src/examples/missions start
```

The application will be available at `http://127.0.0.1:8001`.

## Project structure

The project implements a modular architecture through three packages: `assets`, `ops`, and `staff`. Each package manages a specific domain of space missions, such as physical resources, mission operations, and personnel.

```bash { .no-copy .no-select }
missions/
├── client/           # API request examples
├── packages/
│   ├── assets/       # Physical resource management
│   ├── ops/          # Mission operations
│   └── staff/        # Personnel management
├── server/
│   ├── main.py       # Application entry point
│   └── setup.py      # Database initialization
└── pyproject.toml    # Project configuration
```

## Project configuration

The project is configured through `pyproject.toml`, which defines both the project metadata and application settings:

```toml
--8<-- "src/examples/missions/pyproject.toml"
```

The configuration consists of two main sections. The project section defines basic metadata including the package name, version, and keywords. This information helps identify and categorize the project within a larger ecosystem.

The `plateforme.apps.default` section configures the application's build and runtime behavior. It specifies that the build process should run the `setup` script, which initializes the database with sample data. The `start` configuration indicates that the application should run on port `8001` using the `main.py` entry point.

## Application configuration

The application uses Plateforme's main entry point to configure and connect all components:

```python
--8<-- "src/examples/missions/server/main.py"
```

1. Enable debug mode for development.
2. Configure logging to output debug messages. Advanced configuration can be provided to customize logging behavior.
3. Define the database connection as a simple SQLite engine. Advanced configuration can be provided to specify multiple database engines and custom connection settings.
4. Configure namespaces for the packages. Setting an empty alias allows accessing resources endpoints directly without a prefix.
5. Register the packages to include within the application.

This configuration enables debug mode for development, sets up logging, and configures the database connection. It also registers the required packages and their namespaces, establishing the foundation for the modular architecture described below.

## Application build

The application build process is configured within the `pyproject.toml` file to run the `setup.py` script. The script initializes the database with sample data:

```python
...
--8<-- "src/examples/missions/server/setup.py:snippet"
...
```

??? quote "Source code in `src/examples/missions/server/setup.py`"

    ```python
    --8<-- "src/examples/missions/server/setup.py"
    ```

## Implementation

Each package is defined with a configuration file that includes the package's information and default namespace and API settings. For example, the assets package configuration is defined as follows:

```toml
--8<-- "src/examples/missions/packages/assets/config.toml"
```

### Assets package

The assets package manages physical resources required for space missions. It defines two primary resources for managing materials and rockets, where materials are basic components used in rockets:

```python { title="Define material resource" }
--8<-- "src/examples/missions/packages/assets/materials.py"
```

Rockets are assembled from multiple parts linked to materials:

```python { title="Define rocket resource" }
--8<-- "src/examples/missions/packages/assets/rockets.py"
```

### Operations package

The operations package handles mission planning and space station management. Stations provide mission destinations:

```python { title="Define station resource" }
--8<-- "src/examples/missions/packages/ops/stations.py"
```

Missions coordinate crews, rockets, and stations:

```python { title="Define mission resource" }
--8<-- "src/examples/missions/packages/ops/missions.py"
```

### Staff package

The staff package manages personnel and crew assignments. It defines astronaut profiles:

```python { title="Define astronaut resource" }
--8<-- "src/examples/missions/packages/staff/astronauts.py"
```

And organizes them into crews:

```python { title="Define crew resource" }
--8<-- "src/examples/missions/packages/staff/crews.py"
```

## Playground

### Managing rockets

The system provides comprehensive rocket management capabilities.

#### Add some rockets { .hide }

```http { title="Create some rockets with dry run" }
--8<-- "src/examples/missions/client/create.http:post-rockets"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/missions/client/create.jsonl:post-rockets"
    ```

</div>

#### Fetch rockets { .hide }

```http { title="Fetch rockets '3' and '4' with selected fields" }
--8<-- "src/examples/missions/client/read.http:get-rockets"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/missions/client/read.jsonl:get-rockets"
    ```

</div>

#### Update rockets { .hide }

```http { title="Clear description field for all rockets whose code ends with '2'" }
--8<-- "src/examples/missions/client/update.http:patch-rockets"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/missions/client/update.jsonl:patch-rockets"
    ```

</div>

#### Upsert rockets { .hide }

```http { title="Create or update a new rocket if it does not exist" }
--8<-- "src/examples/missions/client/upsert.http:put-rocket"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/missions/client/upsert.jsonl:put-rocket"
    ```

</div>

#### Delete rockets { .hide }

```http { title="Delete the rocket with id '85'" }
--8<-- "src/examples/missions/client/delete.http:delete-rocket"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/missions/client/delete.jsonl:delete-rocket"
    ```

</div>

### Managing crews

The staff package enables comprehensive crew management.

#### Assign crew leads { .hide }

```http { title="Assign first crew its lead astronaut" }
--8<-- "src/examples/missions/client/update.http:assign-lead"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/missions/client/update.jsonl:assign-lead"
    ```

</div>

#### Filter crews { .hide }

```http { title="Filter crews by astronauts" }
--8<-- "src/examples/missions/client/read.http:filter-crews"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/missions/client/read.jsonl:filter-crews"
    ```

</div>

### Planning missions

The operations package facilitates mission planning and execution.

#### Query missions { .hide }

```http title="Query mission information with pagination and sorting"
--8<-- "src/examples/missions/client/read.http:get-missions"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/missions/client/read.jsonl:get-missions"
    ```

</div>

## Advanced features

### Custom endpoints

The project demonstrates how to create custom endpoints for specific operations. For example, the crew resource includes a custom endpoint for assigning leads:

```python { title="Custom crew endpoint" }
@route.post()
async def assign_lead(self, astronaut: Key[Astronaut]) -> Self:
    lead = await astronaut.resolve()
    if lead not in self.astronauts:
        raise ValueError('The lead must be part of the crew')
    self.lead = lead
    return self
```

This endpoint ensures that only crew members can be assigned as leads.

### Resource relationships

The project showcases also various relationship types:

```python { title="Relationship examples" hl_lines="3 7-10 14-18" }
class Rocket(CRUDResource):
    ...
    parts: list['RocketPart'] = Field(default_factory=list)  # (1)!

class Crew(CRUDResource):
    ...
    astronauts: list[Astronaut] = Field(  # (2)!
        default_factory=list,
        rel_load='selectin',
    )

class Crew(CRUDResource):
    ...
    lead: Astronaut | None = Field(  # (3)!
        default=None,
        init=False,
        association_alias='crew_lead',
    )
```

1. The `Rocket` resource has a one-to-many relationship with `RocketPart` resources.
2. The `Crew` resource has a many-to-many relationship with `Astronaut` resources.
3. The `Crew` resource has a one-to-one relationship with an `Astronaut` resource representing the crew lead.
