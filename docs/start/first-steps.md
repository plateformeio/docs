---
icon: octicons/north-star-16
---

# First steps with the Plateforme framework

This introduction to the Plateforme framework will walk you through the essential steps to get your first application up and running. You will learn how to:

- [x] [Initialize](#project-initialization) a new project.
- [x] [Setup](#application-setup) your application.
- [x] [Create resources](#create-resources) with fields and relationships.
- [x] [Create API routes](#custom-routes) alongside the built-in CRUD operations.
- [x] [Build and run](#build-and-run) your first application.

!!! warning "The documentation is under heavy development!"

    The documentation is actively being developed and might not cover every feature. For full details, refer to the [source code]({{ links.repo.core }}).

---

## Project initialization

To begin, the easiest way to initialize and set up a new project is using the Plateforme built-in CLI. This requires [CLI extra dependencies](install.md#optional-dependencies) to be installed.

Note that for each command, you can get more information using `-h` or `--help` flag. For example, you can get help for the `init` command by running `plateforme init --help`.

Let's execute the initialization wizard command and follow the prompts. You can optionally provide a path argument to the `init` command to create the project in a specific directory. Otherwise, the current directory will be used.

<!-- termynal -->

```bash
$ plateforme init
─────────────────────────────────────────────────────
  🏗  plateforme-cli 0.1.0 → init
─────────────────────────────────────────────────────
? Project name: my-app
? Version: 0.1.0
? Description: My first application
? Author (name): Rodolphe
? Author (email): rodolphe@example.com
? Template: Hero
? Create a new directory for the project? Yes
? Create project in '/path/to/my_app' directory? Yes
---> 100%
INFO:     Project initialized successfully!
```

This will create a basic project structure with the following files:

```bash { .no-copy .no-select }
my_app/
├── main.py           # Application entry point
├── setup.py          # Application build script
├── pyproject.toml    # Project configuration
└── README.md         # Project documentation
```

Where the project and application can be configured within the `pyproject.toml` file.

```toml { title="Configure the project" }
--8<-- "src/start/first-steps/pyproject.toml:project-config"
```

```toml { title="Configure the 'default' application build and start actions" }
--8<-- "src/start/first-steps/pyproject.toml:app-config"
```

## Application setup

Once your project is created, you should have two files named `main.py` and `setup.py` inside your newly created folder. The `main.py` file is the main entry point for your application, and the `setup.py` file is used here as the build script to initialize the database.

```python { title="Setup the application" }
--8<-- "src/start/first-steps/main.py:app"
```

1. The `plateforme.db` setting for the database engines tells Plateforme to use an SQLite database file named `plateforme.db` in the project directory. Advanced database settings can also be provided to specify multiple database engines and custom connection settings.

The Plateforme application instance accepts advanced settings. You can also use a separate Python settings file with environment-specific configurations (see the `enterprise` template when initializing the project).

```python { title="Build script to initialize the database" }
--8<-- "src/start/first-steps/setup.py:snippet"
```

1. The `create_all()` method generates all tables in the database specified by `database_engines`.

## Create resources

Let's start by importing the necessary objects from Plateforme.

```python
--8<-- "src/start/first-steps/main.py:imports"
```

This statement imports four objects from Plateforme:

- `ConfigDict` typed dictionnary for defining resource configurations.
- `CRUDResource` as the base class for creating resources that subscribe to CRUD operations.
- `Field` function for defining fields and relationships configuration within resources.
- `route` decorator for defining custom routes and endpoints.

We can now define our first resources.

```python { title="Define the 'Material' resource" }
--8<-- "src/start/first-steps/main.py:add-material"
```

1. Extend `CRUDResource` to create a new resource.
2. Define a unique `code` field for each material.
3. Define a list of `RocketPart` objects as a many relationship. The `Field(default_factory=list)` means it defaults to an empty list if none is provided.


```python { title="Define the 'Rocket' and 'RocketPart' resources" }
--8<-- "src/start/first-steps/main.py:add-rocket"
```

1. Define a list of `RocketPart` objects as a many relationship. The `Field(default_factory=list)` means it defaults to an empty list if none is provided.
2. Create a composite index on `rocket` and `material` fields to improve query performance and prevent duplicate part codes per rocket.
3. Define a relationship to the `Rocket` resource.
4. Define a relationship to the `Material` resource.

## Custom routes

We can also add custom routes to our resources. Let's add a custom route to the `Material` resource to update its name.

```python { title="Add a custom route to the 'Material' resource" }
class Material(CRUDResource):
    ...

--8<-- "src/start/first-steps/main.py:add-custom-route"
```

1. The `@route.post()` decorator creates a custom endpoint with a `POST` method.
2. The framework inspects the method signature to determine the route parameters, return type, and perform automatic validation and serialization.
3. The method updates the `name` field of the `Material` resource and returns a confirmation message. The modifications will be persisted to the database (fine-grained control is also possible using the dependency injection `AsyncSessionDep`).

??? quote "Source code in `src/start/first-steps/main.py`"

    ```python
    --8<-- "src/start/first-steps/main.py"
    ```

## Build and run

Let's build and run our application using the built-in Plateforme command-line interface.

The CLI infers the project directory from the current working directory.

```bash
cd myapp  # (1)!
```

1. Navigate to the project directory where the `pyproject.toml` file is located.

!!! note "Project directory"

    You can also use the `-p` or `--project` flag to specify the project directory when running any Plateforme commands. For instance, you can run `plateforme -p /path/to/myapp build` to build the application from a different directory.

Once our project is set up, we can first build the application using the `build` command:

<!-- termynal -->

```bash
$ plateforme build
─────────────────────────────────────────────────────
  🏗  plateforme-cli 0.1.0 → build
─────────────────────────────────────────────────────
---> 100%
INFO:     Building project application... (from 'my-app')
INFO:     main:688 - (my-app) pkg:__main__ -> added
INFO:     main:423 - (my-app) initialized
INFO:     Application 'default' built successfully
```

This should generate a `plateforme.db` SQLite database file in the project directory and set up the tables for the `Material`, `Rocket`, and `RocketPart` resources.

Finally, we can start the application server using the `start` command:

<!-- termynal -->

```bash
$ plateforme start
─────────────────────────────────────────────────────
  🏗  plateforme-cli 0.1.0 → start
─────────────────────────────────────────────────────
---> 100%
INFO:     Starting application... (from 'my-app')
INFO:     main:688 - (my-app) pkg:__main__ -> added
INFO:     main:423 - (my-app) initialized
INFO:     Started server process [71407]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)
```

Our application is now running and accessible at `http://127.0.0.1:8001`.

## Next steps

You can play with the application endpoints using the automatically generated CRUD endpoints, see the [basic example](../examples/basic.md) for more details.

For more advanced features, you can explore our [guides](../learn/index.md) and [reference](../reference/index.md) documentation.
