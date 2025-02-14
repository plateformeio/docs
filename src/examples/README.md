# Plateforme examples

Each example below is a complete standalone application that can be built and run with the commands below (see which one to use in the [examples section](#examples)).

## Commands

### CLI

```bash
# Build the application
plateforme -p src/examples/[project] build

# Run the application
plateforme -p src/examples/[project] start
```

### Manual

```bash
# Execute build script
python src/examples/[project]/[file].py

# Run the application
uvicorn [file]:app --port 8001 --reload --app-dir examples/[project]
```

## Examples

### Basic

> `python src/examples/basic/example.py`

> `uvicorn example:app --port 8001 --reload --app-dir src/examples/basic`

### Basic services

#### No specification

> `python src/examples/basic_services/example_no_spec.py`

> `uvicorn example_no_spec:app --port 8001 --reload --app-dir src/examples/basic_services`

#### Simple specification

> `python src/examples/basic_services/example_simple_spec.py`

> `uvicorn example_simple_spec:app --port 8001 --reload --app-dir src/examples/basic_services`

#### Selection specification

> `python src/examples/basic_services/example_selection_spec.py`

> `uvicorn example_selection_spec:app --port 8001 --reload --app-dir src/examples/basic_services`

### Missions

> `plateforme -p src/examples/missions build`

> `plateforme -p src/examples/missions start`
