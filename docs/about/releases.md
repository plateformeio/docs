---
icon: octicons/tag-16
---

!!! note "Current status: `alpha`"

    We're actively working towards our `beta release`. Track our progress [here](roadmap.md#current-progress)!

!!! warning "Alpha phase notice"

    During the `alpha` phase, breaking changes may occur between releases as we establish the core features.

<div class="grid cards" markdown>

-   :octicons-history-24:{ .lg .middle } **Latest release**

    ---

    Version `0.1.0-a2` (Alpha)

    [:octicons-log-16:]({{ links.repo.core }}/releases/tag/0.1.0-a2)
    [:octicons-archive-16:]({{ links.repo.core }}/archive/refs/tags/0.1.0-a2.zip)
    &nbsp;•&nbsp;&nbsp;<small>:octicons-history-16: 2025-02-22</small>

-   :fontawesome-brands-python:{ .lg .middle } **Supported versions**

    ---
    
    Python 3.11+
    
    :octicons-arrow-right-24: [Compatibility](#compatibility)

</div>

## Quick start

| Version | Status | Release Date | Links |
|---------|--------|--------------|-------|
| `0.1.0-a2` | active | 2025-02-22 | [:octicons-tag-16:]({{ links.repo.core }}/releases/tag/0.1.0-a2) [:octicons-download-16:]({{ links.repo.core }}/archive/refs/tags/0.1.0-a2.zip) |

Use the following command to install the latest version of Plateforme:

=== "pip"
    ```bash
    pip install plateforme
    ```

=== "uv"
    ```bash
    uv add plateforme
    ```

??? tip "Install a specific version"

    Use the following command to install a specific version or the current development version of Plateforme:

    === "pip"
        ```bash
        # Specific version
        pip install plateforme==[version]

        # Development version
        pip install git+{{ links.repo.core }}.git
        ```

    === "uv"
        ```bash
        # Specific version
        uv add plateforme==[version]

        # Development version
        uv add git+{{ links.repo.core }}.git
        ```

## Feedback and issues

<div class="grid cards" markdown>

-   :octicons-bug-24:{ .lg .middle } __Issue reporting__

    ---

    Found a bug? Have a feature request?

    [:fontawesome-brands-github: Open an Issue]({{ links.repo.core }}/issues){ .md-button }

-   :octicons-comment-discussion-24:{ .lg .middle } **Feedback**

    ---

    Share your experience, questions and ideas

    [:fontawesome-brands-github: Join the discussion]({{ links.repo.core }}/discussions){ .md-button }

</div>

---

## Changelog

### :octicons-tag-24: **`0.1`**

#### :octicons-hash-24: `alpha-2`

> [:octicons-log-16:]({{ links.repo.core }}/releases/tag/0.1.0-a2)
> [:octicons-archive-16:]({{ links.repo.core }}/archive/refs/tags/0.1.0-a2.zip)
> &nbsp;•&nbsp;&nbsp;<small>:octicons-history-16: 2025-02-22</small>


=== ":octicons-rocket-16: Featured"

    - Added shell feature with enhanced namespace support as part of CLI architecture refactoring
    - Introduced computed field support within schema definitions
    - Added auditable resource basic implementation (work in progress)

=== ":octicons-tools-16: Added"

    - Exported members utility for retrieving module exports
    - Favicon support for docs endpoints
    - Settings dictionary type hints
    - Logging color support detection
    - CLI color support checking
    - Auto mkdir functionality for logging filenames
    - Mutable instance configuration and dictionary
    - Manager methods collection filtering
    - Mutable service configuration

=== ":octicons-bug-16: Fixed"

    - Refactored handling of forward references in type annotations
    - Added deferred type serialization
    - Disabled emoji when not UTF-8
    - Added CLI logging offset
    - Fixed levelname padding calculation
    - Ensured default values for model owner
    - Prevented passing keyword arguments to parent classes
    - Fixed self-referencing associations
    - Inherited correctly from base resource

=== ":octicons-alert-16: Breaking"

    - Refactored after model validators to use instance methods
    - Refactored exports of expressions and selectors
    - Refactored packages placeholder
    - Updated environment configuration

#### :octicons-hash-24: `alpha-1`

> [:octicons-log-16:]({{ links.repo.core }}/releases/tag/0.1.0-a1)
> [:octicons-archive-16:]({{ links.repo.core }}/archive/refs/tags/0.1.0-a1.zip)
> &nbsp;•&nbsp;&nbsp;<small>:octicons-history-16: 2025-02-15</small>

---

## Compatibility

Plateforme is compatible with **Python 3.11 and later versions**. If you need support for an earlier version, please let us know by joining the discussion.
