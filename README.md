# Plateforme Docs

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

The official documentation for the Plateforme framework.

## Installation

Install the required dependencies using the following command:

```bash
hatch run true
```

### Development

Optionally, a custom path to the source code of the `plateforme` framework used for the documentation can be set in the development environment. You can set it using the following command:

```bash
export PLATEFORME="file:///path/to/plateforme"
```

To install the required dependencies for development, use the following command:

```bash
hatch -v run dev:true
```

#### Environment Matrix

The development environment supports different modes that determine documentation features and reference sources. Here's a breakdown of the available options:

| Mode | Description | Dependencies | Environment variables |
| ---- | ----------- | ------------ | --------------------- |
| `minimal` | Basic documentation without API reference and packages | - | - |
| `with-pkg` | Documentation with package references | - | `PACKAGES_PATH=..` |
| `with-pkg-local` | Documentation with local package references | `plateforme @ {env}` | `PLATEFORME=file:///path/to/plateforme`<br>`PACKAGES_PATH=..` |
| `with-ref` | Documentation with API reference from PyPI | `docs[reference]` | `PLUGINS_MKDOCSTRINGS=TRUE` |
| `with-ref-local` | Documentation with API reference from local install | `docs[reference]`<br>`plateforme @ {env}` | `PLATEFORME=file:///path/to/plateforme`<br>`PLUGINS_MKDOCSTRINGS=TRUE` |
| `prelaunch` | Complete documentation with API reference from PyPI | `docs[reference]` | `PACKAGES_PATH=..`<br>`PLUGINS_MKDOCSTRINGS=TRUE` |
| `prelaunch-local` | Complete documentation with API reference from local install | `docs[reference]`<br>`plateforme @ {env}` | `PLATEFORME=file:///path/to/plateforme`<br>`PACKAGES_PATH=..`<br>`PLUGINS_MKDOCSTRINGS=TRUE` |

These modes can be used with any Hatch command using the following syntax:

```bash
hatch [options] run dev.[mode]:[command]
```

For example:

```bash
# Serve standard documentation
hatch -v run dev.minimal:serve

# Serve standard documentation with packages using local source
hatch -v run dev.with-pkg-local:serve

# Serve complete documentation using PyPI source
hatch -v run dev.prelaunch:serve
```

### Production

To install the required dependencies for production, use the following command:

```bash
hatch -v run prod:true
```

## Usage

### Building the documentation

```bash
hatch [options] run [env]:build
```

### Deploying the documentation

```bash
hatch [options] run [env]:deploy {args}
```

> See [versioning](#versioning) for more details.

### Serving the documentation

Start the live-reloading docs server by running either one of the following commands:

```bash
# Test the current documentation locally without versioning
hatch [options] run [env]:serve

# Test the documentation with version selector
hatch [options] run [env]:serve-versions
```

> The `serve` command uses `mkdocs` to serve the documentation, while the `serve-versions` command uses `mike` to serve the documentation with version selector.

## Project layout

    mkdocs.yml      # The configuration file.
    docs/
        index.md    # The documentation homepage.
        ...         # Other documentation markdown pages.
    overrides/
        .icons/     # Icons for the documentation.
        assets/     # Images, logo, styles and other files.
        partials/   # Custom templates and partials.
        index.html  # Home page.
        main.html   # Main page.
        ...         # Other html pages.
    src/
        ...         # Code snippets and examples.
    tests/
        ...         # Test files for the code snippets.

## Versioning

The documentation is versioned using [`mike`](https://github.com/jimporter/mike) dependency.

### Publishing a version

To deploy a new version, run the following command:

```bash
hatch [options] run [env]:deploy --update-aliases [identifier] [alias]
```

In addition, you can specify where to deploy your docs via `-b/--branch`, `-r/--remote`, and `--deploy-prefix`, specifying the branch, remote, and directory prefix within the branch, respectively. To push your docs to a remote branch, simply add `-p/--push` to your command.

To set the default version that appears at the root URL:

```bash
hatch -v run prod:mike set-default latest
```

All modifications can be committed and pushed to the remote repository. By default, the `gh-pages` branch is used.

```bash
git push origin [branch]
```

### Managing versions

Versions can be listed, deleted, and aliased using the following commands:

```bash
# List all versions
mike list

# Delete all or a specific version
mike delete --all
mike delete [identifier]

# Alias a version
mike alias [identifier] [alias]

# Set the default version
mike set-default [alias]
```

### Common options

| Option | Description |
| ------ | ----------- |
| `--push`, `-p` | Push changes immediately to remote |
| `--update-aliases`, `-u` | Allow updating existing aliases |
| `--branch`, `-b` | Specify target branch (default: gh-pages) |
| `--remote`, `-r` | Specify git remote (default: origin) |

## See also

MkDocs and Material for MkDocs documentation:
- [MkDocs](https://www.mkdocs.org)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
