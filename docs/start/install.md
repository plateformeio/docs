---
icon: octicons/move-to-bottom-16
---

Installation is as simple as:

=== "pip"

    ```bash
    pip install plateforme
    ```

=== "uv"

    ```bash
    uv add plateforme
    ```

Plateforme has a few dependencies:

- [`sqlalchemy`](https://pypi.org/project/sqlalchemy), [`alembic`](https://pypi.org/project/alembic), [`aiosqlite`](https://pypi.org/project/aiosqlite): Object-relational mapping, migration tools, and database support.
- [`pydantic`](https://pypi.org/project/pydantic), [`pydantic-core`](https://pypi.org/project/pydantic-core), [`pydantic-settings`](https://pypi.org/project/pydantic-settings): Data validation and settings management.
- [`fastapi`](https://pypi.org/project/fastapi): Routing and middleware built on top of Starlette.
- [`python-dotenv`](https://pypi.org/project/python-dotenv): Environment variable management.

If you've got Python 3.11+ and `pip` installed, you're good to go.

## Optional dependencies

Plateforme has the following optional dependencies:

- **`cli`**: Command-line interface tools powered by the [`typer`](https://pypi.org/project/typer), [`questionary`](https://pypi.org/project/questionary), [`rich`](https://pypi.org/project/rich), and [`jinja2`](https://pypi.org/project/jinja2) packages.
- **`lint`**: Code linting and formatting provided by the [`mypy`](https://pypi.org/project/mypy) and [`ruff`](https://pypi.org/project/ruff) packages.
- **`serve`**: Development server provided by the [`uvicorn`](https://pypi.org/project/uvicorn) package.
- **`test`**: Testing tools provided by the [`pytest`](https://pypi.org/project/pytest), [`coverage`](https://pypi.org/project/coverage), and [`faker`](https://pypi.org/project/faker) packages.

!!! tip "All optional dependencies can be installed with the `all` extra"

To install optional dependencies along with Plateforme:

=== "pip"

    ```bash
    # with the "cli" extra:
    pip install "plateforme[cli]"

    # or with "cli" and "serve" extras:
    pip install "plateforme[cli,serve]"

    # or with all extras:
    pip install "plateforme[all]"
    ```

=== "uv"

    ```bash
    # with the "cli" extra:
    uv add "plateforme[cli]"

    # or with "cli" and "serve" extras:
    uv add "plateforme[cli,serve]"

    # or with all extras:
    uv add "plateforme[all]"
    ```

!!! note "You can also install requirements manually with for instance `pip install uvicorn`"

## Install from repository

And if you prefer to install Plateforme directly from the repository:

=== "pip"

    ```bash
    pip install "git+https://github.com/plateformeio/plateforme@main"

    # or with "cli" and "serve" extras:
    pip install "git+https://github.com/plateformeio/plateforme@main#egg=plateforme[cli,serve]"
    ```

=== "uv"

    ```bash
    uv add "git+https://github.com/plateformeio/plateforme@main"
    
    # or with "cli" and "serve" extras:
    uv add "git+https://github.com/plateformeio/plateforme@main#egg=plateforme[cli,serve]"
    ```
